# Generated from ocga.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ocgaParser import ocgaParser
else:
    from ocgaParser import ocgaParser

# This class defines a complete listener for a parse tree produced by ocgaParser.
class ocgaListener(ParseTreeListener):

    # Enter a parse tree produced by ocgaParser#prog.
    def enterProg(self, ctx:ocgaParser.ProgContext):
        pass

    # Exit a parse tree produced by ocgaParser#prog.
    def exitProg(self, ctx:ocgaParser.ProgContext):
        pass


    # Enter a parse tree produced by ocgaParser#ocga_header.
    def enterOcga_header(self, ctx:ocgaParser.Ocga_headerContext):
        pass

    # Exit a parse tree produced by ocgaParser#ocga_header.
    def exitOcga_header(self, ctx:ocgaParser.Ocga_headerContext):
        pass


    # Enter a parse tree produced by ocgaParser#rule.
    def enterRule(self, ctx:ocgaParser.RuleContext):
        pass

    # Exit a parse tree produced by ocgaParser#rule.
    def exitRule(self, ctx:ocgaParser.RuleContext):
        pass


    # Enter a parse tree produced by ocgaParser#rule_header.
    def enterRule_header(self, ctx:ocgaParser.Rule_headerContext):
        pass

    # Exit a parse tree produced by ocgaParser#rule_header.
    def exitRule_header(self, ctx:ocgaParser.Rule_headerContext):
        pass


    # Enter a parse tree produced by ocgaParser#operator.
    def enterOperator(self, ctx:ocgaParser.OperatorContext):
        pass

    # Exit a parse tree produced by ocgaParser#operator.
    def exitOperator(self, ctx:ocgaParser.OperatorContext):
        pass


    # Enter a parse tree produced by ocgaParser#split_pattern.
    def enterSplit_pattern(self, ctx:ocgaParser.Split_patternContext):
        pass

    # Exit a parse tree produced by ocgaParser#split_pattern.
    def exitSplit_pattern(self, ctx:ocgaParser.Split_patternContext):
        pass


    # Enter a parse tree produced by ocgaParser#split_pattern_element.
    def enterSplit_pattern_element(self, ctx:ocgaParser.Split_pattern_elementContext):
        pass

    # Exit a parse tree produced by ocgaParser#split_pattern_element.
    def exitSplit_pattern_element(self, ctx:ocgaParser.Split_pattern_elementContext):
        pass


    # Enter a parse tree produced by ocgaParser#rule_name.
    def enterRule_name(self, ctx:ocgaParser.Rule_nameContext):
        pass

    # Exit a parse tree produced by ocgaParser#rule_name.
    def exitRule_name(self, ctx:ocgaParser.Rule_nameContext):
        pass


    # Enter a parse tree produced by ocgaParser#string_const.
    def enterString_const(self, ctx:ocgaParser.String_constContext):
        pass

    # Exit a parse tree produced by ocgaParser#string_const.
    def exitString_const(self, ctx:ocgaParser.String_constContext):
        pass


    # Enter a parse tree produced by ocgaParser#argument.
    def enterArgument(self, ctx:ocgaParser.ArgumentContext):
        pass

    # Exit a parse tree produced by ocgaParser#argument.
    def exitArgument(self, ctx:ocgaParser.ArgumentContext):
        pass



del ocgaParser