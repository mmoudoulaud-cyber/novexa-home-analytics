"""Vectorised generator for the NOVEXA Fact_Sales table.

The scenario is deliberately simple and traceable: demand and e-commerce grow,
while supplier/logistics costs, discounts and the low-margin product mix rise.
No hidden margin adjustment is used.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from novexa_home_analytics.config import N_SALES, RANDOM_SEED, RAW_DATA_DIR

FACT_COLUMNS = [
    "Sale_ID", "Date_ID", "Product_ID", "Customer_ID", "Store_ID",
    "Supplier_ID", "Warehouse_ID", "Quantity", "Unit_Price", "Unit_Cost",
    "Discount_Pct", "Gross_Amount", "Discount_Amount", "Net_Amount",
    "Margin_Amount", "Payment_Method", "Sales_Channel",
]

MONTH_FACTOR = {1: .86, 2: .89, 3: .95, 4: 1.00, 5: 1.05, 6: 1.10,
                7: 1.14, 8: 1.08, 9: .98, 10: 1.04, 11: 1.25, 12: 1.34}
YEAR_DEMAND = {2024: 1.00, 2025: 1.09, 2026: 1.20}
PRICE_FACTOR = {2024: 1.00, 2025: 1.025, 2026: 1.050}
# Includes supplier inflation and logistics pressure, both visible in Unit_Cost.
COST_FACTOR = {2024: 1.00, 2025: 1.085, 2026: 1.205}
CHANNEL_PROBS = {
    2024: [0.67, 0.23, 0.10],
    2025: [0.60, 0.29, 0.11],
    2026: [0.53, 0.35, 0.12],
}
CHANNELS = np.array(["Store", "Online", "Click & Collect"])
LOW_MARGIN_CATEGORIES = {"Living Room", "Bedroom", "Office", "Outdoor", "Storage"}


def _load(name: str) -> pd.DataFrame:
    path = RAW_DATA_DIR / f"{name}.csv"
    if not path.exists():
        raise FileNotFoundError(f"Missing required dimension: {path}")
    return pd.read_csv(path)


def generate_sales() -> pd.DataFrame:
    rng = np.random.default_rng(RANDOM_SEED)
    dates = _load("Dim_Date")
    products = _load("Dim_Product")
    customers = _load("Dim_Customer")
    stores = _load("Dim_Store")
    warehouses = _load("Dim_Warehouse")

    date_weights = (
        dates["Year"].map(YEAR_DEMAND).astype(float)
        * dates["Month"].map(MONTH_FACTOR).astype(float)
    ).to_numpy()
    date_idx = rng.choice(len(dates), N_SALES, p=date_weights / date_weights.sum())
    selected_dates = dates.iloc[date_idx].reset_index(drop=True)
    years = selected_dates["Year"].to_numpy(dtype=int)
    months = selected_dates["Month"].to_numpy(dtype=int)

    # Product long tail plus a progressive shift toward lower-margin categories.
    base_popularity = rng.lognormal(mean=0.0, sigma=0.75, size=len(products))
    low_margin = products["Category"].isin(LOW_MARGIN_CATEGORIES).to_numpy()
    product_idx = np.empty(N_SALES, dtype=int)
    for year in (2024, 2025, 2026):
        mask = years == year
        mix_boost = {2024: 1.00, 2025: 1.18, 2026: 1.42}[year]
        weights = base_popularity * np.where(low_margin, mix_boost, 1.0)
        product_idx[mask] = rng.choice(len(products), mask.sum(), p=weights / weights.sum())
    selected_products = products.iloc[product_idx].reset_index(drop=True)

    channels = np.empty(N_SALES, dtype=object)
    for year in (2024, 2025, 2026):
        mask = years == year
        channels[mask] = rng.choice(CHANNELS, mask.sum(), p=CHANNEL_PROBS[year])

    quantity = np.empty(N_SALES, dtype=int)
    quantity_probs = {2024: [.72, .20, .06, .015, .005],
                      2025: [.70, .21, .065, .020, .005],
                      2026: [.68, .22, .070, .025, .005]}
    for year in (2024, 2025, 2026):
        mask = years == year
        quantity[mask] = rng.choice([1, 2, 3, 4, 5], mask.sum(), p=quantity_probs[year])

    # Promotions rise over time and are stronger online and during sales periods.
    discount = np.zeros(N_SALES, dtype=int)
    discount_levels = np.array([0, 5, 10, 15, 20, 25, 30])
    for year in (2024, 2025, 2026):
        for channel in CHANNELS:
            mask = (years == year) & (channels == channel)
            base = {
                2024: {"Store": [.70,.19,.07,.03,.01,0,0], "Online": [.52,.23,.14,.07,.03,.01,0], "Click & Collect": [.60,.22,.11,.05,.02,0,0]},
                2025: {"Store": [.62,.21,.10,.05,.02,0,0], "Online": [.42,.24,.17,.10,.05,.02,0], "Click & Collect": [.53,.23,.13,.07,.03,.01,0]},
                2026: {"Store": [.54,.23,.12,.07,.03,.01,0], "Online": [.32,.24,.19,.12,.08,.04,.01], "Click & Collect": [.45,.24,.16,.09,.04,.02,0]},
            }[year][channel]
            discount[mask] = rng.choice(discount_levels, mask.sum(), p=base)
    promo_mask = np.isin(months, [7, 8, 11, 12]) & (rng.random(N_SALES) < .32)
    discount[promo_mask] = np.minimum(30, discount[promo_mask] + 5)

    price_noise = np.clip(rng.normal(1, .008, N_SALES), .975, 1.025)
    cost_noise = np.clip(rng.normal(1, .010, N_SALES), .970, 1.035)
    unit_price = np.round(selected_products["Unit_Price"].to_numpy(float) * pd.Series(years).map(PRICE_FACTOR).to_numpy() * price_noise, 2)
    unit_cost = np.round(selected_products["Unit_Cost"].to_numpy(float) * pd.Series(years).map(COST_FACTOR).to_numpy() * cost_noise, 2)

    gross = np.round(quantity * unit_price, 2)
    discount_amount = np.round(gross * discount / 100, 2)
    net = np.round(gross - discount_amount, 2)
    margin = np.round(net - quantity * unit_cost, 2)

    store_ids = stores["Store_ID"].to_numpy()
    warehouse_ids = warehouses["Warehouse_ID"].to_numpy()
    customer_ids = customers["Customer_ID"].to_numpy()
    payment = np.where(channels == "Online",
                       rng.choice(["Credit Card", "Bank Transfer", "Gift Card"], N_SALES, p=[.77,.17,.06]),
                       rng.choice(["Credit Card", "Cash", "Bank Transfer", "Gift Card"], N_SALES, p=[.50,.27,.14,.09]))

    result = pd.DataFrame({
        "Sale_ID": np.arange(1, N_SALES + 1),
        "Date_ID": selected_dates["Date_ID"].to_numpy(),
        "Product_ID": selected_products["Product_ID"].to_numpy(),
        "Customer_ID": rng.choice(customer_ids, N_SALES),
        "Store_ID": rng.choice(store_ids, N_SALES),
        "Supplier_ID": selected_products["Supplier_ID"].to_numpy(),
        "Warehouse_ID": rng.choice(warehouse_ids, N_SALES),
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Unit_Cost": unit_cost,
        "Discount_Pct": discount,
        "Gross_Amount": gross,
        "Discount_Amount": discount_amount,
        "Net_Amount": net,
        "Margin_Amount": margin,
        "Payment_Method": payment,
        "Sales_Channel": channels,
    })
    return result.sort_values(["Date_ID", "Sale_ID"]).reset_index(drop=True).assign(
        Sale_ID=lambda frame: np.arange(1, len(frame) + 1)
    )[FACT_COLUMNS]


def save_sales(df: pd.DataFrame) -> None:
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output = RAW_DATA_DIR / "Fact_Sales.csv"
    df.to_csv(output, index=False)
    print(f"{len(df):,} sales generated.")
    print(f"Saved to: {output}")


def generate_sales_dataset() -> pd.DataFrame:
    dataframe = generate_sales()
    save_sales(dataframe)
    return dataframe


if __name__ == "__main__":
    generate_sales_dataset()
