
import pandas as pd
import glob
import os

files = glob.glob("data/raw/*benchmark_indices.csv")

if not files:
    raise FileNotFoundError("Benchmark indices CSV not found")

df = pd.read_csv(files[0])

print("Original shape:", df.shape)

# Convert date
df["date"] = pd.to_datetime(
    df["date"], errors="coerce"
)

# Convert close value to numeric
df["close_value"] = pd.to_numeric(
    df["close_value"], errors="coerce"
)

# Standardize index names
df["index_name"] = df["index_name"].astype(str).str.strip()

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Remove duplicate index-date records
before = len(df)

df = df.drop_duplicates(
    subset=["date", "index_name"],
    keep="last"
)

print("\nDuplicates removed:", before - len(df))

# Validate data
print("Invalid dates:", df["date"].isna().sum())
print("Invalid close values:",
      (df["close_value"].isna() | (df["close_value"] <= 0)).sum())

# Remove invalid records
df = df.dropna(
    subset=["date", "index_name", "close_value"]
)

df = df[df["close_value"] > 0]

# Save cleaned dataset
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/benchmark_indices_cleaned.csv",
    index=False
)

print("\nCleaning completed!")
print("Final shape:", df.shape)
print("Saved: data/processed/benchmark_indices_cleaned.csv")
