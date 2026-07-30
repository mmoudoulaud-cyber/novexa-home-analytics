# Star Schema

**Project:** Novexa Home Analytics

**Version:** 1.0

**Status:** Draft

**Author:** Merryl Moudoulaud

**Date:** July 2026

---

## Objective

This document describes the dimensional data model used for the Novexa Home Analytics project.

The model follows Kimball dimensional modeling principles using a Star Schema architecture with one central fact table and multiple conformed dimensions.

## Logical Model

The analytical model consists of one transactional fact table linked to six conformed dimensions.

### Fact Table

- Fact_Sales

### Dimensions

- Dim_Date
- Dim_Product
- Dim_Store
- Dim_Customer
- Dim_Supplier
- Dim_Warehouse

## Business Process

The project is centered around one core business process:

- Sales Transactions

Each record in the fact table represents one product sold during a single sales transaction (transaction line grain).

---

## Bus Matrix

| Business Process | Date | Product | Store | Customer | Supplier | Warehouse |
|------------------|:----:|:-------:|:-----:|:--------:|:--------:|:---------:|
| Sales Transactions | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Fact Table Grain

The grain of Fact_Sales is defined as:

> One product sold, in one store, to one customer, on one date.

Each row therefore represents a single sales transaction line.

## Relationships

Fact_Sales contains foreign keys referencing each conformed dimension.

| Fact Table | Dimension | Relationship |
|------------|-----------|--------------|
| Fact_Sales | Dim_Date | Many-to-One |
| Fact_Sales | Dim_Product | Many-to-One |
| Fact_Sales | Dim_Store | Many-to-One |
| Fact_Sales | Dim_Customer | Many-to-One |
| Fact_Sales | Dim_Supplier | Many-to-One |
| Fact_Sales | Dim_Warehouse | Many-to-One |

## Physical Diagram

The complete Star Schema diagram is available in:

- star_schema.drawio
- star_schema.png


## Dimension: Dim_Product

### Purpose

Stores descriptive information about products sold by Novexa Home.

This dimension allows analysis by category, brand, supplier, price segment and product lifecycle.

### Business Rules

- Premium products generate higher margins.
- Budget products generate higher sales volumes.
- Garden products are highly seasonal.
- Decoration products are frequently discounted.
- Home Office products experience a sales peak in September.
- Product prices increase gradually over the three-year period.

### Controlled Data Quality Issues

The Product dimension intentionally includes:

- Missing brands (≈1%)
- Missing supplier references (≈0.5%)
- Typographical errors in category names
- Duplicate product descriptions
- Inconsistent capitalization
- Extra spaces in product names

## Dimension: Dim_Store

### Purpose

Stores descriptive information about Novexa Home retail stores.

This dimension supports geographical, regional and operational performance analysis.

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| Store_ID | Integer | Unique store identifier |
| Store_Name | Text | Store name |
| Store_Format | Text | City Center / Retail Park / Shopping Mall |
| City | Text | City |
| Region | Text | French administrative region |
| Opening_Date | Date | Store opening date |
| Surface_Area | Integer | Sales area (m²) |
| Employees | Integer | Number of employees |
| Annual_Target | Decimal | Annual revenue target |
| Warehouse_ID | Integer | Assigned distribution center |
| Is_Flagship | Boolean | Flagship store indicator |

### Business Rules

- 126 stores are distributed across France.
- Flagship stores are located in major metropolitan areas.
- Large stores generate higher revenue.
- Smaller stores often achieve higher margins.
- Some stores consistently underperform.
- Every store is assigned to one warehouse.

### Controlled Data Quality Issues

The Store dimension intentionally includes:

- Missing surface area values
- Inconsistent city capitalization
- Duplicate store names (very limited)
- Missing opening dates

