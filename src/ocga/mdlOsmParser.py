# Simple OSM Parser.
# It reads "objects" and geometry references into set []

from .mdlMisc import getColourName
from math import pi, sin, cos

from .osmparser import readOsmXml0,encodeXmlString, Bbox,DEGREE_LENGTH_M

#base version of T3DObject, should be the same as in OsmParser
class T3DObject0:
    def __init__(self):
        self.id = ""
        self.type = ""
        self.bbox = Bbox()
        self.NodeRefs = []
        self.WayRefs = []
        self.name = ""
        self.descr = ""
        self.key_tags = ""
        self.strWikipediaName = ""
        self.tagBuilding = ""
        self.tagArchitecture = ""
        self.tagManMade = ""
        self.tagBarrier = ""
        self.tagTowerType = ""
        self.tagAmenity = ""
        self.tagDenomination = ""
        self.tagStartDate = ""
        self.tagRuins = ""
        self.tagWikipedia = ""
        self.tagAddrStreet = ""
        self.tagAddrHouseNumber = ""
        self.tagAddrCity = ""
        self.tagAddrDistrict = ""
        self.tagAddrRegion = ""
        self.material = ""
        self.colour = ""
        self.dblHeight = 0
        self.osmtags = {}
        self.size = 0
        self.blnHasBuildingParts = False

        self.bbox.minLat = 0
        self.bbox.minLon = 0
        self.bbox.maxLat = 0
        self.bbox.maxLon = 0

    def getTag(self ,strKey):
        return self.osmtags.get(strKey,'')

    def isBuilding(self):
        # if an object has building tag, it's probably a building (forget about building=no)
        blnBuilding=(self.getTag("building") != "")
        # Relation building is not really a building, it's just a group of building parts.
        if (self.getTag("type") == "building"):
            blnBuilding = False
        return blnBuilding

    def isBuildingPart(self):
        return (self.getTag("building:part") != "")
        
    def init_attributes(self):
        for tag_key, tag_value in self.osmtags.items():

            if tag_key == 'name':
                self.name = tag_value
            if tag_key == 'description':
                self.descr = tag_value
            if tag_key == 'building':
                self.tagBuilding = tag_value
                self.key_tags = self.key_tags + ' building=' + self.tagBuilding
            if tag_key == 'building:architecture':
                self.tagArchitecture = tag_value
            if tag_key == 'start_date':
                self.tagStartDate = tag_value
            if tag_key == 'man_made':
                self.tagManMade = tag_value
                self.key_tags = self.key_tags + ' man_made=' + self.tagManMade
            if tag_key == 'barrier':
                self.tagBarrier = tag_value
                self.key_tags = self.key_tags + ' barrier=' + self.tagBarrier
            # wikipedia
            if tag_key == 'wikipedia':
                self.tagWikipedia = tag_value
            if tag_key == 'addr:street':
                self.tagAddrStreet = tag_value
            if tag_key == 'addr:housenumber':
                self.tagAddrHouseNumber = tag_value
            if tag_key == 'addr:city':
                self.tagAddrCity = tag_value
            if tag_key == 'addr:district':
                self.tagAddrDistrict = tag_value
            if tag_key == 'addr:region':
                self.tagAddrRegion = tag_value
            #ref_temples_ru
            if tag_key == 'ref:temples.ru':
                ref_temples_ru = tag_value
                #print ref_temples_ru
            if tag_key == 'amenity':
                self.tagAmenity = tag_value
            if tag_key == 'denomination':
                self.tagDenomination = tag_value
            if tag_key == 'tower:type':
                self.tagTowerType = tag_value
            if tag_key == 'building:material':
                self.material = tag_value
            #for buildings we have building:colour, for other objects, e.g. fences, just colour
            if ( tag_key == 'building:colour' )  or  ( tag_key == 'colour' ) :
                self.colour = tag_value
                if tag_value[0] == '#':
                    self.colour = getColourName(tag_value)
            if tag_key == 'ruins':
                self.tagRuins = tag_value         

