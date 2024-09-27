"""
Computer Generated Architecture OSM
Inspired mainly by ESRI City Engine
The main difference is that we operate with building parts and their attributes only
Input and output files are both osm-files.
resulting OSM file can be uploaded to OSM DB
"""
import argparse
from pathlib import Path

from copy import copy
from math import cos, sin, atan2, pi
from mdlOsmParser import readOsmXml, writeOsmXml, parseHeightValue, roundHeight
from mdlOsmParser import T3DObject 

#ocga parser and translator 
from ocgaparser import * #ocga2py
from osmGeometry import DEGREE_LENGTH_M

_id_counter=0

# counter for OSM objects.
# we need negative, because those objects are absent (yet) in OSM DB
def getID():
    global _id_counter
    _id_counter=_id_counter-1
    return str(_id_counter)

def resetID():
    global _id_counter
    _id_counter=0
# ======================================================================================================================
# Operations with building parts.
# ======================================================================================================================
# calculate the size of "linearized" split pattern
def calculateTotalPatternSize(split_pattern):
    sum_of_all_sizes = 0
    #we do not expect * here.
    for i in range(len(split_pattern)):
        if str(split_pattern[i][0])[0:1] != "~":  # fixed height
            sum_of_all_sizes = sum_of_all_sizes+ float(split_pattern[i][0])
        else:
            sum_of_all_sizes = sum_of_all_sizes+ float(split_pattern[i][0][1:])
            
    return sum_of_all_sizes        
        
    

# calculate actual dimensions based on the given split pattern
# the function accepts more complex structure, split pattern as it is defined in ocga, with "floating" sizes and repeat patterns,
# but returns much more simple structure, ready for actual split operation: list of length and rule name pairs.  
def calculateDimensionsForSplitPattern(h, split_pattern):
    # we need to calculate heights of the segments
    # it is a bit tricky, because it could be "floating" height, starting with ~, like ~12.34
    
    segments = []    
    sum_of_explicit_sizes = 0
    sum_of_implicit_sizes = 0
    
    k=0 # todo: start with zero
    bln_repeats_present = False
    
    while calculateTotalPatternSize(segments)<h:
        segments = []    
        for i in range(len(split_pattern)):
            if str(str(split_pattern[i][0])[0:1]) == "*":  # complex pattern
                segments += list(split_pattern[i][1])*k
                bln_repeats_present = True
            else: 
                segments += [split_pattern[i]]        
                
        if not bln_repeats_present:
            # if there are no repeat patterns, 
            # we should exit, because nothing can be increased.
            break
        k = k + 1    
        #print(round(h), calculateTotalPatternSize(segments), segments)     
            
            
    for i in range(len(segments)):
        if str(segments[i][0])[0:1] != "~":  # fixed height
            sum_of_explicit_sizes= sum_of_explicit_sizes+ float(segments[i][0])
        else:
            sum_of_implicit_sizes= sum_of_implicit_sizes+ float(segments[i][0][1:])
            
            
    # define values for floating segments proportionally
    for i in range(len(segments)):
        if str(segments[i][0])[0:1] != "~":  # fixed height, does NOT starts with '~'
            size      = float(segments[i][0]) #size
            rule_name = str(segments[i][1])   #rule name
        else:
            size = (h - sum_of_explicit_sizes) * float(segments[i][0][1:]) / sum_of_implicit_sizes
            rule_name = str(segments[i][1])   #rule name
        if size < 0:  # todo: more precise check for negative height. Such elements probably should be excluded from generaion.
            size = 0
            rule_name = 'zero_part'
        segments[i] = (size, rule_name)
    return segments


def copyBuildingPartTags(new_object, old_object):
    # todo: inherit tags
    # some tags should be dropped, e.g. type (as valid for relations only)
    # roof shape may produce funny results if copied for horizontal split
    osmtags = {}
    osmtags["building:part"] = old_object.getTag("building:part")
    osmtags["height"] = old_object.getTag("height")
    osmtags["min_height"] = old_object.getTag("min_height")
    osmtags["building:material"] = old_object.getTag("building:material")
    osmtags["building:colour"] = old_object.getTag("building:colour")
    osmtags["roof:material"] = old_object.getTag("roof:material")
    osmtags["roof:colour"] = old_object.getTag("roof:colour")
    osmtags["roof:height"] = old_object.getTag("roof:height")
    osmtags["roof:shape"] = old_object.getTag("roof:shape")
    osmtags["roof:orientation"] = old_object.getTag("roof:orientation")
    osmtags["roof:direction"] = old_object.getTag("roof:direction")

    if new_object.type == "relation":
        osmtags["type"] = old_object.getTag("type")

    new_object.osmtags=osmtags

