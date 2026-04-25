grammar PLC;

/* ============================================================
    LEXER (Pravidla pro znaky a slova - pisi se VELKYMI PISMENY)
   ============================================================*/

// Bile znaky: mezery, tabulatory, odradkovani
// -> skip rika ANTLRu, at je uplne ignoruje a neposila je dal do parseru
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip; // Jednoradkový komentar
//MULTILINE_COMMENT: '/*' .*? '*/' -> skip; // Viceradkovy komentar


//Klicova slova pro datove typy
TYPE_FLOAT: 'float';
TYPE_INT: 'int';
TYPE_STRING: 'string';
TYPE_BOOL: 'bool';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
READ: 'read';
WRITE: 'write';


BOOL_LITERAL: 'true' | 'false';
STRING_LITERAL: '"'~["\r\n]*'"'; // Text mezi uvozovkami, bez uvozovek
// Jak má vypadat float: desetinne cislo s desetinnou teckou musi byt pred int, jinak by blblo rozpoznani float jako int
FLOAT_LITERAL: [0-9]+ '.' [0-9]*;
//jak ma vypadat int: cele cislo
INT_LITERAL: [0-9]+;
// Identifikator: zacina pismenem, pak mohou být pismena nebo cisla
ID: [a-zA-Z][a-zA-Z0-9]*;

/* ============================================================
    PARSER (Pravidla pro strukturu programu - pisi se malymi pismeny)
   ============================================================*/
program : statement* EOF ;

type_spec: TYPE_FLOAT | TYPE_INT | TYPE_STRING | TYPE_BOOL;

statement
    : ';'                                      # EmptyStatement
    | '{' statement* '}'                       # BlockStatement
    | type_spec ID (',' ID)* ';'               # DeclarationStatement
    | READ ID (',' ID)* ';'                    # ReadStatement
    | WRITE expression (',' expression)* ';'   # WriteStatement
    | expression ';'                           # ExpressionStatement
    | IF '(' expression ')' statement (ELSE statement)?  # IfStatement
    | WHILE '(' expression ')' statement        # WhileStatement
    ;               

expression
    : '(' expression ')'                       # ParensExpression
    | INT_LITERAL                              # IntExpression
    | FLOAT_LITERAL                            # FloatExpression
    | BOOL_LITERAL                             # BoolExpression
    | STRING_LITERAL                           # StringExpression
    | ID                                       # IdExpression
    // 2. UNARNI MINUS A LOGICKE NOT (napr. -5 nebo -a)   
    | ('-'|'!') expression                          # UnaryExpression
    // 3. NASOBENI, DELENI, MODULO (napr. a * b, a / b, a % b)
    | expression op=('*' | '/' | '%') expression  # MulDivModExpression
    // 4. SCITANI A ODCTITANI (napr. a + b, a - b)
    | expression op=('+' | '-' | '.') expression      # AddSubConcatExpression
    // 5. POROVNANI (napr. a < b, a > b)
    | expression op=('<' | '>') expression  # ComparisonExpression
    // 6. Rovnost a Nerovnost (napr. a == b, a != b)
    | expression op=('==' | '!=') expression # EqualityExpression
    // 7. LOGICKE AND (napr. a && b)
    | expression op='&&' expression              # AndExpression
    // 8. LOGICKE OR (napr. a || b)
    | expression op='||' expression              # OrExpression
    // 9. PŘIŘAZENÍ (a = 5). Úplně nejnižší priorita.
    // <assoc=right> znamená, že se to počítá zprava doleva (nejdřív se spočítá pravá strana, pak se uloží doleva)
    | <assoc=right> expression '=' expression  # AssignmentExpression
    ;