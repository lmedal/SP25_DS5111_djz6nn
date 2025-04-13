import sys
sys.path.append('.')

import os
import pandas as pd
from bin.normalize_csv import normalize_csv

def test_normalizer():
    """
    GIVEN a sample CSV file with non-normalized column names
    WHEN the normalize_csv function is applied
    THEN the resulting file should exist and have expected normalized column names
    """
    test_file = "sample_data/test_gainers.csv"
    test_output = "sample_data/test_gainers_norm.csv"

    # GIVEN: Create a sample input CSV
    df = pd.DataFrame({
        "Symbol": ["AAPL", "GOOGL"],
        "Price": [150, 2800],
        "Change": [2, -10],
        "Change %": ["1.3%", "-0.35%"]
    })
    df.to_csv(test_file, index=False)

    # WHEN: Normalize the file
    normalize_csv(test_file)

    # THEN: Check if normalized file is created
    assert os.path.exists(test_output), "❌ Normalized file was not created."

    df_norm = pd.read_csv(test_output)

    # THEN: Check for expected column names
    expected_cols = ["symbol", "price", "price_change", "price_percent_change"]
    for col in expected_cols:
        assert col in df_norm.columns, f"❌ Expected column '{col}' not found."

    print("✅ Test Passed: CSV normalization works as expected.")
