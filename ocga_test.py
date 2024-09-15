import filecmp
from pathlib import Path

from ocga_engine import ocga_process
from ocgaparser import * #ocga2py

print("ocga test")
SAMPLES_DIR=".\\ocga_samples"
OUTPUT_DIR=".\\ocga_output"

def test(rules_file1, input_file1):
    
    #we expect that the rules file contain the funtion checkRulesMy(), and we will pass it to the ocga engine
    with open(SAMPLES_DIR +"\\"+rules_file1) as f:
        lines = f.read()
        
    if Path(rules_file1).suffix == '.ocga':
        lines = ocga2py(lines)
        #print(lines)
        with open(SAMPLES_DIR + "\\" + Path(rules_file1).stem +'_ocga.py', "w") as f2:
            f2.write(lines)        
            
    exec(lines, globals()) # what the fuck those globals are, and how they help here, I dunno. But it works!
    #print(id(checkRulesMy))
    
    input_file= SAMPLES_DIR + "\\" + input_file1
    output_file = OUTPUT_DIR + "\\" + Path(input_file1).stem + "-rewrite.osm"
    reference_file =  SAMPLES_DIR + "\\" + Path(input_file1).stem + "-rewrite.osm"
    ocga_process(input_file, output_file, checkRulesMy)
    print()
    
    result = filecmp.cmp(output_file, reference_file, shallow=False)
    
    return result     


assert test("main_cathedral_of_russian_army_ocga.py", "main_cathedral_of_russian_army.osm" )
assert test("church_of_st_louis_ocga.py",             "church_of_st_louis.osm")
assert test("gorky_park_entrance_ocga.py",            "gorky_park_entrance.osm")
assert test("gorky_park_rotunda_ocga.py",             "gorky_park_rotunda.osm")
assert test("tsaritsino_rotunda_ocga.py",             "tsaritsino_rotunda.osm")
#assert test("alexander_column_ocga.py",               "alexander_column.osm")
assert test("alexander_column.ocga",                  "alexander_column.osm")

print("Tests passed OK")