from novexa_home_analytics.generators.store_generator import (
    generate_store_dimension,
    export_store_dimension,
)

df = generate_store_dimension()

export_store_dimension(df)

print(df.head())

print()

print(df.shape)