# split object in vertical direction.
# since we have only 2.5, it's easy
# outline and tags remain,
# min_height and height are assigned to the new parts.
def split_z_preserve_roof(osmObject, split_pattern):
    Objects2 = []
    N = len(split_pattern)
    height= parseHeightValue(osmObject.getTag("height"))
    min_height = parseHeightValue(osmObject.getTag("min_height"))
    roof_height= parseHeightValue(osmObject.getTag("roof:height"))
    h = height-min_height-roof_height # osm tags are strange. Split ignores roof height

    Heights = calculateDimensionsForSplitPattern(h, split_pattern)

    for i in range(N) :
        # create new object and copy outline and tags
        # it does not depend on split pattern in case of Z split
        new_obj = T3DObject()
        new_obj.id = getID()
        new_obj.type = osmObject.type
        new_obj.NodeRefs = copy(osmObject.NodeRefs)
        new_obj.WayRefs = copy(osmObject.WayRefs)
        copyBuildingPartTags(new_obj, osmObject)
        new_obj.bbox = copy(osmObject.bbox)
        new_obj.size = osmObject.size
        new_obj.scope_sx = osmObject.scope_sx
        new_obj.scope_sy = osmObject.scope_sy
        new_obj.scope_rz = osmObject.scope_rz

        new_obj.scope_min_x = osmObject.scope_min_x
        new_obj.scope_min_y = osmObject.scope_min_y
        new_obj.scope_max_x = osmObject.scope_max_x
        new_obj.scope_max_y = osmObject.scope_max_y

        # we can assign building part tag, it is identical with rule name
        new_obj.osmtags["building:part"] = Heights[i][1]
        if i!=N-1:
            new_obj.osmtags["roof:shape"] = "flat"  # No roof for lower parts, roof shape remains for top-most part only
            new_obj.osmtags["roof:height"] = "0"

        new_obj.osmtags["min_height"] = str(min_height)
        if i != N - 1:
           new_obj.osmtags["height"] = str(min_height+Heights[i][0])
        else:
            new_obj.osmtags["height"] = str(min_height + Heights[i][0]+roof_height)
        min_height=min_height+Heights[i][0]


        Objects2.append(new_obj)
    return Objects2


# Split the object along X axis
def split_x(osmObject, objOsmGeom, split_pattern):
    Objects2 = []
    scope_sx = osmObject.scope_sx
    scope_sy = osmObject.scope_sy

    Lengths = calculateDimensionsForSplitPattern(scope_sx, split_pattern)
    n = len(Lengths)
    #x0 = -scope_sx / 2
    x0 = osmObject.scope_min_x

    for i in range(n):
        new_obj = T3DObject()
        new_obj.id = getID()
        new_obj.type = "way"

        copyBuildingPartTags(new_obj, osmObject)
        new_obj.osmtags["building:part"] = Lengths[i][1]

        dx = Lengths[i][0]

        # todo: cut actual geometry, not bbox only
        insert_Quad(osmObject, objOsmGeom, new_obj.NodeRefs, dx, scope_sy, x0+dx/2, (osmObject.scope_min_y+osmObject.scope_max_y)/2)

        new_obj.scope_rz = osmObject.scope_rz  # coordinate system orientation is inherited, but centroid is moved and
        new_obj.updateBBox(objOsmGeom)         # bbox is updated
        new_obj.updateScopeBBox(objOsmGeom)  # also Bbbox in local coordinates
        new_obj.relative_Ox = x0 + dx / 2
        new_obj.relative_Oy = 0
        Objects2.append(new_obj)
        x0 = x0 + dx

    return Objects2

# Split the object along Y axis
def split_y(osmObject, objOsmGeom, split_pattern):
    Objects2 = []
    scope_sx = osmObject.scope_sx
    scope_sy = osmObject.scope_sy

    Lengths = calculateDimensionsForSplitPattern(scope_sy, split_pattern)
    n = len(Lengths)
    y0 = osmObject.scope_min_y

    for i in range(n):
        new_obj = T3DObject()
        new_obj.id = getID()
        new_obj.type = "way"

        copyBuildingPartTags(new_obj, osmObject)
        new_obj.osmtags["building:part"] = Lengths[i][1]

        dy = Lengths[i][0]

        # todo: cut actual geometry, not bbox only
        insert_Quad(osmObject, objOsmGeom, new_obj.NodeRefs,  scope_sx, dy, (osmObject.scope_min_x+osmObject.scope_max_x)/2, y0+dy/2)



        new_obj.scope_rz = osmObject.scope_rz  # coordinate system orientation is inherited, but centroid is moved and
        new_obj.updateBBox(objOsmGeom)         # bbox is updated
        new_obj.updateScopeBBox(objOsmGeom)  # also Bbbox in local coordinates
        new_obj.relative_Ox = 0
        new_obj.relative_Oy = y0+dy/2

        Objects2.append(new_obj)
        y0 = y0 + dy

    return Objects2


