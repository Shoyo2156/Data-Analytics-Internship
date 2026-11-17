
# Exploratory Data Analysis (EDA) Report
## Online Retail Dataset

**Project:** E-Commerce Data Analysis  
**Tools:** Python, Pandas, NumPy, Matplotlib  
**Dataset:** Online Retail.xlsx

---

## 1. Project Objective

The objective of this project is to analyse online retail transaction data, clean the dataset, identify patterns, study revenue performance and generate meaningful business insights.

## 2. Dataset Overview

- Original Records: 541,909
- Columns: 8
- Cleaned Records: 536,641
- Duplicate Records Removed: 5,268
- Countries: 38

## 3. Data Cleaning

The following operations were performed:

- Checked missing values.
- Identified and removed duplicate records.
- Preserved missing values for further analysis.
- Checked data types.
- Created a Revenue column using Quantity × UnitPrice.
- Extracted Month information from InvoiceDate.

## 4. Missing Values Analysis

| Column | Missing Values |
|---|---:|
| Description | 1,454 |
| CustomerID | 135,080 |
| Other columns | 0 |

Missing CustomerID values were preserved rather than removed.

## 5. Outlier Analysis

IQR method was applied to the Quantity column.

- Lower Bound: -12.5
- Upper Bound: 23.5
- Identified Outliers: 58,501

Outliers were retained because they may represent genuine bulk purchases or unusual transactions.

## 6. Business Performance KPIs

| KPI | Result |
|---|---:|
| Total Revenue | £9,726,006.95 |
| Distinct Invoices | 25,900 |
| Total Quantity | 5,162,502 |
| Average Line Revenue | £18.12 |

## 7. Country-wise Revenue Analysis

Top-performing countries:

| Country | Revenue (£) |
|---|---:|
| United Kingdom | 8,167,128.18 |
| Netherlands | 284,661.54 |
| EIRE | 262,993.38 |
| Germany | 221,509.47 |
| France | 197,317.11 |

The United Kingdom generated the highest revenue.

## 8. Product-wise Revenue Analysis

Top products by revenue:

| Product | Revenue (£) |
|---|---:|
| DOTCOM POSTAGE | 206,245.48 |
| REGENCY CAKESTAND 3 TIER | 164,459.49 |
| WHITE HANGING HEART T-LIGHT HOLDER | 99,612.42 |
| PARTY BUNTING | 98,243.88 |
| JUMBO BAG RED RETROSPOT | 92,175.79 |

DOTCOM POSTAGE recorded the highest revenue.

## 9. Monthly Revenue Analysis

- Highest revenue month: November 2011
- November 2011 Revenue: £1,456,145.80
- Lowest monthly revenue: December 2011

Note: December 2011 contains data only up to December 9, so it is a partial month.

## 10. Correlation Analysis

| Variables | Correlation |
|---|---:|
| Quantity and Revenue | 0.8867 |
| UnitPrice and Revenue | -0.1620 |
| Quantity and UnitPrice | -0.0012 |

Quantity and Revenue show a strong positive correlation.

## 11. Visualizations

The following visualizations were generated:

1. Country-wise Revenue Chart
2. Product-wise Revenue Chart
3. Monthly Revenue Trend Chart
4. Correlation Heatmap

## 12. Key Business Insights

1. The United Kingdom is the largest revenue-generating market.
2. DOTCOM POSTAGE is the highest-revenue product.
3. November 2011 recorded the highest monthly revenue.
4. Quantity has a strong positive relationship with revenue.
5. Bulk transactions contribute to the presence of quantity outliers.

## 13. Conclusion

The EDA project successfully analysed the Online Retail dataset using Python libraries such as Pandas, NumPy and Matplotlib.

The analysis identified important business patterns, revenue trends, top-performing countries and products, and relationships between numerical variables.

These findings can support better business understanding and data-driven decision-making.

---

**Project Status:** Completed
