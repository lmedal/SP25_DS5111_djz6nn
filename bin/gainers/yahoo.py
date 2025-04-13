import os
from bin.gainers.base import GainerProcess

class GainerProcessYahoo(GainerProcess):
    """Processes Yahoo gainers data"""

    def normalize(self):
        print("Normalizing Yahoo gainers...")

    def save_with_timestamp(self):
        print("📥 Downloading Yahoo gainers via Makefile...")
        os.system("make ygainers.csv")
