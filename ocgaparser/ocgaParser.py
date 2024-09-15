# Generated from ocga.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,115,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,4,0,23,8,0,11,0,12,0,24,1,0,1,
        0,1,1,1,1,1,1,1,2,1,2,4,2,34,8,2,11,2,12,2,35,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,3,4,91,8,4,1,5,1,5,1,5,1,5,1,5,3,5,98,8,5,1,6,1,6,1,6,1,6,1,7,
        1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,113,8,9,1,9,0,0,10,0,2,4,6,8,
        10,12,14,16,18,0,0,122,0,20,1,0,0,0,2,28,1,0,0,0,4,31,1,0,0,0,6,
        37,1,0,0,0,8,90,1,0,0,0,10,97,1,0,0,0,12,99,1,0,0,0,14,103,1,0,0,
        0,16,105,1,0,0,0,18,112,1,0,0,0,20,22,3,2,1,0,21,23,3,4,2,0,22,21,
        1,0,0,0,23,24,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,26,1,0,0,0,
        26,27,5,0,0,1,27,1,1,0,0,0,28,29,5,2,0,0,29,30,3,18,9,0,30,3,1,0,
        0,0,31,33,3,6,3,0,32,34,3,8,4,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,
        1,0,0,0,35,36,1,0,0,0,36,5,1,0,0,0,37,38,5,1,0,0,38,39,3,14,7,0,
        39,40,5,20,0,0,40,7,1,0,0,0,41,91,5,3,0,0,42,43,5,4,0,0,43,91,3,
        14,7,0,44,45,5,5,0,0,45,91,3,14,7,0,46,47,5,6,0,0,47,48,3,18,9,0,
        48,49,5,21,0,0,49,50,3,18,9,0,50,91,1,0,0,0,51,52,5,6,0,0,52,53,
        3,18,9,0,53,54,5,21,0,0,54,55,3,18,9,0,55,56,5,21,0,0,56,57,3,18,
        9,0,57,91,1,0,0,0,58,59,5,7,0,0,59,60,3,18,9,0,60,61,5,21,0,0,61,
        62,3,18,9,0,62,91,1,0,0,0,63,64,5,7,0,0,64,65,3,18,9,0,65,66,5,21,
        0,0,66,67,3,18,9,0,67,68,5,21,0,0,68,69,3,18,9,0,69,91,1,0,0,0,70,
        71,5,8,0,0,71,91,3,10,5,0,72,73,5,11,0,0,73,74,3,18,9,0,74,75,5,
        21,0,0,75,76,3,18,9,0,76,91,1,0,0,0,77,91,5,11,0,0,78,79,5,12,0,
        0,79,80,3,16,8,0,80,81,5,21,0,0,81,82,3,18,9,0,82,91,1,0,0,0,83,
        84,5,13,0,0,84,85,3,18,9,0,85,86,5,21,0,0,86,87,3,14,7,0,87,91,1,
        0,0,0,88,91,5,14,0,0,89,91,5,15,0,0,90,41,1,0,0,0,90,42,1,0,0,0,
        90,44,1,0,0,0,90,46,1,0,0,0,90,51,1,0,0,0,90,58,1,0,0,0,90,63,1,
        0,0,0,90,70,1,0,0,0,90,72,1,0,0,0,90,77,1,0,0,0,90,78,1,0,0,0,90,
        83,1,0,0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,9,1,0,0,0,92,93,3,12,6,
        0,93,94,5,22,0,0,94,95,3,10,5,0,95,98,1,0,0,0,96,98,3,12,6,0,97,
        92,1,0,0,0,97,96,1,0,0,0,98,11,1,0,0,0,99,100,3,18,9,0,100,101,5,
        20,0,0,101,102,3,14,7,0,102,13,1,0,0,0,103,104,5,17,0,0,104,15,1,
        0,0,0,105,106,5,17,0,0,106,17,1,0,0,0,107,113,5,16,0,0,108,109,5,
        18,0,0,109,113,5,16,0,0,110,111,5,19,0,0,111,113,5,16,0,0,112,107,
        1,0,0,0,112,108,1,0,0,0,112,110,1,0,0,0,113,19,1,0,0,0,5,24,35,90,
        97,112
    ]