#Extentions for T3DObject required specifically for ocga
class T3DObject(T3DObject0):
    def __init__(self):
        
        super().__init__()
        
        self.parts = [] # all building parts of this building. For buildings only
        self.parent_building = None
        self.parent = None # imidiate parent of this part
        self.children = [] # children of this part
        
        
        self.scope_sx = 0
        self.scope_sy = 0
        self.scope_rz = 0

        self.scope_min_x = 0
        self.scope_min_y = 0
        self.scope_max_x = 0
        self.scope_max_y = 0

        self.relative_Ox = 0
        self.relative_Oy = 0
        self.split_index = 0

        self.rules_processed = False
        
    def updateBBox(self,objOsmGeom):
        if self.type == "way":
            self.bbox.minLat = objOsmGeom.nodes[self.NodeRefs[0]].lat
            self.bbox.minLon = objOsmGeom.nodes[self.NodeRefs[0]].lon
            self.bbox.maxLat = objOsmGeom.nodes[self.NodeRefs[0]].lat
            self.bbox.maxLon = objOsmGeom.nodes[self.NodeRefs[0]].lon

            for node_no in self.NodeRefs:
                lat= objOsmGeom.nodes[node_no].lat
                lon= objOsmGeom.nodes[node_no].lon

                if lat<self.bbox.minLat:
                    self.bbox.minLat=lat

                if lat > self.bbox.maxLat:
                    self.bbox.maxLat = lat

                if lon < self.bbox.minLon:
                    self.bbox.minLon = lon

                if lon>self.bbox.maxLon:
                    self.bbox.maxLon=lon

            self.size=(objOsmGeom.CalculateClosedNodeChainArea(self.NodeRefs, len(self.NodeRefs)-1))**0.5
        else:
            raise Exception("Only ways are supported currently")    

    def calculateScopeBBox(self, objOsmGeom, coordsys="local"):
        if coordsys == "local":
            coord_base_obj = self
        elif coordsys == "building":
            coord_base_obj = self.parent_building
        else:
            raise Exception("Unknown coordinate system selector")

        if self.type == "way":
            lat = objOsmGeom.nodes[self.NodeRefs[0]].lat
            lon = objOsmGeom.nodes[self.NodeRefs[0]].lon

            x, y = coord_base_obj.LatLon2LocalXY(lat, lon)
            min_x = x
            min_y = y
            max_x = x
            max_y = y

            for node_no in self.NodeRefs:
                lat = objOsmGeom.nodes[node_no].lat
                lon = objOsmGeom.nodes[node_no].lon
                x, y = coord_base_obj.LatLon2LocalXY(lat, lon)

                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x
                if y < min_y:
                    min_y = y
                if y > max_y:
                    max_y = y

        elif self.type == "relation":
            lat = objOsmGeom.nodes[objOsmGeom.ways[self.WayRefs[0][0]].NodeRefs[0]].lat
            lon = objOsmGeom.nodes[objOsmGeom.ways[self.WayRefs[0][0]].NodeRefs[0]].lon
            x, y = coord_base_obj.LatLon2LocalXY(lat, lon)
            min_x = x
            min_y = y
            max_x = x
            max_y = y

            for way_no in self.WayRefs:
                for node_no in objOsmGeom.ways[way_no[0]].NodeRefs:
                    lat = objOsmGeom.nodes[node_no].lat
                    lon = objOsmGeom.nodes[node_no].lon
                    x, y = coord_base_obj.LatLon2LocalXY(lat, lon)

                    if x < min_x:
                        min_x = x
                    if x > max_x:
                        max_x = x
                    if y < min_y:
                        min_y = y
                    if y > max_y:
                        max_y = y

        else:
            raise Exception("Unknown object type")

        return min_x,min_y, max_x, max_y

    def updateScopeBBox(self, objOsmGeom):
        min_x,min_y, max_x, max_y = self.calculateScopeBBox(objOsmGeom)

        self.scope_sx = max_x - min_x
        self.scope_sy = max_y - min_y
        # in local coords the object may not be exactly symmetrical, due to rotation
        self.scope_min_x = min_x
        self.scope_min_y = min_y
        self.scope_max_x = max_x
        self.scope_max_y = max_y

    def alignScopeToWorld(self):
        cLat = (self.bbox.minLat + self.bbox.maxLat) / 2

        self.scope_sx = (self.bbox.maxLon - self.bbox.minLon) * DEGREE_LENGTH_M * cos(cLat / 360 * 2 * pi)
        self.scope_sy = (self.bbox.maxLat - self.bbox.minLat) * DEGREE_LENGTH_M

        self.scope_rz = 0


    # scope is aligned according to geometry
    # we search for the oriented bbox with minimal square
    # todo: more efficient algorithm should be found.
    def alignScopeToGeometry(self,objOsmGeom):
        bestAlpha=0
        S=0
        minS=-1
        for i in range(180):
            self.scope_rz = i / 180 * pi
            self.updateScopeBBox(objOsmGeom)
            S = self.scope_sx*self.scope_sy
            if minS == -1:
                minS = S
            if S<minS:
                minS= S
                bestAlpha = i

        self.scope_rz = bestAlpha / 180 * pi
        self.updateScopeBBox(objOsmGeom)

        #lets find more precise angle.
        alpha = bestAlpha
        S = minS
        prevS=minS
        delta_alpha=0.5
        epsilon = 0.0001
        while abs(delta_alpha)>epsilon:
            alpha=alpha+delta_alpha
            self.scope_rz = alpha / 180 * pi
            self.updateScopeBBox(objOsmGeom)
            S = self.scope_sx * self.scope_sy
            if S<prevS:
                #minS= S
                bestAlpha=alpha
            else:
                delta_alpha=-delta_alpha/2
            prevS = S
        self.scope_rz = alpha / 180 * pi
        self.updateScopeBBox(objOsmGeom)
        
    #rotates the scope of the shape.
    #only local coordinate system is rotated, geometry is not touched.
    #since we have only 2.5D here, we can rotate around vertical axis(z) only
    # zAngle -- angle in degrees
    def rotateScope(self, zAngle,objOsmGeom):
        self.scope_rz = self.scope_rz + zAngle/180*pi
        # sx and sy should be recalculated.
        self.updateScopeBBox(objOsmGeom)


    def localXY2LatLon(self,x,y):
        # there is local coordinate system with origin at center point
        # X,Y are in meters
        # it can be rotated.
        cLat = (self.bbox.minLat + self.bbox.maxLat) / 2
        cLon = (self.bbox.minLon + self.bbox.maxLon) / 2
        teta=self.scope_rz
        x1=x*cos(teta) -y*sin(teta)
        y1=x*sin(teta) + y* cos(teta)

        lat = cLat + y1 / DEGREE_LENGTH_M
        lon = cLon + x1 / DEGREE_LENGTH_M / cos(cLat / 360 * 2 * pi)
        return lat, lon

    def LatLon2LocalXY(self,lat,lon):

        cLat = (self.bbox.minLat + self.bbox.maxLat) / 2
        cLon = (self.bbox.minLon + self.bbox.maxLon) / 2

        y1 = (lat - cLat) * DEGREE_LENGTH_M
        x1 = (lon - cLon) * DEGREE_LENGTH_M * cos(cLat / 360 * 2 * pi)

        theta = -self.scope_rz
        x = x1 * cos(theta) - y1 * sin(theta)
        y = x1 * sin(theta) + y1 * cos(theta)

        return x, y


