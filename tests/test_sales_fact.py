import numpy as np
import pandas as pd

from novexa_home_analytics.config import RAW_DATA_DIR, N_SALES


FACT_FILE = RAW_DATA_DIR / "Fact_Sales.csv"


def load_sales():
    return pd.read_csv(FACT_FILE)


def test_fact_sales_file_exists():
    assert FACT_FILE.exists()


def test_number_of_sales():
    df = load_sales()
    assert len(df) == N_SALES


def test_sale_id_unique():
    df = load_sales()
    assert df["Sale_ID"].is_unique


def test_quantity_positive():
    df = load_sales()
    assert (df["Quantity"] > 0).all()


def test_gross_amount():
    df = load_sales()

    expected = (
        df["Quantity"] * df["Unit_Price"]
    ).round(2)

    assert np.allclose(
        expected,
        df["Gross_Amount"],
        atol=0.01,
    )


def test_net_amount():
    df = load_sales()

    expected = (
        df["Gross_Amount"] - df["Discount_Amount"]
    ).round(2)

    assert np.allclose(
        expected,
        df["Net_Amount"],
        atol=0.01,
    )


def test_margin_amount():
    df = load_sales()

    expected = (
        df["Net_Amount"]
        - (df["Quantity"] * df["Unit_Cost"])
    ).round(2)

    assert np.allclose(
    expected,
    df["Margin_Amount"],
    atol=0.01,
)


def test_payment_method():
    df = load_sales()

    allowed = {
        "Credit Card",
        "Cash",
        "Bank Transfer",
        "Gift Card",
    }

    assert set(df["Payment_Method"]).issubset(allowed)


def test_sales_channel():
    df = load_sales()

    allowed = {
        "Store",
        "Online",
        "Click & Collect",
    }

    assert set(df["Sales_Channel"]).issubset(allowed)
    