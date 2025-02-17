import importlib.resources
from pathlib import Path


def package_file_path(package_filepath: str) -> Path:
    return importlib.resources.path("scripts", package_filepath)
