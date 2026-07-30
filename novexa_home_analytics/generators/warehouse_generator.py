"""
Warehouse Dimension Generator
"""

import random

import pandas as pd

from novexa_home_analytics.config import (
    RANDOM_SEED,
    RAW_DATA_DIR,
    N_WAREHOUSES,
)

random.seed(RANDOM_SEED)

CITIES = [
    "Lille",
    "Paris",
    "Lyon",
    "Bordeaux",
    "Marseille",
]


def generate_warehouse_dimension():

    rows = []

    for warehouse_id in range(1, N_WAREHOUSES + 1):

        rows.append(
            {
                "Warehouse_ID": warehouse_id,
                "Warehouse_Name": f"Warehouse {warehouse_id}",
                "City": random.choice(CITIES),
                "Capacity": random.randint(10000, 60000),
                "Employees": random.randint(15, 120),
                "Storage_Cost_m2": round(random.uniform(8, 22), 2),
                "Is_Active": random.random() > 0.02,
            }
        )

    return pd.DataFrame(rows)


def export_warehouse_dimension(df):

    output_file = RAW_DATA_DIR / "Dim_Warehouse.csv"

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8",
    )

    print(f"Warehouse dimension exported to: {output_file}")