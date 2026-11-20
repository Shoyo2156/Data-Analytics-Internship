# Bluestock Mutual Fund Analytics
# Data Dictionary

## 1. Project Overview

This document describes the structure, columns, data types, and business meaning of the 10 datasets used in the Bluestock Mutual Fund Analytics project.

**Purpose:** To provide a clear understanding of the datasets before performing exploratory data analysis (EDA) and building analytical dashboards.

**Source:** Original CSV datasets stored in `data/raw/`.

**Cleaned datasets:** Stored in `data/processed/`.

---

## 2. Dataset: Investor Transactions

**File:** `investor_transactions.csv`  
**Rows:** 32,778  
**Columns:** 13

| Column | Data Type | Description |
|---|---|---|
| investor_id | Object | Unique investor identifier |
| transaction_date | Datetime | Date of transaction |
| amfi_code | Integer | Mutual fund scheme AMFI code |
| transaction_type | Object | SIP, Lumpsum, or Redemption |
| amount_inr | Integer | Transaction amount in INR |
| state | Object | Investor's state |
| city | Object | Investor's city |
| city_tier | Object | City classification |
| age_group | Object | Investor age category |
| gender | Object | Investor gender |
| annual_income_lakh | Float | Annual income in lakh |
| payment_mode | Object | Mode of transaction payment |
| kyc_status | Object | KYC verification status |

## 3. Dataset: Portfolio Holdings

**File:** `portfolio_holdings.csv`  
**Rows:** 322  
**Columns:** 8

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Mutual fund scheme AMFI code |
| stock_symbol | Object | Stock market symbol |
| stock_name | Object | Company or stock name |
| sector | Object | Industry sector |
| weight_pct | Float | Portfolio allocation percentage |
| market_value_cr | Float | Market value in crore |
| current_price_inr | Float | Current stock price in INR |
| portfolio_date | Datetime | Portfolio reporting date |

## 4. Dataset: Benchmark Indices

**File:** `benchmark_indices.csv`  
**Rows:** 8,050  
**Columns:** 3

| Column | Data Type | Description |
|---|---|---|
| date | Datetime | Benchmark observation date |
| index_name | Object | Name of benchmark index |
| close_value | Float | Closing index value |

## 5. Dataset: Fund Master

**File:** `fund_master.csv`  
**Rows:** 40  
**Columns:** 15

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Object | Mutual fund company |
| scheme_name | Object | Mutual fund scheme name |
| category | Object | Fund category |
| sub_category | Object | Fund sub-category |
| plan | Object | Direct or Regular plan |
| launch_date | Datetime | Scheme launch date |
| benchmark | Object | Scheme benchmark |
| expense_ratio_pct | Float | Expense ratio percentage |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Integer | Minimum SIP investment |
| min_lumpsum_amount | Integer | Minimum lumpsum investment |
| fund_manager | Object | Fund manager name |
| risk_category | Object | Risk classification |
| sebi_category_code | Object | SEBI category code |

## 6. Dataset: NAV History

**File:** `nav_history.csv`  
**Rows:** 46,000  
**Columns:** 3

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Mutual fund scheme AMFI code |
| date | Datetime | NAV observation date |
| nav | Float | Net Asset Value of the scheme |

## 7. Dataset: AUM by Fund House

**File:** `aum_by_fund_house.csv`  
**Rows:** 90  
**Columns:** 5

| Column | Data Type | Description |
|---|---|---|
| date | Datetime | Reporting date |
| fund_house | Object | Mutual fund company |
| aum_lakh_crore | Float | Assets under management in lakh crore |
| aum_crore | Integer | Assets under management in crore |
| num_schemes | Integer | Number of schemes managed |

## 8. Dataset: Monthly SIP Inflows

**File:** `monthly_sip_inflows.csv`  
**Rows:** 48  
**Columns:** 6

