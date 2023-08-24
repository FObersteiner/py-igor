from importlib import metadata

from .igor import load, loads  # noqa

__all__ = ("load", "loads")

__version__ = metadata.version("pyigor")
