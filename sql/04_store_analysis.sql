

SELECT
    ds.Store_Name,
    ds.City,
    ds.Store_Type,
    COUNT(*) AS Orders,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(AVG(fs.Net_Amount), 2) AS Average_Basket
FROM Fact_Sales AS fs
JOIN Dim_Store AS ds
    USING (Store_ID)
GROUP BY
    ds.Store_Name,
    ds.City,
    ds.Store_Type
ORDER BY
    Revenue DESC
LIMIT 10;


-- Revenue by Store Type

SELECT
    ds.Store_Type,
    COUNT(*) AS Orders,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(AVG(fs.Net_Amount), 2) AS Average_Basket
FROM Fact_Sales AS fs
JOIN Dim_Store AS ds
    USING (Store_ID)
GROUP BY
    ds.Store_Type
ORDER BY
    Revenue DESC;


-- Revenue by City

SELECT
    ds.City,
    COUNT(DISTINCT ds.Store_ID) AS Stores,
    COUNT(*) AS Orders,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(AVG(fs.Net_Amount), 2) AS Average_Basket
FROM Fact_Sales AS fs
JOIN Dim_Store AS ds
    USING (Store_ID)
GROUP BY
    ds.City
ORDER BY
    Revenue DESC;


-- Revenue by Warehouse

SELECT
    dw.Warehouse_Name,
    dw.City,
    COUNT(*) AS Orders,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(AVG(fs.Net_Amount), 2) AS Average_Basket
FROM Fact_Sales AS fs
JOIN Dim_Warehouse AS dw
    USING (Warehouse_ID)
GROUP BY
    dw.Warehouse_Name,
    dw.City
ORDER BY
    Revenue DESC;