# some kind of hybrid between offset and comp(border) operations
# we create geometry along edges of our roof, to create decorative elements
def comp_border(osmObject, objOsmGeom, rule_name, distance=1, roof_only=False):
    Objects2 = []
    distance = float(distance)
    
    if osmObject.type == "relation":
        raise Exception("relation is not yet supported in the comp_roof_border operation")

    for i in range(len(osmObject.NodeRefs) - 1):
        new_obj = T3DObject()
        new_obj.id = getID()
        new_obj.type = "way"
        new_obj.split_index=i

        copyBuildingPartTags(new_obj, osmObject) # tags are inherited

        lat0 = objOsmGeom.nodes[osmObject.NodeRefs[i]].lat
        lon0 = objOsmGeom.nodes[osmObject.NodeRefs[i]].lon
        x0, y0 = osmObject.LatLon2LocalXY(lat0, lon0)

        lat1 = objOsmGeom.nodes[osmObject.NodeRefs[i + 1]].lat
        lon1 = objOsmGeom.nodes[osmObject.NodeRefs[i + 1]].lon
        x1, y1 = osmObject.LatLon2LocalXY(lat1, lon1)

        xc = (x0 + x1) / 2
        yc = (y0 + y1) / 2
        facade_len = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

        new_obj.scope_rz = osmObject.scope_rz + atan2(y1 - y0, x1 - x0)

        # we need to move the created shape "inwards", so that outer edges coincide.
        # todo: individual shift for each vertex/edge
        rc = (xc * xc + yc * yc) ** 0.5
        dlat, dlon = osmObject.localXY2LatLon(xc / rc * distance/2, yc / rc * distance/2)
        dlat = dlat - (osmObject.bbox.minLat + osmObject.bbox.maxLat) / 2
        dlon = dlon - (osmObject.bbox.minLon + osmObject.bbox.maxLon) / 2

        new_obj.bbox.minLat = min(lat0, lat1) - dlat
        new_obj.bbox.maxLat = max(lat0, lat1) - dlat
        new_obj.bbox.minLon = min(lon0, lon1) - dlon
        new_obj.bbox.maxLon = max(lon0, lon1) - dlon

        insert_Quad(new_obj, objOsmGeom, new_obj.NodeRefs,  facade_len, distance, 0, 0)
        new_obj.updateScopeBBox(objOsmGeom)
        copyBuildingPartTags(new_obj, osmObject)
        new_obj.osmtags["building:part"] = rule_name
        if roof_only:
            new_obj.osmtags["min_height"] = str(
                osmObject.osmtags["height"] - osmObject.osmtags["roof:height"])
        Objects2.append(new_obj)
    return Objects2


#  we cannot really do comp, because building parts are individable,
#  but we will create one more object with the same geometry and height by roof height
def comp_roof(osmObject, objOsmGeom, rule_name):
    Objects2 = []
    if osmObject.type == "relation":
        raise Exception("relation is not supported in the comp_roof_border operation")

    new_obj = T3DObject()
    new_obj.id = getID()
    new_obj.type = "way"
    copyBuildingPartTags(new_obj, osmObject)
    new_obj.NodeRefs = copy(osmObject.NodeRefs) # same nodes.

    new_obj.osmtags["min_height"] = str(parseHeightValue(osmObject.osmtags["height"])- parseHeightValue(osmObject.osmtags["roof:height"]))
    new_obj.osmtags["building:part"] = rule_name
    new_obj.updateBBox(objOsmGeom)
    new_obj.updateScopeBBox(objOsmGeom)
    Objects2.append(new_obj)
    return Objects2

def insert_Quad(osmObject, objOsmGeom, NodeRefs, width, length, x0, y0):
    # 1
    Lat, Lon = osmObject.localXY2LatLon(x0 - width / 2, y0 - length / 2)
    node_no_1 = objOsmGeom.AddNode(getID(), Lat, Lon)
    NodeRefs.append(node_no_1)
    # 2
    Lat, Lon = osmObject.localXY2LatLon(x0 + width / 2, y0 - length / 2)
    NodeRefs.append(objOsmGeom.AddNode(getID(), Lat, Lon))
    # 3
    Lat, Lon = osmObject.localXY2LatLon(x0 + width/2, y0 + length / 2)
    NodeRefs.append(objOsmGeom.AddNode(getID(), Lat, Lon))
    # 4
    Lat, Lon = osmObject.localXY2LatLon(x0 - width/2, y0 + length / 2)
    NodeRefs.append(objOsmGeom.AddNode(getID(), Lat, Lon))
    # 5
    NodeRefs.append(node_no_1)


# todo: insert_circle should be NON-DESTRUCTIVE OPERATION
# object remain, but geometry is changed
def primitiveCircle(osmObject, objOsmGeom,  nVertices=12, radius="'1"):

    new_obj = osmObject
    #new_obj = T3DObject()
    #new_obj.id = getID()
    #new_obj.type = "way"
    new_obj.NodeRefs = []
    if new_obj.type == "relation":
        raise Exception ("relation is not supported")

    R = parseRelativeValue(radius, min(osmObject.scope_sx, osmObject.scope_sy)/2)

    Lat = [None] * nVertices
    Lon = [None] * nVertices
    ids = [None] * nVertices

    for i in range(nVertices):
        alpha = 2 * pi / nVertices * i

        Lat[i], Lon[i] = osmObject.localXY2LatLon(R * cos(alpha), R * sin(alpha))
        ids[i] = getID()
        # print(ids[i], x[i], y[i])
        intNodeNo= objOsmGeom.AddNode(ids[i], Lat[i], Lon[i])
        new_obj.NodeRefs.append(intNodeNo)
    # objOsmGeom.AddNode(ids[0], Lat[0], Lon[0])
    intNodeNo = objOsmGeom.FindNode(ids[0])
    new_obj.NodeRefs.append(intNodeNo)

    new_obj.scope_rz = osmObject.scope_rz  # coordinate system orientation is inherited, but centroid is moved and
    new_obj.updateBBox(objOsmGeom)  # bbox is updated
    new_obj.updateScopeBBox(objOsmGeom)  # also Bbbox in local coordinates


