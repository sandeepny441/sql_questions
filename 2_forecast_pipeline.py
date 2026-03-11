from __future__ import annotations

import re
from collections import defaultdict
from datetime import date, datetime

import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression, Ridge


BASE_REQUIRED_COLUMNS = [
    "nmls",
    "bucket",
    "month",
    "uwm_purchase_from_uwm",
    "all_purchase_from_cotality",
    "uwm_refi_from_uwm",
    "all_refi_from_cotality",
    "uwm_total_from_uwm",
    "all_total_from_cotality",
    "num_states_from_uwm",
    "num_states_from_cotality",
    "num_lenders_from_cotality",
]

FORECAST_COLUMNS = [
    "purchase_fcst_rule",
    "purchase_fcst_ml",
    "purchase_fcst_hybrid",
    "purchase_rule_delta_pct",
    "purchase_ml_delta_pct",
    "refi_fcst_rule",
    "refi_fcst_ml",
    "refi_fcst_hybrid",
    "refi_rule_delta_pct",
    "refi_ml_delta_pct",
    "total_fcst_rule",
    "total_fcst_ml",
    "total_fcst_hybrid",
    "total_rule_delta_pct",
    "total_ml_delta_pct",
]

NUMERIC_COLUMNS = [
    "uwm_purchase_from_uwm",
    "uwm_purchase_from_cotality",
    "all_purchase_from_cotality",
    "uwm_refi_from_uwm",
    "uwm_refi_from_cotality",
    "all_refi_from_cotality",
    "uwm_total_from_uwm",
    "uwm_total_from_cotality",
    "all_total_from_cotality",
    "uwm_total_2025_from_uwm",
    "uwm_total_2025_from_cotality",
    "all_total_2025_from_cotality",
    "num_states_from_uwm",
    "num_states_from_cotality",
    "num_lenders_from_cotality",
]

BUCKET_ORDER = [
    "mega_producer_480plus",
    "super_producer_240_479",
    "high_producer_120_239",
    "active_producer_60_119",
    "standard_producer_25_59",
    "occasional_lo_21_24",
    "part_time_lo_16_20",
    "low_volume_lo_11_15",
    "minimal_lo_6_10",
    "dormant_lo_0_5",
    "unknown_bucket",
]

SPARSE_BUCKETS = {
    "low_volume_lo_11_15",
    "minimal_lo_6_10",
    "dormant_lo_0_5",
}

ERROR_THRESHOLDS = [1, 2, 3, 5, 7, 10, 12, 15, 20, 25, 30, 35, 40, 50]

BUCKET_ALIASES = {
    "dormant_lo_0_5": "dormant_lo_0_5",
    "dormant_lo": "dormant_lo_0_5",
    "minimal_lo_6_10": "minimal_lo_6_10",
    "minimal_lo": "minimal_lo_6_10",
    "low_volume_lo_11_15": "low_volume_lo_11_15",
    "low_volume_lo": "low_volume_lo_11_15",
    "part_time_lo_16_20": "part_time_lo_16_20",
    "part_time_lo": "part_time_lo_16_20",
    "occasional_lo_21_24": "occasional_lo_21_24",
    "occasional_lo": "occasional_lo_21_24",
    "standard_producer_25_59": "standard_producer_25_59",
    "standard_producer": "standard_producer_25_59",
    "active_producer_60_119": "active_producer_60_119",
    "active_producer": "active_producer_60_119",
    "high_producer_120_239": "high_producer_120_239",
    "high_producer": "high_producer_120_239",
    "super_producer_240_479": "super_producer_240_479",
    "super_producer": "super_producer_240_479",
    "mega_producer_480plus": "mega_producer_480plus",
    "mega_producer": "mega_producer_480plus",
}


