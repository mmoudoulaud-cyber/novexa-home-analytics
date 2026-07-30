"""
Store Dimension Generator
"""

import random

import pandas as pd

from novexa_home_analytics.config import (
    N_STORES,
    RANDOM_SEED,
    RAW_DATA_DIR,
)

random.seed(RANDOM_SEED)

CITIES = [
    "Paris",
    "Lyon",
    "Marseille",
    "Bordeaux",
    "Lille",
    "Toulouse",
    "Nantes",
    "Nice",
    "Rennes",
    "Strasbourg",
    "Montpellier",
    "Dijon",
]

STORE_TYPES = [
    "Retail",
    "Outlet",
    "Flagship",
]

REGIONS = [
    "North",
    "South",
    "East",
    "West",
]


def generate_store_dimension():

    rows = []

    for store_id in range(101, 101 + N_STORES):

        rows.append(
            {
                "Store_ID": store_id,
                "Store_Name": f"Novexa Store {store_id}",
                "City": random.choice(CITIES),
                "Region": random.choice(REGIONS),
                "Store_Type": random.choice(STORE_TYPES),
                "Opening_Year": random.randint(2010, 2025),
                "Surface_m2": random.randint(500, 4500),
                "Employees": random.randint(8, 60),
                "Is_Active": random.random() > 0.03,
            }
        )

    return pd.DataFrame(rows)


def export_store_dimension(df):

    output_file = RAW_DATA_DIR / "Dim_Store.csv"

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8",
    )

    print(f"Store dimension exported to: {output_file}")