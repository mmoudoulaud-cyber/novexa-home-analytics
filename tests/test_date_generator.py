from novexa_home_analytics.generators.date_generator import (
    generate_date_dimension,
    validate_date_dimension,
    export_date_dimension,
)

df = generate_date_dimension()

validate_date_dimension(df)

export_date_dimension(df)

print(df.head())