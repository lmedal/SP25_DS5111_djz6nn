"""
factory.py

Creates the appropriate processor using the Factory Design Pattern.
"""

from bin.gainers.mock import GainerProcessMock
from bin.gainers.yahoo import GainerProcessYahoo
from bin.gainers.wsj import GainerProcessWSJ

class GainerFactory:
    """Factory to generate the correct Gainer processor class."""

    def __init__(self, source):
        self.source = source.lower()

    def create_processor(self):
        print(f"[Factory] Creating processor for source: {self.source}")
        if self.source == "yahoo":
            return GainerProcessYahoo()
        elif self.source == "wsj":
            return GainerProcessWSJ()
        elif self.source == "mock":
            return GainerProcessMock()
        else:
            raise ValueError(f"Unsupported source: {self.source}")