# we will read osm file into a set of objects + complex structure with geometry

def readOsmXml(strSrcOsmFile):    
    objOsmGeom = readOsmXml0(strSrcOsmFile)
    Objects = []
    
    # we will skip nodes, since single node buildings are boring 
    
    for _, way in objOsmGeom.ways.items():
        osmObject = T3DObject()
        osmObject.type = 'way'
        osmObject.id = way.id
        osmObject.version =  way.version
        osmObject.timestamp = way.timestamp
        osmObject.NodeRefs  = way.NodeRefs
        osmObject.osmtags = way.osmtags
        osmObject.init_attributes()
        
        osmObject.bbox = objOsmGeom.GetWayBBox(way.id)
        osmObject.size = objOsmGeom.ways[way.id].size
        
        Objects.append(osmObject)
        
    for _, relation in objOsmGeom.relations.items():
        osmObject = T3DObject()
        osmObject.type = 'relation'
        osmObject.id = relation.id
        osmObject.version =  relation.version
        osmObject.timestamp = relation.timestamp
        
        osmObject.WayRefs  = relation.WayRefs
        osmObject.osmtags = relation.osmtags
        osmObject.init_attributes()
        
        osmObject.bbox = objOsmGeom.GetRelationBBox(relation.id)
        osmObject.size = objOsmGeom.relations[relation.id].size
        
        if 'type' not in osmObject.osmtags:
            print('stange relation without type ' + osmObject.id  )
            print('   ', osmObject.osmtags)                
        
        if ('type' in osmObject.osmtags and osmObject.osmtags['type'] == 'building'):
                # also filter 
                # relations of type building are strange objects! \
                pass
        else: 
            Objects.append(osmObject)
    
    return objOsmGeom, Objects


