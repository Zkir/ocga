"""
very simple, antlr4-based parser for  .ocga files.
.ocga is converted to python code, for further use in ocga engine  
"""
import sys
from antlr4 import *
from ocgaparser.ocgaLexer import ocgaLexer
from ocgaparser.ocgaParser import ocgaParser

built_in_immutables = {"scope_sx":    "ctx.scope_sx()",
                       "scope_sy":    "ctx.scope_sy()",
                       "scope_sz":    "ctx.scope_sz()",
                       "scope_rz":    "ctx.scope_rz()",
                       "relative_Ox": "ctx.current_object.relative_Ox"
                      }

def substitute_build_in_immutables(parameter):       
    # TODO: we need proper check for built-in immutables!
    # and also check that literals are defined!
    for key, value in built_in_immutables.items():
        parameter = parameter.replace(key, value)    
        
    return parameter

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
    
    
def visitOperator(operator_ctx, indent):
    s =''
    assert (type(operator_ctx) is ocgaParser.OperatorContext)
    operator_name = operator_ctx.children[0].getText()
    if type(operator_ctx.children[0]) is ocgaParser.СonditionalContext:
        for child in operator_ctx.children[0].children:
            #print (type(child), child.getText()) 
            if type(child) is ocgaParser.LexprContext:
                lexpr = child.getText()
                lexpr=substitute_build_in_immutables(lexpr)
                s += lexpr +  ' '    
            elif type(child) is ocgaParser.OperatorContext:
                #s += ' '*12 + 'pass \n'
                s += visitOperator(child, indent+4)
                
            elif child.getText() in ['if', 'then', 'else', 'endif']:
                if child.getText()=='if':
                    s += ' '*indent +  'if '
                elif child.getText()=='then':
                    s += ': \n'
                elif child.getText()=='else':
                    s += ' '*indent +'else: \n'
                elif child.getText()=='endif':
                    pass # endif is not needed in python
                
            else:
                raise Exception("smth unxepected found: " + child.getText())                            
    else:    
        s += ' '*indent + 'ctx.'+operator_name +'('

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
                    parameter = substitute_build_in_immutables(parameter)
                    
            elif type(op_element) is ocgaParser.ListContext:
                #list (currently) goes to python exactly as it is 
                pass
            else:
                parameter ='"'+parameter + '"'

            if parameter != ',':
                if j >1:
                    s+=', '
                s += parameter
        s += ')\n'
    
    
    return s     


def ocga2py(ocga_lines):
    #input = FileStream(input_file)
    input = InputStream(ocga_lines)
    lexer = ocgaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ocgaParser(stream)
    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Input file containts syntax errors")
        exit(1)
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
                s += visitOperator(operator_ctx, 8)
                
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
