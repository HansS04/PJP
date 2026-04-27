# Generated from PLC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLCParser import PLCParser
else:
    from PLCParser import PLCParser

# This class defines a complete listener for a parse tree produced by PLCParser.
class PLCListener(ParseTreeListener):

    # Enter a parse tree produced by PLCParser#program.
    def enterProgram(self, ctx:PLCParser.ProgramContext):
        pass

    # Exit a parse tree produced by PLCParser#program.
    def exitProgram(self, ctx:PLCParser.ProgramContext):
        pass


    # Enter a parse tree produced by PLCParser#type_spec.
    def enterType_spec(self, ctx:PLCParser.Type_specContext):
        pass

    # Exit a parse tree produced by PLCParser#type_spec.
    def exitType_spec(self, ctx:PLCParser.Type_specContext):
        pass


    # Enter a parse tree produced by PLCParser#EmptyStatement.
    def enterEmptyStatement(self, ctx:PLCParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#EmptyStatement.
    def exitEmptyStatement(self, ctx:PLCParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#BlockStatement.
    def enterBlockStatement(self, ctx:PLCParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#BlockStatement.
    def exitBlockStatement(self, ctx:PLCParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#DeclarationStatement.
    def enterDeclarationStatement(self, ctx:PLCParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#DeclarationStatement.
    def exitDeclarationStatement(self, ctx:PLCParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#ReadStatement.
    def enterReadStatement(self, ctx:PLCParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#ReadStatement.
    def exitReadStatement(self, ctx:PLCParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#WriteStatement.
    def enterWriteStatement(self, ctx:PLCParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#WriteStatement.
    def exitWriteStatement(self, ctx:PLCParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#ExpressionStatement.
    def enterExpressionStatement(self, ctx:PLCParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#ExpressionStatement.
    def exitExpressionStatement(self, ctx:PLCParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#IfStatement.
    def enterIfStatement(self, ctx:PLCParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#IfStatement.
    def exitIfStatement(self, ctx:PLCParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#WhileStatement.
    def enterWhileStatement(self, ctx:PLCParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#WhileStatement.
    def exitWhileStatement(self, ctx:PLCParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#forStatement.
    def enterForStatement(self, ctx:PLCParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#forStatement.
    def exitForStatement(self, ctx:PLCParser.ForStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#fopenStatement.
    def enterFopenStatement(self, ctx:PLCParser.FopenStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#fopenStatement.
    def exitFopenStatement(self, ctx:PLCParser.FopenStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#fappendStatement.
    def enterFappendStatement(self, ctx:PLCParser.FappendStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#fappendStatement.
    def exitFappendStatement(self, ctx:PLCParser.FappendStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#TernaryExpression.
    def enterTernaryExpression(self, ctx:PLCParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#TernaryExpression.
    def exitTernaryExpression(self, ctx:PLCParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#PowerExpression.
    def enterPowerExpression(self, ctx:PLCParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#PowerExpression.
    def exitPowerExpression(self, ctx:PLCParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#IntExpression.
    def enterIntExpression(self, ctx:PLCParser.IntExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#IntExpression.
    def exitIntExpression(self, ctx:PLCParser.IntExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#AddSubConcatExpression.
    def enterAddSubConcatExpression(self, ctx:PLCParser.AddSubConcatExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#AddSubConcatExpression.
    def exitAddSubConcatExpression(self, ctx:PLCParser.AddSubConcatExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#FloatExpression.
    def enterFloatExpression(self, ctx:PLCParser.FloatExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#FloatExpression.
    def exitFloatExpression(self, ctx:PLCParser.FloatExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#UnaryExpression.
    def enterUnaryExpression(self, ctx:PLCParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#UnaryExpression.
    def exitUnaryExpression(self, ctx:PLCParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#OrExpression.
    def enterOrExpression(self, ctx:PLCParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#OrExpression.
    def exitOrExpression(self, ctx:PLCParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#ParensExpression.
    def enterParensExpression(self, ctx:PLCParser.ParensExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#ParensExpression.
    def exitParensExpression(self, ctx:PLCParser.ParensExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#MulDivModExpression.
    def enterMulDivModExpression(self, ctx:PLCParser.MulDivModExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#MulDivModExpression.
    def exitMulDivModExpression(self, ctx:PLCParser.MulDivModExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#BoolExpression.
    def enterBoolExpression(self, ctx:PLCParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#BoolExpression.
    def exitBoolExpression(self, ctx:PLCParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#ComparisonExpression.
    def enterComparisonExpression(self, ctx:PLCParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#ComparisonExpression.
    def exitComparisonExpression(self, ctx:PLCParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#AndExpression.
    def enterAndExpression(self, ctx:PLCParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#AndExpression.
    def exitAndExpression(self, ctx:PLCParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx:PLCParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx:PLCParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#charAtExpression.
    def enterCharAtExpression(self, ctx:PLCParser.CharAtExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#charAtExpression.
    def exitCharAtExpression(self, ctx:PLCParser.CharAtExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#StringExpression.
    def enterStringExpression(self, ctx:PLCParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#StringExpression.
    def exitStringExpression(self, ctx:PLCParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#IdExpression.
    def enterIdExpression(self, ctx:PLCParser.IdExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#IdExpression.
    def exitIdExpression(self, ctx:PLCParser.IdExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#EqualityExpression.
    def enterEqualityExpression(self, ctx:PLCParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#EqualityExpression.
    def exitEqualityExpression(self, ctx:PLCParser.EqualityExpressionContext):
        pass



del PLCParser