"""
Supplier Dimension Generator
"""

import random

import pandas as pd

from novexa_home_analytics.config import (
    RANDOM_SEED,
    RAW_DATA_DIR,
    N_SUPPLIERS,
)

random.seed(RANDOM_SEED)

COUNTRIES = [
    "France",
    "Germany",
    "Italy",
    "Spain",
    "Belgium",
    "Netherlands",
    "Poland",
    "Portugal",
]

SUPPLIER_TYPES = [
    "Manufacturer",
    "Distributor",
    "Wholesaler",
]

RATINGS = [3, 4, 5]


def generate_supplier_dimension():

    rows = []

    for supplier_id in range(2001, 2001 + N_SUPPLIERS):

        country = random.choice(COUNTRIES)

        rows.append(
            {
                "Supplier_ID": supplier_id,
                "Supplier_Name": f"Supplier {supplier_id}",
                "Country": country,
                "Supplier_Type": random.choice(SUPPLIER_TYPES),
                "Rating": random.choice(RATINGS),
                "Lead_Time_Days": random.randint(2, 35),
                "Is_Active": random.random() > 0.05,
            }
        )

    return pd.DataFrame(rows)


def export_supplier_dimension(df):

    output_file = RAW_DATA_DIR / "Dim_Supplier.csv"

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8",
    )

    print(f"Supplier dimension exported to: {output_file}")
