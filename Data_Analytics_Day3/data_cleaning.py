import pandas as pd

data = {
    "Customer": ["Aarav", "Riya", "Kabir", "Aarav", "Neha", None],
    "Region": ["West", "North", "South", "West", None, "East"],
    "Sales": [12000, 15000, None, 12000, 18000, 9000]
}

df = pd.DataFrame(data)

print("===== ORIGINAL DATA =====")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df["Customer"] = df["Customer"].fillna("Unknown")
df["Region"] = df["Region"].fillna("Unknown")
df["Sales"] = df["Sales"].fillna(df["Sales"].median())

print("\n===== CLEANED DATA =====")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned dataset saved successfully!")