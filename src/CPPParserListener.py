# Generated from CPPParser.g4 by ANTLR 4.13.2
from antlr4 import *
from CPPLexer import CPPLexer
if "." in __name__:
    from .CPPParser import CPPParser
else:
    from CPPParser import CPPParser

# This class defines a complete listener for a parse tree produced by CPPParser.
class CPPParserListener(ParseTreeListener):
    def __init__(self):
        self.python_code = []
    # Enter a parse tree produced by CPPParser#program.
    def enterProgram(self, ctx:CPPParser.ProgramContext):
        pass

    # Exit a parse tree produced by CPPParser#program.
    def exitProgram(self, ctx:CPPParser.ProgramContext):
        pass


    # Enter a parse tree produced by CPPParser#preprocessorDirective.
    def enterPreprocessorDirective(self, ctx:CPPParser.PreprocessorDirectiveContext):
        pass

    # Exit a parse tree produced by CPPParser#preprocessorDirective.
    def exitPreprocessorDirective(self, ctx:CPPParser.PreprocessorDirectiveContext):
        pass


    # Enter a parse tree produced by CPPParser#header.
    def enterHeader(self, ctx:CPPParser.HeaderContext):
        pass

    # Exit a parse tree produced by CPPParser#header.
    def exitHeader(self, ctx:CPPParser.HeaderContext):
        pass


    # Enter a parse tree produced by CPPParser#stlFileName.
    def enterStlFileName(self, ctx:CPPParser.StlFileNameContext):
        pass

    # Exit a parse tree produced by CPPParser#stlFileName.
    def exitStlFileName(self, ctx:CPPParser.StlFileNameContext):
        pass


    # Enter a parse tree produced by CPPParser#headFileName.
    def enterHeadFileName(self, ctx:CPPParser.HeadFileNameContext):
        pass

    # Exit a parse tree produced by CPPParser#headFileName.
    def exitHeadFileName(self, ctx:CPPParser.HeadFileNameContext):
        pass


    # Enter a parse tree produced by CPPParser#includeDirective.
    def enterIncludeDirective(self, ctx:CPPParser.IncludeDirectiveContext):
        if ctx.Include():
                self.python_code.append(f"import")
    # Exit a parse tree produced by CPPParser#includeDirective.
    def exitIncludeDirective(self, ctx:CPPParser.IncludeDirectiveContext):
        pass


    # Enter a parse tree produced by CPPParser#usingDirective.
    def enterUsingDirective(self, ctx:CPPParser.UsingDirectiveContext):
        pass

    # Exit a parse tree produced by CPPParser#usingDirective.
    def exitUsingDirective(self, ctx:CPPParser.UsingDirectiveContext):
        pass


    # Enter a parse tree produced by CPPParser#declaration.
    def enterDeclaration(self, ctx:CPPParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#declaration.
    def exitDeclaration(self, ctx:CPPParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#mainFunctionDeclaration.
    def enterMainFunctionDeclaration(self, ctx:CPPParser.MainFunctionDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#mainFunctionDeclaration.
    def exitMainFunctionDeclaration(self, ctx:CPPParser.MainFunctionDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:CPPParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:CPPParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#paramDeclarationList.
    def enterParamDeclarationList(self, ctx:CPPParser.ParamDeclarationListContext):
        pass

    # Exit a parse tree produced by CPPParser#paramDeclarationList.
    def exitParamDeclarationList(self, ctx:CPPParser.ParamDeclarationListContext):
        pass


    # Enter a parse tree produced by CPPParser#initialStatement.
    def enterInitialStatement(self, ctx:CPPParser.InitialStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#initialStatement.
    def exitInitialStatement(self, ctx:CPPParser.InitialStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CPPParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CPPParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#expression.
    def enterExpression(self, ctx:CPPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#expression.
    def exitExpression(self, ctx:CPPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#term.
    def enterTerm(self, ctx:CPPParser.TermContext):
        pass

    # Exit a parse tree produced by CPPParser#term.
    def exitTerm(self, ctx:CPPParser.TermContext):
        pass


    # Enter a parse tree produced by CPPParser#factor.
    def enterFactor(self, ctx:CPPParser.FactorContext):
        pass

    # Exit a parse tree produced by CPPParser#factor.
    def exitFactor(self, ctx:CPPParser.FactorContext):
        pass


    # Enter a parse tree produced by CPPParser#functionCall.
    def enterFunctionCall(self, ctx:CPPParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CPPParser#functionCall.
    def exitFunctionCall(self, ctx:CPPParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CPPParser#functionParams.
    def enterFunctionParams(self, ctx:CPPParser.FunctionParamsContext):
        pass

    # Exit a parse tree produced by CPPParser#functionParams.
    def exitFunctionParams(self, ctx:CPPParser.FunctionParamsContext):
        pass


    # Enter a parse tree produced by CPPParser#functionSrc.
    def enterFunctionSrc(self, ctx:CPPParser.FunctionSrcContext):
        pass

    # Exit a parse tree produced by CPPParser#functionSrc.
    def exitFunctionSrc(self, ctx:CPPParser.FunctionSrcContext):
        pass


    # Enter a parse tree produced by CPPParser#arrayIdentifier.
    def enterArrayIdentifier(self, ctx:CPPParser.ArrayIdentifierContext):
        pass

    # Exit a parse tree produced by CPPParser#arrayIdentifier.
    def exitArrayIdentifier(self, ctx:CPPParser.ArrayIdentifierContext):
        pass


    # Enter a parse tree produced by CPPParser#argumentList.
    def enterArgumentList(self, ctx:CPPParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by CPPParser#argumentList.
    def exitArgumentList(self, ctx:CPPParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by CPPParser#conditionSpecifier.
    def enterConditionSpecifier(self, ctx:CPPParser.ConditionSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#conditionSpecifier.
    def exitConditionSpecifier(self, ctx:CPPParser.ConditionSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#statement.
    def enterStatement(self, ctx:CPPParser.StatementContext):
        pass

    # Exit a parse tree produced by CPPParser#statement.
    def exitStatement(self, ctx:CPPParser.StatementContext):
        pass


    # Enter a parse tree produced by CPPParser#declaratorList.
    def enterDeclaratorList(self, ctx:CPPParser.DeclaratorListContext):
        pass

    # Exit a parse tree produced by CPPParser#declaratorList.
    def exitDeclaratorList(self, ctx:CPPParser.DeclaratorListContext):
        pass


    # Enter a parse tree produced by CPPParser#declarator.
    def enterDeclarator(self, ctx:CPPParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#declarator.
    def exitDeclarator(self, ctx:CPPParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#initializer.
    def enterInitializer(self, ctx:CPPParser.InitializerContext):
        pass

    # Exit a parse tree produced by CPPParser#initializer.
    def exitInitializer(self, ctx:CPPParser.InitializerContext):
        pass


    # Enter a parse tree produced by CPPParser#stlSpecifier.
    def enterStlSpecifier(self, ctx:CPPParser.StlSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#stlSpecifier.
    def exitStlSpecifier(self, ctx:CPPParser.StlSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:CPPParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:CPPParser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#flagSpecifier.
    def enterFlagSpecifier(self, ctx:CPPParser.FlagSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#flagSpecifier.
    def exitFlagSpecifier(self, ctx:CPPParser.FlagSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#inputStatement.
    def enterInputStatement(self, ctx:CPPParser.InputStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#inputStatement.
    def exitInputStatement(self, ctx:CPPParser.InputStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#outputStatement.
    def enterOutputStatement(self, ctx:CPPParser.OutputStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#outputStatement.
    def exitOutputStatement(self, ctx:CPPParser.OutputStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#conditionStatement.
    def enterConditionStatement(self, ctx:CPPParser.ConditionStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#conditionStatement.
    def exitConditionStatement(self, ctx:CPPParser.ConditionStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#literal.
    def enterLiteral(self, ctx:CPPParser.LiteralContext):
        pass

    # Exit a parse tree produced by CPPParser#literal.
    def exitLiteral(self, ctx:CPPParser.LiteralContext):
        pass


    # Enter a parse tree produced by CPPParser#ifWhileConditionStatement.
    def enterIfWhileConditionStatement(self, ctx:CPPParser.IfWhileConditionStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#ifWhileConditionStatement.
    def exitIfWhileConditionStatement(self, ctx:CPPParser.IfWhileConditionStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#ifWhileConditionTerm.
    def enterIfWhileConditionTerm(self, ctx:CPPParser.IfWhileConditionTermContext):
        pass

    # Exit a parse tree produced by CPPParser#ifWhileConditionTerm.
    def exitIfWhileConditionTerm(self, ctx:CPPParser.IfWhileConditionTermContext):
        pass


    # Enter a parse tree produced by CPPParser#forConditionStatement.
    def enterForConditionStatement(self, ctx:CPPParser.ForConditionStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#forConditionStatement.
    def exitForConditionStatement(self, ctx:CPPParser.ForConditionStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#forConditionForSTL.
    def enterForConditionForSTL(self, ctx:CPPParser.ForConditionForSTLContext):
        pass

    # Exit a parse tree produced by CPPParser#forConditionForSTL.
    def exitForConditionForSTL(self, ctx:CPPParser.ForConditionForSTLContext):
        pass


    # Enter a parse tree produced by CPPParser#forConditionForCommon.
    def enterForConditionForCommon(self, ctx:CPPParser.ForConditionForCommonContext):
        pass

    # Exit a parse tree produced by CPPParser#forConditionForCommon.
    def exitForConditionForCommon(self, ctx:CPPParser.ForConditionForCommonContext):
        pass


    # Enter a parse tree produced by CPPParser#iterator.
    def enterIterator(self, ctx:CPPParser.IteratorContext):
        pass

    # Exit a parse tree produced by CPPParser#iterator.
    def exitIterator(self, ctx:CPPParser.IteratorContext):
        pass


    # Enter a parse tree produced by CPPParser#returnResult.
    def enterReturnResult(self, ctx:CPPParser.ReturnResultContext):
        pass

    # Exit a parse tree produced by CPPParser#returnResult.
    def exitReturnResult(self, ctx:CPPParser.ReturnResultContext):
        pass


    # Enter a parse tree produced by CPPParser#returnConditionStatement.
    def enterReturnConditionStatement(self, ctx:CPPParser.ReturnConditionStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#returnConditionStatement.
    def exitReturnConditionStatement(self, ctx:CPPParser.ReturnConditionStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#returnConditionTerm.
    def enterReturnConditionTerm(self, ctx:CPPParser.ReturnConditionTermContext):
        pass

    # Exit a parse tree produced by CPPParser#returnConditionTerm.
    def exitReturnConditionTerm(self, ctx:CPPParser.ReturnConditionTermContext):
        pass


    # Enter a parse tree produced by CPPParser#declarationStatement.
    def enterDeclarationStatement(self, ctx:CPPParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#declarationStatement.
    def exitDeclarationStatement(self, ctx:CPPParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#assignStatement.
    def enterAssignStatement(self, ctx:CPPParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#assignStatement.
    def exitAssignStatement(self, ctx:CPPParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#ioStatement.
    def enterIoStatement(self, ctx:CPPParser.IoStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#ioStatement.
    def exitIoStatement(self, ctx:CPPParser.IoStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#functionCallStatement.
    def enterFunctionCallStatement(self, ctx:CPPParser.FunctionCallStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#functionCallStatement.
    def exitFunctionCallStatement(self, ctx:CPPParser.FunctionCallStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#ifStatement.
    def enterIfStatement(self, ctx:CPPParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#ifStatement.
    def exitIfStatement(self, ctx:CPPParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#elseIfStatement.
    def enterElseIfStatement(self, ctx:CPPParser.ElseIfStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#elseIfStatement.
    def exitElseIfStatement(self, ctx:CPPParser.ElseIfStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#elseStatement.
    def enterElseStatement(self, ctx:CPPParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#elseStatement.
    def exitElseStatement(self, ctx:CPPParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#forStatement.
    def enterForStatement(self, ctx:CPPParser.ForStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#forStatement.
    def exitForStatement(self, ctx:CPPParser.ForStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#whileStatement.
    def enterWhileStatement(self, ctx:CPPParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#whileStatement.
    def exitWhileStatement(self, ctx:CPPParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#endStatement.
    def enterEndStatement(self, ctx:CPPParser.EndStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#endStatement.
    def exitEndStatement(self, ctx:CPPParser.EndStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#iteratorStatement.
    def enterIteratorStatement(self, ctx:CPPParser.IteratorStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#iteratorStatement.
    def exitIteratorStatement(self, ctx:CPPParser.IteratorStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#block.
    def enterBlock(self, ctx:CPPParser.BlockContext):
        pass

    # Exit a parse tree produced by CPPParser#block.
    def exitBlock(self, ctx:CPPParser.BlockContext):
        pass
    def convert_cpp_to_python(cpp_code):
        input_stream = InputStream(cpp_code)
        lexer = CPPLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CPPParser(stream)
        
        # 获取语法树
        tree = parser.program()

        # 创建并应用监听器
        listener = CPPParserListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)



del CPPParser
