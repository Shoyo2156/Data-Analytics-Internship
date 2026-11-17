
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("sales_data.csv")

# KPI Calculations
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
total_orders = len(df)
total_quantity = df["Quantity"].sum()
highest_sale = df["Sales"].max()

# Region Analysis
region_sales = df.groupby("Region")["Sales"].sum()

# Product Analysis
product_sales = df.groupby("Product")["Sales"].sum()

# Display Business Report
print("\n========== SALES ANALYTICS DASHBOARD ==========")

print("\nKEY PERFORMANCE INDICATORS")
print("Total Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))
print("Total Orders:", total_orders)
print("Total Quantity:", total_quantity)
print("Highest Sale:", highest_sale)

print("\nREGION-WISE SALES")
print(region_sales)

print("\nPRODUCT-WISE SALES")
print(product_sales)

# Create Dashboard Charts
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

region_sales.plot(
    kind="bar",
    ax=axes[0],
    title="Region-wise Sales"
)

product_sales.plot(
    kind="bar",
    ax=axes[1],
    title="Product-wise Sales"
)

axes[0].set_xlabel("Region")
axes[0].set_ylabel("Sales Amount")

axes[1].set_xlabel("Product")
axes[1].set_ylabel("Sales Amount")
axes[1].tick_params(axis="x", rotation=45)

plt.tight_layout()

# Save Dashboard
plt.savefig(
    "charts/sales_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
