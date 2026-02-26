from pathlib import Path

# Project Root Path (directory churn_analysis)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Directory of data related to the root of the project
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"