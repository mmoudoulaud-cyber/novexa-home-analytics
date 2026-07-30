"""
Date Dimension Generator

Generates the Dim_Date table for Novexa Home Analytics.
"""

import pandas as pd

from novexa_home_analytics.config import (
    START_YEAR,
    END_YEAR,
    RAW_DATA_DIR,
)

def generate_date_dimension():
    """
    Generate the Date Dimension.
    """

    start_date = f"{START_YEAR}-01-01"
    end_date = "2026-06-30"

    dates = pd.date_range(
        start=start_date,
        end=end_date,
        freq="D"
    )

    df = pd.DataFrame({"Date": dates})
    
# Date key (YYYYMMDD)
    df["Date_ID"] = df["Date"].dt.strftime("%Y%m%d").astype(int)

# Calendar attributes
    df["Year"] = df["Date"].dt.year
    df["Quarter"] = df["Date"].dt.quarter
    df["Month"] = df["Date"].dt.month
    df["Month_Name"] = df["Date"].dt.month_name()

    df["Day"] = df["Date"].dt.day
    df["Day_Name"] = df["Date"].dt.day_name()

# ISO week number
    df["Week"] = df["Date"].dt.isocalendar().week.astype(int)

# Weekend indicator
    df["Is_Weekend"] = df["Date"].dt.dayofweek >= 5
    
    df = df[
    [
        "Date_ID",
        "Date",
        "Year",
        "Quarter",
        "Month",
        "Month_Name",
        "Week",
        "Day",
        "Day_Name",
        "Is_Weekend",
    ]
]

    return df

def export_date_dimension(df):
    """
    Export the Date Dimension to CSV.
    """

    output_file = RAW_DATA_DIR / "Dim_Date.csv"

    df.to_csv(
    output_file,
    index=False,
    encoding="utf-8"
)

    print(f"Date dimension exported to: {output_file}")

def validate_date_dimension(df):
    """
    Validate the generated Date Dimension.
    """

    assert len(df) == 912, "Unexpected number of rows."

    assert df["Date_ID"].is_unique, "Date_ID must be unique."

    assert df.isnull().sum().sum() == 0, "Missing values detected."

    print("✓ Date dimension validation successful.")