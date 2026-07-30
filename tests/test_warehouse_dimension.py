from novexa_home_analytics.generators.warehouse_generator import (
    generate_warehouse_dimension,
    export_warehouse_dimension,
)

df = generate_warehouse_dimension()

export_warehouse_dimension(df)

print(df.head())

print()

print(df.shape)