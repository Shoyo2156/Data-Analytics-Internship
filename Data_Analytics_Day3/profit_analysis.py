import pandas as pd

df = pd.read_csv("sales_data.csv")

df["Profit"] = df["Sales"] - df["Cost"]

total_sales = df["Sales"].sum()
total_cost = df["Cost"].sum()
total_profit = df["Profit"].sum()

profit_margin = (total_profit / total_sales) * 100

print("===== PROFIT ANALYSIS =====")

print("Total Sales:", total_sales)
print("Total Cost:", total_cost)
print("Total Profit:", total_profit)

print("Profit Margin:", round(profit_margin, 2), "%")

print("\nProduct Wise Profit:")
print(df.groupby("Product")["Profit"].sum())

print("\nRegion Wise Profit:")
print(df.groupby("Region")["Profit"].sum())

import matplotlib.pyplot as plt

product_profit = df.groupby("Product")["Profit"].sum()

plt.figure(figsize=(10, 6))

plt.bar(
    product_profit.index,
    product_profit.values
)

plt.title("Product Wise Profit Analysis")
plt.xlabel("Products")
plt.ylabel("Profit Amount")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "charts/product_profit.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# BUSINESS INSIGHTS

best_product = df.groupby("Profit")["Product"].first()

top_product = df.groupby("Product")["Profit"].sum().idxmax()

top_region = df.groupby("Region")["Profit"].sum().idxmax()

highest_sales_product = df.groupby("Product")["Sales"].sum().idxmax()

print("\n===== BUSINESS INSIGHTS =====")

print("Most Profitable Product:", top_product)
print("Most Profitable Region:", top_region)
print("Highest Revenue Product:", highest_sales_product)

print("\nBusiness Recommendation:")
print("Focus on products and regions generating higher profits.")