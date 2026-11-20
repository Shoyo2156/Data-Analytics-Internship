
-- Q1. Top 5 fund houses by latest AUM
SELECT fund_house, aum_crore
FROM fact_aum
WHERE date_key = (SELECT MAX(date_key) FROM fact_aum)
ORDER BY aum_crore DESC
LIMIT 5;


-- Q2. Average NAV per month
SELECT
    d.year,
    d.month,
    d.month_name,
    ROUND(AVG(n.nav), 2) AS average_nav
FROM fact_nav n
JOIN dim_date d ON n.date_key = d.date_key
GROUP BY d.year, d.month, d.month_name
ORDER BY d.year, d.month;


-- Q3. SIP inflows by transaction month
SELECT
    d.year,
    d.month,
    ROUND(SUM(t.amount_inr), 2) AS sip_inflow
FROM fact_transactions t
JOIN dim_date d ON t.date_key = d.date_key
WHERE t.transaction_type = 'SIP'
GROUP BY d.year, d.month
ORDER BY d.year, d.month;


-- Q4. Transactions by state
SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- Q5. Funds with expense ratio below 1%
SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- Q6. Top 5 schemes by AUM
SELECT
    f.scheme_name,
    p.aum_crore
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.aum_crore DESC
LIMIT 5;


-- Q7. Average 1-year return by category
SELECT
    f.category,
    ROUND(AVG(p.return_1yr_pct), 2) AS avg_1yr_return
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
GROUP BY f.category
ORDER BY avg_1yr_return DESC;


-- Q8. Transaction type distribution
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;


-- Q9. Top 10 funds by average NAV
SELECT
    f.scheme_name,
    ROUND(AVG(n.nav), 2) AS average_nav
FROM fact_nav n
JOIN dim_fund f ON n.amfi_code = f.amfi_code
GROUP BY f.amfi_code, f.scheme_name
ORDER BY average_nav DESC
LIMIT 10;


-- Q10. Monthly AUM trend by fund house
SELECT
    d.year,
    d.month,
    a.fund_house,
    ROUND(a.aum_crore, 2) AS aum_crore
FROM fact_aum a
JOIN dim_date d ON a.date_key = d.date_key
ORDER BY d.year, d.month, a.fund_house;