| Column | Data Type | Description |
|---|---|---|
| month | Datetime | Reporting month |
| sip_inflow_crore | Integer | Monthly SIP inflow in crore |
| active_sip_accounts_crore | Float | Active SIP accounts in crore |
| new_sip_accounts_lakh | Float | New SIP accounts in lakh |
| sip_aum_lakh_crore | Float | SIP AUM in lakh crore |
| yoy_growth_pct | Float | Year-over-year growth percentage |

**Data Quality Note:** 12 missing values were found in `yoy_growth_pct`. These values were preserved during cleaning rather than replaced with zero.

## 9. Dataset: Category Inflows

**File:** `category_inflows.csv`  
**Rows:** 144  
**Columns:** 3

| Column | Data Type | Description |
|---|---|---|
| month | Datetime | Reporting month |
| category | Object | Mutual fund category |
| net_inflow_crore | Float | Net inflow in crore |

## 10. Dataset: Industry Folio Count

**File:** `industry_folio_count.csv`  
**Rows:** 21  
**Columns:** 6

| Column | Data Type | Description |
|---|---|---|
| month | Datetime | Reporting month |
| total_folios_crore | Float | Total folios in crore |
| equity_folios_crore | Float | Equity folios in crore |
| debt_folios_crore | Float | Debt folios in crore |
| hybrid_folios_crore | Float | Hybrid folios in crore |
| others_folios_crore | Float | Other category folios in crore |

## 11. Dataset: Scheme Performance

**File:** `scheme_performance.csv`  
**Rows:** 40  
**Columns:** 19 original columns

| Column | Data Type | Description |
|---|---|---|
| amfi_code | Integer | Mutual fund scheme AMFI code |
| scheme_name | Object | Scheme name |
| fund_house | Object | Mutual fund company |
| category | Object | Scheme category |
| plan | Object | Direct or Regular plan |
| return_1yr_pct | Float | One-year return percentage |
| return_3yr_pct | Float | Three-year return percentage |
| return_5yr_pct | Float | Five-year return percentage |
| benchmark_3yr_pct | Float | Three-year benchmark return |
| alpha | Float | Risk-adjusted excess return measure |
| beta | Float | Market sensitivity measure |
| sharpe_ratio | Float | Risk-adjusted return measure |
| sortino_ratio | Float | Downside risk-adjusted return measure |
| std_dev_ann_pct | Float | Annualized standard deviation |
| max_drawdown_pct | Float | Maximum observed drawdown |
| aum_crore | Integer | Assets under management in crore |
| expense_ratio_pct | Float | Expense ratio percentage |
| morningstar_rating | Integer | Morningstar rating |
| risk_grade | Object | Risk grade classification |

**Cleaning Note:** The cleaned performance dataset contains one additional derived column, `return_anomaly`, used to flag unusual return values.

---

## 12. Data Cleaning Summary

The following cleaning and validation activities were performed:

- Converted date columns into appropriate datetime formats.
- Checked and removed duplicate records where applicable.
- Validated numeric and financial values.
- Checked mutual fund AMFI codes.
- Validated NAV values.
- Checked portfolio holding weights.
- Preserved missing SIP YoY growth values.
- Created cleaned CSV files in `data/processed/`.

## 13. Database Integration

The cleaned datasets were loaded into a SQLite database named `bluestock_mf.db`.

The database contains two dimension tables and nine fact tables.

**Dimension tables:**
- dim_fund
- dim_date

**Fact tables:**
- fact_nav
- fact_transactions
- fact_performance
- fact_aum
- fact_benchmark
- fact_portfolio_holdings
- fact_monthly_sip_inflows
- fact_category_inflows
- fact_industry_folio_count

## 14. Conclusion

This data dictionary provides a reference for all 10 original datasets used in the Bluestock Mutual Fund Analytics project. It documents their structure and business meaning and supports the next stages of exploratory data analysis, SQL analytics, and dashboard development.
