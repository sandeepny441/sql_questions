from forecast_pipeline import run_forecast_pipeline

result = run_forecast_pipeline(df, run_month="2026-03")

forecast_df = result["forecast_df"]
purchase_bucket_error = result["bucket_error_tables"]["purchase"]
refi_bucket_error = result["bucket_error_tables"]["refi"]
total_bucket_error = result["bucket_error_tables"]["total"]

purchase_threshold_error = result["threshold_error_tables"]["purchase"]
refi_threshold_error = result["threshold_error_tables"]["refi"]
total_threshold_error = result["threshold_error_tables"]["total"]
