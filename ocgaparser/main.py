"""
very simple, antlr4-based parser for  .ocga files.
.ocga is converted to python code, for further use in ocga engine  
"""
import sys
from antlr4 import *
from ocgaparser.ocgaLexer import ocgaLexer
from ocgaparser.ocgaParser import ocgaParser

def parse_split_pattern_element(split_element):
    size, rule_name = split_element.split(":")
    return (size.strip(), rule_name.strip())

def parse_split_pattern(op_element):
    
    
    parameter = [] #str(parse_split_pattern(op_element.getText()))
    for pattern_element in op_element.children:
        if type(pattern_element) is ocgaParser.Simple_split_patternContext:
            parameter += [parse_split_pattern_element(pattern_element.getText())]
            
        elif type(pattern_element) is ocgaParser.Repeat_split_patternContext:
            child_split_pattern_parsed = parse_split_pattern(pattern_element.children[1])
            Multiplicity =pattern_element.children[-1].getText()
            parameter += [(Multiplicity,child_split_pattern_parsed)]
            
        elif pattern_element.getText() in ['|']:
            pass
        else:
            raise Exception("unexpected split pattern element: "+str(type(pattern_element)) + '  '+ pattern_element.getText() )
            
    parameter = tuple(parameter)  
    return parameter


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
                operator_name = operator_ctx.children[0].getText()
                s += ' '*8 + 'ctx.'+operator_name +'('

                for  j in range(1,len(operator_ctx.children)):
                    op_element = operator_ctx.children[j]
                    
                    parameter = op_element.getText()
                    if parameter == ',':
                        continue
                    if type(op_element) is ocgaParser.Split_patternContext:
                        #recursive parsing of split pattern
                        parameter = parse_split_pattern(op_element)
                        parameter = str(parameter)        

                    elif type(op_element) is ocgaParser.ExprContext:
                        
                        if type(op_element.children[0]) is ocgaParser.Relative_numberContext:
                            parameter ='"'+parameter + '"'    
                        else:    
                           
                            #exit(123)
                            #TODO: we need proper check for build in immutables!
                            # and also check that literals are defined!
                            if "scope_sx" in parameter or "scope_sy" in parameter or "scope_sz" in parameter or "scope_rz" in parameter:
                                #print(parameter)
                                #print(type(op_element.children[0]))
                                parameter = parameter.replace("scope_sx", "ctx.scope_sx()")
                                parameter = parameter.replace("scope_sy", "ctx.scope_sy()")
                                parameter = parameter.replace("scope_sz", "ctx.scope_sz()")
                                parameter = parameter.replace("scope_rz", "ctx.scope_rz()")
                                
                                #print()
                    else:
                        parameter ='"'+parameter + '"'

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
