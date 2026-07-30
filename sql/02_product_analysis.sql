
-- 1. Revenue by category


SELECT
    dp.Category,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(SUM(fs.Margin_Amount), 2) AS Margin,
    ROUND(
        SUM(fs.Margin_Amount) * 100.0
        / SUM(fs.Net_Amount),
        2
    ) AS Margin_Rate
FROM Fact_Sales AS fs
JOIN Dim_Product AS dp
    USING (Product_ID)
GROUP BY
    dp.Category
ORDER BY
    Revenue DESC;


-- Top 10 products by revenue


SELECT
    dp.Product_Name,
    dp.Category,
    ROUND(SUM(fs.Net_Amount), 2) AS Revenue,
    ROUND(SUM(fs.Margin_Amount), 2) AS Margin,
    ROUND(
        SUM(fs.Margin_Amount) * 100.0
        / SUM(fs.Net_Amount),
        2
    ) AS Margin_Rate,
    SUM(fs.Quantity) AS Quantity
FROM Fact_Sales AS fs
JOIN Dim_Product AS dp
    USING (Product_ID)
GROUP BY
    dp.Product_Name,
    dp.Category
ORDER BY
    Revenue DESC
LIMIT 10;

WITH product_sales AS (

    SELECT
        dp.Product_Name,
        dp.Category,
        ROUND(SUM(fs.Net_Amount),2) AS Revenue,
        ROUND(SUM(fs.Margin_Amount),2) AS Margin,
        ROUND(
            SUM(fs.Margin_Amount)*100.0
            /SUM(fs.Net_Amount),
        2) AS Margin_Rate,
        SUM(fs.Quantity) AS Quantity

    FROM Fact_Sales fs

    JOIN Dim_Product dp
        USING(Product_ID)

    GROUP BY
        dp.Product_Name,
        dp.Category

)
SELECT

    RANK() OVER(
        ORDER BY Revenue DESC
    ) AS Product_Rank,

    Product_Name,

    Category,

    Revenue,

    Margin,

    Margin_Rate,

    Quantity

FROM product_sales

ORDER BY Product_Rank

LIMIT 10;



WITH product_sales AS (

    SELECT
        dp.Product_Name,
        ROUND(SUM(fs.Net_Amount), 2) AS Revenue
    FROM Fact_Sales AS fs
    JOIN Dim_Product AS dp
        USING (Product_ID)
    GROUP BY
        dp.Product_Name

),
product_share AS (

    SELECT
        Product_Name,
        Revenue,
        ROUND(
            Revenue * 100.0
            / SUM(Revenue) OVER (),
            2
        ) AS Revenue_Share
    FROM product_sales

),
pareto AS (

    SELECT
        Product_Name,
        Revenue,
        Revenue_Share,

        ROUND(
            SUM(Revenue_Share) OVER (
                ORDER BY Revenue DESC
            ),
            2
        ) AS Cumulative_Share

    FROM product_share

)

SELECT *
FROM pareto;


-- Revenue by subcategory


WITH subcategory_sales AS (

    SELECT
        dp.Category,
        dp.Subcategory,
        ROUND(SUM(fs.Net_Amount), 2) AS Revenue
    FROM Fact_Sales AS fs
    JOIN Dim_Product AS dp
        USING (Product_ID)
    GROUP BY
        dp.Category,
        dp.Subcategory

)

SELECT
    DENSE_RANK() OVER (
        ORDER BY Revenue DESC
    ) AS Subcategory_Rank,
    Category,
    Subcategory,
    Revenue
FROM subcategory_sales
ORDER BY
    Subcategory_Rank;


-- Top products by category

WITH product_sales AS (

    SELECT
        dp.Category,
        dp.Product_Name,
        ROUND(SUM(fs.Net_Amount), 2) AS Revenue
    FROM Fact_Sales AS fs
    JOIN Dim_Product AS dp
        USING (Product_ID)
    GROUP BY
        dp.Category,
        dp.Product_Name

)

SELECT
    Category,
    DENSE_RANK() OVER (
        PARTITION BY Category
        ORDER BY Revenue DESC
    ) AS Product_Rank,
    Product_Name,
    Revenue
FROM product_sales
ORDER BY
    Category,
    Product_Rank;


-- Top 3 products by category


WITH product_sales AS (

    SELECT
        dp.Category,
        dp.Product_Name,
        ROUND(SUM(fs.Net_Amount), 2) AS Revenue
    FROM Fact_Sales AS fs
    JOIN Dim_Product AS dp
        USING (Product_ID)
    GROUP BY
        dp.Category,
        dp.Product_Name

),

ranked_products AS (

    SELECT
        Category,
        Product_Name,
        Revenue,

        DENSE_RANK() OVER (
            PARTITION BY Category
            ORDER BY Revenue DESC
        ) AS Product_Rank

    FROM product_sales

)

SELECT
    Category,
    Product_Rank,
    Product_Name,
    Revenue

FROM ranked_products

WHERE Product_Rank <= 3

ORDER BY
    Category,
    Product_Rank;


