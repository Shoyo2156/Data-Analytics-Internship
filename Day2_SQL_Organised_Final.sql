-- ============================================================
-- DAY 2: SQL SALES ANALYTICS PROJECT
-- Database: Sales_Analytics
-- Table: Sales
-- Purpose: SQL practice + final business analysis
-- Note: Run the data-import section only if the 72 rows are not
-- already present. INSERT IGNORE protects existing Order_IDs.
-- ============================================================


USE Sales_Analytics;


-- SECTION 1: DATA IMPORT (FIRST 72 ORDERS)
-- Existing ORD-0073 to ORD-0100 records are not changed.

USE Sales_Analytics;
START TRANSACTION;
INSERT IGNORE INTO Sales (Order_ID,Order_Date,Customer_Name,Region,City,Product,Category,Quantity,Unit_Price,Sales,Cost,Profit,Payment_Mode) VALUES
('ORD-0001','2026-02-27','Kabir Mehta','North','Chandigarh','Desk','Furniture',4,12000,48000,34000,14000,'UPI'),
('ORD-0002','2026-10-07','Aarav Sharma','North','Delhi','Water Bottle','Accessories',7,427.5,2992.5,1260,1732.5,'Credit Card'),
('ORD-0003','2026-04-30','Kiara Das','Central','Nagpur','Water Bottle','Accessories',1,450,450,180,270,'Net Banking'),
('ORD-0004','2026-08-03','Rohan Mishra','South','Bengaluru','Printer','Electronics',5,13775,68875,54000,14875,'Cash'),
('ORD-0005','2026-06-24','Diya Patel','East','Kolkata','Headphones','Electronics',4,2500,10000,5600,4400,'Cash'),
('ORD-0006','2026-02-19','Kiara Das','East','Patna','Notebook','Stationery',5,76,380,175,205,'Net Banking'),
('ORD-0007','2026-03-05','Myra Nair','West','Mumbai','Smartphone','Electronics',5,22000,110000,82500,27500,'UPI'),
('ORD-0008','2026-01-24','Aditi Jain','South','Bengaluru','Desk','Furniture',2,12000,24000,17000,7000,'Cash'),
('ORD-0009','2026-05-23','Isha Verma','West','Mumbai','Notebook','Stationery',3,80,240,105,135,'Debit Card'),
('ORD-0010','2026-02-06','Saanvi Shah','Central','Indore','Headphones','Electronics',4,2500,10000,5600,4400,'Debit Card'),
('ORD-0011','2026-10-13','Aditi Jain','South','Bengaluru','Notebook','Stationery',1,80,80,35,45,'Debit Card'),
('ORD-0012','2026-07-25','Anaya Singh','East','Bhubaneswar','Smartphone','Electronics',4,22000,88000,66000,22000,'Cash'),
('ORD-0013','2026-07-22','Anaya Singh','West','Ahmedabad','Headphones','Electronics',5,2500,12500,7000,5500,'Net Banking'),
('ORD-0014','2026-10-03','Isha Verma','East','Kolkata','Water Bottle','Accessories',7,472.5,3307.5,1260,2047.5,'Credit Card'),
('ORD-0015','2026-09-18','Kabir Mehta','West','Ahmedabad','Smartphone','Electronics',1,20900,20900,16500,4400,'Credit Card'),
('ORD-0016','2026-08-05','Myra Nair','Central','Indore','Smartphone','Electronics',7,23100,161700,115500,46200,'Net Banking'),
('ORD-0017','2026-05-09','Rohan Mishra','Central','Nagpur','Laptop','Electronics',2,55000,110000,84000,26000,'Debit Card'),
('ORD-0018','2026-02-27','Aarav Sharma','East','Bhubaneswar','Pen Pack','Stationery',3,126,378,165,213,'Debit Card'),
('ORD-0019','2026-09-14','Aditi Jain','South','Hyderabad','Bookshelf','Furniture',2,7000,14000,9200,4800,'Net Banking'),
('ORD-0020','2026-04-12','Myra Nair','South','Chennai','Notebook','Stationery',3,76,228,105,123,'Cash'),
('ORD-0021','2026-01-10','Aarav Sharma','North','Delhi','Notebook','Stationery',5,80,400,175,225,'Net Banking'),
('ORD-0022','2026-02-10','Kabir Mehta','North','Chandigarh','Printer','Electronics',2,14500,29000,21600,7400,'Cash'),
('ORD-0023','2026-10-09','Dev Malhotra','South','Hyderabad','Desk','Furniture',7,12000,84000,59500,24500,'Credit Card'),
('ORD-0024','2026-06-09','Diya Patel','West','Mumbai','Notebook','Stationery',8,84,672,280,392,'Credit Card'),
('ORD-0025','2026-02-02','Aarav Sharma','East','Kolkata','Laptop','Electronics',4,55000,220000,168000,52000,'UPI'),
('ORD-0026','2026-04-28','Reyansh Joshi','North','Delhi','Laptop','Electronics',6,52250,313500,252000,61500,'Debit Card'),
('ORD-0027','2026-09-06','Anaya Singh','South','Chennai','Bookshelf','Furniture',3,7350,22050,13800,8250,'Cash'),
('ORD-0028','2026-04-08','Arjun Rao','North','Jaipur','Smartphone','Electronics',7,22000,154000,115500,38500,'Cash'),
('ORD-0029','2026-01-28','Rohan Mishra','North','Delhi','Laptop','Electronics',7,55000,385000,294000,91000,'Credit Card'),
('ORD-0030','2026-04-09','Arjun Rao','South','Bengaluru','Bookshelf','Furniture',8,7000,56000,36800,19200,'Debit Card'),
('ORD-0031','2026-08-25','Aarav Sharma','South','Hyderabad','Smartphone','Electronics',8,20900,167200,132000,35200,'Net Banking'),
('ORD-0032','2026-01-08','Saanvi Shah','North','Jaipur','Office Chair','Furniture',3,8925,26775,17100,9675,'Credit Card'),
('ORD-0033','2026-07-25','Arjun Rao','North','Jaipur','Headphones','Electronics',7,2375,16625,9800,6825,'Cash'),
('ORD-0034','2026-05-27','Anaya Singh','West','Pune','Bookshelf','Furniture',8,7000,56000,36800,19200,'Credit Card'),
('ORD-0035','2026-01-30','Aarav Sharma','Central','Bhopal','Bookshelf','Furniture',1,7000,7000,4600,2400,'Net Banking'),
('ORD-0036','2026-09-02','Reyansh Joshi','Central','Bhopal','Bookshelf','Furniture',3,6650,19950,13800,6150,'Credit Card'),
('ORD-0037','2026-02-05','Diya Patel','Central','Nagpur','Smartphone','Electronics',4,23100,92400,66000,26400,'Credit Card'),
('ORD-0038','2026-10-24','Aditya Kulkarni','Central','Nagpur','Laptop','Electronics',2,57750,115500,84000,31500,'Net Banking'),
('ORD-0039','2026-09-25','Anaya Singh','East','Patna','Desk','Furniture',4,12000,48000,34000,14000,'Cash'),
('ORD-0040','2026-03-09','Aarav Sharma','East','Patna','Printer','Electronics',6,13775,82650,64800,17850,'Net Banking'),
('ORD-0041','2026-10-16','Kabir Mehta','North','Jaipur','Smartphone','Electronics',4,22000,88000,66000,22000,'UPI'),
('ORD-0042','2026-05-06','Aditi Jain','East','Bhubaneswar','Desk','Furniture',3,12600,37800,25500,12300,'Debit Card'),
('ORD-0043','2026-09-28','Dev Malhotra','North','Delhi','Bookshelf','Furniture',5,6650,33250,23000,10250,'Debit Card'),
('ORD-0044','2026-03-01','Vivaan Gupta','North','Chandigarh','Bookshelf','Furniture',3,7000,21000,13800,7200,'Credit Card'),
('ORD-0045','2026-06-25','Dev Malhotra','South','Bengaluru','Desk','Furniture',8,12000,96000,68000,28000,'UPI'),
('ORD-0046','2026-08-05','Rohan Mishra','East','Kolkata','Laptop','Electronics',1,55000,55000,42000,13000,'Debit Card'),
('ORD-0047','2026-03-24','Diya Patel','West','Mumbai','Bookshelf','Furniture',7,6650,46550,32200,14350,'Credit Card'),
('ORD-0048','2026-10-07','Kabir Mehta','North','Delhi','Notebook','Stationery',3,84,252,105,147,'Debit Card'),
('ORD-0049','2026-07-06','Aditya Kulkarni','North','Delhi','Notebook','Stationery',4,80,320,140,180,'Debit Card'),
('ORD-0050','2026-10-14','Aditi Jain','West','Mumbai','Water Bottle','Accessories',3,450,1350,540,810,'Credit Card'),
('ORD-0051','2026-07-31','Rohan Mishra','North','Chandigarh','Headphones','Electronics',6,2625,15750,8400,7350,'Credit Card'),
('ORD-0052','2026-05-17','Aditi Jain','South','Chennai','Smartphone','Electronics',7,20900,146300,115500,30800,'Credit Card'),
('ORD-0053','2026-04-13','Anaya Singh','West','Mumbai','Notebook','Stationery',5,80,400,175,225,'Credit Card'),
('ORD-0054','2026-07-24','Isha Verma','East','Bhubaneswar','Desk','Furniture',2,12000,24000,17000,7000,'Net Banking'),
('ORD-0055','2026-07-24','Dev Malhotra','Central','Indore','Notebook','Stationery',1,76,76,35,41,'Credit Card'),
('ORD-0056','2026-10-25','Isha Verma','East','Bhubaneswar','Laptop','Electronics',2,57750,115500,84000,31500,'Debit Card'),
('ORD-0057','2026-08-12','Dev Malhotra','Central','Nagpur','Bookshelf','Furniture',2,7350,14700,9200,5500,'Credit Card'),
('ORD-0058','2026-05-11','Isha Verma','North','Jaipur','Pen Pack','Stationery',1,120,120,55,65,'UPI'),
('ORD-0059','2026-06-19','Reyansh Joshi','Central','Indore','Notebook','Stationery',2,80,160,70,90,'Cash'),
('ORD-0060','2026-06-17','Arjun Rao','West','Ahmedabad','Desk','Furniture',3,12000,36000,25500,10500,'Cash'),
('ORD-0061','2026-03-31','Reyansh Joshi','Central','Bhopal','Water Bottle','Accessories',5,472.5,2362.5,900,1462.5,'Debit Card'),
('ORD-0062','2026-05-27','Saanvi Shah','South','Chennai','Pen Pack','Stationery',6,126,756,330,426,'Credit Card'),
('ORD-0063','2026-09-19','Reyansh Joshi','West','Ahmedabad','Headphones','Electronics',2,2500,5000,2800,2200,'Net Banking'),
('ORD-0064','2026-06-21','Rohan Mishra','North','Delhi','Office Chair','Furniture',5,8500,42500,28500,14000,'Credit Card'),
('ORD-0065','2026-01-13','Saanvi Shah','North','Jaipur','Office Chair','Furniture',8,8075,64600,45600,19000,'Net Banking'),
('ORD-0066','2026-04-10','Kabir Mehta','West','Ahmedabad','Printer','Electronics',7,14500,101500,75600,25900,'UPI'),
('ORD-0067','2026-02-24','Aarav Sharma','West','Ahmedabad','Office Chair','Furniture',3,8925,26775,17100,9675,'Credit Card'),
('ORD-0068','2026-03-04','Rohan Mishra','West','Pune','Headphones','Electronics',8,2500,20000,11200,8800,'Net Banking'),
('ORD-0069','2026-09-16','Kiara Das','West','Pune','Bookshelf','Furniture',8,7000,56000,36800,19200,'Cash'),
('ORD-0070','2026-05-13','Vivaan Gupta','South','Chennai','Desk','Furniture',8,12000,96000,68000,28000,'UPI'),
('ORD-0071','2026-05-27','Dev Malhotra','South','Hyderabad','Desk','Furniture',6,12000,72000,51000,21000,'UPI'),
('ORD-0072','2026-03-12','Kiara Das','South','Bengaluru','Office Chair','Furniture',7,8500,59500,39900,19600,'UPI');
COMMIT;

