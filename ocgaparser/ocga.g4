grammar ocga;

prog: ocga_header rule+ EOF ;
ocga_header: OCGA NUMBER;
rule: rule_header operator+;
rule_header: RULE rule_name COLUMN; 
    
/* operators  */

operator:
	ALIGNSCOPE 'geometry' |  
	TAG key_name COMMA tag_value |
	ROOFCOLOUR tag_value |
    ROOFMATERIAL tag_value |
    COLOUR tag_value |
    MATERIAL tag_value |
	OUTERRECTANGLE rule_name  |
	MASSMODEL rule_name |  
	SCALE expr COMMA expr  |
	SCALE expr COMMA expr COMMA expr  |
	TRANSLATE expr COMMA expr  |
	TRANSLATE expr COMMA expr COMMA expr  |
	SPLIT_X split_pattern |
	SPLIT_Y split_pattern |
	SPLIT_Z split_pattern |
	ROTATESCOPE expr |
	ROTATE expr |
	PRIMITIVECYLINDER expr |
	PRIMITIVECYLINDER expr COMMA expr | 
	PRIMITIVEHALFCYLINDER expr |
	PRIMITIVEHALFCYLINDER expr COMMA expr | 
	ROOF roof_shape COMMA expr |  
	ROOFDIRECTION expr |  
	COMPBORDER expr COMMA rule_name |
	RESTORE |
	NIL |
	NOPE
	;  


    
/* spit pattern for split operator */
split_pattern:         split_pattern_element (PIPE split_pattern_element)* ;
split_pattern_element: split_selector COLUMN rule_name     #simple_split_pattern
                     | LPAREN split_pattern RPAREN MULT    #repeat_split_pattern 
					 ;
					 
split_selector:        NUMBER | APPROX_MARK NUMBER ;

/* arithmetic expressions, allowed in certain operators*/
expr:            relative_number 
    |            simple_expr
    |            expr (MULT|DIV) expr 
    |            expr (PLUS|MINUS) expr
	;
relative_number: RELATIVE_MARK NUMBER;
	
simple_expr:     LITERAL
           |     NUMBER
		   |     MINUS NUMBER
           |     LPAREN expr RPAREN 
		   ;


rule_name:            LITERAL;
roof_shape:           LITERAL;
    
key_name  : LITERAL (COLUMN LITERAL)* ;
tag_value : LITERAL | NUMBER ;
    
/* reserved words */
RULE:                 'rule';
OCGA:                 'ocga';
TAG:                  'tag' ;
ROOFCOLOUR:           'roof_colour';
ROOFMATERIAL:         'roof_material';
COLOUR:               'colour';
MATERIAL:             'material';

ALIGNSCOPE:           'align_scope';
OUTERRECTANGLE:       'outer_rectangle';
MASSMODEL:            'massModel';
SCALE:                'scale';
TRANSLATE:            'translate'; 
SPLIT_Z:              'split_z';
SPLIT_X:              'split_x';
SPLIT_Y:              'split_y';
ROTATESCOPE:          'rotate_scope';
PRIMITIVECYLINDER:    'primitive_cylinder';
PRIMITIVEHALFCYLINDER:'primitive_halfcylinder';
ROOF:                 'create_roof';
ROOFDIRECTION:        'roof_direction';
COMPBORDER:           'comp_border'; 
RESTORE:              'restore';
NIL:                  'nil';
NOPE:                 'nope';
ROTATE:               'rotate';

NUMBER
    : ('0' .. '9')+ ('.' ('0' .. '9')+)?
    ;
//it seems that literal definitions in ANTLR cannot intersect	
//that's why more narrow definition NUMBER should precede RULE_NAME
LITERAL:            [A-Za-z0-9_]+;   /*Letters, numbers and underscore */


RELATIVE_MARK: '\'';
APPROX_MARK: '~';

COLUMN:   ':';
COMMA:    ',';
PIPE:     '|';

LCURLY:   '{';
RCURLY:   '}';
LPAREN:   '(';
RPAREN:   ')';

PLUS:     '+';
MINUS:    '-';
MULT:    '*';
DIV:      '/';

                     
COMMENT: '#' ~[\r\n]* ->skip;
NEWLINE : [\r\n]+ -> skip;
WS :  ' ' -> skip;
TAB :  '\t' -> skip;
