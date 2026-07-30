"""
Product Dimension Generator

Generates the Product Dimension for Novexa Home Analytics.
"""

import random
from datetime import datetime, timedelta

import pandas as pd

from novexa_home_analytics.config import (
    N_PRODUCTS,
    N_SUPPLIERS,
    RANDOM_SEED,
)

from novexa_home_analytics.utils.csv_loader import load_csv

random.seed(RANDOM_SEED)

PRICE_RANGES = {
    "Decor": {"cost": (5, 40), "margin": (0.55, 0.65)},
    "Lighting": {"cost": (20, 120), "margin": (0.45, 0.60)},
    "Kitchen": {"cost": (15, 80), "margin": (0.40, 0.55)},
    "Bathroom": {"cost": (20, 100), "margin": (0.40, 0.55)},
    "Storage": {"cost": (40, 250), "margin": (0.40, 0.55)},
    "Office": {"cost": (50, 350), "margin": (0.35, 0.50)},
    "Bedroom": {"cost": (80, 600), "margin": (0.35, 0.45)},
    "Living Room": {"cost": (150, 1200), "margin": (0.30, 0.45)},
    "Outdoor": {"cost": (50, 600), "margin": (0.35, 0.50)},
}

def load_reference_data():
    """Load reference CSV files."""

    adjectives = load_csv("adjectives.csv")
    materials = load_csv("materials.csv")
    brands = load_csv("brands.csv")
    categories = load_csv("categories.csv")
    products = load_csv("products.csv")

    return (
        adjectives,
        materials,
        brands,
        categories,
        products,
    )


def generate_product_name(adjectives, materials, products):
    """Generate a realistic product name."""

    adjective = random.choice(adjectives["Adjective"].tolist())
    material = random.choice(materials["Material"].tolist())
    product = random.choice(products["Product"].tolist())

    return f"{adjective} {material} {product}"


def generate_sku(product_id):
    """Generate SKU."""

    return f"NVX-{product_id}"


def generate_price_segment():
    """Generate product segment."""

    return random.choices(
        ["Entry", "Mid-Range", "Premium"],
        weights=[35, 45, 20],
        k=1,
    )[0]


def generate_cost_and_price(category_name):
    """Generate purchase cost and selling price."""

    config = PRICE_RANGES.get(
        category_name,
        {"cost": (20, 150), "margin": (0.40, 0.55)},
    )

    min_cost, max_cost = config["cost"]
    min_margin, max_margin = config["margin"]

    mode = min_cost + (max_cost - min_cost) * 0.30

    unit_cost = round(
        random.triangular(min_cost, max_cost, mode),
        2,
    )

    margin_rate = random.uniform(min_margin, max_margin)

    unit_price = round(
        unit_cost / (1 - margin_rate),
        2,
    )

    return unit_cost, unit_price


def generate_launch_date():
    """Generate launch date."""

    start = datetime(2020, 1, 1)
    end = datetime(2026, 12, 31)

    delta = end - start

    return (
        start + timedelta(days=random.randint(0, delta.days))
    ).date()


def generate_discontinued():
    """Random discontinued flag."""

    return random.random() < 0.05


def generate_product_dimension():
    """Generate Product Dimension."""

    (
        adjectives,
        materials,
        brands,
        categories,
        products,
    ) = load_reference_data()

    rows = []

    for product_id in range(100001, 100001 + N_PRODUCTS):

        category = categories.sample(n=1).iloc[0]

        segment = generate_price_segment()

        cost, price = generate_cost_and_price(category["Category"])

        rows.append(
            {
                "Product_ID": product_id,
                "SKU": generate_sku(product_id),
                "Product_Name": generate_product_name(
                    adjectives,
                    materials,
                    products,
                ),
                "Brand": random.choice(brands["Brand"].tolist()),
                "Supplier_ID": random.randint(2001, 2000 + N_SUPPLIERS),
                "Category": category["Category"],
                "Subcategory": category["Subcategory"],
                "Price_Segment": segment,
                "Unit_Cost": cost,
                "Unit_Price": price,
                "Base_Margin_Rate": round((price - cost) / price, 4),
                "Launch_Date": generate_launch_date(),
                "Product_Status": random.choices(
    ["Active", "Discontinued"],
    weights=[95, 5],
    k=1,
)[0],
            }
        )

    return pd.DataFrame(rows)

from novexa_home_analytics.config import RAW_DATA_DIR


def export_product_dimension(df):
    """
    Export Product Dimension to CSV.
    """

    output_file = RAW_DATA_DIR / "Dim_Product.csv"

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8",
    )

    print(f"Product dimension exported to: {output_file}")