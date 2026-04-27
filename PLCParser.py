# Generated from PLC.g4 by ANTLR 4.13.2
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
        4,1,46,160,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,2,22,8,2,10,2,12,2,25,9,2,
        1,2,1,2,1,2,1,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,2,1,2,1,2,1,2,
        1,2,1,2,5,2,43,8,2,10,2,12,2,46,9,2,1,2,1,2,1,2,1,2,1,2,5,2,53,8,
        2,10,2,12,2,56,9,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,3,2,70,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,98,8,2,10,
        2,12,2,101,9,2,1,2,3,2,104,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,3,3,118,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,155,8,3,10,3,12,3,158,
        9,3,1,3,0,1,6,4,0,2,4,6,0,6,3,0,30,33,39,39,41,41,1,0,11,12,1,0,
        14,16,2,0,11,11,17,18,1,0,19,20,1,0,21,22,188,0,11,1,0,0,0,2,16,
        1,0,0,0,4,103,1,0,0,0,6,117,1,0,0,0,8,10,3,4,2,0,9,8,1,0,0,0,10,
        13,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,14,1,0,0,0,13,11,1,0,0,
        0,14,15,5,0,0,1,15,1,1,0,0,0,16,17,7,0,0,0,17,3,1,0,0,0,18,104,5,
        1,0,0,19,23,5,2,0,0,20,22,3,4,2,0,21,20,1,0,0,0,22,25,1,0,0,0,23,
        21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,104,5,3,
        0,0,27,28,3,2,1,0,28,33,5,46,0,0,29,30,5,4,0,0,30,32,5,46,0,0,31,
        29,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,
        0,35,33,1,0,0,0,36,37,5,1,0,0,37,104,1,0,0,0,38,39,5,37,0,0,39,44,
        5,46,0,0,40,41,5,4,0,0,41,43,5,46,0,0,42,40,1,0,0,0,43,46,1,0,0,
        0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,47,104,
        5,1,0,0,48,49,5,38,0,0,49,54,3,6,3,0,50,51,5,4,0,0,51,53,3,6,3,0,
        52,50,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,57,1,
        0,0,0,56,54,1,0,0,0,57,58,5,1,0,0,58,104,1,0,0,0,59,60,3,6,3,0,60,
        61,5,1,0,0,61,104,1,0,0,0,62,63,5,34,0,0,63,64,5,5,0,0,64,65,3,6,
        3,0,65,66,5,6,0,0,66,69,3,4,2,0,67,68,5,35,0,0,68,70,3,4,2,0,69,
        67,1,0,0,0,69,70,1,0,0,0,70,104,1,0,0,0,71,72,5,36,0,0,72,73,5,5,
        0,0,73,74,3,6,3,0,74,75,5,6,0,0,75,76,3,4,2,0,76,104,1,0,0,0,77,
        78,5,40,0,0,78,79,5,5,0,0,79,80,3,6,3,0,80,81,5,1,0,0,81,82,3,6,
        3,0,82,83,5,1,0,0,83,84,3,6,3,0,84,85,5,6,0,0,85,86,3,4,2,0,86,104,
        1,0,0,0,87,88,5,7,0,0,88,89,5,46,0,0,89,90,5,4,0,0,90,91,3,6,3,0,
        91,92,5,1,0,0,92,104,1,0,0,0,93,94,5,8,0,0,94,99,5,46,0,0,95,96,
        5,4,0,0,96,98,3,6,3,0,97,95,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,
        99,100,1,0,0,0,100,102,1,0,0,0,101,99,1,0,0,0,102,104,5,1,0,0,103,
        18,1,0,0,0,103,19,1,0,0,0,103,27,1,0,0,0,103,38,1,0,0,0,103,48,1,
        0,0,0,103,59,1,0,0,0,103,62,1,0,0,0,103,71,1,0,0,0,103,77,1,0,0,
        0,103,87,1,0,0,0,103,93,1,0,0,0,104,5,1,0,0,0,105,106,6,3,-1,0,106,
        107,5,5,0,0,107,108,3,6,3,0,108,109,5,6,0,0,109,118,1,0,0,0,110,
        118,5,45,0,0,111,118,5,44,0,0,112,118,5,42,0,0,113,118,5,43,0,0,
        114,118,5,46,0,0,115,116,7,1,0,0,116,118,3,6,3,10,117,105,1,0,0,
        0,117,110,1,0,0,0,117,111,1,0,0,0,117,112,1,0,0,0,117,113,1,0,0,
        0,117,114,1,0,0,0,117,115,1,0,0,0,118,156,1,0,0,0,119,120,10,9,0,
        0,120,121,5,13,0,0,121,155,3,6,3,10,122,123,10,8,0,0,123,124,7,2,
        0,0,124,155,3,6,3,9,125,126,10,7,0,0,126,127,7,3,0,0,127,155,3,6,
        3,8,128,129,10,6,0,0,129,130,7,4,0,0,130,155,3,6,3,7,131,132,10,
        5,0,0,132,133,7,5,0,0,133,155,3,6,3,6,134,135,10,4,0,0,135,136,5,
        23,0,0,136,155,3,6,3,5,137,138,10,3,0,0,138,139,5,24,0,0,139,155,
        3,6,3,4,140,141,10,2,0,0,141,142,5,25,0,0,142,143,3,6,3,0,143,144,
        5,26,0,0,144,145,3,6,3,3,145,155,1,0,0,0,146,147,10,1,0,0,147,148,
        5,27,0,0,148,155,3,6,3,1,149,150,10,11,0,0,150,151,5,9,0,0,151,152,
        3,6,3,0,152,153,5,10,0,0,153,155,1,0,0,0,154,119,1,0,0,0,154,122,
        1,0,0,0,154,125,1,0,0,0,154,128,1,0,0,0,154,131,1,0,0,0,154,134,
        1,0,0,0,154,137,1,0,0,0,154,140,1,0,0,0,154,146,1,0,0,0,154,149,
        1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,7,1,
        0,0,0,158,156,1,0,0,0,11,11,23,33,44,54,69,99,103,117,154,156
    ]

