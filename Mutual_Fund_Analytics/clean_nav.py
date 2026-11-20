
import pandas as pd
import glob
import os

# Locate original NAV history CSV
files = glob.glob("data/raw/*nav_history.csv")

if not files:
    raise FileNotFoundError("NAV history CSV not found")

df = pd.read_csv(files[0])

print("Original shape:", df.shape)

# Convert date into datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Convert NAV into numeric
df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

# Check invalid dates
invalid_dates = df["date"].isna().sum()
print("Invalid dates:", invalid_dates)

# Sort by fund and date
df = df.sort_values(["amfi_code", "date"])

# Remove duplicate fund-date records
before = len(df)
df = df.drop_duplicates(
    subset=["amfi_code", "date"],
    keep="last"
)
print("Duplicates removed:", before - len(df))

# Forward-fill missing NAV within each fund
missing_before = df["nav"].isna().sum()

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

print("Missing NAV before fill:", missing_before)
print("Missing NAV after fill:", df["nav"].isna().sum())

# Validate NAV > 0
invalid_nav = (df["nav"] <= 0).sum()
print("Invalid NAV values:", invalid_nav)

# Remove invalid dates and NAV values
df = df.dropna(subset=["date", "nav"])
df = df[df["nav"] > 0]

# Save cleaned dataset
os.makedirs("data/processed", exist_ok=True)

output = "data/processed/nav_history_cleaned.csv"
df.to_csv(output, index=False)

print("\nCleaning completed!")
print("Final shape:", df.shape)
print("Saved:", output)
print("\nData types:")
print(df.dtypes)
