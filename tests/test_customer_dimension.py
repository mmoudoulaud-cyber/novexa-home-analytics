from novexa_home_analytics.generators.customer_generator import (
    generate_customer_dimension,
    export_customer_dimension,
)

df = generate_customer_dimension()

export_customer_dimension(df)

print(df.head())

print()

print(df.shape)