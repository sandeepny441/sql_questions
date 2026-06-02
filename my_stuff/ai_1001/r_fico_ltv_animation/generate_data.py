#!/usr/bin/env python3
"""
Generate synthetic FICO vs LTV mortgage dataset matching the R script logic.
Exports fico_ltv_sample_data.csv (used by both R and Python versions).
"""

import numpy as np
import pandas as pd

np.random.seed(2024)
n_loans = 520

quarters = ["2023-Q1", "2023-Q2", "2023-Q3", "2023-Q4",
            "2024-Q1", "2024-Q2", "2024-Q3", "2024-Q4"]

# Base variables with correlation structure
fico_base = np.random.normal(726, 48, n_loans)
ltv_base = np.random.normal(82.5, 10.8, n_loans)

fico = np.clip(np.round(fico_base), 585, 848).astype(int)
ltv = np.clip(np.round(ltv_base), 51, 104).astype(int)

# Negative correlation: higher FICO → lower LTV tendency
ltv = np.clip(
    np.round(ltv - 0.034 * (fico - 720) + np.random.normal(0, 6.8, n_loans)),
    51, 104
).astype(int)

# Assign quarters with volume ramp (more loans later)
q_probs = np.array([0.22, 0.24, 0.26, 0.28, 0.20, 0.23, 0.27, 0.30])
q_probs = q_probs / q_probs.sum()
quarter_idx = np.random.choice(8, size=n_loans, p=q_probs)
quarter = np.array(quarters)[quarter_idx]
quarter_num = quarter_idx + 1

# Time-based shift (credit quality evolution)
fico_shift = (quarter_num - 4.5) * 1.35
ltv_shift = (quarter_num - 4.5) * -0.55

fico = np.clip(
    np.round(fico + fico_shift + np.random.normal(0, 4, n_loans)),
    585, 848
).astype(int)
ltv = np.clip(
    np.round(ltv + ltv_shift + np.random.normal(0, 3.5, n_loans)),
    51, 104
).astype(int)

# Risk segments
def risk_segment(f):
    if f >= 760: return "Super Prime"
    elif f >= 720: return "Prime"
    elif f >= 680: return "Near Prime"
    else: return "Subprime"

risk = np.array([risk_segment(x) for x in fico])
risk = pd.Categorical(risk, categories=["Super Prime", "Prime", "Near Prime", "Subprime"])

# Loan amounts
loan_amount = np.clip(
    np.round(np.random.normal(298000, 112000, n_loans)),
    92000, 685000
).astype(int)

# Purpose
purpose = np.random.choice(["Purchase", "Refinance"], n_loans, p=[0.61, 0.39])

df = pd.DataFrame({
    "loan_id": [f"LN{i:06d}" for i in range(1, n_loans + 1)],
    "fico": fico,
    "ltv": ltv,
    "quarter": pd.Categorical(quarter, categories=quarters),
    "quarter_num": quarter_num,
    "risk_segment": risk,
    "loan_amount": loan_amount,
    "purpose": purpose
})

# Sort for nicer ordering
df = df.sort_values(["quarter_num", "fico"]).reset_index(drop=True)

df.to_csv("fico_ltv_sample_data.csv", index=False)

print("=== Synthetic Mortgage Dataset Summary ===")
print(df[["fico", "ltv", "loan_amount"]].describe().round(1))
print("\nRisk segment distribution:")
print(df["risk_segment"].value_counts().reindex(["Super Prime","Prime","Near Prime","Subprime"]))
print("\nLoans per quarter:")
print(df["quarter"].value_counts().sort_index())
print(f"\n✓ Exported {len(df)} rows to fico_ltv_sample_data.csv")
