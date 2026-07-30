# Validation finale du dataset NOVEXA

## Corrections appliquées

- Le pipeline principal exporte désormais toutes les dimensions avant de générer `Fact_Sales`.
- Deux commandes simples ont été ajoutées à la racine : `python generate_dataset.py` et `python create_database.py`.
- Le générateur de ventes a été vectorisé pour produire rapidement 750 000 lignes.
- `Margin_Amount` respecte strictement la formule `Net_Amount - Quantity × Unit_Cost`.
- La baisse de rentabilité résulte de coûts croissants, de remises plus fortes, du développement du e-commerce et d'un mix produit moins favorable.
- Aucun nom de table ou de colonne utilisé dans Power BI n'a été modifié.

## Contrôles exécutés

- Génération complète des six dimensions et de la table de faits : réussie.
- Tests Python : 11 réussis.
- Construction SQLite : réussie.
- Requêtes SQL `00` à `05` : exécutées sans erreur.
- Clés produits/fournisseurs cohérentes : validées par les tests et le pipeline.

## Résultat métier YTD janvier-juin

- Chiffre d'affaires 2026 > 2025 > 2024.
- Nombre de commandes 2026 > 2025 > 2024.
- Taux de marge en baisse : 39,84 % → 35,21 % → 28,36 %.
- Marge absolue sous pression en 2026 : 25,06 M€ contre 25,70 M€ en 2025.
- Remise moyenne en hausse : 2,88 % → 4,10 % → 5,62 %.
- Part Online en hausse : 22,99 % → 29,11 % → 35,13 %.
