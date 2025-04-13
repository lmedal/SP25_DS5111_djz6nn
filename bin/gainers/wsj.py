import os
from bin.gainers.base import GainerProcess

class GainerProcessWSJ(GainerProcess):
    """Processes WSJ gainers data"""

    def normalize(self):
        print("Normalizing WSJ gainers...")

    def save_with_timestamp(self):
        print("📥 Downloading WSJ gainers via Makefile...")
        os.system("make wjsgainers.csv")
