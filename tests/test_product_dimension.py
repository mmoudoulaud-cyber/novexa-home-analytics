from novexa_home_analytics.generators.product_generator import (
    generate_product_dimension,
    export_product_dimension,
)

df = generate_product_dimension()

export_product_dimension(df)

print(df.head())

print()

print(df.shape)