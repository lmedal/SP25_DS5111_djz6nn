"""
mock.py

Provides a mock processor for testing purposes.
"""

from bin.gainers.base import GainerProcess

class GainerProcessMock(GainerProcess):
    def normalize(self):
        print("[Mock] Skipping normalization.")

    def save_with_timestamp(self):
        print("[Mock] Skipping save.")
