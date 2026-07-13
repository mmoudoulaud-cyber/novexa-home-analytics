# Dataset Design

## 1. Business Scenario

The dataset represents the operational activity of Novexa Home, a fictional French home improvement retailer operating through 126 stores and five distribution centers.

The objective of the dataset is to reproduce realistic retail operations over a three-year period (2024–2026), including sales transactions, customer purchases, supplier deliveries and inventory-related events.

The dataset has been intentionally designed to include realistic business behaviors and controlled data quality issues in order to simulate a real Business Intelligence project.

## 2. Tables Overview

| Table | Type | Description |
|--------|------|-------------|
| Dim_Date | Dimension | Calendar information |
| Dim_Product | Dimension | Product catalog |
| Dim_Store | Dimension | Stores |
| Dim_Customer | Dimension | Customers |
| Dim_Supplier | Dimension | Suppliers |
| Dim_Warehouse | Dimension | Distribution Centers |
| Fact_Sales | Fact | Sales transactions |

## 3. Dataset Size

| Table | Estimated Rows |
|--------|---------------:|
| Dim_Date | 1,096 |
| Dim_Product | 2,000 |
| Dim_Store | 126 |
| Dim_Customer | 50,000 |
| Dim_Supplier | 400 |
| Dim_Warehouse | 5 |
| Fact_Sales | 750,000 |

## 4. Business Rules

The synthetic dataset must reproduce realistic business behavior observed in a national home improvement retailer.

### Commercial Rules

- Revenue increases gradually between 2024 and 2026.
- Profitability decreases despite revenue growth.
- Discount campaigns are more frequent during seasonal events.
- Premium products generate higher margins but lower sales volumes.
- Budget products generate higher sales volumes but lower margins.

### Inventory Rules

- Garden products are highly seasonal.
- Decoration products sell consistently throughout the year.
- Home Office products experience increased demand during September.
- Some stores regularly experience stock shortages.

### Supplier Rules

- Supplier delivery performance varies significantly.
- Some suppliers systematically deliver late.
- Purchase costs gradually increase due to inflation.
- Certain suppliers specialize in premium products.

### Store Rules

- Large metropolitan stores generate higher revenue.
- Smaller stores often achieve better profit margins.
- Some stores consistently underperform against company targets.

### Customer Rules

- Loyalty members purchase more frequently.
- Premium customers have higher average basket values.
- New customers receive larger promotional discounts.

## 5. Seasonality

Sales follow realistic seasonal patterns.

| Category | Peak Period |
|----------|-------------|
| Garden | March to July |
| Decoration | November to December |
| Lighting | October to December |
| Kitchen | Stable throughout the year |
| Bathroom | Stable throughout the year |
| Living Room | September and December |
| Bedroom | January and September |
| Home Office | August and September |
| Storage | March and April |
| Small Furniture | September to November |

## 6. Data Quality Issues

The dataset intentionally contains realistic data quality problems.

### Missing Values

- Missing Supplier_ID
- Missing Brand
- Missing Customer City

### Duplicate Records

- Duplicate sales transactions
- Duplicate customer profiles

### Typographical Errors

- Incorrect category names
- Inconsistent supplier names
- Different country spellings

### Invalid Values

- Negative sales amounts
- Zero quantities
- Unrealistic discounts

### Inconsistent Formats

- Country codes (FR, France, FRA)
- Mixed date formats
- Product names with extra spaces


