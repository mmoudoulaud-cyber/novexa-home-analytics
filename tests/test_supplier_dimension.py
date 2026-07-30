from novexa_home_analytics.generators.supplier_generator import (
    generate_supplier_dimension,
    export_supplier_dimension,
)

df = generate_supplier_dimension()

export_supplier_dimension(df)

print(df.head())

print()

print(df.shape)