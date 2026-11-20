
import pandas as pd
import glob
import os

raw_files = glob.glob("data/raw/*.csv")

# Only the 10 original datasets
raw_files = [
    f for f in raw_files
    if any(name in os.path.basename(f) for name in [
        "investor_transactions",
        "portfolio_holdings",
        "benchmark_indices",
        "fund_master",
        "nav_history",
        "aum_by_fund_house",
        "monthly_sip_inflows",
        "category_inflows",
        "industry_folio_count",
        "scheme_performance"
    ])
]

cleaned_files = glob.glob("data/processed/*_cleaned.csv")

print("Original datasets:", len(raw_files))
print("Cleaned datasets:", len(cleaned_files))

print("\n" + "=" * 75)

for file in sorted(cleaned_files):
    df = pd.read_csv(file)

    print(
        os.path.basename(file),
        "| Rows:", len(df),
        "| Columns:", len(df.columns),
        "| Missing:", df.isnull().sum().sum()
    )

print("\n" + "=" * 75)
print("Verification completed!")
