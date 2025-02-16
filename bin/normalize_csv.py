import pandas as pd
import argparse
import os


def normalize_csv(input_path):
    """
    Reads a raw stock gainers CSV file, normalizes it, and saves it as <input_path>_norm.csv.
    """
    assert os.path.exists(input_path), f"Error: File '{input_path}' not found."

    # Load CSV and clean column names
    df = pd.read_csv(input_path)
    df.columns = df.columns.str.strip()  # Trim spaces from column names

    if "Symbol" in df.columns:
        # Yahoo Finance format
        df = df.rename(
            columns={
                "Symbol": "symbol",
                "Price": "price",
                "Change": "price_change",
                "Change %": "price_percent_change",
            }
        )
    elif "Unnamed: 0" in df.columns:
        # WSJ format
        df = df.rename(
            columns={
                "Unnamed: 0": "symbol",
                "Last": "price",
                "Chg": "price_change",
                "% Chg": "price_percent_change",
            }
        )
    else:
        raise ValueError("Error: Unknown CSV format. Cannot normalize.")

    # Ensure required columns exist
    required_columns = {"symbol", "price", "price_change", "price_percent_change"}
    missing_columns = required_columns - set(df.columns)
    assert not missing_columns, f"Error: Missing required columns: {missing_columns}"

    # Convert numeric columns
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["price_change"] = pd.to_numeric(df["price_change"], errors="coerce")

    # Convert percentage column (e.g., "12.34%" → 0.1234)
    df["price_percent_change"] = (
        df["price_percent_change"].astype(str).str.replace("%", "").astype(float) / 100
    )

    # Drop rows with missing values after conversion
    df = df.dropna(subset=["price", "price_change", "price_percent_change"])

    # Save to new file
    output_path = input_path.replace(".csv", "_norm.csv")
    df[["symbol", "price", "price_change", "price_percent_change"]].to_csv(
        output_path, index=False
    )

    print(f"✅ Normalized CSV saved to: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Normalize stock gainer CSV files")
    parser.add_argument("input_file", help="Path to raw CSV file")
    args = parser.parse_args()

    normalize_csv(args.input_file)