class ocgaParser ( Parser ):

    grammarFileName = "ocga.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'rule'", "'ocga'", "'alignScopeToGeometry'", 
                     "'outerRectangle'", "'massModel'", "'scale'", "'translate'", 
                     "'split_z'", "'split_x'", "'split_y'", "'primitiveCylinder'", 
                     "'roof'", "'comp_border'", "'restore'", "'nope'", "<INVALID>", 
                     "<INVALID>", "'''", "'~'", "':'", "','", "'|'", "<INVALID>", 
                     "<INVALID>", "' '", "'\\t'" ]

    symbolicNames = [ "<INVALID>", "RULE", "OCGA", "ALIGNSCOPETOGEOMETRY", 
                      "OUTERRECTANGLE", "MASSMODEL", "SCALE", "TRANSLATE", 
                      "SPLIT_Z", "SPLIT_X", "SPLIT_Y", "PRIMITIVECYLINDER", 
                      "ROOF", "COMPBORDER", "RESTORE", "NOPE", "NUMBER", 
                      "RULE_NAME", "RELATIVE_MARK", "APPROX_MARK", "COLUMN", 
                      "COMMA", "PIPE", "COMMENT", "NEWLINE", "WS", "TAB" ]

    RULE_prog = 0
    RULE_ocga_header = 1
    RULE_rule = 2
    RULE_rule_header = 3
    RULE_operator = 4
    RULE_split_pattern = 5
    RULE_split_pattern_element = 6
    RULE_rule_name = 7
    RULE_string_const = 8
    RULE_argument = 9

    ruleNames =  [ "prog", "ocga_header", "rule", "rule_header", "operator", 
                   "split_pattern", "split_pattern_element", "rule_name", 
                   "string_const", "argument" ]

    EOF = Token.EOF
    RULE=1
    OCGA=2
    ALIGNSCOPETOGEOMETRY=3
    OUTERRECTANGLE=4
    MASSMODEL=5
    SCALE=6
    TRANSLATE=7
    SPLIT_Z=8
    SPLIT_X=9
    SPLIT_Y=10
    PRIMITIVECYLINDER=11
    ROOF=12
    COMPBORDER=13
    RESTORE=14
    NOPE=15
    NUMBER=16
    RULE_NAME=17
    RELATIVE_MARK=18
    APPROX_MARK=19
    COLUMN=20
    COMMA=21
    PIPE=22
    COMMENT=23
    NEWLINE=24
    WS=25
    TAB=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ocga_header(self):
            return self.getTypedRuleContext(ocgaParser.Ocga_headerContext,0)


        def EOF(self):
            return self.getToken(ocgaParser.EOF, 0)

        def rule_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ocgaParser.RuleContext)
            else:
                return self.getTypedRuleContext(ocgaParser.RuleContext,i)


        def getRuleIndex(self):
            return ocgaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ocgaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.ocga_header()
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self.rule_()
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 26
            self.match(ocgaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ocga_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OCGA(self):
            return self.getToken(ocgaParser.OCGA, 0)

        def argument(self):
            return self.getTypedRuleContext(ocgaParser.ArgumentContext,0)


        def getRuleIndex(self):
            return ocgaParser.RULE_ocga_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOcga_header" ):
                listener.enterOcga_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOcga_header" ):
                listener.exitOcga_header(self)




    def ocga_header(self):

        localctx = ocgaParser.Ocga_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ocga_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(ocgaParser.OCGA)
            self.state = 29
            self.argument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rule_header(self):
            return self.getTypedRuleContext(ocgaParser.Rule_headerContext,0)


        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ocgaParser.OperatorContext)
            else:
                return self.getTypedRuleContext(ocgaParser.OperatorContext,i)


        def getRuleIndex(self):
            return ocgaParser.RULE_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule" ):
                listener.enterRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule" ):
                listener.exitRule(self)




    def rule_(self):

        localctx = ocgaParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.rule_header()
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.operator()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 63992) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE(self):
            return self.getToken(ocgaParser.RULE, 0)

        def rule_name(self):
            return self.getTypedRuleContext(ocgaParser.Rule_nameContext,0)


        def COLUMN(self):
            return self.getToken(ocgaParser.COLUMN, 0)

        def getRuleIndex(self):
            return ocgaParser.RULE_rule_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_header" ):
                listener.enterRule_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_header" ):
                listener.exitRule_header(self)




    def rule_header(self):

        localctx = ocgaParser.Rule_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rule_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ocgaParser.RULE)
            self.state = 38
            self.rule_name()
            self.state = 39
            self.match(ocgaParser.COLUMN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALIGNSCOPETOGEOMETRY(self):
            return self.getToken(ocgaParser.ALIGNSCOPETOGEOMETRY, 0)

        def OUTERRECTANGLE(self):
            return self.getToken(ocgaParser.OUTERRECTANGLE, 0)

        def rule_name(self):
            return self.getTypedRuleContext(ocgaParser.Rule_nameContext,0)


        def MASSMODEL(self):
            return self.getToken(ocgaParser.MASSMODEL, 0)

        def SCALE(self):
            return self.getToken(ocgaParser.SCALE, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ocgaParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(ocgaParser.ArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ocgaParser.COMMA)
            else:
                return self.getToken(ocgaParser.COMMA, i)

        def TRANSLATE(self):
            return self.getToken(ocgaParser.TRANSLATE, 0)

        def SPLIT_Z(self):
            return self.getToken(ocgaParser.SPLIT_Z, 0)

        def split_pattern(self):
            return self.getTypedRuleContext(ocgaParser.Split_patternContext,0)


        def PRIMITIVECYLINDER(self):
            return self.getToken(ocgaParser.PRIMITIVECYLINDER, 0)

        def ROOF(self):
            return self.getToken(ocgaParser.ROOF, 0)

        def string_const(self):
            return self.getTypedRuleContext(ocgaParser.String_constContext,0)


        def COMPBORDER(self):
            return self.getToken(ocgaParser.COMPBORDER, 0)

        def RESTORE(self):
            return self.getToken(ocgaParser.RESTORE, 0)

        def NOPE(self):
            return self.getToken(ocgaParser.NOPE, 0)

        def getRuleIndex(self):
            return ocgaParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = ocgaParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operator)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(ocgaParser.ALIGNSCOPETOGEOMETRY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(ocgaParser.OUTERRECTANGLE)
                self.state = 43
                self.rule_name()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.match(ocgaParser.MASSMODEL)
                self.state = 45
                self.rule_name()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.match(ocgaParser.SCALE)
                self.state = 47
                self.argument()
                self.state = 48
                self.match(ocgaParser.COMMA)
                self.state = 49
                self.argument()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.match(ocgaParser.SCALE)
                self.state = 52
                self.argument()
                self.state = 53
                self.match(ocgaParser.COMMA)
                self.state = 54
                self.argument()
                self.state = 55
                self.match(ocgaParser.COMMA)
                self.state = 56
                self.argument()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.match(ocgaParser.TRANSLATE)
                self.state = 59
                self.argument()
                self.state = 60
                self.match(ocgaParser.COMMA)
                self.state = 61
                self.argument()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 63
                self.match(ocgaParser.TRANSLATE)
                self.state = 64
                self.argument()
                self.state = 65
                self.match(ocgaParser.COMMA)
                self.state = 66
                self.argument()
                self.state = 67
                self.match(ocgaParser.COMMA)
                self.state = 68
                self.argument()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 70
                self.match(ocgaParser.SPLIT_Z)
                self.state = 71
                self.split_pattern()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 72
                self.match(ocgaParser.PRIMITIVECYLINDER)
                self.state = 73
                self.argument()
                self.state = 74
                self.match(ocgaParser.COMMA)
                self.state = 75
                self.argument()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 77
                self.match(ocgaParser.PRIMITIVECYLINDER)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 78
                self.match(ocgaParser.ROOF)
                self.state = 79
                self.string_const()
                self.state = 80
                self.match(ocgaParser.COMMA)
                self.state = 81
                self.argument()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 83
                self.match(ocgaParser.COMPBORDER)
                self.state = 84
                self.argument()
                self.state = 85
                self.match(ocgaParser.COMMA)
                self.state = 86
                self.rule_name()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 88
                self.match(ocgaParser.RESTORE)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 89
                self.match(ocgaParser.NOPE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Split_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def split_pattern_element(self):
            return self.getTypedRuleContext(ocgaParser.Split_pattern_elementContext,0)


        def PIPE(self):
            return self.getToken(ocgaParser.PIPE, 0)

        def split_pattern(self):
            return self.getTypedRuleContext(ocgaParser.Split_patternContext,0)


        def getRuleIndex(self):
            return ocgaParser.RULE_split_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSplit_pattern" ):
                listener.enterSplit_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSplit_pattern" ):
                listener.exitSplit_pattern(self)




    def split_pattern(self):

        localctx = ocgaParser.Split_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_split_pattern)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.split_pattern_element()
                self.state = 93
                self.match(ocgaParser.PIPE)
                self.state = 94
                self.split_pattern()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.split_pattern_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Split_pattern_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(ocgaParser.ArgumentContext,0)


        def COLUMN(self):
            return self.getToken(ocgaParser.COLUMN, 0)

        def rule_name(self):
            return self.getTypedRuleContext(ocgaParser.Rule_nameContext,0)


        def getRuleIndex(self):
            return ocgaParser.RULE_split_pattern_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSplit_pattern_element" ):
                listener.enterSplit_pattern_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSplit_pattern_element" ):
                listener.exitSplit_pattern_element(self)




    def split_pattern_element(self):

        localctx = ocgaParser.Split_pattern_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_split_pattern_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.argument()
            self.state = 100
            self.match(ocgaParser.COLUMN)
            self.state = 101
            self.rule_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE_NAME(self):
            return self.getToken(ocgaParser.RULE_NAME, 0)

        def getRuleIndex(self):
            return ocgaParser.RULE_rule_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_name" ):
                listener.enterRule_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_name" ):
                listener.exitRule_name(self)




    def rule_name(self):

        localctx = ocgaParser.Rule_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rule_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ocgaParser.RULE_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE_NAME(self):
            return self.getToken(ocgaParser.RULE_NAME, 0)

        def getRuleIndex(self):
            return ocgaParser.RULE_string_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_const" ):
                listener.enterString_const(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_const" ):
                listener.exitString_const(self)




    def string_const(self):

        localctx = ocgaParser.String_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_string_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ocgaParser.RULE_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ocgaParser.NUMBER, 0)

        def RELATIVE_MARK(self):
            return self.getToken(ocgaParser.RELATIVE_MARK, 0)

        def APPROX_MARK(self):
            return self.getToken(ocgaParser.APPROX_MARK, 0)

        def getRuleIndex(self):
            return ocgaParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = ocgaParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argument)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(ocgaParser.NUMBER)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(ocgaParser.RELATIVE_MARK)
                self.state = 109
                self.match(ocgaParser.NUMBER)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.match(ocgaParser.APPROX_MARK)
                self.state = 111
                self.match(ocgaParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