-- Verify the imported dataset (expected: 100 orders).
SELECT COUNT(*) AS Total_Orders, SUM(Sales) AS Total_Revenue,
       SUM(Profit) AS Total_Profit, SUM(Quantity) AS Total_Quantity
FROM Sales;

-- SECTION 2: BASIC SQL (SELECT, WHERE, LIMIT, ORDER BY)

SELECT Order_ID FROM Sales ORDER BY Order_ID LIMIT 10;

SELECT * FROM Sales;

SELECT Order_ID, Customer_Name, Sales
FROM Sales;

SELECT *
FROM Sales
LIMIT 10;

SELECT *
FROM Sales
WHERE Region = 'West';

SELECT *
FROM Sales
WHERE Category = 'Electronics';

SELECT *
FROM Sales
WHERE Sales > 10000;

SELECT *
FROM Sales
ORDER BY Sales DESC;

SELECT *
FROM Sales
ORDER BY Sales ASC;


-- SECTION 3: AGGREGATE FUNCTIONS (SUM, COUNT, AVG, MAX, MIN)

SELECT SUM(Sales) AS Total_Revenue
FROM Sales;

SELECT COUNT(*) AS Total_Orders
FROM Sales;

SELECT AVG(Sales) AS Average_Sales
FROM Sales;

