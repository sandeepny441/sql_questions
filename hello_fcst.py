df_uwm_creation:

import pandas as pd
import numpy as np

import pandas as pd
from datetime import datetime


# ─────────────────────────────────────────────────────────────
# 1. Define RUN_DATE as today's date (when the script is executed)
# ─────────────────────────────────────────────────────────────
from datetime import datetime, date

# Default: today's date
RUN_DATE = datetime.now().date()
print(f"RUN_DATE: {RUN_DATE}")

# # Override with a specific date (still a date object)
# RUN_DATE = date(2026, 3, 8)
# print(f"RUN_DATE: {RUN_DATE}")

# Current year-month based on run date (YYYY-MM format)
current_month_str = RUN_DATE.strftime('%Y-%m')
print(current_month_str)


import pandas as pd

data = {
    'NMLS': [
        1525255537,     # Example 1
        1666017,        # Example 2
        12285553        # Example 3 (includes the only Refi in the original data)
    ],
    'loan_purpose': [
        'Purchase_uwm',
        'Purchase_uwm',
        'Refi_uwm'
    ],
    'sale_date': [
        '2025-11-13',
        '2025-11-18',
        '2025-11-26'
    ]
}

df_uwm = pd.DataFrame(data)

# Convert sale_date to datetime (recommended for any date-based analysis)
df_uwm['sale_date'] = pd.to_datetime(df_uwm['sale_date'])

# Preview
df_uwm

import pandas as pd

# Assuming df_uwm already exists with columns: NMMLS, loan_purpose, sale_date

# Create the desired structure
df_uwm_sales_by_date = df_uwm[['NMLS', 'sale_date', 'loan_purpose']].copy()

# Convert sale_date to datetime (if not already)
df_uwm_sales_by_date['sale_date'] = pd.to_datetime(df_uwm_sales_by_date['sale_date'])

# Create the count columns
df_uwm_sales_by_date['purchase_uwm'] = (df_uwm_sales_by_date['loan_purpose'] == 'Purchase_uwm').astype(int)
df_uwm_sales_by_date['refi_uwm']     = (df_uwm_sales_by_date['loan_purpose'] == 'Refi_uwm').astype(int)

# Select final columns and sort
df_uwm_sales_by_date = df_uwm_sales_by_date[['NMLS', 'sale_date', 'purchase_uwm', 'refi_uwm']] \
    .sort_values('sale_date') \
    .reset_index(drop=True)

# Optional: drop the temporary loan_purpose column if desired
# df_uwm_sales_by_date = df_uwm_sales_by_date.drop(columns=['loan_purpose'], errors='ignore')


df_uwm_sales_by_date


# ─────────────────────────────────────────────────────────────
# 2. Your original preparation steps
# ─────────────────────────────────────────────────────────────
df_uwm['sale_month'] = df_uwm['sale_date'].dt.to_period('M').astype(str)
df_uwm['purchase_uwm'] = (df_uwm['loan_purpose'] == 'Purchase_uwm').astype(int)
df_uwm['refi_uwm']     = (df_uwm['loan_purpose'] == 'Refi_uwm').astype(int)

# Get unique NMLS IDs
unique_nmls = df_uwm['NMLS'].unique()

# ─────────────────────────────────────────────────────────────
# 3. Generate months — include current month explicitly
# ─────────────────────────────────────────────────────────────
# Historical months: Jan 2025 → current month (inclusive)
months = pd.date_range(
    start='2025-01-01',
    end=RUN_DATE,
    freq='MS'
).strftime('%Y-%m').tolist()

# If current month is not already in the list (edge case), add it
if current_month_str not in months:
    months.append(current_month_str)

# ─────────────────────────────────────────────────────────────
# 4. Create full grid: every NMLS × every relevant month
# ─────────────────────────────────────────────────────────────
full_grid = pd.DataFrame(
    [(n, m) for n in unique_nmls for m in months],
    columns=['NMLS', 'sale_month']
)

