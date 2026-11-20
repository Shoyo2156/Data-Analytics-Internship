
import pandas as pd
import glob
import os

files = glob.glob("data/raw/*portfolio_holdings.csv")

if not files:
    raise FileNotFoundError("Portfolio holdings CSV not found")

df = pd.read_csv(files[0])

print("Original shape:", df.shape)

# Convert date
df["portfolio_date"] = pd.to_datetime(
    df["portfolio_date"], errors="coerce"
)

# Convert numeric columns
numeric_columns = [
    "amfi_code",
    "weight_pct",
    "market_value_cr",
    "current_price_inr"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Remove duplicate fund-stock-date records
before = len(df)

df = df.drop_duplicates(
    subset=["amfi_code", "stock_symbol", "portfolio_date"],
    keep="last"
)

print("\nDuplicates removed:", before - len(df))

# Check invalid values
print("Invalid dates:", df["portfolio_date"].isna().sum())
print("Invalid AMFI codes:", df["amfi_code"].isna().sum())
print("Invalid weights:", ((df["weight_pct"] < 0) | (df["weight_pct"] > 100)).sum())
print("Invalid market values:", (df["market_value_cr"] < 0).sum())
print("Invalid stock prices:", (df["current_price_inr"] <= 0).sum())

# Remove invalid essential records
df = df.dropna(
    subset=[
        "amfi_code", "stock_symbol", "portfolio_date",
        "weight_pct", "market_value_cr", "current_price_inr"
    ]
)

df = df[
    (df["weight_pct"] >= 0) &
    (df["weight_pct"] <= 100) &
    (df["market_value_cr"] >= 0) &
    (df["current_price_inr"] > 0)
]

# Save
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/portfolio_holdings_cleaned.csv",
    index=False
)

print("\nCleaning completed!")
print("Final shape:", df.shape)
print("Saved: data/processed/portfolio_holdings_cleaned.csv")
