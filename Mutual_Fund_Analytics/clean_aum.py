
import pandas as pd
import glob
import os

files = glob.glob("data/raw/*aum_by_fund_house.csv")

if not files:
    raise FileNotFoundError("AUM dataset not found")

df = pd.read_csv(files[0])

print("Original shape:", df.shape)

# Convert date
df["date"] = pd.to_datetime(
    df["date"], errors="coerce"
)

# Convert numeric columns
numeric_columns = [
    "aum_lakh_crore",
    "aum_crore",
    "num_schemes"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove duplicate fund house-date combinations
before = len(df)

df = df.drop_duplicates(
    subset=["date", "fund_house"],
    keep="last"
)

print("Duplicates removed:", before - len(df))

# Check invalid values
print("Invalid dates:", df["date"].isna().sum())

print("Invalid AUM values:",
      ((df["aum_crore"] <= 0) |
       (df["aum_lakh_crore"] <= 0)).sum())

print("Invalid scheme counts:",
      (df["num_schemes"] < 0).sum())

# Remove invalid records
df = df.dropna(
    subset=["date", "fund_house",
            "aum_lakh_crore", "aum_crore", "num_schemes"]
)

df = df[
    (df["aum_crore"] > 0) &
    (df["aum_lakh_crore"] > 0) &
    (df["num_schemes"] >= 0)
]

# Save
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/aum_by_fund_house_cleaned.csv",
    index=False
)

print("\nCleaning completed!")
print("Final shape:", df.shape)
print("Saved: data/processed/aum_by_fund_house_cleaned.csv")
