# Generated from ocga.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ocgaParser import ocgaParser
else:
    from ocgaParser import ocgaParser

# This class defines a complete generic visitor for a parse tree produced by ocgaParser.

class ocgaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ocgaParser#prog.
    def visitProg(self, ctx:ocgaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ocgaParser#ocga_header.
    def visitOcga_header(self, ctx:ocgaParser.Ocga_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ocgaParser#rule.
    def visitRule(self, ctx:ocgaParser.RuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ocgaParser#rule_header.
    def visitRule_header(self, ctx:ocgaParser.Rule_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ocgaParser#operator.
    def visitOperator(self, ctx:ocgaParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ocgaParser#split_pattern.
    def visitSplit_pattern(self, ctx:ocgaParser.Split_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ocgaParser#split_pattern_element.
    def visitSplit_pattern_element(self, ctx:ocgaParser.Split_pattern_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ocgaParser#rule_name.
    def visitRule_name(self, ctx:ocgaParser.Rule_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ocgaParser#string_const.
    def visitString_const(self, ctx:ocgaParser.String_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ocgaParser#argument.
    def visitArgument(self, ctx:ocgaParser.ArgumentContext):
        return self.visitChildren(ctx)



del ocgaParser