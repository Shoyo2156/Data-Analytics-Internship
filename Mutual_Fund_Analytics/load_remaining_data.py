
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
import os

DB_PATH = "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DB_PATH}")

# Define remaining five tables
table_schemas = {
    "fact_benchmark": """
        CREATE TABLE IF NOT EXISTS fact_benchmark (
            date_key INTEGER NOT NULL,
            index_name TEXT NOT NULL,
            close_value REAL NOT NULL CHECK(close_value > 0),
            PRIMARY KEY (date_key, index_name),
            FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
        )
    """,

    "fact_portfolio_holdings": """
        CREATE TABLE IF NOT EXISTS fact_portfolio_holdings (
            amfi_code INTEGER NOT NULL,
            stock_symbol TEXT NOT NULL,
            stock_name TEXT,
            sector TEXT,
            weight_pct REAL,
            market_value_cr REAL,
            current_price_inr REAL,
            date_key INTEGER NOT NULL,
            PRIMARY KEY (amfi_code, stock_symbol, date_key),
            FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
            FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
        )
    """,

    "fact_monthly_sip_inflows": """
        CREATE TABLE IF NOT EXISTS fact_monthly_sip_inflows (
            date_key INTEGER PRIMARY KEY,
            sip_inflow_crore REAL,
            active_sip_accounts_crore REAL,
            new_sip_accounts_lakh REAL,
            sip_aum_lakh_crore REAL,
            yoy_growth_pct REAL,
            FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
        )
    """,

    "fact_category_inflows": """
        CREATE TABLE IF NOT EXISTS fact_category_inflows (
            date_key INTEGER NOT NULL,
            category TEXT NOT NULL,
            net_inflow_crore REAL,
            PRIMARY KEY (date_key, category),
            FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
        )
    """,

    "fact_industry_folio_count": """
        CREATE TABLE IF NOT EXISTS fact_industry_folio_count (
            date_key INTEGER PRIMARY KEY,
            total_folios_crore REAL,
            equity_folios_crore REAL,
            debt_folios_crore REAL,
            hybrid_folios_crore REAL,
            others_folios_crore REAL,
            FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
        )
    """
}

# Create tables
with sqlite3.connect(DB_PATH) as conn:
    conn.execute("PRAGMA foreign_keys = ON")

    for table, schema in table_schemas.items():
        conn.execute(schema)

print("Five additional tables created successfully!")

# Function to load a dataset
def load_dataset(file_path, table_name, date_column):
    df = pd.read_csv(file_path)

    df[date_column] = pd.to_datetime(
        df[date_column], errors="coerce"
    ).dt.strftime("%Y-%m-%d")

    # Get date key from dim_date
    date_map_df = pd.read_sql(
        "SELECT date_key, full_date FROM dim_date",
        engine
    )

    date_map = dict(
        zip(date_map_df["full_date"], date_map_df["date_key"])
    )

    df["date_key"] = df[date_column].map(date_map)

    if df["date_key"].isna().any():
        raise ValueError(
            f"Some dates in {file_path} are missing from dim_date"
        )

    df = df.drop(columns=[date_column])

    # Prevent accidental duplicate loading
    with engine.connect() as conn:
        count = conn.exec_driver_sql(
            f"SELECT COUNT(*) FROM {table_name}"
        ).scalar()

    if count > 0:
        raise RuntimeError(
            f"{table_name} already contains {count} rows. "
            "Not loading again."
        )

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    print(f"{table_name}: {len(df)} rows loaded")


# Load benchmark indices
load_dataset(
    "data/processed/benchmark_indices_cleaned.csv",
    "fact_benchmark",
    "date"
)

# Load portfolio holdings
load_dataset(
    "data/processed/portfolio_holdings_cleaned.csv",
    "fact_portfolio_holdings",
    "portfolio_date"
)

# Load monthly SIP inflows
load_dataset(
    "data/processed/monthly_sip_inflows_cleaned.csv",
    "fact_monthly_sip_inflows",
    "month"
)

# Load category inflows
load_dataset(
    "data/processed/category_inflows_cleaned.csv",
    "fact_category_inflows",
    "month"
)

# Load industry folio count
load_dataset(
    "data/processed/industry_folio_count_cleaned.csv",
    "fact_industry_folio_count",
    "month"
)

# Final verification
tables = list(table_schemas.keys())

print("\nFINAL VERIFICATION")

with engine.connect() as conn:
    for table in tables:
        count = conn.exec_driver_sql(
            f"SELECT COUNT(*) FROM {table}"
        ).scalar()

        print(f"{table}: {count} rows")

print("\nAll remaining datasets loaded successfully!")
