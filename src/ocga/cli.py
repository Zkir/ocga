"""
Computer Generated Architecture OSM
Command line interface to OCGA engine
"""    
import argparse
from .ocga_engine import ocga_process2

def main():
    parser = argparse.ArgumentParser(
        prog='ocga',
        description='ocga scripting engine',
        epilog='Created by Zkir 2024-2026')

    parser.add_argument('-i', '--input', required=True, type=str, help='input file, should be osm-xml' )
    parser.add_argument('-o', '--output', required=True, type=str, help='output osm-xml with created parts' )
    parser.add_argument('-r', '--rules', required=True, type=str, help='transformation rules in .ocga file' )
    args = parser.parse_args()

    input_file_name = args.input
    output_file_name = args.output
    rules_file_name = args.rules
    
    ocga_process2(input_file_name, output_file_name, rules_file_name,output_file_name+'.py', strip_rules_names=True)

if __name__ == '__main__':
    main()