"""
base.py

Defines abstract base classes for GainerDownload and GainerProcess.
"""

from abc import ABC, abstractmethod

class GainerDownload(ABC):
    """Abstract base class for all gainers' downloaders"""

    @abstractmethod
    def download(self):
        """Download method must be implemented by subclasses"""

    def __str__(self):
        return f"{self.__class__.__name__}"

class GainerProcess(ABC):
    """Abstract base class for all gainers' processors"""

    @abstractmethod
    def normalize(self):
        """Normalize method must be implemented by subclasses"""

    @abstractmethod
    def save_with_timestamp(self):
        """Save method must be implemented by subclasses"""

    def __str__(self):
        return f"{self.__class__.__name__}"
