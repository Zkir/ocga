"""
osm parser to read osm files
"""

# init file for ocgaparser package
from .main import readOsmXml0
from .osmGeometry import TBbox as Bbox 
from .mdlXmlParser import encodeXmlString
from .osmGeometry  import DEGREE_LENGTH_M
