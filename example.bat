@echo off
rem example file to quickly convert and see 3d model
rem SET MODEL_NAME=rossi_pavilion
rem SET MODEL_NAME=komsomolskaya_station
rem SET MODEL_NAME=main_cathedral_of_russian_army
SET MODEL_NAME=danilov_belltower

rem ===========  Step 1.  =================================================================================================
rem Apply ocga rules to building outline(s)
ocga -i docs\ocga_samples\%MODEL_NAME%.osm -r docs\ocga_samples\%MODEL_NAME%.ocga -o docs\ocga_output\%MODEL_NAME%-rewrite.osm
IF %ERRORLEVEL% NEQ 0 goto :error

rem ===========  Step 2.  =================================================================================================
rem Open the generated file in JOSM (if it's running)
curl -s -o nul "http://localhost:8111/open_file?filename=d:/ocga/docs/ocga_output/%MODEL_NAME%-rewrite.osm&new_layer=true"


goto :end
:error
popd  
echo something got wrong
pause
:end

