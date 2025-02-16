import sys
import os

# Find 'bin'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from bin.normalize_csv import normalize_csv

def test_normalizer():
    test_file = "sample_data/test_gainers.csv"
    test_output = "sample_data/test_gainers_norm.csv"

    # Create a dummy CSV file
    df = pd.DataFrame({
        "Symbol": ["AAPL", "GOOGL"],
        "Price": [150, 2800],
        "Change": [2, -10],
        "Change %": ["1.3%", "-0.35%"]
    })
    df.to_csv(test_file, index=False)

    # Run normalization
    normalize_csv(test_file)

    # Verify output
    assert os.path.exists(test_output), "Normalized file not created"
    df_norm = pd.read_csv(test_output)

    assert "symbol" in df_norm.columns
    assert "price" in df_norm.columns
    assert "price_change" in df_norm.columns
    assert "price_percent_change" in df_norm.columns

    print("✅ Test Passed: CSV Normalization Works!")

if __name__ == "__main__":
    test_normalizer()
