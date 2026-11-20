
import pandas as pd
import glob
import os

# Find investor transactions file
files = glob.glob("data/raw/*investor_transactions.csv")

if not files:
    raise FileNotFoundError("Investor transactions CSV not found")

df = pd.read_csv(files[0])

print("Original shape:", df.shape)

# Convert transaction date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.lower()
    .replace({
        "sip": "SIP",
        "lumpsum": "Lumpsum",
        "lump sum": "Lumpsum",
        "redemption": "Redemption"
    })
)

# Validate amount
df["amount_inr"] = pd.to_numeric(
    df["amount_inr"],
    errors="coerce"
)

# Standardize KYC status
df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.upper()
)

print("\nTransaction Types:")
print(df["transaction_type"].value_counts(dropna=False))

print("\nKYC Status Values:")
print(df["kyc_status"].value_counts(dropna=False))

# Check invalid values
valid_types = ["SIP", "Lumpsum", "Redemption"]

print("\nInvalid transaction types:",
      (~df["transaction_type"].isin(valid_types)).sum())

print("Invalid dates:", df["transaction_date"].isna().sum())

print("Invalid amounts:",
      (df["amount_inr"].isna() | (df["amount_inr"] <= 0)).sum())

# Save invalid records separately for review
invalid = (
    df["transaction_date"].isna()
    | df["amount_inr"].isna()
    | (df["amount_inr"] <= 0)
    | ~df["transaction_type"].isin(valid_types)
)

os.makedirs("data/processed", exist_ok=True)

df[invalid].to_csv(
    "data/processed/transactions_rejected.csv",
    index=False
)

# Keep only valid records
df = df[~invalid].copy()

df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("\nCleaning completed!")
print("Final shape:", df.shape)
print("Rejected records:", invalid.sum())
print("Saved: data/processed/investor_transactions_cleaned.csv")