SELECT MAX(Sales) AS Highest_Sale
FROM Sales;

SELECT MIN(Sales) AS Lowest_Sale
FROM Sales;


-- SECTION 4: GROUP BY AND HAVING

SELECT
    Region,
    SUM(Sales) AS Total_Sales
FROM Sales
GROUP BY Region;

SELECT
    Category,
    SUM(Sales) AS Total_Sales
FROM Sales
GROUP BY Category;

SELECT
    Category,
    SUM(Profit) AS Total_Profit
FROM Sales
GROUP BY Category;

SELECT
    Payment_Mode,
    COUNT(*) AS Total_Orders
FROM Sales
GROUP BY Payment_Mode;

SELECT
    Region,
    AVG(Sales) AS Average_Sales
FROM Sales
GROUP BY Region;

SELECT
    Region,
    SUM(Sales) AS Total_Sales
FROM Sales
GROUP BY Region
HAVING SUM(Sales) > 1000000;


-- SECTION 5: JOINS
-- CREATE TABLE Customers is a one-time setup. If Customers already
-- exists, skip the CREATE TABLE statement and run the SELECT/JOINs.

CREATE TABLE IF NOT EXISTS Customers AS
SELECT DISTINCT
    Customer_Name,
    Region,
    City
FROM Sales;

