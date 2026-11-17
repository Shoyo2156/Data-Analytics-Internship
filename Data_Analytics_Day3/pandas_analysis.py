import pandas as pd

df = pd.read_csv("sales_data.csv")

print("===== PANDAS SALES ANALYSIS =====")

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nRegion Wise Sales:")
print(df.groupby("Region")["Sales"].sum())

print("\nProduct Wise Sales:")
print(df.groupby("Product")["Sales"].sum())

print("\nTotal Revenue:", df["Sales"].sum())
print("Average Revenue:", df["Sales"].mean())