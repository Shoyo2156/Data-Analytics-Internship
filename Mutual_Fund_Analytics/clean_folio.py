
import pandas as pd
import glob
import os

files = glob.glob("data/raw/*industry_folio_count.csv")

if not files:
    raise FileNotFoundError("Industry folio dataset not found")

df = pd.read_csv(files[0])

print("Original shape:", df.shape)

# Convert month to datetime
df["month"] = pd.to_datetime(
    df["month"], errors="coerce"
)

# Convert numeric columns
numeric_columns = [
    "total_folios_crore",
    "equity_folios_crore",
    "debt_folios_crore",
    "hybrid_folios_crore",
    "others_folios_crore"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Remove duplicate months
before = len(df)

df = df.drop_duplicates(
    subset=["month"],
    keep="last"
)

print("\nDuplicates removed:", before - len(df))

# Check invalid values
print("Invalid dates:", df["month"].isna().sum())

for col in numeric_columns:
    print(f"Negative values in {col}:", (df[col] < 0).sum())

# Remove invalid records
df = df.dropna(subset=["month"] + numeric_columns)

for col in numeric_columns:
    df = df[df[col] >= 0]

# Save cleaned dataset
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/industry_folio_count_cleaned.csv",
    index=False
)

print("\nCleaning completed!")
print("Final shape:", df.shape)
print("Saved: data/processed/industry_folio_count_cleaned.csv")
