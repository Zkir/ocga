from importlib.metadata import version, PackageNotFoundError
from .ocga_engine import ocga_process2

try:
    __version__ = version("ocga")
except PackageNotFoundError:
    # package is not installed, e.g. when running from local source
    __version__ = "unknown"
