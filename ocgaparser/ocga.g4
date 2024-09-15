grammar ocga;

prog: ocga_header rule+ EOF ;
ocga_header: OCGA argument;
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
	SCALE argument COMMA argument  |
	SCALE argument COMMA argument COMMA argument  |
	TRANSLATE argument COMMA argument  |
	TRANSLATE argument COMMA argument COMMA argument  |
	SPLIT_Z split_pattern |
	PRIMITIVECYLINDER argument |
	PRIMITIVECYLINDER argument COMMA argument| 
	ROOF string_const COMMA argument|  
	COMPBORDER argument COMMA rule_name |
	RESTORE |
	NOPE
	;  
    
/* spit pattern */
split_pattern: split_pattern_element (PIPE split_pattern_element)* ;
    
split_pattern_element: argument COLUMN rule_name;

rule_name:            RULE_NAME;
string_const:         RULE_NAME;
argument:             NUMBER | RELATIVE_MARK NUMBER | APPROX_MARK NUMBER ; 
key_name  : RULE_NAME (COLUMN RULE_NAME)* ;
tag_value : RULE_NAME | NUMBER ;
    
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
PRIMITIVECYLINDER:    'primitive_cylinder';
ROOF:                 'create_roof';
COMPBORDER:           'comp_border'; 
RESTORE:              'restore';
NOPE:                 'nope';

NUMBER
    : ('0' .. '9')+ ('.' ('0' .. '9')+)?
    ;
//it seems that literal definitions in ANTLR cannot intersect	
//that's why more narrow definition NUMBER should precede RULE_NAME
RULE_NAME:            [A-Za-z0-9_]+;   /*Letters, numbers and underscore */


RELATIVE_MARK: '\'';
APPROX_MARK: '~';



COLUMN:               ':';
COMMA:                ',';
PIPE:                 '|';
                     
COMMENT: '#' ~[\r\n]* ->skip;
NEWLINE : [\r\n]+ -> skip;
WS :  ' ' -> skip;
TAB :  '\t' -> skip;
