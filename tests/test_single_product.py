from novexa_home_analytics.generators.product_generator import (
    generate_product_dimension,
)


def test_generate_single_product():
    df = generate_product_dimension()

    assert len(df) > 0

    product = df.iloc[0]

    assert product["Product_ID"] > 0
    assert product["SKU"].startswith("NVX-")
    assert product["Unit_Cost"] > 0
    assert product["Unit_Price"] > product["Unit_Cost"]
    