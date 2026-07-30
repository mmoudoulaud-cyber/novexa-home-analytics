from novexa_home_analytics.config import (
    PROJECT_ROOT,
    RAW_DATA_DIR,
    N_PRODUCTS,
    N_CUSTOMERS,
    N_SALES,
    MISSING_RATE,
)


def test_config_loaded():
    assert PROJECT_ROOT.exists()
    assert RAW_DATA_DIR.exists()
    assert N_PRODUCTS > 0
    assert N_CUSTOMERS > 0
    assert N_SALES > 0
    assert 0 <= MISSING_RATE <= 1