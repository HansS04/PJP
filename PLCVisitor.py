# Generated from PLC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLCParser import PLCParser
else:
    from PLCParser import PLCParser

# This class defines a complete generic visitor for a parse tree produced by PLCParser.

class PLCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLCParser#program.
    def visitProgram(self, ctx:PLCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#type_spec.
    def visitType_spec(self, ctx:PLCParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#EmptyStatement.
    def visitEmptyStatement(self, ctx:PLCParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#BlockStatement.
    def visitBlockStatement(self, ctx:PLCParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#DeclarationStatement.
    def visitDeclarationStatement(self, ctx:PLCParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#ReadStatement.
    def visitReadStatement(self, ctx:PLCParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#WriteStatement.
    def visitWriteStatement(self, ctx:PLCParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#ExpressionStatement.
    def visitExpressionStatement(self, ctx:PLCParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#IfStatement.
    def visitIfStatement(self, ctx:PLCParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#WhileStatement.
    def visitWhileStatement(self, ctx:PLCParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#forStatement.
    def visitForStatement(self, ctx:PLCParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#fopenStatement.
    def visitFopenStatement(self, ctx:PLCParser.FopenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#fappendStatement.
    def visitFappendStatement(self, ctx:PLCParser.FappendStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#TernaryExpression.
    def visitTernaryExpression(self, ctx:PLCParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#PowerExpression.
    def visitPowerExpression(self, ctx:PLCParser.PowerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#IntExpression.
    def visitIntExpression(self, ctx:PLCParser.IntExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#AddSubConcatExpression.
    def visitAddSubConcatExpression(self, ctx:PLCParser.AddSubConcatExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#FloatExpression.
    def visitFloatExpression(self, ctx:PLCParser.FloatExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#UnaryExpression.
    def visitUnaryExpression(self, ctx:PLCParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#OrExpression.
    def visitOrExpression(self, ctx:PLCParser.OrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#ParensExpression.
    def visitParensExpression(self, ctx:PLCParser.ParensExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#MulDivModExpression.
    def visitMulDivModExpression(self, ctx:PLCParser.MulDivModExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#BoolExpression.
    def visitBoolExpression(self, ctx:PLCParser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#ComparisonExpression.
    def visitComparisonExpression(self, ctx:PLCParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#AndExpression.
    def visitAndExpression(self, ctx:PLCParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:PLCParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#charAtExpression.
    def visitCharAtExpression(self, ctx:PLCParser.CharAtExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#StringExpression.
    def visitStringExpression(self, ctx:PLCParser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#IdExpression.
    def visitIdExpression(self, ctx:PLCParser.IdExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#EqualityExpression.
    def visitEqualityExpression(self, ctx:PLCParser.EqualityExpressionContext):
        return self.visitChildren(ctx)



del PLCParser