# ─────────────────────────────────────────────────────────────
# 5. Aggregate actual data
# ─────────────────────────────────────────────────────────────
agg = df_uwm.groupby(['NMLS', 'sale_month'], as_index=False)[
    ['purchase_uwm', 'refi_uwm']
].sum()

# ─────────────────────────────────────────────────────────────
# 6. Merge + fill missing months (including current month) with 0
# ─────────────────────────────────────────────────────────────
df_uwm_monthly = full_grid.merge(
    agg,
    on=['NMLS', 'sale_month'],
    how='left'
).fillna({'purchase_uwm': 0, 'refi_uwm': 0})

# Ensure integer type
df_uwm_monthly[['purchase_uwm', 'refi_uwm']] = \
    df_uwm_monthly[['purchase_uwm', 'refi_uwm']].astype(int)

# Sort chronologically
df_uwm_monthly = df_uwm_monthly.sort_values(['NMLS', 'sale_month']).reset_index(drop=True)


df_uwm_monthly['purchase_uwm'] += np.random.randint(8, 16, size=len(df_uwm_monthly))
df_uwm_monthly['refi_uwm']     += np.random.randint(5, 11,  size=len(df_uwm_monthly))

with pd.option_context("display.max_rows", 500):
    display(df_uwm_monthly.head(60))

# df_uwm_monthly.to_csv('df_uwm_monthly.csv', index = None)

# ==================================
# ==================================
# ==================================

import pandas as pd
import numpy as np
import pandas as pd
from datetime import datetime

# ─────────────────────────────────────────────────────────────
# 1. Define RUN_DATE as today's date (when the script is executed)
# ─────────────────────────────────────────────────────────────
from datetime import datetime, date
# ─────────────────────────────────────────────────────────────
# 1. Define RUN_DATE as today's date (when the script is executed)
# ─────────────────────────────────────────────────────────────
RUN_DATE = datetime.now().date()
print(f"RUN_DATE: {RUN_DATE}")

# Current year-month string (YYYY-MM)
current_month_str = RUN_DATE.strftime('%Y-%m')

import pandas as pd

data = {
    'NMLS': [
        1525255537,     # Same as DF_UWM #1
        1666017,        # Same as DF_UWM #2
        12285553        # Same as DF_UWM #3
    ],
    'sale_date': [
        '2025-09-05',   # Example date with Refi_all (from original cotality sample)
        '2025-01-03',   # Example date with Purchase_all
        '2025-10-10'    # Another Purchase_all date
    ],
    'lender_name': [
        'UNITED WHOLESALE MTG',   # UWM
        'UNITED WHOLESALE MTG',   # UWM
        'JMAC LENDING'            # Non-UWM lender (to show diversity)
    ],
    'loan_purpose': [
        'Refi_all',
        'Purchase_all',
        'Purchase_all'
    ]
}

df_cotality = pd.DataFrame(data)

# Convert sale_date to datetime
df_cotality['sale_date'] = pd.to_datetime(df_cotality['sale_date'])

# Preview
df_cotality

import pandas as pd

# Assuming df_cotality already exists with columns: NMLS, sale_date, lender_name, loan_purpose

df_cotality_sales_by_date = df_cotality[['NMLS', 'sale_date', 'loan_purpose']].copy()

# Ensure sale_date is datetime
df_cotality_sales_by_date['sale_date'] = pd.to_datetime(df_cotality_sales_by_date['sale_date'])

# Create indicator columns
df_cotality_sales_by_date['purchase_all'] = (df_cotality_sales_by_date['loan_purpose'] == 'Purchase_all').astype(int)
df_cotality_sales_by_date['refi_all']     = (df_cotality_sales_by_date['loan_purpose'] == 'Refi_all').astype(int)

# Final selection, sorting, and reset index
df_cotality_sales_by_date = df_cotality_sales_by_date[['NMLS', 'sale_date', 'purchase_all', 'refi_all']] \
    .sort_values('sale_date') \
    .reset_index(drop=True)

