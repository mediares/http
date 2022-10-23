import dataclasses
import importlib.metadata
import typing

try:
    __version__ = importlib.metadata.version("mediares.http")
except importlib.metadata.PackageNotFoundError:
    # package is not installed
    pass
