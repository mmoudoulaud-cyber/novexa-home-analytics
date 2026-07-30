/*
============================================================
Project : Novexa Home Analytics
File    : 01_sales_overview.sql

Purpose
-------
Create the main sales KPIs.

Author : Merryl Moudoulaud
============================================================
*/

------------------------------------------------------------
-- 1. Total revenue
------------------------------------------------------------

SELECT
    ROUND(SUM(Net_Amount), 2) AS Total_Revenue
FROM Fact_Sales;

------------------------------------------------------------
-- 2. Total orders
------------------------------------------------------------

SELECT
    COUNT(*) AS Total_Orders
FROM Fact_Sales;

------------------------------------------------------------
-- 3. Total quantity sold
------------------------------------------------------------

SELECT
    SUM(Quantity) AS Total_Quantity
FROM Fact_Sales;

------------------------------------------------------------
-- 4. Average basket
------------------------------------------------------------

SELECT
    ROUND(AVG(Net_Amount),2) AS Average_Basket
FROM Fact_Sales;

------------------------------------------------------------
-- 5. Total margin
------------------------------------------------------------

SELECT
    ROUND(SUM(Margin_Amount),2) AS Total_Margin
FROM Fact_Sales;

------------------------------------------------------------
-- 6. Sales by sales channel
------------------------------------------------------------

SELECT
    Sales_Channel,
    COUNT(*) AS Total_Orders,
    ROUND(SUM(Net_Amount), 2) AS Total_Revenue,
    ROUND(SUM(Margin_Amount), 2) AS Total_Margin,
    ROUND(
        SUM(Margin_Amount) * 100.0 / SUM(Net_Amount),
        2
    ) AS Margin_Rate,
    ROUND(AVG(Net_Amount), 2) AS Average_Basket
FROM Fact_Sales
GROUP BY Sales_Channel
ORDER BY Total_Revenue DESC;


SELECT
    MIN(Unit_Price) AS Min_Price,
    ROUND(AVG(Unit_Price), 2) AS Avg_Price,
    MAX(Unit_Price) AS Max_Price
FROM Fact_Sales;

SELECT
    Quantity,
    COUNT(*) AS Number_of_Sales
FROM Fact_Sales
GROUP BY Quantity
ORDER BY Quantity;




SELECT
    Sales_Channel,
    COUNT(*) AS Total_Orders,
    ROUND(SUM(Net_Amount), 2) AS Total_Revenue,
    ROUND(SUM(Margin_Amount), 2) AS Total_Margin,
    ROUND(
        SUM(Margin_Amount) * 100.0 / SUM(Net_Amount),
        2
    ) AS Margin_Rate,
    ROUND(AVG(Net_Amount), 2) AS Average_Basket
FROM Fact_Sales
GROUP BY Sales_Channel
ORDER BY Total_Revenue DESC;

-- Revenue share by sales channel --

WITH sales_by_channel AS (
    SELECT
        Sales_Channel,
        ROUND(SUM(Net_Amount), 2) AS Total_Revenue
    FROM Fact_Sales
    GROUP BY Sales_Channel
)
SELECT
    Sales_Channel,
    Total_Revenue,
    ROUND(
        Total_Revenue * 100.0 / SUM(Total_Revenue) OVER (),
        2
    ) AS Revenue_Share
FROM sales_by_channel
ORDER BY Total_Revenue DESC;

SELECT
    fs.sales_channel,
    dd.Year,
    dd.Month,
    dd.Month_Name,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue
FROM Fact_Sales as fs
JOIN Dim_Date as dd
USING (Date_ID)
GROUP BY fs.sales_channel, dd.Year, dd.Month, dd.Month_Name
ORDER BY dd.Year, dd.Month, fs.Sales_Channel;

SELECT
    Category,
    ROUND(SUM(Net_Amount), 2) AS Revenue,
    ROUND(SUM(Margin_Amount), 2) AS Margin,
    ROUND(
        SUM(Margin_Amount) * 100.0
        / SUM(Net_Amount),
        2
    ) AS Margin_Rate
FROM Fact_Sales
JOIN Dim_Product
USING (Product_ID)
GROUP BY Category
ORDER BY Revenue DESC;

------------------------------------------------------------
-- Revenue by payment method
------------------------------------------------------------

SELECT
    Payment_Method,
    COUNT(*) AS Total_Orders,
    ROUND(SUM(Net_Amount), 2) AS Revenue,
    ROUND(AVG(Net_Amount), 2) AS Average_Basket
FROM Fact_Sales
GROUP BY Payment_Method
ORDER BY Revenue DESC;

------------------------------------------------------------
-- 10. Monthly revenue growth
------------------------------------------------------------

WITH monthly_sales AS (

    SELECT
        dd.Year,
        dd.Month,
        dd.Month_Name,
        ROUND(SUM(fs.Net_Amount), 2) AS Revenue
    FROM Fact_Sales AS fs
    JOIN Dim_Date AS dd
        USING (Date_ID)
    GROUP BY
        dd.Year,
        dd.Month,
        dd.Month_Name

),

monthly_growth AS (

    SELECT
        Year,
        Month,
        Month_Name,
        Revenue,
        LAG(Revenue) OVER (
            ORDER BY Year, Month
        ) AS Previous_Revenue
    FROM monthly_sales

)

SELECT
    Year,
    Month,
    Month_Name,
    Revenue,
    Previous_Revenue,
    ROUND(
        (
            Revenue - Previous_Revenue
        ) * 100.0
        / Previous_Revenue,
        2
    ) AS Growth_Pct
FROM monthly_growth
ORDER BY
    Year,
    Month;