df_cotality_sales_by_date





# ─────────────────────────────────────────────────────────────
# 2. Prepare the base data
# ─────────────────────────────────────────────────────────────
df_cotality['sale_date'] = pd.to_datetime(df_cotality['sale_date'])
df_cotality['sale_month'] = df_cotality['sale_date'].dt.to_period('M').astype(str)

df_cotality['purchase_all'] = (df_cotality['loan_purpose'] == 'Purchase_all').astype(int)
df_cotality['refi_all']     = (df_cotality['loan_purpose'] == 'Refi_all').astype(int)

# ─────────────────────────────────────────────────────────────
# 3. Lifetime total distinct lenders (unchanged)
# ─────────────────────────────────────────────────────────────
total_lenders_per_nmls = (
    df_cotality
    .groupby('NMLS')['lender_name']
    .nunique()
    .reset_index(name='total_lenders_ever')
)

# ─────────────────────────────────────────────────────────────
# 4. Get unique NMLS
# ─────────────────────────────────────────────────────────────
unique_nmls = df_cotality['NMLS'].unique()

# ─────────────────────────────────────────────────────────────
# 5. Generate months: Jan 2025 → current month (inclusive)
# ─────────────────────────────────────────────────────────────
months = pd.date_range(
    start='2025-01-01',
    end=RUN_DATE,
    freq='MS'
).strftime('%Y-%m').tolist()

# Safety check: make sure current month is included
if current_month_str not in months:
    months.append(current_month_str)

# ─────────────────────────────────────────────────────────────
# 6. Create full grid: every NMLS × every relevant month
# ─────────────────────────────────────────────────────────────
full_grid = pd.DataFrame(
    [(n, m) for n in unique_nmls for m in months],
    columns=['NMLS', 'sale_month']
)

# ─────────────────────────────────────────────────────────────
# 7. Aggregate monthly counts (including monthly distinct lenders)
# ─────────────────────────────────────────────────────────────
agg_monthly = df_cotality.groupby(['NMLS', 'sale_month'], as_index=False).agg(
    purchase_all=('purchase_all', 'sum'),
    refi_all=('refi_all', 'sum'),
    num_lenders_this_month=('lender_name', 'nunique')
)

# ─────────────────────────────────────────────────────────────
# 8. Merge + fill missing months (including current month) with 0
# ─────────────────────────────────────────────────────────────
df_cotality_monthly = (
    full_grid
    .merge(agg_monthly, on=['NMLS', 'sale_month'], how='left')
    .merge(total_lenders_per_nmls, on='NMLS', how='left')
    .fillna({
        'purchase_all': 0,
        'refi_all': 0,
        'num_lenders_this_month': 0,
        'total_lenders_ever': 0
    })
)

# Ensure integer types
int_cols = ['purchase_all', 'refi_all', 'num_lenders_this_month', 'total_lenders_ever']
df_cotality_monthly[int_cols] = df_cotality_monthly[int_cols].astype(int)

# Sort chronologically
df_cotality_monthly = df_cotality_monthly.sort_values(['NMLS', 'sale_month']).reset_index(drop=True)

# Optional full preview (first 25 rows or more)
with pd.option_context("display.max_rows", 500):
    display(df_cotality_monthly.head(50))


# Apply inflation ~10× larger than the previous UWM adjustment
df_cotality_monthly['purchase_all'] += np.random.randint(80, 151, size=len(df_cotality_monthly))
df_cotality_monthly['refi_all']     += np.random.randint(50, 101, size=len(df_cotality_monthly))

df_cotality_monthly = df_cotality_monthly.drop(columns = ['num_lenders_this_month', 'total_lenders_ever'])

with pd.option_context("display.max_rows", 500):
    display(df_cotality_monthly[:])

# df_cotality_monthly.to_csv('df_cotality_monthly.csv', index = None)

# ==================================
# ==================================
# ==================================
# Current date & month (hard-coded for clarity, but you can keep using RUN_DATE)
import pandas as pd
from datetime import datetime, date

