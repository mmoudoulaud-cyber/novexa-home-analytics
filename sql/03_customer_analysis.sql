------------------------------------------------------------
-- File : 03_customer_analysis.sql
-- Project : Novexa Home Analytics
-- Purpose :
-- Analyse customer behaviour to identify
-- high-value segments and business opportunities.


-- Business Question:
-- Which loyalty level generates the highest revenue?


-- Revenue by loyalty level


SELECT
    dc.Loyalty_Level,
    COUNT(DISTINCT dc.Customer_ID) AS Customers,
    COUNT(*) AS Orders,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(AVG(fs.Net_Amount), 2) AS Average_Basket
FROM Fact_Sales AS fs
JOIN Dim_Customer AS dc
    USING (Customer_ID)
GROUP BY
    dc.Loyalty_Level
ORDER BY
    Revenue DESC;


-- Revenue by gender

SELECT
    dc.Gender,
    COUNT(DISTINCT dc.Customer_ID) AS Customers,
    COUNT(*) AS Orders,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(AVG(fs.Net_Amount), 2) AS Average_Basket
FROM Fact_Sales AS fs
JOIN Dim_Customer AS dc
    USING (Customer_ID)
GROUP BY
    dc.Gender
ORDER BY
    Revenue DESC;

-- Revenue by Age Group

SELECT
CASE
    WHEN Age < 25 THEN '18-24'
    WHEN Age < 35 THEN '25-34'
    WHEN Age < 45 THEN '35-44'
    WHEN Age < 55 THEN '45-54'
    ELSE '55+'
END AS Age_Group,
    COUNT(DISTINCT dc.Customer_ID) AS Customers,
    COUNT(*) AS Orders,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(AVG(fs.Net_Amount), 2) AS Average_Basket
FROM Fact_Sales AS fs
JOIN Dim_Customer AS dc
    USING (Customer_ID)
GROUP BY
    Age_Group
ORDER BY
    Revenue DESC;   


-- Top Customers

WITH customer_sales AS (

    SELECT
        First_Name || ' ' || Last_Name AS Customer_Name,
        COUNT(*) AS Orders,
        ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
        ROUND(AVG(fs.Net_Amount), 2) AS Average_Basket
    FROM Fact_Sales AS fs
    JOIN Dim_Customer AS dc
        USING (Customer_ID)
    GROUP BY
        Customer_Name

)

SELECT
    DENSE_RANK() OVER (
        ORDER BY Revenue DESC
    ) AS Customer_Rank,
    Customer_Name,
    Orders,
    Revenue,
    Average_Basket
FROM customer_sales
ORDER BY
    Customer_Rank
LIMIT 10;

-- Revenue by City

SELECT
    dc.City,
    COUNT(DISTINCT dc.Customer_ID) AS Customers,
    COUNT(*) AS Orders,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(AVG(fs.Net_Amount), 2) AS Average_Basket
FROM Fact_Sales AS fs
JOIN Dim_Customer AS dc
    USING (Customer_ID)
GROUP BY
    dc.City
ORDER BY
    Revenue DESC;

-- Revenue by Country

SELECT
    dc.Country,
    COUNT(DISTINCT dc.Customer_ID) AS Customers,
    COUNT(*) AS Orders,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(AVG(fs.Net_Amount), 2) AS Average_Basket
FROM Fact_Sales AS fs
JOIN Dim_Customer AS dc
    USING (Customer_ID)
GROUP BY
    dc.Country
ORDER BY
    Revenue DESC;





