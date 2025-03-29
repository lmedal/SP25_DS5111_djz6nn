"""
wsj.py

Implements GainerProcess for WSJ gainers.
"""

import datetime
import os
from bin.gainers.base import GainerProcess

class GainerProcessWSJ(GainerProcess):
    """Processes WSJ gainers data"""

    def normalize(self):
        print("Normalizing WSJ gainers...")

    def save_with_timestamp(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = getattr(self, "output_filename", f"data/raw/wsj_gainers_{now}.csv")
        print(f"Saving WSJ gainers to {filename}")

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write("symbol,price,price_change,price_percent_change\n")
            f.write("MSFT,310,4.5,+1.7%\n")