def run_forecast_pipeline(df: pd.DataFrame, run_month: str | None = None) -> dict:
    forecast_df = _prepare_dataframe(df, run_month)
    records, rows_by_nmls, rows_by_month = _build_panel_indexes(forecast_df)

    rule_context = _apply_rule_market_forecast(
        records,
        rows_by_nmls,
        rows_by_month,
        run_month,
    )
    ml_context = _apply_ml_market_forecast(
        records,
        rows_by_nmls,
        rows_by_month,
        run_month,
    )
    hybrid_sources = _apply_hybrid_forecast(
        records,
        rule_context["future_months"],
        rule_context["metric_scores"],
        ml_context["metric_scores"],
    )

    output_df = _records_to_dataframe(forecast_df, records)
    bucket_tables = {
        metric_name: pd.DataFrame(summary_rows)
        for metric_name, summary_rows in _build_bucket_error_summaries(
            records,
            rule_context["test_months"],
        ).items()
    }
    threshold_tables = {
        metric_name: pd.DataFrame(summary_rows)
        for metric_name, summary_rows in _build_error_threshold_summaries(
            records,
            rule_context["test_months"],
        ).items()
    }

    return {
        "forecast_df": output_df,
        "bucket_error_tables": bucket_tables,
        "threshold_error_tables": threshold_tables,
        "rule_context": rule_context,
        "ml_context": ml_context,
        "hybrid_sources": hybrid_sources,
    }


