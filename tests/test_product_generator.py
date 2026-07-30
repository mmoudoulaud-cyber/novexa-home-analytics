from novexa_home_analytics.generators.product_generator import (
    load_reference_data,
)

(
    adjectives,
    materials,
    brands,
    categories,
    products,
) = load_reference_data()

print(adjectives.head())
print()

print(materials.head())
print()

print(brands.head())
print()

print(categories.head())
print()

print(products.head())

