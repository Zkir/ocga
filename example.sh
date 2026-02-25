# example file to quickly convert and see 3d model
# MODEL_NAME=rossi_pavilion
MODEL_NAME=komsomolskaya_station
# ===========  Step 1.  =================================================================================================
# Apply ocga rules to building outline(s)
ocga -i docs/ocga_samples/$MODEL_NAME.osm -r docs/ocga_samples/$MODEL_NAME.ocga -o docs/ocga_output/$MODEL_NAME-rewrite.osm

# ===========  Step 2.  =================================================================================================
# Generate 3D model
# we use osm2world, but blosm can be used as well
# probably I am dumb, but I do not undersand how to use relative paths here

(cd /home/zkir/osm2world  ; sh osm2world.sh -i /home/zkir/src/ocga/docs/ocga_output/$MODEL_NAME-rewrite.osm -o /home/zkir/src/ocga/docs/ocga_output/$MODEL_NAME.gltf )


# ===========  Step 2.  =================================================================================================
# activate 3d viewer. On Win10, it is built in.
f3d docs/ocga_output/$MODEL_NAME.gltf
