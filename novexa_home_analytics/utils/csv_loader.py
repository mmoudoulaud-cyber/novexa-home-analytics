from pathlib import Path

import pandas as pd


REFERENCE_DATA_DIR = (
    Path(__file__).resolve().parent.parent.parent
    / "assets"
    / "reference_data"
)


def load_csv(filename: str) -> pd.DataFrame:
    """
    Load a CSV file from the reference_data folder.
    """

    file_path = REFERENCE_DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Reference file not found: {file_path}"
        )

    try:
        return pd.read_csv(file_path)

    except pd.errors.EmptyDataError:
        raise ValueError(
            f"{filename} is empty."
        )