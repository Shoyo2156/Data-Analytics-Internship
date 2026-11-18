
import requests
import pandas as pd
import os
import time

# MFAPI Base URL
BASE_URL = "https://api.mfapi.in/mf/"

# Six required mutual fund schemes
schemes = {
    125497: "HDFC Top 100 Direct",
    119551: "SBI Bluechip",
    120503: "ICICI Bluechip",
    118632: "Nippon Large Cap",
    119092: "Axis Bluechip",
    120841: "Kotak Bluechip"
}

# Output folder
OUTPUT_FOLDER = "data/raw"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

all_nav_data = []

print("=" * 70)
print("BLUESTOCK - LIVE MUTUAL FUND NAV FETCH")
print("=" * 70)

for code, scheme_name in schemes.items():

    url = f"{BASE_URL}{code}"

    try:
        print(f"\nFetching: {scheme_name} ({code})")

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        result = response.json()

        # Extract NAV records
        nav_records = result.get("data", [])

        if not nav_records:
            print("WARNING: No NAV records returned.")
            continue

        df = pd.DataFrame(nav_records)

        # Add scheme information
        df["amfi_code"] = code
        df["scheme_name"] = scheme_name

        # Arrange columns
        df = df[[
            "amfi_code",
            "scheme_name",
            "date",
            "nav"
        ]]

        # Convert NAV to numeric
        df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

        # Save individual scheme CSV
        filename = f"live_nav_{code}.csv"
        filepath = os.path.join(OUTPUT_FOLDER, filename)

        df.to_csv(filepath, index=False)

        all_nav_data.append(df)

        print("Scheme:", scheme_name)
        print("Records:", len(df))
        print("Latest NAV:", df.iloc[0]["nav"])
        print("Saved:", filepath)

        time.sleep(0.5)

    except requests.exceptions.RequestException as e:
        print(f"API ERROR for {code}: {e}")

    except (ValueError, KeyError) as e:
        print(f"DATA ERROR for {code}: {e}")

# Combine all schemes
if all_nav_data:

    combined_df = pd.concat(
        all_nav_data,
        ignore_index=True
    )

    combined_path = os.path.join(
        OUTPUT_FOLDER,
        "live_nav_all_schemes.csv"
    )

    combined_df.to_csv(
        combined_path,
        index=False
    )

    print("\n" + "=" * 70)
    print("LIVE NAV FETCH COMPLETED")
    print("=" * 70)

    print("Total Schemes:", combined_df["amfi_code"].nunique())
    print("Total NAV Records:", len(combined_df))
    print("Combined File:", combined_path)

else:
    print("\nNo NAV data was successfully fetched.")
