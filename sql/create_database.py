"""
Create SQLite database from generated CSV files.

Author: Merryl Moudoulaud
"""

from pathlib import Path
import sqlite3

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
DATABASE_DIR = PROJECT_ROOT / "database"
DATABASE_FILE = DATABASE_DIR / "novexa_home.db"

TABLES = [
    "Dim_Date",
    "Dim_Product",
    "Dim_Supplier",
    "Dim_Store",
    "Dim_Warehouse",
    "Dim_Customer",
    "Fact_Sales",
]


def create_database():

    DATABASE_DIR.mkdir(exist_ok=True)

    if DATABASE_FILE.exists():
        DATABASE_FILE.unlink()

    connection = sqlite3.connect(DATABASE_FILE)

    try:
        for table in TABLES:

            csv_file = RAW_DATA_DIR / f"{table}.csv"

            print(f"Loading {table}...")

            df = pd.read_csv(csv_file)

            df.to_sql(
                name=table,
                con=connection,
                if_exists="replace",
                index=False,
            )

            print(f"✓ {len(df):,} rows")

    finally:
        connection.close()

    print()
    print(f"Database created:")
    print(DATABASE_FILE)


if __name__ == "__main__":
    create_database()