
import pandas as pd
import glob
import os

files = glob.glob("data/raw/*fund_master.csv")

if not files:
    raise FileNotFoundError("Fund master CSV not found")

df = pd.read_csv(files[0])

print("Original shape:", df.shape)

# Convert columns to correct data types
df["amfi_code"] = pd.to_numeric(
    df["amfi_code"], errors="coerce"
)

df["launch_date"] = pd.to_datetime(
    df["launch_date"], errors="coerce"
)

numeric_columns = [
    "expense_ratio_pct",
    "exit_load_pct",
    "min_sip_amount",
    "min_lumpsum_amount"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove duplicate AMFI codes
before = len(df)
df = df.drop_duplicates(
    subset=["amfi_code"],
    keep="last"
)

print("Duplicate AMFI codes removed:", before - len(df))

# Validate important fields
print("Missing AMFI codes:", df["amfi_code"].isna().sum())
print("Invalid expense ratios:",
      ((df["expense_ratio_pct"] < 0) |
       (df["expense_ratio_pct"] > 100)).sum())

# Save cleaned file
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/fund_master_cleaned.csv",
    index=False
)

print("\nCleaning completed!")
print("Final shape:", df.shape)
print("Saved: data/processed/fund_master_cleaned.csv")
print(df.dtypes)
