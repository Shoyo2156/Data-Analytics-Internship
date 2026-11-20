
import pandas as pd
import glob
import os

files = glob.glob("data/raw/*monthly_sip_inflows.csv")

if not files:
    raise FileNotFoundError("Monthly SIP dataset not found")

df = pd.read_csv(files[0])

print("Original shape:", df.shape)

# Convert month to datetime
df["month"] = pd.to_datetime(
    df["month"], errors="coerce"
)

# Convert numeric columns
numeric_columns = [
    "sip_inflow_crore",
    "active_sip_accounts_crore",
    "new_sip_accounts_lakh",
    "sip_aum_lakh_crore",
    "yoy_growth_pct"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove duplicate months
before = len(df)

df = df.drop_duplicates(
    subset=["month"],
    keep="last"
)

print("\nDuplicates removed:", before - len(df))

# Validate date
print("Invalid dates:", df["month"].isna().sum())

# Validate non-negative financial metrics
non_negative_columns = [
    "sip_inflow_crore",
    "active_sip_accounts_crore",
    "new_sip_accounts_lakh",
    "sip_aum_lakh_crore"
]

for col in non_negative_columns:
    print(
        f"Invalid {col}:",
        (df[col] < 0).sum()
    )

# Remove records with invalid essential fields
df = df.dropna(
    subset=["month"] + non_negative_columns
)

for col in non_negative_columns:
    df = df[df[col] >= 0]

# Keep missing YoY growth as NaN
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/monthly_sip_inflows_cleaned.csv",
    index=False
)

print("\nCleaning completed!")
print("Final shape:", df.shape)

print("\nRemaining missing values:")
print(df.isnull().sum())

print("\nSaved: data/processed/monthly_sip_inflows_cleaned.csv")
