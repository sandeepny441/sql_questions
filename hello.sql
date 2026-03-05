```python
import numpy as np
import pandas as pd

# Works directly on df_uwm (no copy, no df alias)

# 1) MonthPeriod from FundedDate (or Month if FundedDate is unavailable)
if "FundedDate" in df_uwm.columns:
    df_uwm["MonthPeriod"] = pd.to_datetime(df_uwm["FundedDate"], errors="coerce").dt.to_period("M")
elif "Month" in df_uwm.columns:
    df_uwm["MonthPeriod"] = pd.to_datetime(df_uwm["Month"], errors="coerce").dt.to_period("M")
else:
    raise ValueError("df_uwm must have FundedDate or Month")

# 2) Normalize Purpose -> Purchase / Refi
purpose_lower = df_uwm["Purpose"].astype(str).str.lower()
df_uwm["PurposeNorm"] = np.select(
    [
        purpose_lower.str.contains("purch", na=False),
        purpose_lower.str.contains("refi", na=False),
    ],
    ["Purchase", "Refi"],
    default=np.nan,
)

valid_sales_mask = df_uwm["MonthPeriod"].notna() & df_uwm["PurposeNorm"].isin(["Purchase", "Refi"])
group_cols = ["NMLS", "MonthPeriod", "PurposeNorm"]

# 3) Monthly Purchase/Refi counts
if "LoanID" in df_uwm.columns:
    monthly_counts = (
        df_uwm.loc[valid_sales_mask]
        .groupby(group_cols)["LoanID"]
        .nunique()
        .rename("Count")
        .reset_index()
    )
else:
    monthly_counts = (
        df_uwm.loc[valid_sales_mask]
        .groupby(group_cols)
        .size()
        .rename("Count")
        .reset_index()
    )

monthly = (
    monthly_counts.pivot_table(
        index=["NMLS", "MonthPeriod"],
        columns="PurposeNorm",
        values="Count",
        fill_value=0,
        aggfunc="sum",
    )
    .reset_index()
    .rename_axis(None, axis=1)
)

for c in ["Purchase", "Refi"]:
    if c not in monthly.columns:
        monthly[c] = 0
monthly["Total"] = monthly["Purchase"] + monthly["Refi"]

# 4) Build full NMLS x Month grid so missing months show 0 sales
all_nmls = df_uwm["NMLS"].dropna().unique()
all_months = pd.period_range(df_uwm["MonthPeriod"].min(), df_uwm["MonthPeriod"].max(), freq="M")

grid = pd.MultiIndex.from_product([all_nmls, all_months], names=["NMLS", "MonthPeriod"]).to_frame(index=False)
report = grid.merge(monthly, on=["NMLS", "MonthPeriod"], how="left")
report[["Purchase", "Refi", "Total"]] = report[["Purchase", "Refi", "Total"]].fillna(0).astype(int)

# 5) Num_States per NMLS
if "PropertyState" in df_uwm.columns:
    num_states = (
        df_uwm.dropna(subset=["NMLS", "PropertyState"])
        .groupby("NMLS")["PropertyState"]
        .nunique()
        .rename("Num_States")
        .reset_index()
    )
    report = report.merge(num_states, on="NMLS", how="left")
else:
    report["Num_States"] = pd.NA

# 6) Trailing last 12 months total (from latest month in dataset)
latest_month = report["MonthPeriod"].max()
start_month = latest_month - 11  # inclusive 12 months

trailing12 = (
    report.loc[(report["MonthPeriod"] >= start_month) & (report["MonthPeriod"] <= latest_month)]
    .groupby("NMLS")["Total"]
    .sum()
    .rename("Total_Sales_Last_12_Months")
    .reset_index()
)

report = report.merge(trailing12, on="NMLS", how="left")
report["Total_Sales_Last_12_Months"] = report["Total_Sales_Last_12_Months"].fillna(0).astype(int)

# 7) Final output sorted by last 12 months sales
report["Month"] = report["MonthPeriod"].dt.to_timestamp().dt.strftime("%m/%Y")

final_report = (
    report[
        ["NMLS", "Month", "Purchase", "Refi", "Total", "Total_Sales_Last_12_Months", "Num_States", "MonthPeriod"]
    ]
    .sort_values(["Total_Sales_Last_12_Months", "NMLS", "MonthPeriod"], ascending=[False, True, True])
    .drop(columns=["MonthPeriod"])
    .reset_index(drop=True)
)

final_report.head(50)
```
