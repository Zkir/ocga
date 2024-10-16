import filecmp
from pathlib import Path

from ocga_engine import ocga_process2

print("ocga test")
SAMPLES_DIR=".\\ocga_samples"
OUTPUT_DIR=".\\ocga_output"

def test(rules_file1, input_file1):
    
    input_file= SAMPLES_DIR + "\\" + input_file1
    output_file = OUTPUT_DIR + "\\" + Path(input_file1).stem + "-rewrite.osm"
    reference_file =  SAMPLES_DIR + "\\" + Path(input_file1).stem + "-rewrite.osm"
    
    ocga_process2(input_file, output_file, SAMPLES_DIR +"\\"+ rules_file1, compiled_rules_file = OUTPUT_DIR + "\\" + Path(rules_file1).stem +'_ocga.py' )
    
    print()
    
    result = filecmp.cmp(output_file, reference_file, shallow=False)
    
    return result     

#old py rules

assert test("gorky_park_entrance_ocga.py",            "gorky_park_entrance.osm")
#new ocga rules
assert test("church_of_st_louis.ocga",                "church_of_st_louis.osm")
assert test("gorky_park_rotunda.ocga",                "gorky_park_rotunda.osm")
assert test("tsaritsino_rotunda.ocga",                "tsaritsino_rotunda.osm")
assert test("main_cathedral_of_russian_army.ocga",    "main_cathedral_of_russian_army.osm" )
assert test("alexander_column.ocga",                  "alexander_column.osm")
assert test("moscow_manege.ocga",                     "moscow_manege.osm")
assert test("komsomolskaya_station.ocga",             "komsomolskaya_station.osm")

print("Tests passed OK")