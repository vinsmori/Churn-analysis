import pandas as pd
from .utils import RAW_DATA_DIR

def load_telco_data(filename: str = "telco-customer-churn.csv") -> pd.DataFrame:
    csv_path = RAW_DATA_DIR / filename
    if not csv_path.exists():
        raise FileNotFoundError(f"Expected file at {csv_path}. "
                                f"Please download the dataset and place it there.")
    return pd.read_csv(csv_path)