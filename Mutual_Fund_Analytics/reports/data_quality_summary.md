
# Bluestock Mutual Fund Analytics
## Day 1 – Data Quality Summary

### 1. Dataset Overview

Total CSV datasets: 10
Total records across datasets: 87,533
Total columns across datasets: 81

### 2. Data Completeness

- 9 datasets have no missing values.
- Monthly SIP Inflows contains 12 missing values in yoy_growth_pct.
- No duplicate rows found in any of the 10 datasets.

### 3. Data Type Observations

- Date columns are currently stored as object.
- NAV values are stored as float64.
- AMFI scheme codes are stored as int64.
- Financial amounts use integer or floating-point types.

Date columns should be converted to appropriate datetime types during preprocessing.

### 4. AMFI Code Validation

- Unique Fund Master codes: 40
- Unique NAV History codes: 40
- Matching codes: 40
- Missing codes: 0

Status: PASSED

### 5. Live NAV API Integration

Source: MFAPI (mfapi.in)

- Schemes fetched: 6
- Total NAV records: 20,493
- Individual CSV files generated: 6
- Combined CSV generated: 1

### 6. Observations and Recommendations

1. Investigate 12 missing YoY growth values.
2. Convert date columns into datetime format.
3. Validate NAV values for zero or negative entries.
4. Check portfolio weight percentages.
5. Validate transaction amounts and AMFI codes.
6. Preserve original raw datasets without modification.

### 7. Conclusion

All 10 source datasets were successfully loaded.
AMFI code validation passed for all 40 schemes.
Live NAV data was successfully fetched for six schemes.

Day 1 data ingestion activities completed successfully.
