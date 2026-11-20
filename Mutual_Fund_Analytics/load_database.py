
import pandas as pd
import sqlite3
from sqlalchemy import create_engine, text
import os

DB_PATH = "bluestock_mf.db"
SCHEMA_PATH = "sql/schema.sql"

# Database connection
engine = create_engine(f"sqlite:///{DB_PATH}")

# Enable foreign keys
with engine.connect() as conn:
    conn.execute(text("PRAGMA foreign_keys = ON"))

# Execute schema
with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    schema = f.read()

raw_connection = sqlite3.connect(DB_PATH)
raw_connection.executescript(schema)
raw_connection.commit()
raw_connection.close()

print("Database schema created successfully!")

# Helper function
def load_table(file_path, table_name):
    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    print(f"{table_name}: {len(df)} rows loaded")


# Load dimension table
load_table(
    "data/processed/fund_master_cleaned.csv",
    "dim_fund"
)

# Create date dimension from all date-based datasets
date_columns = {
    "data/processed/nav_history_cleaned.csv": "date",
    "data/processed/investor_transactions_cleaned.csv": "transaction_date",
    "data/processed/benchmark_indices_cleaned.csv": "date",
    "data/processed/aum_by_fund_house_cleaned.csv": "date",
    "data/processed/monthly_sip_inflows_cleaned.csv": "month",
    "data/processed/category_inflows_cleaned.csv": "month",
    "data/processed/industry_folio_count_cleaned.csv": "month",
    "data/processed/portfolio_holdings_cleaned.csv": "portfolio_date"
}

all_dates = set()

for file_path, column in date_columns.items():
    df = pd.read_csv(file_path)
    dates = pd.to_datetime(df[column], errors="coerce").dropna()

    all_dates.update(dates.dt.strftime("%Y-%m-%d").tolist())

date_df = pd.DataFrame({"full_date": sorted(all_dates)})

date_df["date_key"] = date_df["full_date"].str.replace("-", "").astype(int)
date_df["date"] = pd.to_datetime(date_df["full_date"])
date_df["year"] = date_df["date"].dt.year
date_df["quarter"] = date_df["date"].dt.quarter
date_df["month"] = date_df["date"].dt.month
date_df["month_name"] = date_df["date"].dt.month_name()
date_df["day"] = date_df["date"].dt.day

date_df = date_df[
    ["date_key", "full_date", "year", "quarter",
     "month", "month_name", "day"]
]

date_df.to_sql(
    "dim_date",
    engine,
    if_exists="append",
    index=False
)

print("dim_date:", len(date_df), "rows loaded")

# Create date key mapping
date_map = dict(
    zip(date_df["full_date"], date_df["date_key"])
)

# Load NAV
nav = pd.read_csv("data/processed/nav_history_cleaned.csv")
nav["date"] = pd.to_datetime(nav["date"]).dt.strftime("%Y-%m-%d")
nav["date_key"] = nav["date"].map(date_map)

nav = nav[["amfi_code", "date_key", "nav"]]
nav.to_sql("fact_nav", engine, if_exists="append", index=False)

print("fact_nav:", len(nav), "rows loaded")

# Load transactions
transactions = pd.read_csv(
    "data/processed/investor_transactions_cleaned.csv"
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
).dt.strftime("%Y-%m-%d")

transactions["date_key"] = transactions[
    "transaction_date"
].map(date_map)

transactions = transactions.drop(columns=["transaction_date"])

transactions = transactions[
    [
        "investor_id", "amfi_code", "date_key",
        "transaction_type", "amount_inr", "state",
        "city", "city_tier", "age_group", "gender",
        "annual_income_lakh", "payment_mode", "kyc_status"
    ]
]

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="append",
    index=False
)

print("fact_transactions:", len(transactions), "rows loaded")

# Load performance
performance = pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
)

performance = performance.drop(columns=[
    "scheme_name", "fund_house", "category", "plan",
    "return_anomaly"
], errors="ignore")

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="append",
    index=False
)

print("fact_performance:", len(performance), "rows loaded")

# Load AUM
aum = pd.read_csv(
    "data/processed/aum_by_fund_house_cleaned.csv"
)

aum["date"] = pd.to_datetime(aum["date"]).dt.strftime("%Y-%m-%d")
aum["date_key"] = aum["date"].map(date_map)

aum = aum[
    ["date_key", "fund_house", "aum_lakh_crore",
     "aum_crore", "num_schemes"]
]

aum.to_sql("fact_aum", engine, if_exists="append", index=False)

print("fact_aum:", len(aum), "rows loaded")

# Verify counts
print("\nDATABASE VERIFICATION")

tables = [
    "dim_fund",
    "dim_date",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

with engine.connect() as conn:
    for table in tables:
        count = conn.execute(
            text(f"SELECT COUNT(*) FROM {table}")
        ).scalar()

        print(f"{table}: {count} rows")

print("\nDatabase loading completed!")
print("Database file:", DB_PATH)
