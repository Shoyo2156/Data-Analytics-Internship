
import pandas as pd
import glob
import os

files = glob.glob("data/raw/*scheme_performance.csv")

if not files:
    raise FileNotFoundError("Scheme performance CSV not found")

df = pd.read_csv(files[0])

print("Original shape:", df.shape)

# Return and performance columns
numeric_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

# Convert columns to numeric
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nMissing numeric values:")
print(df[numeric_columns].isna().sum())

# Expense ratio validation
expense_invalid = (
    (df["expense_ratio_pct"] < 0.1)
    | (df["expense_ratio_pct"] > 2.5)
)

print("\nExpense ratio outside 0.1%-2.5%:")
print(expense_invalid.sum())

print("\nExpense ratio anomalies:")
print(df.loc[expense_invalid, [
    "scheme_name", "expense_ratio_pct"
]])

# Flag unusually high/low returns for review
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

anomaly_flags = pd.DataFrame(index=df.index)

for col in return_columns:
    anomaly_flags[col + "_flag"] = (
        (df[col] < -100) | (df[col] > 200)
    )

df["return_anomaly"] = anomaly_flags.any(axis=1)

print("\nReturn anomaly records:")
print(df["return_anomaly"].sum())

# Save anomalies for review
os.makedirs("data/processed", exist_ok=True)

df[df["return_anomaly"] | expense_invalid].to_csv(
    "data/processed/performance_anomalies.csv",
    index=False
)

# Save cleaned data
df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("\nCleaning completed!")
print("Final shape:", df.shape)
print("Saved: data/processed/scheme_performance_cleaned.csv")