def primitiveHalfCircle(osmObject, objOsmGeom, nVertices=12, radius=None):

    new_obj = osmObject
    # new_obj = T3DObject()
    # new_obj.id = getID()
    # new_obj.type = "way"
    new_obj.NodeRefs = []
    if new_obj.type == "relation":
        raise Exception("relation is not supported")

    if radius is None:
        R = min(osmObject.scope_sx, osmObject.scope_sy)
    else:
        R = radius

    Lat = [None] * nVertices
    Lon = [None] * nVertices
    ids = [None] * nVertices

    for i in range(nVertices):
        alpha = -pi/2+pi / (nVertices-1) * i

        Lat[i], Lon[i] = osmObject.localXY2LatLon(osmObject.scope_min_x+R * cos(alpha), R * sin(alpha))
        ids[i] = getID()
        # print(ids[i], x[i], y[i])
        intNodeNo= objOsmGeom.AddNode(ids[i], Lat[i], Lon[i])
        new_obj.NodeRefs.append(intNodeNo)
    # objOsmGeom.AddNode(ids[0], Lat[0], Lon[0])
    intNodeNo = objOsmGeom.FindNode(ids[0])
    new_obj.NodeRefs.append(intNodeNo)

    new_obj.scope_rz = osmObject.scope_rz  # coordinate system orientation is inherited, but centroid is moved and
    new_obj.updateBBox(objOsmGeom)  # bbox is updated
    new_obj.updateScopeBBox(objOsmGeom)  # also Bbbox in local coordinates
    return


def parseRelativeValue(val, abs_size):
    if type(val) == str:
        if val[0:1] == "'":
            val = float(str(val)[1:]) * abs_size
    if type(val) == str:
        val=float(val)
    return val

def scale(osmObject, objOsmGeom, sx, sy, sz=None):
    if osmObject.type == "relation":
        raise Exception("todo: relations is not supported in scale operation")

    if sz is not None:
        # Luckily, z-scale is simple. No matrix, no geometry
        # just update tags
        height = parseHeightValue(osmObject.getTag("height"))
        min_height = parseHeightValue(osmObject.getTag("min_height"))
        roof_height = parseHeightValue(osmObject.getTag("roof:height"))
        h = height - min_height
        sz=parseRelativeValue(sz,h)

        kz=sz/h
        # min_height remains, we need to update height and roof height
        height=min_height+sz
        roof_height =roof_height*kz
        if round(roof_height, 3) > round(height,3) - round(min_height,3):
            roof_height = round(height,3) - round(min_height,3)-0.01
        osmObject.osmtags["height"] = str(height)
        osmObject.osmtags["roof:height"] = str(roof_height)

    sx = parseRelativeValue(sx, osmObject.scope_sx)
    sy = parseRelativeValue(sy, osmObject.scope_sy)
    kx = sx / osmObject.scope_sx
    ky = sy / osmObject.scope_sy

    if kx != 1 or ky != 1:
        # we should not transfer the same node twice
        if osmObject.NodeRefs[0] == osmObject.NodeRefs[-1]:
            closed_way_flag = 1
        else:
            closed_way_flag = 0

        new_node_refs =[]
        for i in range(len(osmObject.NodeRefs)-closed_way_flag):
            node = osmObject.NodeRefs[i]
            x, y = osmObject.LatLon2LocalXY(objOsmGeom.nodes[node].lat, objOsmGeom.nodes[node].lon)
            x = x*kx
            y = y*ky
            lat, lon=osmObject.localXY2LatLon(x, y)

            node_ref=objOsmGeom.AddNode(getID(), lat, lon)
            new_node_refs.append(node_ref)

        if closed_way_flag == 1:
            new_node_refs.append(new_node_refs[0])

        osmObject.NodeRefs=new_node_refs

    osmObject.updateBBox(objOsmGeom)
    osmObject.updateScopeBBox(objOsmGeom)


