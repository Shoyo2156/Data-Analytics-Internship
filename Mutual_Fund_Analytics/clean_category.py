
import pandas as pd
import glob
import os

files = glob.glob("data/raw/*category_inflows.csv")

if not files:
    raise FileNotFoundError("Category inflows CSV not found")

df = pd.read_csv(files[0])

print("Original shape:", df.shape)

# Convert month to datetime
df["month"] = pd.to_datetime(
    df["month"], errors="coerce"
)

# Convert net inflow to numeric
df["net_inflow_crore"] = pd.to_numeric(
    df["net_inflow_crore"], errors="coerce"
)

# Standardize category text
df["category"] = df["category"].astype(str).str.strip()

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate month-category combinations
before = len(df)

df = df.drop_duplicates(
    subset=["month", "category"],
    keep="last"
)

print("\nDuplicates removed:", before - len(df))

# Check invalid values
print("Invalid dates:", df["month"].isna().sum())
print("Invalid inflows:", df["net_inflow_crore"].isna().sum())

# Remove records with missing essential values
df = df.dropna(
    subset=["month", "category", "net_inflow_crore"]
)

# Save cleaned dataset
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/category_inflows_cleaned.csv",
    index=False
)

print("\nCleaning completed!")
print("Final shape:", df.shape)
print("Saved: data/processed/category_inflows_cleaned.csv")
