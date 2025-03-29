"""
yahoo.py

Implements GainerProcess for Yahoo gainers.
"""

import datetime
import os
from bin.gainers.base import GainerProcess

class GainerProcessYahoo(GainerProcess):
    """Processes Yahoo gainers data"""

    def normalize(self):
        print("Normalizing Yahoo gainers...")

    def save_with_timestamp(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = getattr(self, "output_filename", f"data/raw/yahoo_gainers_{now}.csv")
        print(f"Saving Yahoo gainers to {filename}")

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write("symbol,price,price_change,price_percent_change\n")
            f.write("AAPL,150,2.3,+1.5%\n")
