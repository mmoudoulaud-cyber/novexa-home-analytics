# Business Requirements Document

**Project:** NOVEXA Home Analytics

**Version:** 2.0

**Author:** Merryl Moudoulaud

**Date:** July 2026

---

# 1. Business Context

NOVEXA Home has experienced continuous revenue and order growth over recent years. However, despite this positive commercial performance, overall profitability has steadily declined.

Executive management needs greater visibility into business performance to better understand the factors driving this trend and support data-driven decision-making.

The objective of this project is to provide an interactive Business Intelligence solution capable of analysing sales performance, profitability and business drivers through a Power BI dashboard.

---

# 2. Problem Statement

Although the company continues to grow, management has identified a gradual decline in overall profitability.

Several hypotheses have been raised:

- Increasing discount levels
- Changing sales channel mix
- Differences in profitability between product categories
- Uneven store performance

The Business Intelligence solution aims to validate these hypotheses using data.

---

# 3. Project Objectives

The project aims to:

- Monitor overall business performance
- Analyse revenue and profitability trends
- Understand the impact of discounts on margin
- Compare sales channels
- Identify the most profitable product categories
- Compare store performance
- Provide actionable business recommendations

---

# 4. Business Questions

The dashboard should answer the following business questions.

## Executive Management

- Why is profitability declining despite revenue growth?
- How have revenue and margin evolved over time?
- Which business drivers have the greatest impact on profitability?

## Sales

- Which sales channels generate the highest revenue?
- How do discounts affect profitability?
- How has the average basket evolved?

## Products

- Which product categories generate the highest revenue?
- Which categories have the highest and lowest margin rates?
- Which products contribute most to profitability?

## Stores

- Which cities generate the highest revenue?
- Which stores perform above or below average?
- How does profitability vary across store formats?

---

# 5. Business KPIs

The dashboard includes the following KPIs.

| KPI | Business Purpose |
|------|------------------|
| Revenue | Monitor commercial performance |
| Orders | Measure sales activity |
| Margin % | Measure profitability |
| Margin Amount | Measure financial performance |
| Average Basket | Analyse customer purchasing behaviour |
| Discount Rate | Measure pricing strategy |
| Revenue by Channel | Compare sales channels |
| Revenue by Category | Compare product performance |

---

# 6. Functional Requirements

The Power BI report must allow users to:

- Filter by Year
- Filter by Product Category
- Filter by Sales Channel
- Filter by Store
- Analyse Year-over-Year performance
- Explore product and store performance
- Navigate across dashboard pages

---

# 7. Data Model

The analytical solution is based on a Star Schema including:

- Fact_Sales
- Dim_Date
- Dim_Product
- Dim_Customer
- Dim_Store
- Dim_Supplier
- Dim_Warehouse

---

# 8. Dashboard Structure

The reporting solution consists of five pages.

## Executive Sales Dashboard

High-level KPIs and business performance overview.

## Sales Performance

Analysis of sales channels, customer behaviour and discounts.

## Product Performance

Analysis of product categories, revenue and profitability.

## Store Performance

Comparison of store and city performance.

## Profitability Insights

Summary of key findings and business recommendations.

---

# 9. Success Criteria

The project will be considered successful if:

- The dashboard answers the identified business questions.
- KPIs remain consistent across all report pages.
- Business users can easily identify profitability drivers.
- The report supports data-driven decision-making.
- Insights are clearly communicated through effective visualisations.