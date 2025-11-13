# Generated from FiveStar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FiveStarParser import FiveStarParser
else:
    from FiveStarParser import FiveStarParser

# This class defines a complete listener for a parse tree produced by FiveStarParser.
class FiveStarListener(ParseTreeListener):

    # Enter a parse tree produced by FiveStarParser#program.
    def enterProgram(self, ctx:FiveStarParser.ProgramContext):
        pass

    # Exit a parse tree produced by FiveStarParser#program.
    def exitProgram(self, ctx:FiveStarParser.ProgramContext):
        pass


    # Enter a parse tree produced by FiveStarParser#assignment.
    def enterAssignment(self, ctx:FiveStarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by FiveStarParser#assignment.
    def exitAssignment(self, ctx:FiveStarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by FiveStarParser#list.
    def enterList(self, ctx:FiveStarParser.ListContext):
        pass

    # Exit a parse tree produced by FiveStarParser#list.
    def exitList(self, ctx:FiveStarParser.ListContext):
        pass


    # Enter a parse tree produced by FiveStarParser#expression.
    def enterExpression(self, ctx:FiveStarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by FiveStarParser#expression.
    def exitExpression(self, ctx:FiveStarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by FiveStarParser#value.
    def enterValue(self, ctx:FiveStarParser.ValueContext):
        pass

    # Exit a parse tree produced by FiveStarParser#value.
    def exitValue(self, ctx:FiveStarParser.ValueContext):
        pass



del FiveStarParser