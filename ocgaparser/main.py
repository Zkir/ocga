"""
very simple, antlr4-based parser for  .ocga files.
.ocga is converted to python code, for further use in ocga engine  
"""
import sys
from antlr4 import *
from ocgaparser.ocgaLexer import ocgaLexer
from ocgaparser.ocgaParser import ocgaParser

def parse_split_pattern(split_pattern):
    split_pattern_as_list =[]
    split_elements = split_pattern.split("|")
    for split_element in split_elements:
        size, rule_name = split_element.split(":")
        split_pattern_as_list.append((size, rule_name))

    return tuple(split_pattern_as_list)


def ocga2py(ocga_lines):
    #input = FileStream(input_file)
    input = InputStream(ocga_lines)
    lexer = ocgaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ocgaParser(stream)
    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Input file containts syntax errors")
        exit()
    s = ""
    for child in tree.children:
        if type(child) is ocgaParser.Ocga_headerContext:
            ocga_verison = child.children[1].getText()
            if ocga_verison == "0.1":
                #print("ocga version "+ocga_verison)
                s += '#automatically generated ocga-py \n'
                s += 'def checkRulesMy(ctx):\n'
            else:
                print("ERROR: unknown ocga version: "+ocga_verison)
                exit()
        if type(child) is ocgaParser.RuleContext:
            rule_name = child.children[0].children[1].getText()
            if rule_name != "building":
                s += ' '*4 + 'if ctx.getTag("building:part") == "'+rule_name+'":\n'
            else:
                s += ' '*4 + 'if ctx.getTag("building") != "":\n'
            #print ("rule " + rule_name  +':' )
            for i in range(1,len(child.children)):
                operator_ctx=child.children[i]
                #print ("    ", end="")
                operator_name = operator_ctx.children[0].getText()
                s += ' '*8 + 'ctx.'+operator_name +'('

                for  j in range(1,len(operator_ctx.children)):
                    op_element = operator_ctx.children[j]
                    
                    parameter = op_element.getText()
                    if parameter == ',':
                        continue
                    if type(op_element) is ocgaParser.Split_patternContext:
                        parameter = str(parse_split_pattern(op_element.getText()))
                    elif type(op_element) is ocgaParser.ExprContext:
                        
                        if type(op_element.children[0]) is ocgaParser.Relative_numberContext:
                            parameter ='"'+parameter + '"'    
                        else:    
                           
                            #exit(123)
                            #TODO: we need proper check for build in immutables!
                            # and also check that literals are defined!
                            if "scope_sx" in parameter or "scope_sy" in parameter or "scope_sz" in parameter:
                                #print(parameter)
                                #print(type(op_element.children[0]))
                                parameter = parameter.replace("scope_sx", "ctx.scope_sx()")
                                parameter = parameter.replace("scope_sy", "ctx.scope_sy()")
                                parameter = parameter.replace("scope_sz", "ctx.scope_sz()")
                                #print()
                    else:
                        parameter ='"'+parameter + '"'
                    #print (parameter, end=" ")

                    if parameter != ',':
                        if j >1:
                            s+=', '
                        s += parameter
                s += ')\n'
                #print()
            s += '\n'

    return s


def main(argv):
    input_file="alexander_column.ocga"
    output_file="alexander_column_ocga.py"
    with open(input_file) as f:
        ocga_lines = f.read()
    py_lines = ocga2py(ocga_lines)
    print(py_lines)
    exec(py_lines, globals())
    print(id(checkRulesMy))
    with open(output_file,"w") as f:
        f.write(py_lines)


if __name__ == '__main__':
    main(sys.argv)
