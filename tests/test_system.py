import sys
import platform

def test_os():
    """Ensure the OS is Linux"""
    assert platform.system() == "Linux", f"Expected Linux, got {platform.system()}"

def test_python_version():
    """Ensure Python version is either 3.10, 3.11 or 3.12"""
    allowed_versions = {"3.10", "3.11", "3.12"}
    assert sys.version.split()[0][:4] in allowed_versions, f"Python {sys.version} is not in {allowed_versions}"