# ─────────────────────────────────────────────────────────────
# RUN_DATE: Choose how the current date is determined
# ─────────────────────────────────────────────────────────────

# Option A: Use today's actual date (recommended for production/live runs)
RUN_DATE = datetime.now().date()

# Option B: Hard-code a specific date for testing / backtesting
# RUN_DATE = date(2026, 1, 8)   # Example: January 8, 2026
# RUN_DATE = date(2025, 12, 15) # Another example

print(f"RUN_DATE used: {RUN_DATE}")
print(f"Current month (YYYY-MM): {RUN_DATE.strftime('%Y-%m')}")

# For pandas date operations
CURRENT_DATE = pd.to_datetime(RUN_DATE)
CURRENT_MONTH = CURRENT_DATE.strftime('%Y-%m')


import pandas as pd 
import numpy as np 

import os
os.listdir()

df_uwm_monthly = pd.read_csv("df_uwm_monthly.csv")
df_cotality_monthly = pd.read_csv("df_cotality_monthly.csv")

df_uwm_monthly.tail()

df_cotality_monthly.head()

import pandas as pd

# Merge the two monthly dataframes
df_merged = pd.merge(
    df_uwm_monthly[['NMLS', 'sale_month', 'purchase_uwm', 'refi_uwm']],
    df_cotality_monthly[['NMLS', 'sale_month', 'purchase_all', 'refi_all']],
    on=['NMLS', 'sale_month'],
    how='outer'           # keep all months even if one side is missing
).fillna(0)               # fill missing values with 0

# Rename the four key count columns with "_actuals" suffix
df_merged = df_merged.rename(columns={
    'purchase_uwm': 'purchase_uwm_actuals',
    'refi_uwm':     'refi_uwm_actuals',
    'purchase_all': 'purchase_all_actuals',
    'refi_all':     'refi_all_actuals'
})

# Sort for clean presentation (by NMLS then chronological month)
df_merged = df_merged.sort_values(['NMLS', 'sale_month']).reset_index(drop=True)

# Add the two new forecast columns filled with 0
df_merged['purchase_all_fcst_rule'] = 0
df_merged['refi_all_fcst_rule'] = 0
df_merged['purchase_all_fcst_ml'] = 0
df_merged['refi_all_fcst_ml'] = 0

# Optional: make sure they're integers
df_merged['purchase_all_fcst_rule'] = df_merged['purchase_all_fcst_rule'].astype(int)
df_merged['refi_all_fcst_rule'] = df_merged['refi_all_fcst_rule'].astype(int)
df_merged['purchase_all_fcst_ml'] = df_merged['purchase_all_fcst_ml'].astype(int)
df_merged['refi_all_fcst_ml'] = df_merged['refi_all_fcst_ml'].astype(int)


with pd.option_context("display.max_rows", 500):
    display(df_merged.head(40))

# # Rule based logic in detail

# Run month (M) = Current month = January 2026 (M = '2026-01')
# Forecast window = Most recent 3 months including current:
# → Nov 2025, Dec 2025, Jan 2026
# But for UWM pace/trend calculation → use only the last 2 completed months (exclude current month)
# → Nov 2025 + Dec 2025 ÷ 2 = recent UWM pace
# Baseline window = 4 months immediately before the forecast window:
# → Jul 2025, Aug 2025, Sep 2025, Oct 2025


# For each broker (NMLS) separately, and separately for Purchase and Refi:

