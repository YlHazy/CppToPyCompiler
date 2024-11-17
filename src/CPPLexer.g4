lexer grammar CPPLexer;

// Literals
IntegerLiteral: ('-'? DecimalLiteral) | HexadecimalLiteral | BinaryLiteral | '0';
FloatingLiteral: '-'? (Fractionalconstant Exponentpart? Floatingsuffix? | Digitsequence Exponentpart Floatingsuffix?);
BooleanLiteral: 'true' | 'false';
PointerLiteral: 'nullptr';

// Keywords
Auto: 'auto';
Bool: 'bool';
Break: 'break';
Cin: 'cin';
Cout: 'cout';
Case: 'case';
Catch: 'catch';
Char: 'char';
Const: 'const';
Decltype: 'decltype';
Default: 'default';
Delete: 'delete';
Do: 'do';
Double: 'double';
ElseIf: 'else if';
Else: 'else';
Enum: 'enum';
EndLine: 'endl';
Explicit: 'explicit';
Export: 'export';
Extern: 'extern';
Final: 'final';
Float: 'float';
For: 'for';
Friend: 'friend';
If: 'if';
Int: 'int';
Include: '#include';
Long: 'long';
Main: 'main';
Namespace: 'namespace';
Return: 'return';
String: 'string';
Short: 'short';
Signed: 'signed';
Static: 'static';
Struct: 'struct';
Switch: 'switch';
Stack: 'stack';
Size_t: 'size_t';
Try: 'try';
Typedef: 'typedef';
Typeid_: 'typeid';
Union: 'union';
Unsigned: 'unsigned';
Using: 'using';
Void: 'void';
Vector: 'vector';
While: 'while';

// Operators
LeftParen: '(';
RightParen: ')';
LeftBrace: '{';
RightBrace: '}';
LeftBrackets: '[';
RightBrackets: ']';
Plus: '+';
Minus: '-';
Star: '*';
Div: '/';
Mod: '%';
Caret: '^';
And: '&';
Or: '|';
Tilde: '~';
Not: '!' | 'not';
Assign: '=';
Stdin: '>>';
Stdout: '<<';
Less: '<';
Greater: '>';
Equal: '==';
NotEqual: '!=';
LessEqual: '<=';
GreaterEqual: '>=';
AndAnd: '&&' | 'and';
OrOr: '||' | 'or';
PlusPlus: '++';
MinusMinus: '--';
PlusEqual: '+=';
MinusEqual: '-=';
StarEqual: '*=';
DivEqual: '/=';
Comma: ',';
Arrow: '->';
Semi: ';';
Dot: '.';
DoubleQuotation: '"';
Colon: ':';


// Const value of char and string
EscapedChar: '\\' ('n' | 't' | '\\' | '\'' | '"' | 'r' | 'b' | 'f' | 'v' | '0');

CharLiteral: '\'' (EscapedChar | ~[\r\n\\])? '\'';
StringLiteral: '"' (EscapedChar | ~[\r\n\\])* '"';

// Identifiers
Identifier: NONDIGIT (NONDIGIT | DIGIT)*;

fragment NONDIGIT: [a-zA-Z_];
fragment DIGIT: [0-9];

// Literals and fragments
DecimalLiteral: NONZERODIGIT DIGIT*;
HexadecimalLiteral: ('0x' | '0X') HEXADECIMALDIGIT+;
BinaryLiteral: ('0b' | '0B') BINARYDIGIT+;

fragment NONZERODIGIT: [1-9];
fragment HEXADECIMALDIGIT: [0-9a-fA-F];
fragment BINARYDIGIT: [01];
fragment Fractionalconstant: Digitsequence? '.' Digitsequence | Digitsequence '.';
fragment Exponentpart: ('e' | 'E') [+-]? Digitsequence;
fragment Floatingsuffix: [flFL];
fragment Digitsequence: DIGIT+;

// Whitespace and comments
Whitespace: [ \t\r\n]+ -> skip;
BlockComment: '/*' .*? '*/' -> skip;
LineComment: '//' ~[\r\n]* -> skip;
