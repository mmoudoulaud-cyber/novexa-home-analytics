from novexa_home_analytics.generators.product_generator import (
    load_reference_data,
    generate_product_name,
)

(
    adjectives,
    materials,
    brands,
    categories,
    products,
) = load_reference_data()

for _ in range(10):
    print(
        generate_product_name(
            adjectives,
            materials,
            products,
        )
    )