# Baseline market volume (per broker)
# Total purchase_all_actuals (or refi_all_actuals) of this broker in the 4 baseline months (Jul–Oct 2025) ÷ 4
# Baseline UWM pace (market-wide, not per broker)
# Total purchase_uwm_actuals (or refi_uwm_actuals) across all brokers in the same 4 baseline months ÷ 4
# Recent UWM pace (market-wide trend signal)
# Total purchase_uwm_actuals (or refi_uwm_actuals) across all brokers in the last 2 completed months (Nov + Dec 2025) ÷ 2
# Trend adjustment factor (percent change)(recent_UWM_pace - baseline_UWM_pace) / baseline_UWM_pace
# → If baseline UWM pace = 0 → set factor = 0 (no trend)
# Adjusted market forecast (per broker)baseline_market_volume_per_broker × (1 + percent_change)
# Apply this same adjusted monthly volume to all 3 months in the forecast window
# → Nov 2025, Dec 2025, Jan 2026 get the same forecast value (per broker, per loan type)

# This means:

# The trend signal comes from the overall UWM market behavior (all brokers combined)
# But the actual forecast level is scaled to each individual broker’s historical baseline volume


import pandas as pd
import numpy as np

# Define windows (relative to current month)
forecast_months = pd.date_range(
    end=CURRENT_DATE, periods=3, freq='MS'
).strftime('%Y-%m').tolist()   # ['2025-11', '2025-12', '2026-01']

baseline_end = pd.to_datetime(forecast_months[0]) - pd.offsets.MonthBegin(1)
baseline_months = pd.date_range(
    start=baseline_end - pd.offsets.MonthBegin(3),  # 4 months before Nov
    periods=4, freq='MS'
).strftime('%Y-%m').tolist()   # ['2025-07', '2025-08', '2025-09', '2025-10']

trend_months = forecast_months[:2]  # Only Nov + Dec for UWM pace



import pandas as pd
import numpy as np

# ─────────────────────────────────────────────────────────────
# RULE-BASED FORECAST LOGIC (applied after df_merged is ready)
# ─────────────────────────────────────────────────────────────

# 1. Define the time windows dynamically based on current run date/month
forecast_months = pd.date_range(
    end=RUN_DATE,
    periods=3,
    freq='MS'
).strftime('%Y-%m').tolist()   # e.g. ['2025-11', '2025-12', '2026-01']

# Baseline: 4 months immediately before the earliest forecast month
baseline_end = pd.to_datetime(forecast_months[0]) - pd.offsets.MonthBegin(1)
baseline_months = pd.date_range(
    start=baseline_end - pd.offsets.MonthBegin(3),  # 4 months back
    periods=4,
    freq='MS'
).strftime('%Y-%m').tolist()   # e.g. ['2025-07', '2025-08', '2025-09', '2025-10']

# Trend signal: only the 2 most recent **completed** months (exclude current)
trend_months = forecast_months[:2]  # e.g. ['2025-11', '2025-12']

print(f"Forecast window (3 months incl. current): {', '.join(forecast_months)}")
print(f"Baseline window (4 months): {', '.join(baseline_months)}")
print(f"Trend signal from (2 completed months): {', '.join(trend_months)}")

# ─────────────────────────────────────────────────────────────
# Step 1: Calculate market-wide UWM paces (aggregate across ALL brokers)
# ─────────────────────────────────────────────────────────────
# Baseline (4 months) average UWM volume per month
baseline_uwm_purchase = df_merged[
    df_merged['sale_month'].isin(baseline_months)
]['purchase_uwm_actuals'].sum() / 4

baseline_uwm_refi = df_merged[
    df_merged['sale_month'].isin(baseline_months)
]['refi_uwm_actuals'].sum() / 4

# Recent (2 completed months) average UWM volume per month
recent_uwm_purchase = df_merged[
    df_merged['sale_month'].isin(trend_months)
]['purchase_uwm_actuals'].sum() / 2

recent_uwm_refi = df_merged[
    df_merged['sale_month'].isin(trend_months)
]['refi_uwm_actuals'].sum() / 2

# Trend adjustment factors (market-wide)
purchase_trend_factor = (
    (recent_uwm_purchase - baseline_uwm_purchase) / baseline_uwm_purchase
    if baseline_uwm_purchase != 0 else 0.0
)

refi_trend_factor = (
    (recent_uwm_refi - baseline_uwm_refi) / baseline_uwm_refi
    if baseline_uwm_refi != 0 else 0.0
)

