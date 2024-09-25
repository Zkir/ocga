rem example file to quickly convert and see 3d model

rem ===========  Step 1.  =================================================================================================
rem Apply ocga rules to building outline(s)
ocga_engine -i ocga_samples\moscow_manege.osm -r ocga_samples\moscow_manege.ocga -o ocga_output\moscow_manege-rewrite.osm

rem ===========  Step 2.  =================================================================================================
rem Generate 3D model 
rem we use osm2world, but blosm can be used as well
rem probably I am dumb, but I do not undersand how to use relative paths here
pushd
cd d:\osm2world  && call osm2world -i d:\ocga\ocga_output\moscow_manege-rewrite.osm -o d:\ocga\ocga_output\moscow_manege.gltf 
rem popd does not work!!!
popd  

rem ===========  Step 2.  =================================================================================================
rem activate 3d viewer. On Win10, it is built in. 
d:\ocga\ocga_output\moscow_manege.gltf
cd d:\ocga
pause
