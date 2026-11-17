import requests
import pandas as pd

# API URL
url = "https://api.frankfurter.app/latest?from=USD"

# Send GET request
response = requests.get(url)

# Check response status
print("Status Code:", response.status_code)

# Convert JSON response
data = response.json()

# Display JSON data
print(data)

# Convert exchange rates into DataFrame
rates = data["rates"]

df = pd.DataFrame(
    list(rates.items()),
    columns=["Currency", "Exchange_Rate"]
)

# Add base currency and date
df["Base_Currency"] = data["base"]
df["Date"] = data["date"]

# Save as CSV
df.to_csv("exchange_rates.csv", index=False)

print("\nCSV file created successfully!")
print(df.head())