class PLCParser ( Parser ):

    grammarFileName = "PLC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "','", "'('", "')'", 
                     "'fopen'", "'fappend'", "'['", "']'", "'-'", "'!'", 
                     "'**'", "'*'", "'/'", "'%'", "'+'", "'.'", "'<'", "'>'", 
                     "'=='", "'!='", "'&&'", "'||'", "'?'", "':'", "'='", 
                     "<INVALID>", "<INVALID>", "'float'", "'int'", "'string'", 
                     "'bool'", "'if'", "'else'", "'while'", "'read'", "'write'", 
                     "'file'", "'for'", "'char'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS", "COMMENT", "TYPE_FLOAT", "TYPE_INT", "TYPE_STRING", 
                      "TYPE_BOOL", "IF", "ELSE", "WHILE", "READ", "WRITE", 
                      "FILE", "FOR", "CHAR", "BOOL_LITERAL", "STRING_LITERAL", 
                      "FLOAT_LITERAL", "INT_LITERAL", "ID" ]

    RULE_program = 0
    RULE_type_spec = 1
    RULE_statement = 2
    RULE_expression = 3

    ruleNames =  [ "program", "type_spec", "statement", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    WS=28
    COMMENT=29
    TYPE_FLOAT=30
    TYPE_INT=31
    TYPE_STRING=32
    TYPE_BOOL=33
    IF=34
    ELSE=35
    WHILE=36
    READ=37
    WRITE=38
    FILE=39
    FOR=40
    CHAR=41
    BOOL_LITERAL=42
    STRING_LITERAL=43
    FLOAT_LITERAL=44
    INT_LITERAL=45
    ID=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PLCParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLCParser.StatementContext,i)


        def getRuleIndex(self):
            return PLCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PLCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140702054881702) != 0):
                self.state = 8
                self.statement()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.match(PLCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_FLOAT(self):
            return self.getToken(PLCParser.TYPE_FLOAT, 0)

        def TYPE_INT(self):
            return self.getToken(PLCParser.TYPE_INT, 0)

        def TYPE_STRING(self):
            return self.getToken(PLCParser.TYPE_STRING, 0)

        def TYPE_BOOL(self):
            return self.getToken(PLCParser.TYPE_BOOL, 0)

        def FILE(self):
            return self.getToken(PLCParser.FILE, 0)

        def CHAR(self):
            return self.getToken(PLCParser.CHAR, 0)

        def getRuleIndex(self):
            return PLCParser.RULE_type_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_spec" ):
                listener.enterType_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_spec" ):
                listener.exitType_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_spec" ):
                return visitor.visitType_spec(self)
            else:
                return visitor.visitChildren(self)




    def type_spec(self):

        localctx = PLCParser.Type_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2764885196800) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLCParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(PLCParser.IF, 0)
        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLCParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(PLCParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)


    class ReadStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(PLCParser.READ, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PLCParser.ID)
            else:
                return self.getToken(PLCParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStatement" ):
                listener.enterReadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStatement" ):
                listener.exitReadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStatement" ):
                return visitor.visitReadStatement(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)


    class FopenStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PLCParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFopenStatement" ):
                listener.enterFopenStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFopenStatement" ):
                listener.exitFopenStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFopenStatement" ):
                return visitor.visitFopenStatement(self)
            else:
                return visitor.visitChildren(self)


    class EmptyStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStatement" ):
                return visitor.visitEmptyStatement(self)
            else:
                return visitor.visitChildren(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(PLCParser.WRITE, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStatement" ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStatement" ):
                listener.exitWriteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStatement" ):
                return visitor.visitWriteStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(PLCParser.FOR, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)

        def statement(self):
            return self.getTypedRuleContext(PLCParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)


    class BlockStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLCParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(PLCParser.WHILE, 0)
        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(PLCParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)


    class FappendStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PLCParser.ID, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFappendStatement" ):
                listener.enterFappendStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFappendStatement" ):
                listener.exitFappendStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFappendStatement" ):
                return visitor.visitFappendStatement(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_spec(self):
            return self.getTypedRuleContext(PLCParser.Type_specContext,0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PLCParser.ID)
            else:
                return self.getToken(PLCParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatement" ):
                listener.enterDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatement" ):
                listener.exitDeclarationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationStatement" ):
                return visitor.visitDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = PLCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = PLCParser.EmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(PLCParser.T__0)
                pass
            elif token in [2]:
                localctx = PLCParser.BlockStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(PLCParser.T__1)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140702054881702) != 0):
                    self.state = 20
                    self.statement()
                    self.state = 25
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 26
                self.match(PLCParser.T__2)
                pass
            elif token in [30, 31, 32, 33, 39, 41]:
                localctx = PLCParser.DeclarationStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.type_spec()
                self.state = 28
                self.match(PLCParser.ID)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 29
                    self.match(PLCParser.T__3)
                    self.state = 30
                    self.match(PLCParser.ID)
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 36
                self.match(PLCParser.T__0)
                pass
            elif token in [37]:
                localctx = PLCParser.ReadStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.match(PLCParser.READ)
                self.state = 39
                self.match(PLCParser.ID)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 40
                    self.match(PLCParser.T__3)
                    self.state = 41
                    self.match(PLCParser.ID)
                    self.state = 46
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 47
                self.match(PLCParser.T__0)
                pass
            elif token in [38]:
                localctx = PLCParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.match(PLCParser.WRITE)
                self.state = 49
                self.expression(0)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 50
                    self.match(PLCParser.T__3)
                    self.state = 51
                    self.expression(0)
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 57
                self.match(PLCParser.T__0)
                pass
            elif token in [5, 11, 12, 42, 43, 44, 45, 46]:
                localctx = PLCParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 59
                self.expression(0)
                self.state = 60
                self.match(PLCParser.T__0)
                pass
            elif token in [34]:
                localctx = PLCParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 62
                self.match(PLCParser.IF)
                self.state = 63
                self.match(PLCParser.T__4)
                self.state = 64
                self.expression(0)
                self.state = 65
                self.match(PLCParser.T__5)
                self.state = 66
                self.statement()
                self.state = 69
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 67
                    self.match(PLCParser.ELSE)
                    self.state = 68
                    self.statement()


                pass
            elif token in [36]:
                localctx = PLCParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 71
                self.match(PLCParser.WHILE)
                self.state = 72
                self.match(PLCParser.T__4)
                self.state = 73
                self.expression(0)
                self.state = 74
                self.match(PLCParser.T__5)
                self.state = 75
                self.statement()
                pass
            elif token in [40]:
                localctx = PLCParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 77
                self.match(PLCParser.FOR)
                self.state = 78
                self.match(PLCParser.T__4)
                self.state = 79
                self.expression(0)
                self.state = 80
                self.match(PLCParser.T__0)
                self.state = 81
                self.expression(0)
                self.state = 82
                self.match(PLCParser.T__0)
                self.state = 83
                self.expression(0)
                self.state = 84
                self.match(PLCParser.T__5)
                self.state = 85
                self.statement()
                pass
            elif token in [7]:
                localctx = PLCParser.FopenStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 87
                self.match(PLCParser.T__6)
                self.state = 88
                self.match(PLCParser.ID)
                self.state = 89
                self.match(PLCParser.T__3)
                self.state = 90
                self.expression(0)
                self.state = 91
                self.match(PLCParser.T__0)
                pass
            elif token in [8]:
                localctx = PLCParser.FappendStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 93
                self.match(PLCParser.T__7)
                self.state = 94
                self.match(PLCParser.ID)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 95
                    self.match(PLCParser.T__3)
                    self.state = 96
                    self.expression(0)
                    self.state = 101
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 102
                self.match(PLCParser.T__0)
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLCParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernaryExpression" ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernaryExpression" ):
                listener.exitTernaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernaryExpression" ):
                return visitor.visitTernaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class PowerExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerExpression" ):
                listener.enterPowerExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerExpression" ):
                listener.exitPowerExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerExpression" ):
                return visitor.visitPowerExpression(self)
            else:
                return visitor.visitChildren(self)


    class IntExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_LITERAL(self):
            return self.getToken(PLCParser.INT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpression" ):
                listener.enterIntExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpression" ):
                listener.exitIntExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpression" ):
                return visitor.visitIntExpression(self)
            else:
                return visitor.visitChildren(self)


    class AddSubConcatExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubConcatExpression" ):
                listener.enterAddSubConcatExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubConcatExpression" ):
                listener.exitAddSubConcatExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubConcatExpression" ):
                return visitor.visitAddSubConcatExpression(self)
            else:
                return visitor.visitChildren(self)


    class FloatExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LITERAL(self):
            return self.getToken(PLCParser.FLOAT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatExpression" ):
                listener.enterFloatExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatExpression" ):
                listener.exitFloatExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpression" ):
                return visitor.visitFloatExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpression" ):
                listener.enterOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpression" ):
                listener.exitOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpression" ):
                return visitor.visitOrExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParensExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PLCParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpression" ):
                listener.enterParensExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpression" ):
                listener.exitParensExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpression" ):
                return visitor.visitParensExpression(self)
            else:
                return visitor.visitChildren(self)


    class MulDivModExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivModExpression" ):
                listener.enterMulDivModExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivModExpression" ):
                listener.exitMulDivModExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivModExpression" ):
                return visitor.visitMulDivModExpression(self)
            else:
                return visitor.visitChildren(self)


    class BoolExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_LITERAL(self):
            return self.getToken(PLCParser.BOOL_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpression" ):
                listener.enterBoolExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpression" ):
                listener.exitBoolExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpression" ):
                return visitor.visitBoolExpression(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpression" ):
                listener.enterComparisonExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpression" ):
                listener.exitComparisonExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpression" ):
                return visitor.visitComparisonExpression(self)
            else:
                return visitor.visitChildren(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpression" ):
                listener.enterAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpression" ):
                listener.exitAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpression" ):
                return visitor.visitAndExpression(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpression" ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpression" ):
                listener.exitAssignmentExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpression" ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)


    class CharAtExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharAtExpression" ):
                listener.enterCharAtExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharAtExpression" ):
                listener.exitCharAtExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharAtExpression" ):
                return visitor.visitCharAtExpression(self)
            else:
                return visitor.visitChildren(self)


    class StringExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(PLCParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpression" ):
                listener.enterStringExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpression" ):
                listener.exitStringExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpression" ):
                return visitor.visitStringExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PLCParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpression" ):
                listener.enterIdExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpression" ):
                listener.exitIdExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpression" ):
                return visitor.visitIdExpression(self)
            else:
                return visitor.visitChildren(self)


    class EqualityExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLCParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLCParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PLCParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = PLCParser.ParensExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 106
                self.match(PLCParser.T__4)
                self.state = 107
                self.expression(0)
                self.state = 108
                self.match(PLCParser.T__5)
                pass
            elif token in [45]:
                localctx = PLCParser.IntExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(PLCParser.INT_LITERAL)
                pass
            elif token in [44]:
                localctx = PLCParser.FloatExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(PLCParser.FLOAT_LITERAL)
                pass
            elif token in [42]:
                localctx = PLCParser.BoolExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.match(PLCParser.BOOL_LITERAL)
                pass
            elif token in [43]:
                localctx = PLCParser.StringExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(PLCParser.STRING_LITERAL)
                pass
            elif token in [46]:
                localctx = PLCParser.IdExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114
                self.match(PLCParser.ID)
                pass
            elif token in [11, 12]:
                localctx = PLCParser.UnaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 116
                self.expression(10)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 154
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = PLCParser.PowerExpressionContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 119
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 120
                        localctx.op = self.match(PLCParser.T__12)
                        self.state = 121
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = PLCParser.MulDivModExpressionContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 122
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 123
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 124
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = PLCParser.AddSubConcatExpressionContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 125
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 126
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 395264) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = PLCParser.ComparisonExpressionContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 128
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 129
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 130
                        self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = PLCParser.EqualityExpressionContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 131
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 132
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 133
                        self.expression(6)
                        pass

                    elif la_ == 6:
                        localctx = PLCParser.AndExpressionContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 134
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 135
                        localctx.op = self.match(PLCParser.T__22)
                        self.state = 136
                        self.expression(5)
                        pass

                    elif la_ == 7:
                        localctx = PLCParser.OrExpressionContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 137
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 138
                        localctx.op = self.match(PLCParser.T__23)
                        self.state = 139
                        self.expression(4)
                        pass

                    elif la_ == 8:
                        localctx = PLCParser.TernaryExpressionContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 140
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 141
                        self.match(PLCParser.T__24)
                        self.state = 142
                        self.expression(0)
                        self.state = 143
                        self.match(PLCParser.T__25)
                        self.state = 144
                        self.expression(3)
                        pass

                    elif la_ == 9:
                        localctx = PLCParser.AssignmentExpressionContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 146
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 147
                        self.match(PLCParser.T__26)
                        self.state = 148
                        self.expression(1)
                        pass

                    elif la_ == 10:
                        localctx = PLCParser.CharAtExpressionContext(self, PLCParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 149
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 150
                        self.match(PLCParser.T__8)
                        self.state = 151
                        self.expression(0)
                        self.state = 152
                        self.match(PLCParser.T__9)
                        pass

             
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 11)
         




