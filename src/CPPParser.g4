parser grammar CPPParser;

options {
    tokenVocab=CPPLexer; // 引用词法分析器 CPPLexer
}

// Start rule
program: (preprocessorDirective | declaration)* EOF;

// Preprocessor directives
preprocessorDirective: includeDirective | usingDirective;

// headers
header: Less headFileName Greater | DoubleQuotation headFileName DoubleQuotation;
stlFileName: String | Stack | Vector;
headFileName: stlFileName | Identifier;

// Include directive
includeDirective: Include header;

// Using directive
usingDirective: Using Namespace Identifier Semi;

// Declarations
declaration: mainFunctionDeclaration
           | functionDeclaration
           ;

// Main function declaration
mainFunctionDeclaration: declarationSpecifier Main LeftParen RightParen block;

// Function declarations
functionDeclaration: declarationSpecifier Identifier LeftParen paramDeclarationList? RightParen block;
paramDeclarationList: initialStatement (Comma initialStatement)*;
initialStatement: flagSpecifier? declarationSpecifier declaratorList;

// Type specifier (matches keywords for types from the lexer)
typeSpecifier: Int | Float | Double | Bool | Char | Void | String | Size_t;

// Expressions
expression: term ((Plus | Minus) term)*;

// Terms in expressions (multiplication, division, etc.)
term: factor ((Star | Div | Mod) factor)*;

// Factors in expressions (atoms)
factor: IntegerLiteral
      | FloatingLiteral
      | BooleanLiteral
      | Identifier
      | arrayIdentifier
      | LeftParen expression RightParen
      | literal
      | functionCall;

// Function calls
functionCall: functionSrc functionParams;
functionParams: LeftParen argumentList? RightParen;
functionSrc: ((Identifier | Cin) Dot)* Identifier;

// Identifier for Array
arrayIdentifier: Identifier LeftBrackets (Identifier | expression) RightBrackets;

// Argument list for function calls
argumentList: (Cin | Identifier | factor | expression) (Comma (Cin | Identifier | factor | expression))*;

// Condition specifier (matches keywords for types from the lexer)
conditionSpecifier: Less | Greater | Equal | NotEqual | LessEqual | GreaterEqual;

// statements in blocks(functions)
statement: declarationStatement
         | assignStatement
         | ioStatement
         | functionCallStatement
         | ifStatement
         | forStatement
         | whileStatement
         | endStatement
         | iteratorStatement;

// declaration statement
declaratorList: declarator (Comma declarator)*;

// declarator
declarator: And? (Identifier | arrayIdentifier) initializer?;

initializer:
    Assign factor
    | Assign functionCall
    | Assign expression
    | Assign literal;

stlSpecifier: stlFileName Less typeSpecifier Greater;

// Specifier of declaration
declarationSpecifier: typeSpecifier
                    | stlSpecifier;

// Extra Specifier of declaration
flagSpecifier: Static? Const;

// ioStatement
inputStatement: Cin Stdin (Identifier | arrayIdentifier) (Stdin (Identifier | arrayIdentifier))*;
outputStatement: Cout Stdout (Identifier | arrayIdentifier | literal | EndLine) (Stdout (Identifier | arrayIdentifier | literal | EndLine))*;

// conditionStatement
conditionStatement: (Identifier | arrayIdentifier | functionCall | arrayIdentifier) (conditionSpecifier (Identifier | arrayIdentifier | literal | factor | expression))?;
literal: CharLiteral | StringLiteral;


// logic condition statement of if and while
// ifWhileConditionStatement: LeftParen* Not? (inputStatement | conditionStatement) RightParen* ((AndAnd | OrOr) LeftParen* Not? (inputStatement | conditionStatement) RightParen*)*;
ifWhileConditionStatement
    : Not? ifWhileConditionTerm ((AndAnd | OrOr) Not? ifWhileConditionTerm)*;

ifWhileConditionTerm
    : LeftParen ifWhileConditionStatement RightParen
    | inputStatement
    | conditionStatement;



// logic condition statement of for
forConditionStatement: forConditionForSTL
                     | forConditionForCommon;

forConditionForSTL: typeSpecifier Identifier Colon Identifier;
forConditionForCommon: (initialStatement | declarator) Semi conditionStatement Semi (declarator|iterator);
iterator: ((Identifier | arrayIdentifier) PlusPlus)
        | (PlusPlus (Identifier | arrayIdentifier))
        | ((Identifier | arrayIdentifier) MinusMinus)
        | (MinusMinus (Identifier | arrayIdentifier))
        | ((Identifier | arrayIdentifier) PlusEqual expression)
        | ((Identifier | arrayIdentifier) MinusEqual expression)
        | ((Identifier | arrayIdentifier) StarEqual expression)
        | ((Identifier | arrayIdentifier) DivEqual expression);

// result of return
returnResult: factor | expression | literal | returnConditionStatement;
returnConditionStatement: Not? returnConditionTerm ((AndAnd | OrOr) Not? returnConditionTerm)*;
returnConditionTerm
    : LeftParen returnConditionStatement RightParen
    | conditionStatement;

declarationStatement: flagSpecifier? declarationSpecifier declaratorList Semi;

assignStatement: declarator Semi;

ioStatement: inputStatement Semi
           | outputStatement Semi;

functionCallStatement: functionCall Semi;

ifStatement: If LeftParen ifWhileConditionStatement RightParen (statement | block) elseIfStatement* elseStatement?;
elseIfStatement: ElseIf LeftParen ifWhileConditionStatement RightParen (statement | block);
elseStatement: Else (statement | block);

forStatement: For LeftParen forConditionStatement RightParen (statement | block);

whileStatement: While LeftParen ifWhileConditionStatement RightParen (statement | block);

endStatement: (Break | (Return returnResult?)) Semi;

iteratorStatement: iterator Semi;

// Blocks (used for function bodies, loops, etc.)
block: LeftBrace statement statement* RightBrace;