def _prepare_dataframe(df: pd.DataFrame, run_month: str | None = None) -> pd.DataFrame:
    missing_columns = [column for column in BASE_REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    prepared = df.copy()
    prepared["bucket"] = prepared["bucket"].apply(_normalize_bucket)
    prepared["_month_dt"] = prepared["month"].apply(_parse_month_value)
    if prepared["_month_dt"].isna().any():
        invalid_rows = prepared.loc[prepared["_month_dt"].isna(), ["nmls", "month"]].head(10)
        raise ValueError(f"Could not parse some month values. Sample rows:\n{invalid_rows}")

    for column in NUMERIC_COLUMNS:
        if column in prepared.columns:
            prepared[column] = pd.to_numeric(prepared[column], errors="coerce").fillna(0.0)

    for column in FORECAST_COLUMNS:
        if column not in prepared.columns:
            prepared[column] = 0.0
        else:
            prepared[column] = pd.to_numeric(prepared[column], errors="coerce").fillna(0.0)

    prepared["_month_label"] = prepared["_month_dt"].apply(_format_month)
    prepared = _append_missing_future_rows(prepared, run_month)
    prepared = prepared.sort_values(["nmls", "_month_dt"]).reset_index(drop=True)
    return prepared


def _normalize_bucket(value) -> str:
    if pd.isna(value):
        return "unknown_bucket"

    normalized = re.sub(r"[^a-z0-9]+", "_", str(value).strip().lower()).strip("_")
    return BUCKET_ALIASES.get(normalized, normalized or "unknown_bucket")


def _parse_month_value(value) -> pd.Timestamp:
    if pd.isna(value):
        return pd.NaT

    if isinstance(value, pd.Period):
        return value.to_timestamp(how="start")

    if isinstance(value, (pd.Timestamp, datetime, date)):
        return pd.Timestamp(value).to_period("M").to_timestamp(how="start")

    text = str(value).strip().replace(",", "").replace("  ", " ")
    for fmt in ("%m/%Y", "%m/%y", "%Y-%m", "%Y/%m", "%b %Y", "%B %Y", "%Y-%m-%d"):
        try:
            return pd.Timestamp(datetime.strptime(text, fmt)).to_period("M").to_timestamp(how="start")
        except ValueError:
            continue

    parsed = pd.to_datetime(text, errors="coerce")
    if pd.isna(parsed):
        return pd.NaT
    return parsed.to_period("M").to_timestamp(how="start")


def _append_missing_future_rows(df: pd.DataFrame, run_month: str | None = None) -> pd.DataFrame:
    available_months = sorted(df["_month_dt"].dropna().unique().tolist())
    if not available_months:
        return df

    anchor_month = _resolve_anchor_month(available_months, run_month)
    future_months = _compute_rule_windows(anchor_month)["future_months"]
    placeholder_rows = []

    for nmls, group in df.groupby("nmls", sort=False):
        month_set = set(group["_month_dt"].tolist())
        for future_month in future_months:
            if future_month in month_set:
                continue

            prior_rows = group.loc[group["_month_dt"] < future_month].sort_values("_month_dt")
            if prior_rows.empty:
                continue

            source_row = prior_rows.iloc[-1].to_dict()
            source_row["month"] = _format_month(future_month)
            source_row["_month_dt"] = future_month
            source_row["_month_label"] = _format_month(future_month)

            # Keep trusted internal UWM fields from the latest available month,
            # but leave market actuals blank on auto-created future rows.
            source_row["all_purchase_from_cotality"] = np.nan
            source_row["all_refi_from_cotality"] = np.nan
            source_row["all_total_from_cotality"] = np.nan

            for column in FORECAST_COLUMNS:
                source_row[column] = 0.0

            placeholder_rows.append(source_row)

    if not placeholder_rows:
        return df

    return pd.concat([df, pd.DataFrame(placeholder_rows)], ignore_index=True, sort=False)


def _build_panel_indexes(df: pd.DataFrame):
    records = df.to_dict(orient="index")
    rows_by_nmls = defaultdict(dict)
    rows_by_month = defaultdict(list)

    for idx, row in records.items():
        month = row["_month_dt"]
        rows_by_nmls[row["nmls"]][month] = idx
        rows_by_month[month].append(idx)

    return records, rows_by_nmls, rows_by_month


def _records_to_dataframe(df: pd.DataFrame, records: dict) -> pd.DataFrame:
    output = pd.DataFrame.from_dict(records, orient="index").sort_index()
    output = output[[column for column in df.columns if column not in {"_month_dt", "_month_label"}]]
    return output


def _mean(values) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def _mean_absolute(values) -> float:
    return round(_mean([abs(value) for value in values]), 2) if values else 0.0


def _shift_month(value: pd.Timestamp, offset: int) -> pd.Timestamp:
    return (value.to_period("M") + offset).to_timestamp(how="start")


def _compute_rule_windows(anchor_month: pd.Timestamp) -> dict:
    return {
        "test_baseline_months": [_shift_month(anchor_month, offset) for offset in (-8, -7, -6, -5)],
        "test_months": [_shift_month(anchor_month, offset) for offset in (-4, -3)],
        "future_baseline_months": [_shift_month(anchor_month, offset) for offset in (-6, -5, -4, -3)],
        "future_months": [_shift_month(anchor_month, offset) for offset in (-2, -1, 0)],
    }


def _format_month(value: pd.Timestamp) -> str:
    return value.strftime("%m/%Y")


def _resolve_anchor_month(available_months, run_month: str | None) -> pd.Timestamp:
    if run_month:
        return _parse_month_value(run_month)

    current_month = pd.Timestamp(date.today()).to_period("M").to_timestamp(how="start")
    if current_month in available_months:
        return current_month

    return max(available_months)


def _average_monthly_value(records, rows_by_month, months, key):
    monthly_means = []
    for month in months:
        month_rows = rows_by_month.get(month, [])
        monthly_means.append(_mean([records[idx][key] for idx in month_rows]))
    return _mean(monthly_means)


def _signed_delta_pct(forecast_value, actual_value):
    if actual_value == 0:
        return 0.0
    return round(((forecast_value - actual_value) / actual_value) * 100, 2)


def _apply_rule_market_forecast(records, rows_by_nmls, rows_by_month, run_month=None):
    anchor_month = _resolve_anchor_month(rows_by_month.keys(), run_month)
    windows = _compute_rule_windows(anchor_month)
    required_months = (
        windows["test_baseline_months"]
        + windows["test_months"]
        + windows["future_baseline_months"]
        + windows["future_months"]
    )
    missing_months = [_format_month(month) for month in required_months if month not in rows_by_month]
    if missing_months:
        raise ValueError(f"Missing months required for forecasting: {missing_months}")

    metric_map = [
        ("all_purchase_from_cotality", "uwm_purchase_from_uwm", "purchase_fcst_rule", "purchase_rule_delta_pct"),
        ("all_refi_from_cotality", "uwm_refi_from_uwm", "refi_fcst_rule", "refi_rule_delta_pct"),
        ("all_total_from_cotality", "uwm_total_from_uwm", "total_fcst_rule", "total_rule_delta_pct"),
    ]
    metric_scores = {}

    for market_key, uwm_key, forecast_key, delta_key in metric_map:
        metric_name = forecast_key.replace("_fcst_rule", "")
        test_uwm_baseline_avg = _average_monthly_value(records, rows_by_month, windows["test_baseline_months"], uwm_key)
        test_uwm_target_avg = _average_monthly_value(records, rows_by_month, windows["test_months"], uwm_key)
        test_trend_factor = test_uwm_target_avg / test_uwm_baseline_avg if test_uwm_baseline_avg else 0.0

        future_uwm_baseline_avg = _average_monthly_value(records, rows_by_month, windows["future_baseline_months"], uwm_key)
        future_uwm_target_avg = _average_monthly_value(records, rows_by_month, windows["future_months"], uwm_key)
        future_trend_factor = future_uwm_target_avg / future_uwm_baseline_avg if future_uwm_baseline_avg else 0.0

        current_test_deltas = []
        for nmls_rows in rows_by_nmls.values():
            if any(month not in nmls_rows for month in windows["test_baseline_months"]):
                continue

            test_market_baseline_avg = _mean(
                [records[nmls_rows[month]][market_key] for month in windows["test_baseline_months"]]
            )
            test_forecast_value = round(test_market_baseline_avg * test_trend_factor, 2)

            for test_month in windows["test_months"]:
                if test_month not in nmls_rows:
                    continue
                idx = nmls_rows[test_month]
                current_delta = _signed_delta_pct(test_forecast_value, records[idx][market_key])
                current_test_deltas.append(current_delta)
                if records[idx][forecast_key] == 0:
                    records[idx][forecast_key] = test_forecast_value
                if records[idx][delta_key] == 0 and records[idx][forecast_key] != 0:
                    records[idx][delta_key] = _signed_delta_pct(records[idx][forecast_key], records[idx][market_key])

            if any(month not in nmls_rows for month in windows["future_baseline_months"]):
                continue

            future_market_baseline_avg = _mean(
                [records[nmls_rows[month]][market_key] for month in windows["future_baseline_months"]]
            )
            future_forecast_value = round(future_market_baseline_avg * future_trend_factor, 2)

            for future_month in windows["future_months"]:
                if future_month not in nmls_rows:
                    continue
                idx = nmls_rows[future_month]
                records[idx][forecast_key] = future_forecast_value
                records[idx][delta_key] = 0.0

        metric_scores[metric_name] = current_test_deltas

    return {
        "anchor_month": _format_month(anchor_month),
        "test_baseline_months": [_format_month(month) for month in windows["test_baseline_months"]],
        "test_months": [_format_month(month) for month in windows["test_months"]],
        "future_baseline_months": [_format_month(month) for month in windows["future_baseline_months"]],
        "future_months": [_format_month(month) for month in windows["future_months"]],
        "metric_scores": metric_scores,
    }


def _build_training_months(rows_by_nmls, cutoff_month):
    months = set()
    for nmls_rows in rows_by_nmls.values():
        for month in nmls_rows:
            if month >= cutoff_month:
                continue

            lag_months = [_shift_month(month, -offset) for offset in (1, 2, 3, 4)]
            if all(lag_month in nmls_rows for lag_month in lag_months):
                months.add(month)

    return sorted(months)


def _build_feature_dict(records, nmls_rows, target_month, market_key, uwm_key, history_override=None):
    history_override = history_override or {}
    lag_months = [_shift_month(target_month, -offset) for offset in (1, 2, 3, 4)]
    market_lags = [
        history_override.get(lag_month, records[nmls_rows[lag_month]][market_key])
        for lag_month in lag_months
    ]
    uwm_lags = [records[nmls_rows[lag_month]][uwm_key] for lag_month in lag_months]
    target_row = records[nmls_rows[target_month]]

    market_avg_4 = _mean(market_lags)
    recent_market_avg_2 = _mean(market_lags[:2])
    older_market_avg_2 = _mean(market_lags[2:])
    uwm_avg_4 = _mean(uwm_lags)

    return {
        "bucket": target_row["bucket"],
        "month_sin": np.sin(2 * np.pi * target_month.month / 12),
        "month_cos": np.cos(2 * np.pi * target_month.month / 12),
        "market_lag_1": market_lags[0],
        "market_lag_2": market_lags[1],
        "market_lag_3": market_lags[2],
        "market_lag_4": market_lags[3],
        "market_avg_4": market_avg_4,
        "market_delta_2v2": recent_market_avg_2 - older_market_avg_2,
        "market_ratio_2v2": (recent_market_avg_2 / older_market_avg_2) if older_market_avg_2 else 0.0,
        "uwm_current": target_row[uwm_key],
        "uwm_lag_1": uwm_lags[0],
        "uwm_lag_2": uwm_lags[1],
        "uwm_avg_4": uwm_avg_4,
        "uwm_trend": (target_row[uwm_key] / uwm_avg_4) if uwm_avg_4 else 0.0,
        "num_states_from_uwm": target_row["num_states_from_uwm"],
        "num_states_from_cotality": target_row["num_states_from_cotality"],
        "num_lenders_from_cotality": target_row["num_lenders_from_cotality"],
    }


def _fit_ridge_model(records, rows_by_nmls, training_months, market_key, uwm_key, bucket_selector=None):
    feature_rows = []
    targets = []

    for month in training_months:
        for nmls_rows in rows_by_nmls.values():
            if month not in nmls_rows:
                continue
            lag_months = [_shift_month(month, -offset) for offset in (1, 2, 3, 4)]
            if any(lag_month not in nmls_rows for lag_month in lag_months):
                continue

            idx = nmls_rows[month]
            target_row = records[idx]
            if bucket_selector and not bucket_selector(target_row["bucket"]):
                continue

            feature_rows.append(_build_feature_dict(records, nmls_rows, month, market_key, uwm_key))
            targets.append(target_row[market_key])

    if len(feature_rows) < 3:
        return None, None

    vectorizer = DictVectorizer(sparse=False)
    x_matrix = vectorizer.fit_transform(feature_rows)
    y_vector = np.log1p(np.array(targets, dtype=float))

    model = Ridge(alpha=1.0)
    model.fit(x_matrix, y_vector)
    return vectorizer, model


def _fit_sparse_hurdle_model(records, rows_by_nmls, training_months, market_key, uwm_key):
    feature_rows = []
    activity_targets = []
    positive_feature_rows = []
    positive_targets = []

    for month in training_months:
        for nmls_rows in rows_by_nmls.values():
            if month not in nmls_rows:
                continue
            lag_months = [_shift_month(month, -offset) for offset in (1, 2, 3, 4)]
            if any(lag_month not in nmls_rows for lag_month in lag_months):
                continue

            idx = nmls_rows[month]
            target_row = records[idx]
            if target_row["bucket"] not in SPARSE_BUCKETS:
                continue

            features = _build_feature_dict(records, nmls_rows, month, market_key, uwm_key)
            target_value = target_row[market_key]
            feature_rows.append(features)
            activity_targets.append(1 if target_value > 0 else 0)

            if target_value > 0:
                positive_feature_rows.append(features)
                positive_targets.append(target_value)

    if not feature_rows:
        return {
            "vectorizer": None,
            "activity_model": None,
            "positive_model": None,
            "activity_rate": 0.0,
            "positive_mean": 0.0,
        }

    vectorizer = DictVectorizer(sparse=False)
    x_matrix = vectorizer.fit_transform(feature_rows)
    activity_rate = _mean(activity_targets)
    positive_mean = _mean(positive_targets)

    activity_model = None
    if len(set(activity_targets)) > 1:
        activity_model = LogisticRegression(max_iter=1000, class_weight="balanced")
        activity_model.fit(x_matrix, np.array(activity_targets, dtype=int))

    positive_model = None
    if len(positive_feature_rows) >= 3:
        positive_x = vectorizer.transform(positive_feature_rows)
        positive_y = np.log1p(np.array(positive_targets, dtype=float))
        positive_model = Ridge(alpha=1.0)
        positive_model.fit(positive_x, positive_y)

    return {
        "vectorizer": vectorizer,
        "activity_model": activity_model,
        "positive_model": positive_model,
        "activity_rate": activity_rate,
        "positive_mean": positive_mean,
    }


def _predict_with_model(vectorizer, model, features, fallback_value):
    if vectorizer is None or model is None:
        return round(max(fallback_value, 0.0), 2)

    transformed = vectorizer.transform([features])
    prediction = float(np.expm1(model.predict(transformed)[0]))
    return round(max(prediction, 0.0), 2)


def _predict_with_hurdle_model(model_bundle, features, fallback_value):
    vectorizer = model_bundle["vectorizer"]
    activity_model = model_bundle["activity_model"]
    positive_model = model_bundle["positive_model"]

    if vectorizer is None:
        return round(max(fallback_value, 0.0), 2)

    transformed = vectorizer.transform([features])

    if activity_model is not None:
        activity_probability = float(activity_model.predict_proba(transformed)[0][1])
    else:
        activity_probability = model_bundle["activity_rate"]

    if positive_model is not None:
        positive_mean = float(np.expm1(positive_model.predict(transformed)[0]))
    else:
        positive_mean = model_bundle["positive_mean"]

    if positive_mean <= 0:
        positive_mean = fallback_value

    prediction = activity_probability * max(positive_mean, 0.0)
    return round(max(prediction, 0.0), 2)


def _recursive_market_forecast(
    records,
    rows_by_nmls,
    months_to_predict,
    market_key,
    uwm_key,
    forecast_key,
    delta_key,
    regular_vectorizer,
    regular_model,
    sparse_model_bundle,
    score_against_actual,
    persist,
):
    ordered_months = sorted(months_to_predict)
    forecast_results = {}

    for nmls_rows in rows_by_nmls.values():
        predicted_history = {}
        for target_month in ordered_months:
            if target_month not in nmls_rows:
                continue

            lag_months = [_shift_month(target_month, -offset) for offset in (1, 2, 3, 4)]
            if any(lag_month not in nmls_rows and lag_month not in predicted_history for lag_month in lag_months):
                continue

            features = _build_feature_dict(
                records,
                nmls_rows,
                target_month,
                market_key,
                uwm_key,
                history_override=predicted_history,
            )
            fallback_value = features["market_avg_4"] * features["uwm_trend"]
            idx = nmls_rows[target_month]
            row = records[idx]
            if row["bucket"] in SPARSE_BUCKETS:
                forecast_value = _predict_with_hurdle_model(sparse_model_bundle, features, fallback_value)
            else:
                forecast_value = _predict_with_model(regular_vectorizer, regular_model, features, fallback_value)

            current_delta = _signed_delta_pct(forecast_value, row[market_key]) if score_against_actual else 0.0
            forecast_results[(row["nmls"], row["_month_label"])] = {
                "forecast": forecast_value,
                "delta": current_delta,
            }

            if persist:
                if score_against_actual:
                    if row[forecast_key] == 0:
                        row[forecast_key] = forecast_value
                    if row[delta_key] == 0 and row[forecast_key] != 0:
                        row[delta_key] = _signed_delta_pct(row[forecast_key], row[market_key])
                else:
                    row[forecast_key] = forecast_value
                    row[delta_key] = 0.0

            predicted_history[target_month] = forecast_value

    return forecast_results


def _apply_ml_market_forecast(records, rows_by_nmls, rows_by_month, run_month=None):
    anchor_month = _resolve_anchor_month(rows_by_month.keys(), run_month)
    windows = _compute_rule_windows(anchor_month)

    metric_map = [
        ("all_purchase_from_cotality", "uwm_purchase_from_uwm", "purchase_fcst_ml", "purchase_ml_delta_pct"),
        ("all_refi_from_cotality", "uwm_refi_from_uwm", "refi_fcst_ml", "refi_ml_delta_pct"),
    ]
    backtest_training_months = _build_training_months(rows_by_nmls, min(windows["test_months"]))
    future_training_months = _build_training_months(rows_by_nmls, min(windows["future_months"]))

    metric_scores = {}
    backtest_forecasts = {}

    for market_key, uwm_key, forecast_key, delta_key in metric_map:
        metric_name = forecast_key.replace("_fcst_ml", "")
        backtest_vectorizer, backtest_model = _fit_ridge_model(
            records,
            rows_by_nmls,
            backtest_training_months,
            market_key,
            uwm_key,
            bucket_selector=lambda bucket: bucket not in SPARSE_BUCKETS,
        )
        backtest_sparse_bundle = _fit_sparse_hurdle_model(
            records,
            rows_by_nmls,
            backtest_training_months,
            market_key,
            uwm_key,
        )
        score_months = _recursive_market_forecast(
            records,
            rows_by_nmls,
            windows["test_months"],
            market_key,
            uwm_key,
            forecast_key,
            delta_key,
            backtest_vectorizer,
            backtest_model,
            backtest_sparse_bundle,
            score_against_actual=True,
            persist=False,
        )
        metric_scores[metric_name] = [result["delta"] for result in score_months.values()]
        backtest_forecasts[metric_name] = score_months
        _recursive_market_forecast(
            records,
            rows_by_nmls,
            windows["test_months"],
            market_key,
            uwm_key,
            forecast_key,
            delta_key,
            backtest_vectorizer,
            backtest_model,
            backtest_sparse_bundle,
            score_against_actual=True,
            persist=True,
        )

        future_vectorizer, future_model = _fit_ridge_model(
            records,
            rows_by_nmls,
            future_training_months,
            market_key,
            uwm_key,
            bucket_selector=lambda bucket: bucket not in SPARSE_BUCKETS,
        )
        future_sparse_bundle = _fit_sparse_hurdle_model(
            records,
            rows_by_nmls,
            future_training_months,
            market_key,
            uwm_key,
        )
        _recursive_market_forecast(
            records,
            rows_by_nmls,
            windows["future_months"],
            market_key,
            uwm_key,
            forecast_key,
            delta_key,
            future_vectorizer,
            future_model,
            future_sparse_bundle,
            score_against_actual=False,
            persist=True,
        )

    total_deltas = []
    purchase_forecasts = backtest_forecasts.get("purchase", {})
    refi_forecasts = backtest_forecasts.get("refi", {})
    for key, purchase_result in purchase_forecasts.items():
        if key not in refi_forecasts:
            continue
        nmls, month_label = key
        month = _parse_month_value(month_label)
        idx = rows_by_nmls[nmls][month]
        total_forecast = round(purchase_result["forecast"] + refi_forecasts[key]["forecast"], 2)
        total_actual = records[idx]["all_total_from_cotality"]
        total_deltas.append(_signed_delta_pct(total_forecast, total_actual))
    metric_scores["total"] = total_deltas

    for nmls_rows in rows_by_nmls.values():
        for month in sorted(windows["test_months"] + windows["future_months"]):
            if month not in nmls_rows:
                continue

            idx = nmls_rows[month]
            row = records[idx]
            if month in windows["test_months"]:
                if row["total_fcst_ml"] == 0:
                    row["total_fcst_ml"] = round(row["purchase_fcst_ml"] + row["refi_fcst_ml"], 2)
                if row["total_ml_delta_pct"] == 0 and row["total_fcst_ml"] != 0:
                    row["total_ml_delta_pct"] = _signed_delta_pct(row["total_fcst_ml"], row["all_total_from_cotality"])
            else:
                row["total_fcst_ml"] = round(row["purchase_fcst_ml"] + row["refi_fcst_ml"], 2)
                row["total_ml_delta_pct"] = 0.0

    return {
        "anchor_month": _format_month(anchor_month),
        "test_months": [_format_month(month) for month in windows["test_months"]],
        "future_months": [_format_month(month) for month in windows["future_months"]],
        "backtest_training_months": [_format_month(month) for month in backtest_training_months],
        "future_training_months": [_format_month(month) for month in future_training_months],
        "metric_scores": metric_scores,
    }


def _score_from_deltas(deltas):
    if not deltas:
        return float("inf")
    return abs(_mean(deltas))


def _apply_hybrid_forecast(records, future_month_labels, rule_scores, ml_scores):
    metric_sources = {}
    for metric_name in ("purchase", "refi", "total"):
        rule_score = _score_from_deltas(rule_scores.get(metric_name, []))
        ml_score = _score_from_deltas(ml_scores.get(metric_name, []))
        metric_sources[metric_name] = "rule" if rule_score <= ml_score else "ml"

    for row in records.values():
        if row["_month_label"] not in future_month_labels:
            continue
        for metric_name in ("purchase", "refi", "total"):
            source = metric_sources[metric_name]
            row[f"{metric_name}_fcst_hybrid"] = row[f"{metric_name}_fcst_{source}"]

    return metric_sources


def _build_bucket_error_summaries(records, test_month_labels):
    metric_configs = [
        ("purchase", "purchase_rule_delta_pct", "purchase_ml_delta_pct"),
        ("refi", "refi_rule_delta_pct", "refi_ml_delta_pct"),
        ("total", "total_rule_delta_pct", "total_ml_delta_pct"),
    ]
    summaries = {}

    for metric_name, rule_delta_key, ml_delta_key in metric_configs:
        bucket_rule_deltas = defaultdict(list)
        bucket_ml_deltas = defaultdict(list)
        overall_rule_deltas = []
        overall_ml_deltas = []

        for row in records.values():
            if row["_month_label"] not in test_month_labels:
                continue
            bucket_rule_deltas[row["bucket"]].append(row[rule_delta_key])
            bucket_ml_deltas[row["bucket"]].append(row[ml_delta_key])
            overall_rule_deltas.append(row[rule_delta_key])
            overall_ml_deltas.append(row[ml_delta_key])

        remaining_buckets = sorted((set(bucket_rule_deltas) | set(bucket_ml_deltas)) - set(BUCKET_ORDER))
        summary_rows = []
        for bucket in BUCKET_ORDER + remaining_buckets:
            summary_rows.append(
                {
                    "bucket": bucket,
                    "rule_based_avg_abs_error_pct": _mean_absolute(bucket_rule_deltas.get(bucket, [])),
                    "ml_based_avg_abs_error_pct": _mean_absolute(bucket_ml_deltas.get(bucket, [])),
                }
            )

        summary_rows.append(
            {
                "bucket": "Overall",
                "rule_based_avg_abs_error_pct": _mean_absolute(overall_rule_deltas),
                "ml_based_avg_abs_error_pct": _mean_absolute(overall_ml_deltas),
            }
        )
        summaries[metric_name] = summary_rows

    return summaries


def _build_error_threshold_summaries(records, test_month_labels):
    metric_configs = [
        ("purchase", "purchase_rule_delta_pct", "purchase_ml_delta_pct"),
        ("refi", "refi_rule_delta_pct", "refi_ml_delta_pct"),
        ("total", "total_rule_delta_pct", "total_ml_delta_pct"),
    ]
    summaries = {}

    for metric_name, rule_delta_key, ml_delta_key in metric_configs:
        rule_errors_by_nmls = defaultdict(list)
        ml_errors_by_nmls = defaultdict(list)

        for row in records.values():
            if row["_month_label"] not in test_month_labels:
                continue
            rule_errors_by_nmls[row["nmls"]].append(abs(row[rule_delta_key]))
            ml_errors_by_nmls[row["nmls"]].append(abs(row[ml_delta_key]))

        all_nmls = sorted(set(rule_errors_by_nmls) | set(ml_errors_by_nmls))
        if not all_nmls:
            summaries[metric_name] = []
            continue

        rule_avg_abs_by_nmls = {nmls: _mean(rule_errors_by_nmls.get(nmls, [])) for nmls in all_nmls}
        ml_avg_abs_by_nmls = {nmls: _mean(ml_errors_by_nmls.get(nmls, [])) for nmls in all_nmls}
        total_los = len(all_nmls)

        summary_rows = []
        for threshold in ERROR_THRESHOLDS:
            rule_count = sum(1 for value in rule_avg_abs_by_nmls.values() if value <= threshold)
            ml_count = sum(1 for value in ml_avg_abs_by_nmls.values() if value <= threshold)
            summary_rows.append(
                {
                    "error_pct_threshold": f"{threshold}%",
                    "rule_based_num_los_within_threshold": rule_count,
                    "rule_based_cumulative_pct_of_los": round((rule_count / total_los) * 100, 2),
                    "ml_based_num_los_within_threshold": ml_count,
                    "ml_based_cumulative_pct_of_los": round((ml_count / total_los) * 100, 2),
                }
            )
        summaries[metric_name] = summary_rows

    return summaries