# ─────────────────────────────────────────────────────────────
# Print UWM Overall Market Trend Summary
# ─────────────────────────────────────────────────────────────
print("\n" + "┌" + "─" * 60 + "┐")
print(f"  UWM OVERALL MARKET TREND SUMMARY (Aggregate across all brokers)")
print(f"  RUN DATE: {RUN_DATE} | Current month: {CURRENT_MONTH}")
print("├" + "─" * 60 + "┤")
print(f"  Baseline period (4 months): {', '.join(baseline_months)}")
print(f"    → Avg monthly Purchase UWM: {baseline_uwm_purchase:.1f}")
print(f"    → Avg monthly Refi UWM:     {baseline_uwm_refi:.1f}")
print("│")
print(f"  Recent period (2 completed months): {', '.join(trend_months)}")
print(f"    → Avg monthly Purchase UWM: {recent_uwm_purchase:.1f}")
print(f"    → Avg monthly Refi UWM:     {recent_uwm_refi:.1f}")
print("│")
print("  Trend Adjustment Factor:")
print(f"    Purchase: {purchase_trend_factor:.3f}  ({purchase_trend_factor*100:+.1f}%)")
print(f"    Refi:     {refi_trend_factor:.3f}  ({refi_trend_factor*100:+.1f}%)")
print("└" + "─" * 60 + "┘")

# ─────────────────────────────────────────────────────────────
# Step 2: Per-broker baseline market volume (from the 4 baseline months)
# ─────────────────────────────────────────────────────────────
df_baseline_per_broker = df_merged[
    df_merged['sale_month'].isin(baseline_months)
].groupby('NMLS', as_index=False).agg(
    baseline_purchase=('purchase_all_actuals', 'sum'),
    baseline_refi=('refi_all_actuals', 'sum')
)

# Average monthly baseline per broker
df_baseline_per_broker['baseline_monthly_purchase'] = df_baseline_per_broker['baseline_purchase'] / 4
df_baseline_per_broker['baseline_monthly_refi']     = df_baseline_per_broker['baseline_refi'] / 4

# ─────────────────────────────────────────────────────────────
# Step 3: Apply market-wide trend adjustment → per-broker forecast
# ─────────────────────────────────────────────────────────────
df_baseline_per_broker['fcst_purchase_rule'] = (
    df_baseline_per_broker['baseline_monthly_purchase'] * (1 + purchase_trend_factor)
).round(0).astype(int)

df_baseline_per_broker['fcst_refi_rule'] = (
    df_baseline_per_broker['baseline_monthly_refi'] * (1 + refi_trend_factor)
).round(0).astype(int)

# ─────────────────────────────────────────────────────────────
# Step 4: Apply the same forecast value to all 3 forecast months per broker
# ─────────────────────────────────────────────────────────────
forecast_map_purchase = df_baseline_per_broker.set_index('NMLS')['fcst_purchase_rule'].to_dict()
forecast_map_refi     = df_baseline_per_broker.set_index('NMLS')['fcst_refi_rule'].to_dict()

# Apply only in the forecast window
mask_forecast = df_merged['sale_month'].isin(forecast_months)

df_merged.loc[mask_forecast, 'purchase_all_fcst_rule'] = \
    df_merged.loc[mask_forecast, 'NMLS'].map(forecast_map_purchase).fillna(0).astype(int)

df_merged.loc[mask_forecast, 'refi_all_fcst_rule'] = \
    df_merged.loc[mask_forecast, 'NMLS'].map(forecast_map_refi).fillna(0).astype(int)

# Optional: Quick sample preview of forecast application
# print("\nSample of forecast application (first few rows in forecast window):")
# print(df_merged[df_merged['sale_month'].isin(forecast_months)]
#       [['NMLS', 'sale_month', 'purchase_all_fcst_rule', 'refi_all_fcst_rule']]
#       .head(10))

df_merged


# df_merged.to_csv('final_forecast_df.csv', index = None)



