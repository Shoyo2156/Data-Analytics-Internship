
import pandas as pd
import os
import glob

DATA_FOLDER = os.path.join("data", "raw")

# Find all CSV files automatically
files = sorted(glob.glob(os.path.join(DATA_FOLDER, "*.csv")))

datasets = {}

print("=" * 70)
print("BLUESTOCK MUTUAL FUND ANALYTICS - DATA INGESTION")
print("=" * 70)

for path in files:

    file = os.path.basename(path)

    try:
        df = pd.read_csv(path)
        datasets[file] = df

        print("\n" + "=" * 70)
        print("DATASET:", file)
        print("=" * 70)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"ERROR loading {file}: {e}")

print("\n" + "=" * 70)
print("DATA INGESTION COMPLETED")
print("Successfully Loaded:", len(datasets), "/", len(files))
print("=" * 70)


# ==========================================
# FUND MASTER EXPLORATION
# ==========================================


fund_file = [
    f for f in datasets.keys()
    if "01_fund_master.csv" in f
][0]

fund_master = datasets[fund_file]


print("\n" + "=" * 70)
print("FUND MASTER EXPLORATION")
print("=" * 70)

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub-Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

print("\nTotal Unique AMFI Codes:")
print(fund_master["amfi_code"].nunique())

print("\nFund House Count:")
print(fund_master["fund_house"].nunique())


# ==========================================
# AMFI CODE VALIDATION
# ==========================================

nav_file = [
    f for f in datasets.keys()
    if "02_nav_history.csv" in f
][0]

nav_history = datasets[nav_file]

# Extract unique AMFI codes
fund_codes = set(fund_master["amfi_code"].unique())
nav_codes = set(nav_history["amfi_code"].unique())

# Find matching and missing codes
matching_codes = fund_codes.intersection(nav_codes)
missing_codes = fund_codes - nav_codes

print("\n" + "=" * 70)
print("AMFI CODE VALIDATION")
print("=" * 70)

print("Unique Fund Master Codes:", len(fund_codes))
print("Unique NAV History Codes:", len(nav_codes))
print("Matching AMFI Codes:", len(matching_codes))
print("Missing AMFI Codes:", len(missing_codes))

if missing_codes:
    print("\nMissing Codes:")
    print(sorted(missing_codes))
else:
    print("\nSUCCESS: All Fund Master AMFI codes exist in NAV History!")

print("\nValidation Status:",
      "PASSED" if not missing_codes else "FAILED")
