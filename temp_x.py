
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

result = (
    df
    .groupby(["nmls", "month", "loan_purpose"])
    .size()
    .reset_index(name="loan_count")
)