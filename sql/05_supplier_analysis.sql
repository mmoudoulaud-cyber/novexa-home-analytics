
SELECT
    ds.Supplier_Name,
    COUNT(*) AS Orders,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(AVG(fs.Net_Amount), 2) AS Average_Basket
FROM Fact_Sales AS fs
JOIN Dim_Supplier AS ds
    USING (Supplier_ID)
GROUP BY
    ds.Supplier_Name
ORDER BY
    Revenue DESC;

-- Top suppliers by Revenue

SELECT
    ds.Supplier_Name,
    COUNT(*) AS Orders,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(AVG(fs.Net_Amount), 2) AS Average_Basket
FROM Fact_Sales AS fs
JOIN Dim_Supplier AS ds
    USING (Supplier_ID)
GROUP BY
    ds.Supplier_Name
ORDER BY
    Revenue DESC
LIMIT 10;

-- Supplier performance

SELECT
    ds.Supplier_Name,
    COUNT(DISTINCT dp.Product_ID) AS Products,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(SUM(fs.Margin_Amount), 2) AS Margin,
    ROUND(
        SUM(fs.Margin_Amount) * 100.0
        / SUM(fs.Net_Amount),
        2
    ) AS Margin_Rate
FROM Fact_Sales AS fs
JOIN Dim_Supplier AS ds
    USING (Supplier_ID)
JOIN Dim_Product AS dp
    USING (Product_ID)
GROUP BY
    ds.Supplier_Name
ORDER BY
    Revenue DESC;   


