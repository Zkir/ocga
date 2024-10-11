@echo off
rem example file to quickly convert and see 3d model
rem SET MODEL_NAME=rossi_pavilion
SET MODEL_NAME=komsomolskaya_station
rem ===========  Step 1.  =================================================================================================
rem Apply ocga rules to building outline(s)
ocga_engine.py -i ocga_samples\%MODEL_NAME%.osm -r ocga_samples\%MODEL_NAME%.ocga -o ocga_output\%MODEL_NAME%-rewrite.osm
IF %ERRORLEVEL% NEQ 0 goto :error

rem ===========  Step 2.  =================================================================================================
rem Generate 3D model 
rem we use osm2world, but blosm can be used as well
rem probably I am dumb, but I do not undersand how to use relative paths here
pushd
cd d:\osm2world  && call osm2world -i d:\ocga\ocga_output\%MODEL_NAME%-rewrite.osm -o d:\ocga\ocga_output\%MODEL_NAME%.gltf 
IF %ERRORLEVEL% NEQ 0 goto :error
rem popd does not work!!!
popd  

rem ===========  Step 2.  =================================================================================================
rem activate 3d viewer. On Win10, it is built in. 
d:\ocga\ocga_output\%MODEL_NAME%.gltf
cd d:\ocga
goto :end
:error 
echo something got wrong
pause
:end

