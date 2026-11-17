import pandas as pd

# Load dataset
df = pd.read_excel("Data_Analytics_Day4_EDA/Online Retail.xlsx")

# Display first 5 rows
print(df.head())

# Dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Total missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# Missing values percentage
missing_percent = (df.isnull().sum() / len(df)) * 100

print("\nMissing Values Percentage:")
print(missing_percent)

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records
df_cleaned = df.drop_duplicates().copy()

print("\nOriginal Dataset Shape:")
print(df.shape)

print("\nCleaned Dataset Shape:")
print(df_cleaned.shape)

print("\nDuplicates Removed:")
print(df.shape[0] - df_cleaned.shape[0])

# Missing values after duplicate removal
print("\nMissing Values After Cleaning:")
print(df_cleaned.isnull().sum())

# Save cleaned dataset
df_cleaned.to_csv("cleaned_online_retail.csv", index=False)

print("\nCleaned dataset saved successfully!")

# Outlier Detection using IQR

Q1 = df_cleaned["Quantity"].quantile(0.25)
Q3 = df_cleaned["Quantity"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df_cleaned[
    (df_cleaned["Quantity"] < lower_limit) |
    (df_cleaned["Quantity"] > upper_limit)
]

print("\nLower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Total Outliers:", len(outliers))

# Display top 10 outlier records
print("\nTop 10 Outlier Records:")
print(outliers[["InvoiceNo", "Description", "Quantity", "UnitPrice", "Country"]].head(10))

# Calculate Revenue
df_cleaned["Revenue"] = (
    df_cleaned["Quantity"] * df_cleaned["UnitPrice"]
)

print("\nRevenue Column Added!")
print(df_cleaned[["Description", "Quantity", "UnitPrice", "Revenue"]].head(10))

# Country-wise Revenue Analysis

country_sales = df_cleaned.groupby("Country")["Revenue"].sum()

country_sales = country_sales.sort_values(ascending=False)

print("\nTop 10 Countries by Revenue:")
print(country_sales.head(10))

import matplotlib.pyplot as plt

# Top 10 countries chart
top_countries = country_sales.head(10)

plt.figure(figsize=(12, 6))
top_countries.plot(kind="bar")

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("country_revenue.png")
plt.savefig("country_revenue.png")
plt.close()

# Product-wise Revenue Analysis

product_sales = (
    df_cleaned.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Products by Revenue:")
print(product_sales.head(10))

product_sales = (
    df_cleaned.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Products by Revenue:")
print(product_sales.head(10))

# Product-wise Revenue Analysis

product_sales = (
    df_cleaned.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Products by Revenue:")
print(product_sales.head(10))

# Top 10 Products Revenue Chart

top_products = product_sales.head(10)

plt.figure(figsize=(12, 7))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig("product_revenue.png", format="png", bbox_inches="tight")
plt.close()

# Convert InvoiceDate to datetime
df_cleaned["InvoiceDate"] = pd.to_datetime(df_cleaned["InvoiceDate"])

# Extract month
df_cleaned["Month"] = df_cleaned["InvoiceDate"].dt.to_period("M")

# Monthly revenue
monthly_sales = df_cleaned.groupby("Month")["Revenue"].sum()

print("\nMonthly Revenue:")
print(monthly_sales)

# Monthly Revenue Trend Chart

plt.figure(figsize=(12, 6))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig("monthly_revenue.png", format="png")
plt.close()


# ==========================================
# STEP 27: CORRELATION ANALYSIS
# ==========================================

correlation = df_cleaned[
    ["Quantity", "UnitPrice", "Revenue"]
].corr()

print("\nCorrelation Matrix:")
print(correlation)


# ==========================================
# STEP 28: CORRELATION HEATMAP
# ==========================================

import seaborn as sns

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Sales Data Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()


# ==========================================
# STEP 29: KEY PERFORMANCE INDICATORS
# ==========================================

total_revenue = df_cleaned["Revenue"].sum()
total_transactions = df_cleaned["InvoiceNo"].nunique()
total_quantity = df_cleaned["Quantity"].sum()
average_revenue = df_cleaned["Revenue"].mean()

print("\n========== BUSINESS KPIs ==========")
print("Total Revenue:", round(total_revenue, 2))
print("Total Transactions:", total_transactions)
print("Total Quantity Sold:", total_quantity)
print("Average Line Revenue:", round(average_revenue, 2))


# ==========================================
# STEP 30: FINAL BUSINESS INSIGHTS
# ==========================================

best_country = country_sales.idxmax()
best_country_revenue = country_sales.max()

best_product = product_sales.idxmax()
best_product_revenue = product_sales.max()

best_month = monthly_sales.idxmax()
best_month_revenue = monthly_sales.max()

print("\n========== FINAL BUSINESS INSIGHTS ==========")

print("Top Revenue Country:", best_country)
print("Country Revenue:", round(best_country_revenue, 2))

print("Top Revenue Product:", best_product)
print("Product Revenue:", round(best_product_revenue, 2))

print("Best Revenue Month:", best_month)
print("Monthly Revenue:", round(best_month_revenue, 2))


# ==========================================
# STEP 31: SAVE FINAL CLEANED DATASET
# ==========================================

df_cleaned.to_csv("cleaned_online_retail.csv", index=False)

print("\nFinal EDA Analysis Completed Successfully!")