SELECT * FROM Customers;

SELECT
    S.Order_ID,
    S.Customer_Name,
    C.City,
    S.Sales
FROM Sales S
INNER JOIN Customers C
ON S.Customer_Name = C.Customer_Name;

SELECT
    C.Customer_Name,
    C.City,
    S.Order_ID,
    S.Sales
FROM Customers C
LEFT JOIN Sales S
ON C.Customer_Name = S.Customer_Name;

SELECT
    S.Order_ID,
    S.Customer_Name,
    C.City
FROM Sales S
RIGHT JOIN Customers C
ON S.Customer_Name = C.Customer_Name;


-- SECTION 6: SUBQUERIES

SELECT *
FROM Sales
WHERE Sales > (
    SELECT AVG(Sales)
    FROM Sales
);

SELECT *
FROM Sales
WHERE Sales = (
    SELECT MAX(Sales)
    FROM Sales
);

SELECT DISTINCT Customer_Name
FROM Sales
WHERE Customer_Name IN (
    SELECT Customer_Name
    FROM Sales
    WHERE Sales > (
        SELECT AVG(Sales)
        FROM Sales
    )
);

SELECT Product, SUM(Sales) AS Total_Sales
FROM Sales
GROUP BY Product
HAVING SUM(Sales) > (
    SELECT AVG(Product_Total)
    FROM (
        SELECT SUM(Sales) AS Product_Total
        FROM Sales
        GROUP BY Product
    ) AS Product_Summary
);


