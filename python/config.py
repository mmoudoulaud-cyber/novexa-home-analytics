"""
Novexa Home Analytics

Global project configuration.

Author: Merryl Moudoulaud
"""

from pathlib import Path

# ==========================================================
# PROJECT PATHS
# ==========================================================

# Root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data folders
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
INTERIM_DATA_DIR = PROJECT_ROOT / "data" / "interim"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Logs folder
LOG_DIR = PROJECT_ROOT / "logs"

# ==========================================================
# DATASET CONFIGURATION
# ==========================================================

RANDOM_SEED = 42

START_YEAR = 2024
END_YEAR = 2026

N_PRODUCTS = 2000
N_CUSTOMERS = 50000
N_SUPPLIERS = 400
N_STORES = 126
N_WAREHOUSES = 5
N_SALES = 750000

# ==========================================================
# DATA QUALITY
# ==========================================================

# Percentage of missing values
MISSING_RATE = 0.01

# Percentage of duplicate rows
DUPLICATE_RATE = 0.005

# Percentage of typographical errors
TYPO_RATE = 0.003

# Percentage of outliers
OUTLIER_RATE = 0.002