#osm file is rewritten  from Objects list and OsmGeom
def writeOsmXml(objOsmGeom, Objects, strOutputOsmFileName, blnUpdatable):
    fo = open(strOutputOsmFileName, 'w', encoding="utf-8")

    # Print #fo, "<?xml version='1.0' encoding='UTF-8'?>"
    fo.write('<?xml version=\'1.0\' encoding=\'utf-8\'?>' + '\n')
    fo.write('<osm version="0.6" generator="zkir manually">' + '\n')
    # fo.write('  <bounds minlat="' + str(object1.bbox.minLat) + '" minlon="' + str(object1.bbox.minLon) + '" maxlat="' + str(
    #    object1.bbox.maxLat) + '" maxlon="' + str(object1.bbox.maxLon) + '"/> ' + '\n')

    for i, node in objOsmGeom.nodes.items():
        obj_id = node.id
        obj_ver = "1"
        node_lat = node.lat
        node_lon = node.lon
        node_used=False
        for obj in Objects:
            for node_ref in obj.NodeRefs:
                if i==node_ref:
                    node_used = True
                    break
            if node_used:
                break

        if node_used:
            if int(obj_id)<0 and blnUpdatable:
                action=' action="modify" '
            else:
                action=''

            fo.write('  <node id="' + obj_id + '"' + action + ' version="' + obj_ver + '"  lat="' + str(node_lat) + '" lon="' + str(
                      node_lon) + '"/>' + '\n')

    for osmObject in Objects:
        if osmObject.type == "way":
            if int(osmObject.id) < 0 and blnUpdatable:
                action = ' action="modify" '
            else:
                action = ''
            fo.write('  <way id="' + osmObject.id + '"'+action+' version="' + "1" + '" >' + '\n')
            for node in osmObject.NodeRefs:
                fo.write('    <nd ref="' + objOsmGeom.GetNodeID(node) + '" />' + '\n')

        if osmObject.type == "relation":
            if int(osmObject.id) < 0 and blnUpdatable:
                action = ' action="modify" '
            else:
                action = ''
            fo.write('  <relation id="' + osmObject.id + '"'+action + ' version="' + "1" + '" >' + '\n')
            for way in osmObject.WayRefs:
                fo.write(
                    '    <member type="way" ref="' + objOsmGeom.GetWayID(way[0]) + '" role="' + way[1] + '"  />' + '\n')
        for tag in osmObject.osmtags:
            if osmObject.getTag(tag)!="":
                fo.write('    <tag k="' + tag + '" v="' + encodeXmlString(osmObject.getTag(tag)) + '" />' + '\n')
        if osmObject.type == "way":
            fo.write('  </way>' + '\n')
        if osmObject.type == "relation":
            fo.write('  </relation>' + '\n')
    fo.write('</osm>' + '\n')
    fo.close()


def roundHeight(Objects):
    for obj in Objects:
        for key in obj.osmtags:
            if key == "height" or key == "min_height" or key == "roof:height":
                height = obj.osmtags[key]
                if (height != ""):
                    height = round(parseHeightValue(height), 3)
                    height = "{:g}".format(height)
                    obj.osmtags[key] = str(height)

            if key == "roof:direction":
                alpha = obj.osmtags[key]
                if (alpha != ""):
                    alpha = round(float(alpha), 3)
                    alpha = "{:g}".format(alpha)
                    obj.osmtags[key] = str(alpha)
                    

def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False                    

def parseHeightValue(strHeigth):
    if strHeigth.endswith(' м'):
        strHeigth = strHeigth[0:-2]
    if strHeigth.endswith(' m'):
        strHeigth = strHeigth[0:-2]
    if strHeigth == 'high' or strHeigth == 'low':
        strHeigth = '0'
    if strHeigth.endswith("'"):
        strHeigth=strHeigth[0:-1]
        strHeigth=float(strHeigth.strip())*0.3048
    if strHeigth == "":
        strHeigth = '0'
    if not isfloat(strHeigth):
        print ("Unparsed height value: " + strHeigth)
        strHeigth = '0'
    return float(strHeigth)