def translate (osmObject, objOsmGeom, dx, dy, dz=None):
    if osmObject.type == "relation":
        raise Exception("todo: relations is not supported")

    if dz is not None:
        # Luckily, z-scale is simple. No matrix, no geometry
        height = parseHeightValue(osmObject.getTag("height"))
        min_height = parseHeightValue(osmObject.getTag("min_height"))
        h = height - min_height
        dz=parseRelativeValue(dz, h)

        #min_height remains, we need to update height and roof height
        osmObject.osmtags["min_height"] = str(min_height+dz)
        osmObject.osmtags["height"] = str(height+dz)
        #osmObject.scope_sz=sz

    dx = parseRelativeValue(dx, osmObject.scope_sx)
    dy = parseRelativeValue(dy, osmObject.scope_sy)

    if dx != 0 or dy != 0:
        # we should not transfer the same node twice
        if osmObject.NodeRefs[0] == osmObject.NodeRefs[-1]:
            closed_way_flag = 1
        else:
            closed_way_flag = 0

        new_node_refs =[]
        for i in range(len(osmObject.NodeRefs)-closed_way_flag):
            node = osmObject.NodeRefs[i]
            x, y = osmObject.LatLon2LocalXY(objOsmGeom.nodes[node].lat, objOsmGeom.nodes[node].lon)
            x = x + dx
            y = y + dy
            lat, lon=osmObject.localXY2LatLon(x, y)

            node_ref=objOsmGeom.AddNode(getID(), lat, lon)
            new_node_refs.append(node_ref)

        if closed_way_flag == 1:
            new_node_refs.append(new_node_refs[0])

        osmObject.NodeRefs=new_node_refs

    osmObject.updateBBox(objOsmGeom)
    osmObject.updateScopeBBox(objOsmGeom)


def bevel(osmObject, objOsmGeom, r, node_list=None):

    if osmObject.type == "relation":
        raise Exception("todo: relations is not supported")
        # we should not transfer the same node twice

    if osmObject.NodeRefs[0] == osmObject.NodeRefs[-1]:
        closed_way_flag = 1
    else:
        closed_way_flag = 0
        raise Exception ("Bevel is allowed only for closed polygons")

    new_node_refs = []
    #print (osmObject.NodeRefs)
    if node_list is None:
        node_list = range(len(osmObject.NodeRefs) - closed_way_flag)
    for i in range(len(osmObject.NodeRefs) - closed_way_flag):
        if i in node_list:
            if i == 0:
                magic = 1
            else:
                magic = 0
            nodeA = osmObject.NodeRefs[i-1-magic]
            nodeO = osmObject.NodeRefs[i]
            nodeB = osmObject.NodeRefs[i+1]
            #print (nodeA,nodeO, nodeB)

            x0, y0 = osmObject.LatLon2LocalXY(objOsmGeom.nodes[nodeO].lat, objOsmGeom.nodes[nodeO].lon)
            xa, ya = osmObject.LatLon2LocalXY(objOsmGeom.nodes[nodeA].lat, objOsmGeom.nodes[nodeA].lon)
            xb, yb = osmObject.LatLon2LocalXY(objOsmGeom.nodes[nodeB].lat, objOsmGeom.nodes[nodeB].lon)
            dxa = xa - x0
            dya = ya - y0
            ra = (dxa*dxa+dya*dya)**0.5
            dxa = dxa / ra
            dya = dya / ra

            dxb = xb - x0
            dyb = yb - y0
            rb = (dxb*dxb+dyb*dyb)**0.5

            dxb = dxb/rb
            dyb = dyb/rb

            x1 = x0 + (dxa) * r
            y1 = y0 + (dya) * r

            x2 = x0 + (dxb) * r
            y2 = y0 + (dyb) * r

            lat, lon = osmObject.localXY2LatLon(x1, y1)
            node_ref = objOsmGeom.AddNode(getID(), lat, lon)
            new_node_refs.append(node_ref)

            lat, lon = osmObject.localXY2LatLon(x2, y2)
            node_ref = objOsmGeom.AddNode(getID(), lat, lon)
            new_node_refs.append(node_ref)
        else:
            node_ref=osmObject.NodeRefs[i]
            new_node_refs.append(node_ref)

    if closed_way_flag == 1:
        new_node_refs.append(new_node_refs[0])

    osmObject.NodeRefs = new_node_refs
    osmObject.updateBBox(objOsmGeom)
    osmObject.updateScopeBBox(objOsmGeom)


def setParentChildRelationship(old_obj, new_objects):
    if old_obj.isBuilding():
        parent_building = old_obj
    else:
        parent_building = old_obj.parent_building

    old_obj.children.extend(new_objects)
    parent_building.parts.extend(new_objects)
    for new_obj in new_objects:
        new_obj.parent=old_obj
        new_obj.parent_building=parent_building