-- SECTION 7: WINDOW FUNCTIONS (ROW_NUMBER, RANK, RUNNING TOTAL)

SELECT
    Order_ID,
    Customer_Name,
    Sales,
    ROW_NUMBER() OVER (
        ORDER BY Sales DESC
    ) AS Row_Num
FROM Sales;

SELECT
    Product,
    Sales,
    RANK() OVER (
        ORDER BY Sales DESC
    ) AS Sales_Rank
FROM Sales;

SELECT
    Order_ID,
    Region,
    Sales,
    RANK() OVER (
        PARTITION BY Region
        ORDER BY Sales DESC
    ) AS Region_Rank
FROM Sales;

SELECT
    Order_ID,
    Order_Date,
    Sales,
    SUM(Sales) OVER (
        ORDER BY Order_Date, Order_ID
    ) AS Running_Total
FROM Sales;


-- SECTION 8: FINAL BUSINESS ANALYSIS QUERIES
-- 1. Overall business performance
-- 2. Profit margin
-- 3. Regional performance
-- 4. Best-performing region
-- 5. Top 5 products
-- 6. Category performance
-- 7. Top 10 customers
-- 8. Customer segmentation
-- 9. Monthly sales trends
-- 10. Payment mode analysis

SELECT
    COUNT(*) AS Total_Orders,
    SUM(Sales) AS Total_Revenue,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity,
    ROUND(AVG(Sales), 2) AS Average_Order_Value
FROM Sales;

SELECT
    ROUND(
        SUM(Profit) / SUM(Sales) * 100, 2
    ) AS Profit_Margin_Percentage
FROM Sales;

SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(*) AS Total_Orders
FROM Sales
GROUP BY Region
ORDER BY Total_Sales DESC;

SELECT
    Region,
    SUM(Sales) AS Total_Sales
FROM Sales
GROUP BY Region
ORDER BY Total_Sales DESC
LIMIT 1;

SELECT
    Product,
    SUM(Sales) AS Total_Revenue,
    SUM(Profit) AS Total_Profit
FROM Sales
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 5;

SELECT
    Category,
    SUM(Sales) AS Revenue,
    SUM(Profit) AS Profit,
    SUM(Quantity) AS Units_Sold
FROM Sales
GROUP BY Category
ORDER BY Revenue DESC;

SELECT
    Customer_Name,
    COUNT(*) AS Total_Orders,
    SUM(Sales) AS Total_Spending
FROM Sales
GROUP BY Customer_Name
ORDER BY Total_Spending DESC
LIMIT 10;

SELECT
    Customer_Name,
    SUM(Sales) AS Total_Spending,
    CASE
        WHEN SUM(Sales) >= 100000 THEN 'High Value'
        WHEN SUM(Sales) >= 50000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS Customer_Segment
FROM Sales
GROUP BY Customer_Name
ORDER BY Total_Spending DESC;

SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS Sales_Month,
    SUM(Sales) AS Monthly_Revenue,
    SUM(Profit) AS Monthly_Profit
FROM Sales
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Sales_Month;

SELECT
    Payment_Mode,
    COUNT(*) AS Total_Orders,
    SUM(Sales) AS Total_Revenue
FROM Sales
GROUP BY Payment_Mode
ORDER BY Total_Revenue DESC;

USE Sales_Analytics;

SELECT
    COUNT(*) AS Total_Orders,
    SUM(Sales) AS Total_Revenue,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity
FROM Sales;


-- END OF DAY 2 SQL PROJECT
