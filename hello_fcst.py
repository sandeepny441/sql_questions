"""
Copy-paste notebook blocks for running the forecast pipeline from an existing df.

Each block below is designed to be copied into Jupyter as a separate cell.
The code starts from a dataframe named `df`.
"""


# =============================================================================
# BLOCK 1: Imports and required-column check
# =============================================================================
"""
import pandas as pd
from forecast_pipeline import run_forecast_pipeline

REQUIRED_COLUMNS = [
    "nmls",
    "bucket",
    "month",
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

missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

print("Input rows:", len(df))
print("Unique NMLS:", df["nmls"].nunique())
print("Buckets:", sorted(df["bucket"].dropna().astype(str).unique().tolist()))
"""


# =============================================================================
# BLOCK 2: Run month and bucket job list
# =============================================================================
"""
run_month = "2026-03"

bucket_jobs = [
    ("mega", "mega_producer_480plus"),
    ("super", "super_producer_240_479"),
    ("high", "high_producer_120_239"),
    ("active", "active_producer_60_119"),
    ("standard", "standard_producer_25_59"),
    ("occasional", "occasional_lo_21_24"),
    ("part_time", "part_time_lo_16_20"),
    (
        "sparse",
        [
            "low_volume_lo_11_15",
            "minimal_lo_6_10",
            "dormant_lo_0_5",
        ],
    ),
    ("unknown", "unknown_bucket"),
]
"""


# =============================================================================
# BLOCK 3: Helper to run one bucket or bucket-group
# =============================================================================
"""
job_results = {}

def run_one_job(job_name, bucket_filter):
    print(f"Running job: {job_name} | bucket_filter={bucket_filter}")
    result = run_forecast_pipeline(
        df,
        run_month=run_month,
        bucket_filter=bucket_filter,
    )
    job_results[job_name] = result
    print("Rows returned:", len(result["forecast_df"]))
    print("Unique NMLS returned:", result["forecast_df"]["nmls"].nunique())
    print("Hybrid sources:", result["hybrid_sources"])
    return result
"""


# =============================================================================
# BLOCK 4: Example single-bucket run
# =============================================================================
"""
active_result = run_one_job("active", "active_producer_60_119")

active_result["forecast_df"].head()
"""


# =============================================================================
# BLOCK 5: Example sparse-bucket run
# =============================================================================
"""
sparse_result = run_one_job(
    "sparse",
    ["low_volume_lo_11_15", "minimal_lo_6_10", "dormant_lo_0_5"],
)

sparse_result["forecast_df"].head()
"""


# =============================================================================
# BLOCK 6: Run all bucket jobs one by one
# =============================================================================
"""
for job_name, bucket_filter in bucket_jobs:
    run_one_job(job_name, bucket_filter)
"""


# =============================================================================
# BLOCK 7: Combine all forecast outputs after all jobs finish
# =============================================================================
"""
final_forecast_df = pd.concat(
    [result["forecast_df"] for result in job_results.values()],
    ignore_index=True,
)

month_sort_key = pd.to_datetime(final_forecast_df["month"], format="%m/%Y", errors="coerce")
final_forecast_df = (
    final_forecast_df.assign(_month_sort_key=month_sort_key)
    .sort_values(["nmls", "_month_sort_key", "month"])
    .drop(columns="_month_sort_key")
    .reset_index(drop=True)
)

print(final_forecast_df.shape)
final_forecast_df.head()
"""


# =============================================================================
# BLOCK 8: Build final bucket-error tables from the combined forecast dataframe
# =============================================================================
"""
def get_test_month_labels(run_month_text):
    anchor = pd.Timestamp(run_month_text + "-01")
    test_months = [
        (anchor.to_period("M") - 4).to_timestamp().strftime("%m/%Y"),
        (anchor.to_period("M") - 3).to_timestamp().strftime("%m/%Y"),
    ]
    return test_months

test_month_labels = get_test_month_labels(run_month)

def make_bucket_error_table(forecast_df, metric_name):
    rule_col = f"{metric_name}_rule_delta_pct"
    ml_col = f"{metric_name}_ml_delta_pct"
    scoped = forecast_df[forecast_df["month"].isin(test_month_labels)].copy()

    summary = (
        scoped.groupby("bucket", dropna=False)
        .agg(
            rule_based_avg_abs_error_pct=(rule_col, lambda s: round(s.abs().mean(), 2)),
            ml_based_avg_abs_error_pct=(ml_col, lambda s: round(s.abs().mean(), 2)),
        )
        .reset_index()
    )

    overall = pd.DataFrame(
        [
            {
                "bucket": "Overall",
                "rule_based_avg_abs_error_pct": round(scoped[rule_col].abs().mean(), 2),
                "ml_based_avg_abs_error_pct": round(scoped[ml_col].abs().mean(), 2),
            }
        ]
    )

    return pd.concat([summary, overall], ignore_index=True)

purchase_bucket_error = make_bucket_error_table(final_forecast_df, "purchase")
refi_bucket_error = make_bucket_error_table(final_forecast_df, "refi")
total_bucket_error = make_bucket_error_table(final_forecast_df, "total")

purchase_bucket_error
"""


# =============================================================================
# BLOCK 9: Build final threshold-error tables from the combined forecast dataframe
# =============================================================================
"""
ERROR_THRESHOLDS = [1, 2, 3, 5, 7, 10, 12, 15, 20, 25, 30, 35, 40, 50]

def make_threshold_table(forecast_df, metric_name):
    rule_col = f"{metric_name}_rule_delta_pct"
    ml_col = f"{metric_name}_ml_delta_pct"
    scoped = forecast_df[forecast_df["month"].isin(test_month_labels)].copy()

    rule_by_nmls = (
        scoped.groupby("nmls", dropna=False)[rule_col]
        .apply(lambda s: s.abs().mean())
        .fillna(0)
    )
    ml_by_nmls = (
        scoped.groupby("nmls", dropna=False)[ml_col]
        .apply(lambda s: s.abs().mean())
        .fillna(0)
    )

    total_los = max(len(rule_by_nmls.index.union(ml_by_nmls.index)), 1)
    rows = []
    for threshold in ERROR_THRESHOLDS:
        rule_count = int((rule_by_nmls <= threshold).sum())
        ml_count = int((ml_by_nmls <= threshold).sum())
        rows.append(
            {
                "error_pct_threshold": f"{threshold}%",
                "rule_based_num_los_within_threshold": rule_count,
                "rule_based_cumulative_pct_of_los": round((rule_count / total_los) * 100, 2),
                "ml_based_num_los_within_threshold": ml_count,
                "ml_based_cumulative_pct_of_los": round((ml_count / total_los) * 100, 2),
            }
        )

    return pd.DataFrame(rows)

purchase_threshold_error = make_threshold_table(final_forecast_df, "purchase")
refi_threshold_error = make_threshold_table(final_forecast_df, "refi")
total_threshold_error = make_threshold_table(final_forecast_df, "total")

total_threshold_error
"""


# =============================================================================
# BLOCK 10: Optional saves
# =============================================================================
"""
final_forecast_df.to_csv("final_forecast_df.csv", index=False)
purchase_bucket_error.to_csv("purchase_bucket_error.csv", index=False)
refi_bucket_error.to_csv("refi_bucket_error.csv", index=False)
total_bucket_error.to_csv("total_bucket_error.csv", index=False)
purchase_threshold_error.to_csv("purchase_threshold_error.csv", index=False)
refi_threshold_error.to_csv("refi_threshold_error.csv", index=False)
total_threshold_error.to_csv("total_threshold_error.csv", index=False)
"""
