"""Generate all NOVEXA dimensions and the sales fact table."""

from novexa_home_analytics.config import RAW_DATA_DIR
from novexa_home_analytics.generators.date_generator import (
    export_date_dimension,
    generate_date_dimension,
    validate_date_dimension,
)
from novexa_home_analytics.generators.supplier_generator import (
    export_supplier_dimension,
    generate_supplier_dimension,
)
from novexa_home_analytics.generators.warehouse_generator import (
    export_warehouse_dimension,
    generate_warehouse_dimension,
)
from novexa_home_analytics.generators.store_generator import (
    export_store_dimension,
    generate_store_dimension,
)
from novexa_home_analytics.generators.customer_generator import (
    export_customer_dimension,
    generate_customer_dimension,
)
from novexa_home_analytics.generators.product_generator import (
    export_product_dimension,
    generate_product_dimension,
)
from novexa_home_analytics.generators.sales_generator import generate_sales_dataset


def main() -> None:
    """Regenerate every CSV required by SQLite and Power BI."""
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    generators = [
        ("Date", generate_date_dimension, export_date_dimension, validate_date_dimension),
        ("Supplier", generate_supplier_dimension, export_supplier_dimension, None),
        ("Warehouse", generate_warehouse_dimension, export_warehouse_dimension, None),
        ("Store", generate_store_dimension, export_store_dimension, None),
        ("Customer", generate_customer_dimension, export_customer_dimension, None),
        ("Product", generate_product_dimension, export_product_dimension, None),
    ]

    for name, generate, export, validate in generators:
        print(f"Generating {name} dimension...")
        dataframe = generate()
        if validate:
            validate(dataframe)
        export(dataframe)

    print("Generating Sales fact...")
    generate_sales_dataset()
    print("\nDataset generation completed.")


if __name__ == "__main__":
    main()