def rebuildBuildingOutline(Objects, objOsmGeom):
    """Rebuild the building outline. Currently mock-up, no polygon intersections, just bbox"""
    Objects2=[]
    for obj in Objects:
        if obj.isBuilding() and len(obj.parts) > 0:
            # print(obj.id, obj.name)
            min_x, min_y, max_x, max_y = obj.parts[0].calculateScopeBBox(objOsmGeom, "building")
            for child in obj.parts:
                min_x1, min_y1, max_x1, max_y1 = child.calculateScopeBBox(objOsmGeom, "building")
                # print("    ", child.id, child.getTag("building:part"), child.name)  # min_x, min_y, max_x, max_y
                if min_x1 < min_x:
                    min_x = min_x1

                if min_y1 < min_y:
                    min_y = min_y1

                if max_x1 > max_x:
                    max_x = max_x1

                if max_y1 > max_y:
                    max_y = max_y1

            if obj.type=="way":
                new_obj=obj
                new_obj.NodeRefs = []
            else:
                new_obj = T3DObject()
                new_obj.id = getID()
                new_obj.type = "way"
                new_obj.osmtags = obj.osmtags
                if new_obj.osmtags.get("type","") == "multipolygon":
                    new_obj.osmtags.pop("type")
                    
                new_obj.parts = obj.parts
                new_obj.scope_sx = obj.scope_sx
                new_obj.scope_sy = obj.scope_sy
                new_obj.scope_rz = obj.scope_rz
                new_obj.bbox = obj.bbox


            insert_Quad(new_obj, objOsmGeom, new_obj.NodeRefs, max_x - min_x, max_y - min_y, (max_x + min_x) / 2,
                        (max_y + min_y) / 2)
            new_obj.updateBBox(objOsmGeom)
            new_obj.updateScopeBBox(objOsmGeom)
            scale(new_obj, objOsmGeom, "'1.01", "'1.01")
            Objects2.append(new_obj)
        else:
            Objects2.append(obj)
    return Objects2


