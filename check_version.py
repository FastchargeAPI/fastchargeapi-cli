#!env python3

from pathlib import Path

import tomli

pyproject = tomli.loads(
    (Path(__file__).parent / "pyproject.toml").absolute().read_text()
)

toml_version = pyproject["tool"]["poetry"]["version"]

from fastchargeapi_cli import __version__

if __name__ == "__main__":
    if __version__ != toml_version:
        print(f"__version__ in __init__.py: {__version__}")
        print(f"version in pyproject.toml: {toml_version}")
        print("Versions do not match!")
        exit(1)
    else:
        print("Versions ok.")
