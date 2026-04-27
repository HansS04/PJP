// Generated from /home/slivka/Desktop/SCHOOL/tretak/PJP/PROJECT/PLC.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PLCParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, WS=28, COMMENT=29, TYPE_FLOAT=30, TYPE_INT=31, 
		TYPE_STRING=32, TYPE_BOOL=33, IF=34, ELSE=35, WHILE=36, READ=37, WRITE=38, 
		FILE=39, FOR=40, CHAR=41, BOOL_LITERAL=42, STRING_LITERAL=43, FLOAT_LITERAL=44, 
		INT_LITERAL=45, ID=46;
	public static final int
		RULE_program = 0, RULE_type_spec = 1, RULE_statement = 2, RULE_expression = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "type_spec", "statement", "expression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'{'", "'}'", "','", "'('", "')'", "'fopen'", "'fappend'", 
			"'['", "']'", "'-'", "'!'", "'**'", "'*'", "'/'", "'%'", "'+'", "'.'", 
			"'<'", "'>'", "'=='", "'!='", "'&&'", "'||'", "'?'", "':'", "'='", null, 
			null, "'float'", "'int'", "'string'", "'bool'", "'if'", "'else'", "'while'", 
			"'read'", "'write'", "'file'", "'for'", "'char'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "WS", "COMMENT", "TYPE_FLOAT", "TYPE_INT", "TYPE_STRING", 
			"TYPE_BOOL", "IF", "ELSE", "WHILE", "READ", "WRITE", "FILE", "FOR", "CHAR", 
			"BOOL_LITERAL", "STRING_LITERAL", "FLOAT_LITERAL", "INT_LITERAL", "ID"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "PLC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PLCParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(PLCParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(11);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 140702054881702L) != 0)) {
				{
				{
				setState(8);
				statement();
				}
				}
				setState(13);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(14);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Type_specContext extends ParserRuleContext {
		public TerminalNode TYPE_FLOAT() { return getToken(PLCParser.TYPE_FLOAT, 0); }
		public TerminalNode TYPE_INT() { return getToken(PLCParser.TYPE_INT, 0); }
		public TerminalNode TYPE_STRING() { return getToken(PLCParser.TYPE_STRING, 0); }
		public TerminalNode TYPE_BOOL() { return getToken(PLCParser.TYPE_BOOL, 0); }
		public TerminalNode FILE() { return getToken(PLCParser.FILE, 0); }
		public TerminalNode CHAR() { return getToken(PLCParser.CHAR, 0); }
		public Type_specContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_spec; }
	}

	public final Type_specContext type_spec() throws RecognitionException {
		Type_specContext _localctx = new Type_specContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_type_spec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2764885196800L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends StatementContext {
		public TerminalNode IF() { return getToken(PLCParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(PLCParser.ELSE, 0); }
		public IfStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ReadStatementContext extends StatementContext {
		public TerminalNode READ() { return getToken(PLCParser.READ, 0); }
		public List<TerminalNode> ID() { return getTokens(PLCParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PLCParser.ID, i);
		}
		public ReadStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionStatementContext extends StatementContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FopenStatementContext extends StatementContext {
		public TerminalNode ID() { return getToken(PLCParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public FopenStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class EmptyStatementContext extends StatementContext {
		public EmptyStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WriteStatementContext extends StatementContext {
		public TerminalNode WRITE() { return getToken(PLCParser.WRITE, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public WriteStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ForStatementContext extends StatementContext {
		public TerminalNode FOR() { return getToken(PLCParser.FOR, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ForStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BlockStatementContext extends StatementContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatementContext extends StatementContext {
		public TerminalNode WHILE() { return getToken(PLCParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public WhileStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FappendStatementContext extends StatementContext {
		public TerminalNode ID() { return getToken(PLCParser.ID, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public FappendStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationStatementContext extends StatementContext {
		public Type_specContext type_spec() {
			return getRuleContext(Type_specContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(PLCParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PLCParser.ID, i);
		}
		public DeclarationStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		int _la;
		try {
			setState(103);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				_localctx = new EmptyStatementContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(18);
				match(T__0);
				}
				break;
			case T__1:
				_localctx = new BlockStatementContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(19);
				match(T__1);
				setState(23);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 140702054881702L) != 0)) {
					{
					{
					setState(20);
					statement();
					}
					}
					setState(25);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(26);
				match(T__2);
				}
				break;
			case TYPE_FLOAT:
			case TYPE_INT:
			case TYPE_STRING:
			case TYPE_BOOL:
			case FILE:
			case CHAR:
				_localctx = new DeclarationStatementContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(27);
				type_spec();
				setState(28);
				match(ID);
				setState(33);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(29);
					match(T__3);
					setState(30);
					match(ID);
					}
					}
					setState(35);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(36);
				match(T__0);
				}
				break;
			case READ:
				_localctx = new ReadStatementContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(38);
				match(READ);
				setState(39);
				match(ID);
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(40);
					match(T__3);
					setState(41);
					match(ID);
					}
					}
					setState(46);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(47);
				match(T__0);
				}
				break;
			case WRITE:
				_localctx = new WriteStatementContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(48);
				match(WRITE);
				setState(49);
				expression(0);
				setState(54);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(50);
					match(T__3);
					setState(51);
					expression(0);
					}
					}
					setState(56);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(57);
				match(T__0);
				}
				break;
			case T__4:
			case T__10:
			case T__11:
			case BOOL_LITERAL:
			case STRING_LITERAL:
			case FLOAT_LITERAL:
			case INT_LITERAL:
			case ID:
				_localctx = new ExpressionStatementContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(59);
				expression(0);
				setState(60);
				match(T__0);
				}
				break;
			case IF:
				_localctx = new IfStatementContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(62);
				match(IF);
				setState(63);
				match(T__4);
				setState(64);
				expression(0);
				setState(65);
				match(T__5);
				setState(66);
				statement();
				setState(69);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(67);
					match(ELSE);
					setState(68);
					statement();
					}
					break;
				}
				}
				break;
			case WHILE:
				_localctx = new WhileStatementContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(71);
				match(WHILE);
				setState(72);
				match(T__4);
				setState(73);
				expression(0);
				setState(74);
				match(T__5);
				setState(75);
				statement();
				}
				break;
			case FOR:
				_localctx = new ForStatementContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(77);
				match(FOR);
				setState(78);
				match(T__4);
				setState(79);
				expression(0);
				setState(80);
				match(T__0);
				setState(81);
				expression(0);
				setState(82);
				match(T__0);
				setState(83);
				expression(0);
				setState(84);
				match(T__5);
				setState(85);
				statement();
				}
				break;
			case T__6:
				_localctx = new FopenStatementContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(87);
				match(T__6);
				setState(88);
				match(ID);
				setState(89);
				match(T__3);
				setState(90);
				expression(0);
				setState(91);
				match(T__0);
				}
				break;
			case T__7:
				_localctx = new FappendStatementContext(_localctx);
				enterOuterAlt(_localctx, 11);
				{
				setState(93);
				match(T__7);
				setState(94);
				match(ID);
				setState(99);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(95);
					match(T__3);
					setState(96);
					expression(0);
					}
					}
					setState(101);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(102);
				match(T__0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TernaryExpressionContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TernaryExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PowerExpressionContext extends ExpressionContext {
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public PowerExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntExpressionContext extends ExpressionContext {
		public TerminalNode INT_LITERAL() { return getToken(PLCParser.INT_LITERAL, 0); }
		public IntExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddSubConcatExpressionContext extends ExpressionContext {
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public AddSubConcatExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FloatExpressionContext extends ExpressionContext {
		public TerminalNode FLOAT_LITERAL() { return getToken(PLCParser.FLOAT_LITERAL, 0); }
		public FloatExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UnaryExpressionContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public UnaryExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OrExpressionContext extends ExpressionContext {
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public OrExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParensExpressionContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ParensExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulDivModExpressionContext extends ExpressionContext {
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public MulDivModExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BoolExpressionContext extends ExpressionContext {
		public TerminalNode BOOL_LITERAL() { return getToken(PLCParser.BOOL_LITERAL, 0); }
		public BoolExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonExpressionContext extends ExpressionContext {
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ComparisonExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AndExpressionContext extends ExpressionContext {
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public AndExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentExpressionContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public AssignmentExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CharAtExpressionContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public CharAtExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringExpressionContext extends ExpressionContext {
		public TerminalNode STRING_LITERAL() { return getToken(PLCParser.STRING_LITERAL, 0); }
		public StringExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdExpressionContext extends ExpressionContext {
		public TerminalNode ID() { return getToken(PLCParser.ID, 0); }
		public IdExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class EqualityExpressionContext extends ExpressionContext {
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public EqualityExpressionContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
				{
				_localctx = new ParensExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(106);
				match(T__4);
				setState(107);
				expression(0);
				setState(108);
				match(T__5);
				}
				break;
			case INT_LITERAL:
				{
				_localctx = new IntExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(110);
				match(INT_LITERAL);
				}
				break;
			case FLOAT_LITERAL:
				{
				_localctx = new FloatExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(111);
				match(FLOAT_LITERAL);
				}
				break;
			case BOOL_LITERAL:
				{
				_localctx = new BoolExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(112);
				match(BOOL_LITERAL);
				}
				break;
			case STRING_LITERAL:
				{
				_localctx = new StringExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(113);
				match(STRING_LITERAL);
				}
				break;
			case ID:
				{
				_localctx = new IdExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(114);
				match(ID);
				}
				break;
			case T__10:
			case T__11:
				{
				_localctx = new UnaryExpressionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(115);
				_la = _input.LA(1);
				if ( !(_la==T__10 || _la==T__11) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(116);
				expression(10);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(156);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(154);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
					case 1:
						{
						_localctx = new PowerExpressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(119);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(120);
						((PowerExpressionContext)_localctx).op = match(T__12);
						setState(121);
						expression(10);
						}
						break;
					case 2:
						{
						_localctx = new MulDivModExpressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(122);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(123);
						((MulDivModExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 114688L) != 0)) ) {
							((MulDivModExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(124);
						expression(9);
						}
						break;
					case 3:
						{
						_localctx = new AddSubConcatExpressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(125);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(126);
						((AddSubConcatExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 395264L) != 0)) ) {
							((AddSubConcatExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(127);
						expression(8);
						}
						break;
					case 4:
						{
						_localctx = new ComparisonExpressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(128);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(129);
						((ComparisonExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__18 || _la==T__19) ) {
							((ComparisonExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(130);
						expression(7);
						}
						break;
					case 5:
						{
						_localctx = new EqualityExpressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(131);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(132);
						((EqualityExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__20 || _la==T__21) ) {
							((EqualityExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(133);
						expression(6);
						}
						break;
					case 6:
						{
						_localctx = new AndExpressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(134);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(135);
						((AndExpressionContext)_localctx).op = match(T__22);
						setState(136);
						expression(5);
						}
						break;
					case 7:
						{
						_localctx = new OrExpressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(137);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(138);
						((OrExpressionContext)_localctx).op = match(T__23);
						setState(139);
						expression(4);
						}
						break;
					case 8:
						{
						_localctx = new TernaryExpressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(140);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(141);
						match(T__24);
						setState(142);
						expression(0);
						setState(143);
						match(T__25);
						setState(144);
						expression(3);
						}
						break;
					case 9:
						{
						_localctx = new AssignmentExpressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(146);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(147);
						match(T__26);
						setState(148);
						expression(1);
						}
						break;
					case 10:
						{
						_localctx = new CharAtExpressionContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(149);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(150);
						match(T__8);
						setState(151);
						expression(0);
						setState(152);
						match(T__9);
						}
						break;
					}
					} 
				}
				setState(158);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 3:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 9);
		case 1:
			return precpred(_ctx, 8);
		case 2:
			return precpred(_ctx, 7);
		case 3:
			return precpred(_ctx, 6);
		case 4:
			return precpred(_ctx, 5);
		case 5:
			return precpred(_ctx, 4);
		case 6:
			return precpred(_ctx, 3);
		case 7:
			return precpred(_ctx, 2);
		case 8:
			return precpred(_ctx, 1);
		case 9:
			return precpred(_ctx, 11);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001.\u00a0\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0005\u0000\n\b"+
		"\u0000\n\u0000\f\u0000\r\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002\u0016\b\u0002\n"+
		"\u0002\f\u0002\u0019\t\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0005\u0002 \b\u0002\n\u0002\f\u0002#\t\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005"+
		"\u0002+\b\u0002\n\u0002\f\u0002.\t\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0005\u00025\b\u0002\n\u0002\f\u00028\t"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0003\u0002F\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002b\b"+
		"\u0002\n\u0002\f\u0002e\t\u0002\u0001\u0002\u0003\u0002h\b\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003"+
		"\u0003v\b\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0005\u0003\u009b\b\u0003\n\u0003\f\u0003\u009e\t\u0003\u0001\u0003"+
		"\u0000\u0001\u0006\u0004\u0000\u0002\u0004\u0006\u0000\u0006\u0003\u0000"+
		"\u001e!\'\'))\u0001\u0000\u000b\f\u0001\u0000\u000e\u0010\u0002\u0000"+
		"\u000b\u000b\u0011\u0012\u0001\u0000\u0013\u0014\u0001\u0000\u0015\u0016"+
		"\u00bc\u0000\u000b\u0001\u0000\u0000\u0000\u0002\u0010\u0001\u0000\u0000"+
		"\u0000\u0004g\u0001\u0000\u0000\u0000\u0006u\u0001\u0000\u0000\u0000\b"+
		"\n\u0003\u0004\u0002\u0000\t\b\u0001\u0000\u0000\u0000\n\r\u0001\u0000"+
		"\u0000\u0000\u000b\t\u0001\u0000\u0000\u0000\u000b\f\u0001\u0000\u0000"+
		"\u0000\f\u000e\u0001\u0000\u0000\u0000\r\u000b\u0001\u0000\u0000\u0000"+
		"\u000e\u000f\u0005\u0000\u0000\u0001\u000f\u0001\u0001\u0000\u0000\u0000"+
		"\u0010\u0011\u0007\u0000\u0000\u0000\u0011\u0003\u0001\u0000\u0000\u0000"+
		"\u0012h\u0005\u0001\u0000\u0000\u0013\u0017\u0005\u0002\u0000\u0000\u0014"+
		"\u0016\u0003\u0004\u0002\u0000\u0015\u0014\u0001\u0000\u0000\u0000\u0016"+
		"\u0019\u0001\u0000\u0000\u0000\u0017\u0015\u0001\u0000\u0000\u0000\u0017"+
		"\u0018\u0001\u0000\u0000\u0000\u0018\u001a\u0001\u0000\u0000\u0000\u0019"+
		"\u0017\u0001\u0000\u0000\u0000\u001ah\u0005\u0003\u0000\u0000\u001b\u001c"+
		"\u0003\u0002\u0001\u0000\u001c!\u0005.\u0000\u0000\u001d\u001e\u0005\u0004"+
		"\u0000\u0000\u001e \u0005.\u0000\u0000\u001f\u001d\u0001\u0000\u0000\u0000"+
		" #\u0001\u0000\u0000\u0000!\u001f\u0001\u0000\u0000\u0000!\"\u0001\u0000"+
		"\u0000\u0000\"$\u0001\u0000\u0000\u0000#!\u0001\u0000\u0000\u0000$%\u0005"+
		"\u0001\u0000\u0000%h\u0001\u0000\u0000\u0000&\'\u0005%\u0000\u0000\',"+
		"\u0005.\u0000\u0000()\u0005\u0004\u0000\u0000)+\u0005.\u0000\u0000*(\u0001"+
		"\u0000\u0000\u0000+.\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000\u0000"+
		",-\u0001\u0000\u0000\u0000-/\u0001\u0000\u0000\u0000.,\u0001\u0000\u0000"+
		"\u0000/h\u0005\u0001\u0000\u000001\u0005&\u0000\u000016\u0003\u0006\u0003"+
		"\u000023\u0005\u0004\u0000\u000035\u0003\u0006\u0003\u000042\u0001\u0000"+
		"\u0000\u000058\u0001\u0000\u0000\u000064\u0001\u0000\u0000\u000067\u0001"+
		"\u0000\u0000\u000079\u0001\u0000\u0000\u000086\u0001\u0000\u0000\u0000"+
		"9:\u0005\u0001\u0000\u0000:h\u0001\u0000\u0000\u0000;<\u0003\u0006\u0003"+
		"\u0000<=\u0005\u0001\u0000\u0000=h\u0001\u0000\u0000\u0000>?\u0005\"\u0000"+
		"\u0000?@\u0005\u0005\u0000\u0000@A\u0003\u0006\u0003\u0000AB\u0005\u0006"+
		"\u0000\u0000BE\u0003\u0004\u0002\u0000CD\u0005#\u0000\u0000DF\u0003\u0004"+
		"\u0002\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000Fh\u0001"+
		"\u0000\u0000\u0000GH\u0005$\u0000\u0000HI\u0005\u0005\u0000\u0000IJ\u0003"+
		"\u0006\u0003\u0000JK\u0005\u0006\u0000\u0000KL\u0003\u0004\u0002\u0000"+
		"Lh\u0001\u0000\u0000\u0000MN\u0005(\u0000\u0000NO\u0005\u0005\u0000\u0000"+
		"OP\u0003\u0006\u0003\u0000PQ\u0005\u0001\u0000\u0000QR\u0003\u0006\u0003"+
		"\u0000RS\u0005\u0001\u0000\u0000ST\u0003\u0006\u0003\u0000TU\u0005\u0006"+
		"\u0000\u0000UV\u0003\u0004\u0002\u0000Vh\u0001\u0000\u0000\u0000WX\u0005"+
		"\u0007\u0000\u0000XY\u0005.\u0000\u0000YZ\u0005\u0004\u0000\u0000Z[\u0003"+
		"\u0006\u0003\u0000[\\\u0005\u0001\u0000\u0000\\h\u0001\u0000\u0000\u0000"+
		"]^\u0005\b\u0000\u0000^c\u0005.\u0000\u0000_`\u0005\u0004\u0000\u0000"+
		"`b\u0003\u0006\u0003\u0000a_\u0001\u0000\u0000\u0000be\u0001\u0000\u0000"+
		"\u0000ca\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000df\u0001\u0000"+
		"\u0000\u0000ec\u0001\u0000\u0000\u0000fh\u0005\u0001\u0000\u0000g\u0012"+
		"\u0001\u0000\u0000\u0000g\u0013\u0001\u0000\u0000\u0000g\u001b\u0001\u0000"+
		"\u0000\u0000g&\u0001\u0000\u0000\u0000g0\u0001\u0000\u0000\u0000g;\u0001"+
		"\u0000\u0000\u0000g>\u0001\u0000\u0000\u0000gG\u0001\u0000\u0000\u0000"+
		"gM\u0001\u0000\u0000\u0000gW\u0001\u0000\u0000\u0000g]\u0001\u0000\u0000"+
		"\u0000h\u0005\u0001\u0000\u0000\u0000ij\u0006\u0003\uffff\uffff\u0000"+
		"jk\u0005\u0005\u0000\u0000kl\u0003\u0006\u0003\u0000lm\u0005\u0006\u0000"+
		"\u0000mv\u0001\u0000\u0000\u0000nv\u0005-\u0000\u0000ov\u0005,\u0000\u0000"+
		"pv\u0005*\u0000\u0000qv\u0005+\u0000\u0000rv\u0005.\u0000\u0000st\u0007"+
		"\u0001\u0000\u0000tv\u0003\u0006\u0003\nui\u0001\u0000\u0000\u0000un\u0001"+
		"\u0000\u0000\u0000uo\u0001\u0000\u0000\u0000up\u0001\u0000\u0000\u0000"+
		"uq\u0001\u0000\u0000\u0000ur\u0001\u0000\u0000\u0000us\u0001\u0000\u0000"+
		"\u0000v\u009c\u0001\u0000\u0000\u0000wx\n\t\u0000\u0000xy\u0005\r\u0000"+
		"\u0000y\u009b\u0003\u0006\u0003\nz{\n\b\u0000\u0000{|\u0007\u0002\u0000"+
		"\u0000|\u009b\u0003\u0006\u0003\t}~\n\u0007\u0000\u0000~\u007f\u0007\u0003"+
		"\u0000\u0000\u007f\u009b\u0003\u0006\u0003\b\u0080\u0081\n\u0006\u0000"+
		"\u0000\u0081\u0082\u0007\u0004\u0000\u0000\u0082\u009b\u0003\u0006\u0003"+
		"\u0007\u0083\u0084\n\u0005\u0000\u0000\u0084\u0085\u0007\u0005\u0000\u0000"+
		"\u0085\u009b\u0003\u0006\u0003\u0006\u0086\u0087\n\u0004\u0000\u0000\u0087"+
		"\u0088\u0005\u0017\u0000\u0000\u0088\u009b\u0003\u0006\u0003\u0005\u0089"+
		"\u008a\n\u0003\u0000\u0000\u008a\u008b\u0005\u0018\u0000\u0000\u008b\u009b"+
		"\u0003\u0006\u0003\u0004\u008c\u008d\n\u0002\u0000\u0000\u008d\u008e\u0005"+
		"\u0019\u0000\u0000\u008e\u008f\u0003\u0006\u0003\u0000\u008f\u0090\u0005"+
		"\u001a\u0000\u0000\u0090\u0091\u0003\u0006\u0003\u0003\u0091\u009b\u0001"+
		"\u0000\u0000\u0000\u0092\u0093\n\u0001\u0000\u0000\u0093\u0094\u0005\u001b"+
		"\u0000\u0000\u0094\u009b\u0003\u0006\u0003\u0001\u0095\u0096\n\u000b\u0000"+
		"\u0000\u0096\u0097\u0005\t\u0000\u0000\u0097\u0098\u0003\u0006\u0003\u0000"+
		"\u0098\u0099\u0005\n\u0000\u0000\u0099\u009b\u0001\u0000\u0000\u0000\u009a"+
		"w\u0001\u0000\u0000\u0000\u009az\u0001\u0000\u0000\u0000\u009a}\u0001"+
		"\u0000\u0000\u0000\u009a\u0080\u0001\u0000\u0000\u0000\u009a\u0083\u0001"+
		"\u0000\u0000\u0000\u009a\u0086\u0001\u0000\u0000\u0000\u009a\u0089\u0001"+
		"\u0000\u0000\u0000\u009a\u008c\u0001\u0000\u0000\u0000\u009a\u0092\u0001"+
		"\u0000\u0000\u0000\u009a\u0095\u0001\u0000\u0000\u0000\u009b\u009e\u0001"+
		"\u0000\u0000\u0000\u009c\u009a\u0001\u0000\u0000\u0000\u009c\u009d\u0001"+
		"\u0000\u0000\u0000\u009d\u0007\u0001\u0000\u0000\u0000\u009e\u009c\u0001"+
		"\u0000\u0000\u0000\u000b\u000b\u0017!,6Ecgu\u009a\u009c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}