# ======================================================================================================================
class OCGAContext:

    def __init__(self, objOsmGeom, Objects):
        self.current_object = None
        self.unprocessed_rules_exist = True
        self.current_object_destructed = False
        self.objOsmGeom= objOsmGeom
        self.Objects = Objects
        self.Objects2 = []
        for obj in self.Objects:
            #obj.updateBBox(objOsmGeom)
            obj.alignScopeToWorld()

    # ==================================================================================================================
    # Wrappers for the OCGA operations
    # ==================================================================================================================

    # attributes
    def getTag(self, key):
        value=self.current_object.getTag(key)
        if key == "height" or key == "min_height" or key == "roof:height":
            value = parseHeightValue(value)
        return value

    def _setTag(self, key, value):
        self.current_object.osmtags[key] = str(value)
    
    def tag(self, key, value):     
        #if not self.current_object.isBuilding() and key in ['height', 'min_height', 'roof:height']:
        #    print("WARNING: tag " + key + " cannot be changed directly. Please use scale/translate/create_roof operators instead") #raise Exception
        
        self._setTag(key, value) 

    def colour(self, value):
        self._setTag("building:colour", value) 
        
    def material(self, value):
        self._setTag("building:material", value) 
        
    def roof_colour(self, value):
        self._setTag("roof:colour", value) 
        
    def roof_material(self, value):
        self._setTag("roof:material", value) 
        
    def roof_direction(self, value):
        self._setTag("roof:direction", (360-self.scope_rz()+value)%360) 
    # ========================================================================
    # Scope
    # ========================================================================
    def scope_sx(self):
        return self.current_object.scope_sx

    def scope_sy(self):
        return self.current_object.scope_sy

    def scope_sz(self):
        scope_sz=self.getTag("height")-self.getTag("min_height")
        return scope_sz

    def scope_rz(self):
        return self.current_object.scope_rz/pi*180

    def align_scope(self, alignment):
        allowed_alignments = ['geometry']
        alignment = str(alignment)
        if alignment not in allowed_alignments:
            raise Exception("Allowed parameters for align_scope operation are:" + str(allowed_alignments) )
        
        if alignment == 'geometry':
            self.current_object.alignScopeToGeometry(self.objOsmGeom)

    def alignXToLongerScopeSide(self):
        if self.current_object.scope_sx < self.current_object.scope_sy:
            self.current_object.rotateScope(90, self.objOsmGeom)

    def rotateScope(self, zAngle):
        self.current_object.rotateScope(zAngle, self.objOsmGeom)

    # ===========================================================================
    # Geometry creation
    # ===========================================================================
    def outer_rectangle(self, rule_name):
        """Creates an outer (bbox) rectangle in replacement of the current shape"""
        self.split_x((("~1", rule_name),))

        if self.current_object.isBuilding():
            # we cannot really delete building outline.
            self.restore()

    def primitive_cylinder(self, radius, nVertices=12):
        """replaces the geometry of the current object with cylinder/circle"""
        
        if type(nVertices) is str:
            nVertices=int(nVertices)

        primitiveCircle(self.current_object, self.objOsmGeom, nVertices, radius)
        if radius is None:
            scale(self.current_object, self.objOsmGeom, self.current_object.scope_sx,self.current_object.scope_sy)

    def primitiveHalfCylinder(self, nVertices=12, radius=None):
        """replaces the geometry of the current object with half of cylinder/circle"""
        primitiveHalfCircle(self.current_object, self.objOsmGeom, nVertices,radius)
        scale(self.current_object, self.objOsmGeom, self.current_object.scope_sx,self.current_object.scope_sy)
        
    def create_roof(self, roof_shape, roof_height):
        """ Not really a geometry operation, but rather tag setter."""    
        self._setTag("roof:shape", roof_shape)
        
        roof_height = parseRelativeValue(roof_height, self.scope_sz())
        self._setTag("roof:height", roof_height)

    # ===========================================================================
    # Geometry subdivision
    # ===========================================================================
    def split_x(self, split_pattern):
        new_objects = split_x(self.current_object, self.objOsmGeom, split_pattern)
        self.nil()
        self.Objects2.extend(new_objects)
        setParentChildRelationship(self.current_object, new_objects)
        self.unprocessed_rules_exist = True

    def split_y(self, split_pattern):
        new_objects = split_y(self.current_object, self.objOsmGeom, split_pattern)
        self.nil()
        self.Objects2.extend(new_objects)
        setParentChildRelationship(self.current_object, new_objects)
        self.unprocessed_rules_exist = True

    def split_z_preserve_roof(self, split_pattern):
        # for z axis it is much more convinient to go from top to bottom
        # in such a case lines breaks look nicer.
        split_pattern = split_pattern[::-1]  #reverse!
        new_objects = split_z_preserve_roof(self.current_object, split_pattern)

        self.nil()
        self.Objects2.extend(new_objects)
        setParentChildRelationship(self.current_object, new_objects)
        self.unprocessed_rules_exist = True
        
    def split_z(self, split_pattern):
        #we do not have proper implemenation for simple split_z, but it is already used in samples.
        self.split_z_preserve_roof(split_pattern) 

    def comp_roof_border(self, distance, rule_name ):
        new_objects = comp_border(self.current_object, self.objOsmGeom, rule_name, distance, True)
        self.nil()
        self.Objects2.extend(new_objects)
        setParentChildRelationship(self.current_object, new_objects)
        self.unprocessed_rules_exist = True

    def comp_border(self, distance, rule_name):
        new_objects = comp_border(self.current_object, self.objOsmGeom, rule_name, distance)
        self.nil()
        self.Objects2.extend(new_objects)
        setParentChildRelationship(self.current_object, new_objects)
        self.unprocessed_rules_exist = True

    def comp_roof(self, rule_name):
        new_objects = comp_roof(self.current_object, self.objOsmGeom, rule_name)
        self.Objects2.extend(new_objects)
        setParentChildRelationship(self.current_object, new_objects)
        self.unprocessed_rules_exist = True

    # ===========================================================================
    # Transformations
    # ===========================================================================
    def scale(self, sx, sy, sz=None):
        scale(self.current_object, self.objOsmGeom, sx, sy, sz)

    def translate(self, dx, dy, dz=None):
        translate(self.current_object, self.objOsmGeom, dx, dy, dz)

    def rotate(self, rz):
        raise Exception("rotate operation is non implemented yet")

    # ===========================================================================
    # Geometry modifications
    # ===========================================================================
    def bevel(self, r, node_list=None):
        """bevel operation -- """
        bevel(self.current_object, self.objOsmGeom, r, node_list)

    # ===========================================================================
    # flow control operations
    # ===========================================================================
    def massModel(self, rule_name):
        """Creates a building part with the height specified in the parent building
           applicable only to building outline"""
        if not self.current_object.isBuilding():
            raise Exception("massModel operation is allowed only for buildings")

        self.split_z_preserve_roof((("~1", rule_name),))
        self.restore()
        
    def nope(self):
        """Just and empty operation, to let all operations be defined """
        pass




    def restore(self):
        """restores the current shape. Can be useful if it was destructed by split or comp operation"""
        osmObject=self.current_object
        if self.Objects2.count(osmObject) == 0:
            self.Objects2.append(osmObject)

    # deletes the current shape from the list of the shapes
    def nil(self):
        """safely deletes the object from the list of existing shapes
            useful to create holes via split operations"""
        if self.Objects2.count(self.current_object) > 0:
            self.Objects2.remove(self.current_object)

        # we also need to delete the object from the list of its parent building
        parent_building=self.current_object.parent_building
        if parent_building is not None:
            if parent_building.parts.count(self.current_object)>0:
                parent_building.parts.remove(self.current_object)

    # ==================================================================================================================
    # Main loop for rule processing
    # ==================================================================================================================
    def processRules(self, checkRules):
        """Main loop for rule processing"""
        self.unprocessed_rules_exist = True
        cycles_passed=0
        n1=len(self.Objects)

        while self.unprocessed_rules_exist:
            self.Objects2 = []
            self.unprocessed_rules_exist = False # we will clear flag and set it again if some rule modifies the list of parts
            for self.current_object in self.Objects:
                # destructive operations like split can remove the current object
                # non-destructive operations, like setTag, preserve it.
                # we copy it, but the check rule can remove it, if necessary
                self.Objects2.append(self.current_object)
                # check object modification rules
                if not self.current_object.rules_processed:
                    #process each object only once.
                    checkRules(self)
                    self.current_object.rules_processed = True

                if self.current_object.isBuilding() and self.Objects2.count(self.current_object) == 0:
                    #we cannot delete building outline, it is required as part of the model
                    raise Exception("Destruction of the building outline is not allowed")

            self.Objects = self.Objects2
            cycles_passed=cycles_passed+1

        print("cycles passed:", cycles_passed)
        print("building parts created: "+ str(len(self.Objects2)-n1))


