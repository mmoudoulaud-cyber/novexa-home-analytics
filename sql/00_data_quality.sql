/*
============================================================
Project : Novexa Home Analytics
File    : 00_data_quality.sql

Purpose
-------
Check the quality of the dataset before creating reports
and dashboards.

Author : Merryl Moudoulaud
============================================================
*/

------------------------------------------------------------
-- 1. Check the number of rows
------------------------------------------------------------

-- Check that every table has been loaded.

SELECT 'Dim_Date' AS Table_Name, COUNT(*) AS Row_Count
FROM Dim_Date

UNION ALL

SELECT 'Dim_Product', COUNT(*)
FROM Dim_Product

UNION ALL

SELECT 'Dim_Customer', COUNT(*)
FROM Dim_Customer

UNION ALL

SELECT 'Dim_Store', COUNT(*)
FROM Dim_Store

UNION ALL

SELECT 'Dim_Supplier', COUNT(*)
FROM Dim_Supplier

UNION ALL

SELECT 'Dim_Warehouse', COUNT(*)
FROM Dim_Warehouse

UNION ALL

SELECT 'Fact_Sales', COUNT(*)
FROM Fact_Sales;

------------------------------------------------------------
-- 2. Check for NULL values
------------------------------------------------------------

-- Product_ID

SELECT COUNT(*) AS Missing_Product_ID
FROM Fact_Sales
WHERE Product_ID IS NULL;

-- Customer_ID

SELECT COUNT(*) AS Missing_Customer_ID
FROM Fact_Sales
WHERE Customer_ID IS NULL;

-- Store_ID

SELECT COUNT(*) AS Missing_Store_ID
FROM Fact_Sales
WHERE Store_ID IS NULL;

-- Supplier_ID

SELECT COUNT(*) AS Missing_Supplier_ID
FROM Fact_Sales
WHERE Supplier_ID IS NULL;

-- Warehouse_ID

SELECT COUNT(*) AS Missing_Warehouse_ID
FROM Fact_Sales
WHERE Warehouse_ID IS NULL;

-- Date_ID

SELECT COUNT(*) AS Missing_Date_ID
FROM Fact_Sales
WHERE Date_ID IS NULL;

-- Quantity

SELECT COUNT(*) AS Missing_Quantity
FROM Fact_Sales
WHERE Quantity IS NULL;

-- Unit_Price

SELECT COUNT(*) AS Missing_Unit_Price
FROM Fact_Sales
WHERE Unit_Price IS NULL;

-- Unit_Cost

SELECT COUNT(*) AS Missing_Unit_Cost
FROM Fact_Sales
WHERE Unit_Cost IS NULL;

-- Net_Amount

SELECT COUNT(*) AS Missing_Net_Amount
FROM Fact_Sales
WHERE Net_Amount IS NULL;

------------------------------------------------------------
-- 3. Check duplicate IDs
------------------------------------------------------------

-- Sale_ID

SELECT
    Sale_ID,
    COUNT(*) AS Occurrences
FROM Fact_Sales
GROUP BY Sale_ID
HAVING COUNT(*) > 1;

-- Product_ID

SELECT
    Product_ID,
    COUNT(*) AS Occurrences
FROM Dim_Product
GROUP BY Product_ID
HAVING COUNT(*) > 1;


SELECT
    Customer_ID,
    COUNT(*) AS Occurrences
FROM Dim_Customer
GROUP BY Customer_ID
HAVING COUNT(*) > 1;

SELECT
    Supplier_ID,
    COUNT(*) AS Occurrences
FROM Dim_Supplier
GROUP BY Supplier_ID
HAVING COUNT(*) > 1;

SELECT
    Store_ID,
    COUNT(*) AS Occurrences
FROM Dim_Store
GROUP BY Store_ID
HAVING COUNT(*) > 1;

SELECT
    Warehouse_ID,
    COUNT(*) AS Occurrences
FROM Dim_Warehouse
GROUP BY Warehouse_ID
HAVING COUNT(*) > 1;



------------------------------------------------------------
-- 4. Check foreign keys
------------------------------------------------------------

-- Check Product_ID

SELECT COUNT(*) AS Missing_Product_ID
FROM Fact_Sales f
LEFT JOIN Dim_Product p
    ON f.Product_ID = p.Product_ID
WHERE p.Product_ID IS NULL;

-- Check Customer_ID

SELECT COUNT(*) AS Missing_Customer_ID
FROM Fact_Sales f
LEFT JOIN Dim_Customer c
    ON f.Customer_ID = c.Customer_ID
WHERE c.Customer_ID IS NULL;

-- Check Store_ID

SELECT COUNT(*) AS Missing_Store_ID
FROM Fact_Sales f
LEFT JOIN Dim_Store s
    ON f.Store_ID = s.Store_ID
WHERE s.Store_ID IS NULL;

-- Check Supplier_ID

SELECT COUNT(*) AS Missing_Supplier_ID
FROM Fact_Sales f
LEFT JOIN Dim_Supplier sp
    ON f.Supplier_ID = sp.Supplier_ID
WHERE sp.Supplier_ID IS NULL;

-- Check Warehouse_ID

SELECT COUNT(*) AS Missing_Warehouse_ID
FROM Fact_Sales f
LEFT JOIN Dim_Warehouse w
    ON f.Warehouse_ID = w.Warehouse_ID
WHERE w.Warehouse_ID IS NULL;

-- Check Date_ID

SELECT COUNT(*) AS Missing_Date_ID
FROM Fact_Sales f
LEFT JOIN Dim_Date d
    ON f.Date_ID = d.Date_ID
WHERE d.Date_ID IS NULL;

------------------------------------------------------------
-- 5. Check business rules
------------------------------------------------------------

-- Quantity must be greater than zero.

SELECT *
FROM Fact_Sales
WHERE Quantity <= 0;

-- Unit_Cost must be greater than zero.

SELECT *
FROM Fact_Sales
WHERE Unit_Cost <= 0;

-- Unit_Price must be greater than zero.

SELECT *
FROM Fact_Sales
WHERE Unit_Price <= 0;

-- Unit_Price must be greater than or equal to Unit_Cost.

SELECT *
FROM Fact_Sales
WHERE Unit_Price < Unit_Cost;  

-- Discount percentage must be between 0 and 100.

SELECT *
FROM Fact_Sales
WHERE Discount_Pct < 0
   OR Discount_Pct > 100;


------------------------------------------------------------
-- 6. Check calculated fields
------------------------------------------------------------

-- Gross_Amount = Quantity × Unit_Price

SELECT *
FROM Fact_Sales
WHERE ROUND(Quantity * Unit_Price, 2) <> ROUND(Gross_Amount, 2);

-- Net_Amount = Gross_Amount - Discount_Amount

SELECT *
FROM Fact_Sales
WHERE ROUND(Gross_Amount - Discount_Amount, 2) <> ROUND(Net_Amount, 2);

-- Margin_Amount = Net_Amount - (Quantity × Unit_Cost)

SELECT *
FROM Fact_Sales
WHERE ROUND(Net_Amount - (Quantity * Unit_Cost), 2) <> ROUND(Margin_Amount, 2);

