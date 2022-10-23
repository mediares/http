import dataclasses
import importlib.metadata
import typing

try:
    __version__ = importlib.metadata.version("mediares.http")
except importlib.metadata.PackageNotFoundError:
    # package is not installed
    pass


RequestMethod = typing.Literal[
    'CONNECT',
    'DELETE',
    'GET',
    'HEAD',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'TRACE',
]


@dataclasses.dataclass
class Request:
    method: RequestMethod
    url: str
    params: dict
    headers: dict
