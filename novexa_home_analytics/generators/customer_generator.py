"""
Customer Dimension Generator
"""

import random

import pandas as pd
from faker import Faker

from novexa_home_analytics.config import (
    N_CUSTOMERS,
    RANDOM_SEED,
    RAW_DATA_DIR,
)

fake = Faker("fr_FR")
Faker.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)


def generate_customer_dimension():

    rows = []

    loyalty_levels = [
        "Bronze",
        "Silver",
        "Gold",
        "Platinum",
    ]

    for customer_id in range(1000001, 1000001 + N_CUSTOMERS):

        rows.append(
            {
                "Customer_ID": customer_id,
                "First_Name": fake.first_name(),
                "Last_Name": fake.last_name(),
                "Gender": random.choice(
                    ["Male", "Female"]
                ),
                "Age": random.randint(18, 85),
                "City": fake.city(),
                "Country": "France",
                "Loyalty_Level": random.choices(
                    loyalty_levels,
                    weights=[45, 30, 20, 5],
                    k=1,
                )[0],
                "Registration_Year": random.randint(
                    2018,
                    2026,
                ),
                "Is_Active": random.random() > 0.08,
            }
        )

    return pd.DataFrame(rows)


def export_customer_dimension(df):

    output_file = RAW_DATA_DIR / "Dim_Customer.csv"

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8",
    )

    print(
        f"Customer dimension exported to: {output_file}"
    )