# =============== main part
def checkDuplicatedNodes(objOsmGeom):
    duplicated_nodes = {}
    duplicate = None
    ids =  list(objOsmGeom.nodes.keys())
                
    for i in range(len(ids)):
        for j in range(len(ids)):
            if i==j: 
                continue
                
            node1 = objOsmGeom.nodes[ids[i]]
            node2 = objOsmGeom.nodes[ids[j]]
            pi = 3.14
            
            dist =  (((node1.lat-node2.lat)*DEGREE_LENGTH_M)**2 +  ((node1.lon-node2.lon)*DEGREE_LENGTH_M*cos(node1.lat / 180 * pi))**2)**0.5
            
                
            if  dist < 0.01: #less then centimeter
                if node1.id[0] == '-' and node2.id[0] == '-':
                    # from two newly created node whe should prefer one created first
                    if abs(int(node1.id)) <abs(int(node2.id)):
                        duplicate = (node1.id, node2.id)
                    else:     
                        duplicate = (node2.id, node1.id)
                        
                elif node1.id[0] == '-' or node2.id[0] == '-': 
                    # at list one node is old, we should prefer it                 
                    #print ("two old nodes, skipping")
                
                    if node1.id[0] != '-' :
                        duplicate = (node1.id, node2.id)
                    else:    
                        duplicate = (node2.id, node1.id)
                    
                if duplicate[1] not in duplicated_nodes:
                    duplicated_nodes[duplicate[1]] = duplicate[0]
                    
    #print("duplicated nodes found:", len(duplicated_nodes))
    return duplicated_nodes


def ocga_process(input_file, output_file, checkRulesMy, updatable=False, rebuild_outline=True):
    print("processing file ", input_file)
    resetID()

    objOsmGeom, Objects = readOsmXml(input_file)

    ctx = OCGAContext(objOsmGeom, Objects)
    ctx.processRules(checkRulesMy)

    # todo: we need to rebuild building outline, because it should match parts
    # unlike CE, where building outline is not really used.
    if rebuild_outline:
        ctx.Objects=rebuildBuildingOutline(ctx.Objects, ctx.objOsmGeom)

    #some optimizations, so that the output file will look a bit more nice  

    # round height
    roundHeight(ctx.Objects)
    
    #check for duplicated nodes. 
    duplicated_nodes = checkDuplicatedNodes(ctx.objOsmGeom)
    
    #remove duplicated nodes
    # we need to remove them from ways only, unused nodes will be dropped automatically.
    
    for osmObject in ctx.Objects:
        if osmObject.type == "way":
            for i in range(len(osmObject.NodeRefs)):
                if osmObject.NodeRefs[i] in duplicated_nodes:
                    #if osmObject.NodeRefs[i] in ctx.objOsmGeom.nodes:
                    #    ctx.objOsmGeom.removeNode(osmObject.NodeRefs[i])
                    osmObject.NodeRefs[i] = duplicated_nodes[osmObject.NodeRefs[i]]
                    
        if osmObject.osmtags.get("roof:shape","") == "flat":
            osmObject.osmtags.pop ("roof:height")
    
    # todo: also we need to optimize geometry somehow, remove duplicated WAYS and create multypolygons    
                
    writeOsmXml(ctx.objOsmGeom, ctx.Objects, output_file, updatable)

    
def ocga_process2(input_file, output_file, rules_file, compiled_rules_file=None, updatable=False, rebuild_outline=True):     
    
    
    with open(rules_file) as f:
        lines = f.read()
        
    if Path(rules_file).suffix == '.ocga':
        
        # if ocga file is specified, let's compile it to python
        lines = ocga2py(lines)
        if compiled_rules_file:
            # if a filename for compiled rules is specified,
            # lets output the py file
            # it maybe usefull for debug purposes
            with open(compiled_rules_file, "w") as f2:
                f2.write(lines)        
            
    exec(lines, globals()) # what the fuck those globals are, and how they help here, I dunno. But it works!
    
    # we expect that the rules file contains the funtion checkRulesMy(), 
    # (either written manually or created by compiler)
    # and we will pass it to the ocga engine
    ocga_process(input_file, output_file, checkRulesMy)
    


def main():
    parser = argparse.ArgumentParser(
        prog='ocga',
        description='ocga scripting engine',
        epilog='Created by zkir (c) 2024')

    parser.add_argument('-i', '--input', required=True, type=str, help='input file, should be osm-xml' )
    parser.add_argument('-o', '--output', required=True, type=str, help='output osm-xml with created parts' )
    parser.add_argument('-r', '--rules', required=True, type=str, help='transformation rules in .ocga file' )
    args = parser.parse_args()

    input_file_name = args.input
    output_file_name = args.output
    rules_file_name = args.rules
    
    ocga_process2(input_file_name, output_file_name, rules_file_name)

if __name__ == '__main__':
    main()