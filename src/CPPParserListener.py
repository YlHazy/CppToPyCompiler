# Generated from CPPParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CPPParser import CPPParser
else:
    from CPPParser import CPPParser

# This class defines a complete listener for a parse tree produced by CPPParser.
class CPPParserListener(ParseTreeListener):

    # Enter a parse tree produced by CPPParser#translationUnit.
    def enterTranslationUnit(self, ctx:CPPParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by CPPParser#translationUnit.
    def exitTranslationUnit(self, ctx:CPPParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by CPPParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:CPPParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:CPPParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#idExpression.
    def enterIdExpression(self, ctx:CPPParser.IdExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#idExpression.
    def exitIdExpression(self, ctx:CPPParser.IdExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#unqualifiedId.
    def enterUnqualifiedId(self, ctx:CPPParser.UnqualifiedIdContext):
        pass

    # Exit a parse tree produced by CPPParser#unqualifiedId.
    def exitUnqualifiedId(self, ctx:CPPParser.UnqualifiedIdContext):
        pass


    # Enter a parse tree produced by CPPParser#qualifiedId.
    def enterQualifiedId(self, ctx:CPPParser.QualifiedIdContext):
        pass

    # Exit a parse tree produced by CPPParser#qualifiedId.
    def exitQualifiedId(self, ctx:CPPParser.QualifiedIdContext):
        pass


    # Enter a parse tree produced by CPPParser#nestedNameSpecifier.
    def enterNestedNameSpecifier(self, ctx:CPPParser.NestedNameSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#nestedNameSpecifier.
    def exitNestedNameSpecifier(self, ctx:CPPParser.NestedNameSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#lambdaExpression.
    def enterLambdaExpression(self, ctx:CPPParser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#lambdaExpression.
    def exitLambdaExpression(self, ctx:CPPParser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#lambdaIntroducer.
    def enterLambdaIntroducer(self, ctx:CPPParser.LambdaIntroducerContext):
        pass

    # Exit a parse tree produced by CPPParser#lambdaIntroducer.
    def exitLambdaIntroducer(self, ctx:CPPParser.LambdaIntroducerContext):
        pass


    # Enter a parse tree produced by CPPParser#lambdaCapture.
    def enterLambdaCapture(self, ctx:CPPParser.LambdaCaptureContext):
        pass

    # Exit a parse tree produced by CPPParser#lambdaCapture.
    def exitLambdaCapture(self, ctx:CPPParser.LambdaCaptureContext):
        pass


    # Enter a parse tree produced by CPPParser#captureDefault.
    def enterCaptureDefault(self, ctx:CPPParser.CaptureDefaultContext):
        pass

    # Exit a parse tree produced by CPPParser#captureDefault.
    def exitCaptureDefault(self, ctx:CPPParser.CaptureDefaultContext):
        pass


    # Enter a parse tree produced by CPPParser#captureList.
    def enterCaptureList(self, ctx:CPPParser.CaptureListContext):
        pass

    # Exit a parse tree produced by CPPParser#captureList.
    def exitCaptureList(self, ctx:CPPParser.CaptureListContext):
        pass


    # Enter a parse tree produced by CPPParser#capture.
    def enterCapture(self, ctx:CPPParser.CaptureContext):
        pass

    # Exit a parse tree produced by CPPParser#capture.
    def exitCapture(self, ctx:CPPParser.CaptureContext):
        pass


    # Enter a parse tree produced by CPPParser#simpleCapture.
    def enterSimpleCapture(self, ctx:CPPParser.SimpleCaptureContext):
        pass

    # Exit a parse tree produced by CPPParser#simpleCapture.
    def exitSimpleCapture(self, ctx:CPPParser.SimpleCaptureContext):
        pass


    # Enter a parse tree produced by CPPParser#initcapture.
    def enterInitcapture(self, ctx:CPPParser.InitcaptureContext):
        pass

    # Exit a parse tree produced by CPPParser#initcapture.
    def exitInitcapture(self, ctx:CPPParser.InitcaptureContext):
        pass


    # Enter a parse tree produced by CPPParser#lambdaDeclarator.
    def enterLambdaDeclarator(self, ctx:CPPParser.LambdaDeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#lambdaDeclarator.
    def exitLambdaDeclarator(self, ctx:CPPParser.LambdaDeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#postfixExpression.
    def enterPostfixExpression(self, ctx:CPPParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#postfixExpression.
    def exitPostfixExpression(self, ctx:CPPParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#typeIdOfTheTypeId.
    def enterTypeIdOfTheTypeId(self, ctx:CPPParser.TypeIdOfTheTypeIdContext):
        pass

    # Exit a parse tree produced by CPPParser#typeIdOfTheTypeId.
    def exitTypeIdOfTheTypeId(self, ctx:CPPParser.TypeIdOfTheTypeIdContext):
        pass


    # Enter a parse tree produced by CPPParser#expressionList.
    def enterExpressionList(self, ctx:CPPParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by CPPParser#expressionList.
    def exitExpressionList(self, ctx:CPPParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by CPPParser#pseudoDestructorName.
    def enterPseudoDestructorName(self, ctx:CPPParser.PseudoDestructorNameContext):
        pass

    # Exit a parse tree produced by CPPParser#pseudoDestructorName.
    def exitPseudoDestructorName(self, ctx:CPPParser.PseudoDestructorNameContext):
        pass


    # Enter a parse tree produced by CPPParser#unaryExpression.
    def enterUnaryExpression(self, ctx:CPPParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#unaryExpression.
    def exitUnaryExpression(self, ctx:CPPParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#unaryOperator.
    def enterUnaryOperator(self, ctx:CPPParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by CPPParser#unaryOperator.
    def exitUnaryOperator(self, ctx:CPPParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by CPPParser#newExpression_.
    def enterNewExpression_(self, ctx:CPPParser.NewExpression_Context):
        pass

    # Exit a parse tree produced by CPPParser#newExpression_.
    def exitNewExpression_(self, ctx:CPPParser.NewExpression_Context):
        pass


    # Enter a parse tree produced by CPPParser#newPlacement.
    def enterNewPlacement(self, ctx:CPPParser.NewPlacementContext):
        pass

    # Exit a parse tree produced by CPPParser#newPlacement.
    def exitNewPlacement(self, ctx:CPPParser.NewPlacementContext):
        pass


    # Enter a parse tree produced by CPPParser#newTypeId.
    def enterNewTypeId(self, ctx:CPPParser.NewTypeIdContext):
        pass

    # Exit a parse tree produced by CPPParser#newTypeId.
    def exitNewTypeId(self, ctx:CPPParser.NewTypeIdContext):
        pass


    # Enter a parse tree produced by CPPParser#newDeclarator_.
    def enterNewDeclarator_(self, ctx:CPPParser.NewDeclarator_Context):
        pass

    # Exit a parse tree produced by CPPParser#newDeclarator_.
    def exitNewDeclarator_(self, ctx:CPPParser.NewDeclarator_Context):
        pass


    # Enter a parse tree produced by CPPParser#noPointerNewDeclarator.
    def enterNoPointerNewDeclarator(self, ctx:CPPParser.NoPointerNewDeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#noPointerNewDeclarator.
    def exitNoPointerNewDeclarator(self, ctx:CPPParser.NoPointerNewDeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#newInitializer_.
    def enterNewInitializer_(self, ctx:CPPParser.NewInitializer_Context):
        pass

    # Exit a parse tree produced by CPPParser#newInitializer_.
    def exitNewInitializer_(self, ctx:CPPParser.NewInitializer_Context):
        pass


    # Enter a parse tree produced by CPPParser#deleteExpression.
    def enterDeleteExpression(self, ctx:CPPParser.DeleteExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#deleteExpression.
    def exitDeleteExpression(self, ctx:CPPParser.DeleteExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#noExceptExpression.
    def enterNoExceptExpression(self, ctx:CPPParser.NoExceptExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#noExceptExpression.
    def exitNoExceptExpression(self, ctx:CPPParser.NoExceptExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#castExpression.
    def enterCastExpression(self, ctx:CPPParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#castExpression.
    def exitCastExpression(self, ctx:CPPParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#pointerMemberExpression.
    def enterPointerMemberExpression(self, ctx:CPPParser.PointerMemberExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#pointerMemberExpression.
    def exitPointerMemberExpression(self, ctx:CPPParser.PointerMemberExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:CPPParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:CPPParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:CPPParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:CPPParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#shiftExpression.
    def enterShiftExpression(self, ctx:CPPParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#shiftExpression.
    def exitShiftExpression(self, ctx:CPPParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#shiftOperator.
    def enterShiftOperator(self, ctx:CPPParser.ShiftOperatorContext):
        pass

    # Exit a parse tree produced by CPPParser#shiftOperator.
    def exitShiftOperator(self, ctx:CPPParser.ShiftOperatorContext):
        pass


    # Enter a parse tree produced by CPPParser#relationalExpression.
    def enterRelationalExpression(self, ctx:CPPParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#relationalExpression.
    def exitRelationalExpression(self, ctx:CPPParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#equalityExpression.
    def enterEqualityExpression(self, ctx:CPPParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#equalityExpression.
    def exitEqualityExpression(self, ctx:CPPParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#andExpression.
    def enterAndExpression(self, ctx:CPPParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#andExpression.
    def exitAndExpression(self, ctx:CPPParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:CPPParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:CPPParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:CPPParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:CPPParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:CPPParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:CPPParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:CPPParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:CPPParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:CPPParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:CPPParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:CPPParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:CPPParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:CPPParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by CPPParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:CPPParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by CPPParser#expression.
    def enterExpression(self, ctx:CPPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#expression.
    def exitExpression(self, ctx:CPPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#constantExpression.
    def enterConstantExpression(self, ctx:CPPParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#constantExpression.
    def exitConstantExpression(self, ctx:CPPParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#statement.
    def enterStatement(self, ctx:CPPParser.StatementContext):
        pass

    # Exit a parse tree produced by CPPParser#statement.
    def exitStatement(self, ctx:CPPParser.StatementContext):
        pass


    # Enter a parse tree produced by CPPParser#labeledStatement.
    def enterLabeledStatement(self, ctx:CPPParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#labeledStatement.
    def exitLabeledStatement(self, ctx:CPPParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#expressionStatement.
    def enterExpressionStatement(self, ctx:CPPParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#expressionStatement.
    def exitExpressionStatement(self, ctx:CPPParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#compoundStatement.
    def enterCompoundStatement(self, ctx:CPPParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#compoundStatement.
    def exitCompoundStatement(self, ctx:CPPParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#statementSeq.
    def enterStatementSeq(self, ctx:CPPParser.StatementSeqContext):
        pass

    # Exit a parse tree produced by CPPParser#statementSeq.
    def exitStatementSeq(self, ctx:CPPParser.StatementSeqContext):
        pass


    # Enter a parse tree produced by CPPParser#selectionStatement.
    def enterSelectionStatement(self, ctx:CPPParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#selectionStatement.
    def exitSelectionStatement(self, ctx:CPPParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#condition.
    def enterCondition(self, ctx:CPPParser.ConditionContext):
        pass

    # Exit a parse tree produced by CPPParser#condition.
    def exitCondition(self, ctx:CPPParser.ConditionContext):
        pass


    # Enter a parse tree produced by CPPParser#iterationStatement.
    def enterIterationStatement(self, ctx:CPPParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#iterationStatement.
    def exitIterationStatement(self, ctx:CPPParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#forInitStatement.
    def enterForInitStatement(self, ctx:CPPParser.ForInitStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#forInitStatement.
    def exitForInitStatement(self, ctx:CPPParser.ForInitStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#forRangeDeclaration.
    def enterForRangeDeclaration(self, ctx:CPPParser.ForRangeDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#forRangeDeclaration.
    def exitForRangeDeclaration(self, ctx:CPPParser.ForRangeDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#forRangeInitializer.
    def enterForRangeInitializer(self, ctx:CPPParser.ForRangeInitializerContext):
        pass

    # Exit a parse tree produced by CPPParser#forRangeInitializer.
    def exitForRangeInitializer(self, ctx:CPPParser.ForRangeInitializerContext):
        pass


    # Enter a parse tree produced by CPPParser#jumpStatement.
    def enterJumpStatement(self, ctx:CPPParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#jumpStatement.
    def exitJumpStatement(self, ctx:CPPParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#declarationStatement.
    def enterDeclarationStatement(self, ctx:CPPParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#declarationStatement.
    def exitDeclarationStatement(self, ctx:CPPParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#declarationseq.
    def enterDeclarationseq(self, ctx:CPPParser.DeclarationseqContext):
        pass

    # Exit a parse tree produced by CPPParser#declarationseq.
    def exitDeclarationseq(self, ctx:CPPParser.DeclarationseqContext):
        pass


    # Enter a parse tree produced by CPPParser#declaration.
    def enterDeclaration(self, ctx:CPPParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#declaration.
    def exitDeclaration(self, ctx:CPPParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#blockDeclaration.
    def enterBlockDeclaration(self, ctx:CPPParser.BlockDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#blockDeclaration.
    def exitBlockDeclaration(self, ctx:CPPParser.BlockDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#aliasDeclaration.
    def enterAliasDeclaration(self, ctx:CPPParser.AliasDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#aliasDeclaration.
    def exitAliasDeclaration(self, ctx:CPPParser.AliasDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#simpleDeclaration.
    def enterSimpleDeclaration(self, ctx:CPPParser.SimpleDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#simpleDeclaration.
    def exitSimpleDeclaration(self, ctx:CPPParser.SimpleDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:CPPParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:CPPParser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#emptyDeclaration_.
    def enterEmptyDeclaration_(self, ctx:CPPParser.EmptyDeclaration_Context):
        pass

    # Exit a parse tree produced by CPPParser#emptyDeclaration_.
    def exitEmptyDeclaration_(self, ctx:CPPParser.EmptyDeclaration_Context):
        pass


    # Enter a parse tree produced by CPPParser#attributeDeclaration.
    def enterAttributeDeclaration(self, ctx:CPPParser.AttributeDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#attributeDeclaration.
    def exitAttributeDeclaration(self, ctx:CPPParser.AttributeDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#declSpecifier.
    def enterDeclSpecifier(self, ctx:CPPParser.DeclSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#declSpecifier.
    def exitDeclSpecifier(self, ctx:CPPParser.DeclSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#declSpecifierSeq.
    def enterDeclSpecifierSeq(self, ctx:CPPParser.DeclSpecifierSeqContext):
        pass

    # Exit a parse tree produced by CPPParser#declSpecifierSeq.
    def exitDeclSpecifierSeq(self, ctx:CPPParser.DeclSpecifierSeqContext):
        pass


    # Enter a parse tree produced by CPPParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:CPPParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:CPPParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:CPPParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:CPPParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#typedefName.
    def enterTypedefName(self, ctx:CPPParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by CPPParser#typedefName.
    def exitTypedefName(self, ctx:CPPParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by CPPParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CPPParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CPPParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#trailingTypeSpecifier.
    def enterTrailingTypeSpecifier(self, ctx:CPPParser.TrailingTypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#trailingTypeSpecifier.
    def exitTrailingTypeSpecifier(self, ctx:CPPParser.TrailingTypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#typeSpecifierSeq.
    def enterTypeSpecifierSeq(self, ctx:CPPParser.TypeSpecifierSeqContext):
        pass

    # Exit a parse tree produced by CPPParser#typeSpecifierSeq.
    def exitTypeSpecifierSeq(self, ctx:CPPParser.TypeSpecifierSeqContext):
        pass


    # Enter a parse tree produced by CPPParser#trailingTypeSpecifierSeq.
    def enterTrailingTypeSpecifierSeq(self, ctx:CPPParser.TrailingTypeSpecifierSeqContext):
        pass

    # Exit a parse tree produced by CPPParser#trailingTypeSpecifierSeq.
    def exitTrailingTypeSpecifierSeq(self, ctx:CPPParser.TrailingTypeSpecifierSeqContext):
        pass


    # Enter a parse tree produced by CPPParser#simpleTypeLengthModifier.
    def enterSimpleTypeLengthModifier(self, ctx:CPPParser.SimpleTypeLengthModifierContext):
        pass

    # Exit a parse tree produced by CPPParser#simpleTypeLengthModifier.
    def exitSimpleTypeLengthModifier(self, ctx:CPPParser.SimpleTypeLengthModifierContext):
        pass


    # Enter a parse tree produced by CPPParser#simpleTypeSignednessModifier.
    def enterSimpleTypeSignednessModifier(self, ctx:CPPParser.SimpleTypeSignednessModifierContext):
        pass

    # Exit a parse tree produced by CPPParser#simpleTypeSignednessModifier.
    def exitSimpleTypeSignednessModifier(self, ctx:CPPParser.SimpleTypeSignednessModifierContext):
        pass


    # Enter a parse tree produced by CPPParser#simpleTypeSpecifier.
    def enterSimpleTypeSpecifier(self, ctx:CPPParser.SimpleTypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#simpleTypeSpecifier.
    def exitSimpleTypeSpecifier(self, ctx:CPPParser.SimpleTypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#theTypeName.
    def enterTheTypeName(self, ctx:CPPParser.TheTypeNameContext):
        pass

    # Exit a parse tree produced by CPPParser#theTypeName.
    def exitTheTypeName(self, ctx:CPPParser.TheTypeNameContext):
        pass


    # Enter a parse tree produced by CPPParser#decltypeSpecifier.
    def enterDecltypeSpecifier(self, ctx:CPPParser.DecltypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#decltypeSpecifier.
    def exitDecltypeSpecifier(self, ctx:CPPParser.DecltypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#elaboratedTypeSpecifier.
    def enterElaboratedTypeSpecifier(self, ctx:CPPParser.ElaboratedTypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#elaboratedTypeSpecifier.
    def exitElaboratedTypeSpecifier(self, ctx:CPPParser.ElaboratedTypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#enumName.
    def enterEnumName(self, ctx:CPPParser.EnumNameContext):
        pass

    # Exit a parse tree produced by CPPParser#enumName.
    def exitEnumName(self, ctx:CPPParser.EnumNameContext):
        pass


    # Enter a parse tree produced by CPPParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:CPPParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:CPPParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#enumHead.
    def enterEnumHead(self, ctx:CPPParser.EnumHeadContext):
        pass

    # Exit a parse tree produced by CPPParser#enumHead.
    def exitEnumHead(self, ctx:CPPParser.EnumHeadContext):
        pass


    # Enter a parse tree produced by CPPParser#opaqueEnumDeclaration.
    def enterOpaqueEnumDeclaration(self, ctx:CPPParser.OpaqueEnumDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#opaqueEnumDeclaration.
    def exitOpaqueEnumDeclaration(self, ctx:CPPParser.OpaqueEnumDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#enumkey.
    def enterEnumkey(self, ctx:CPPParser.EnumkeyContext):
        pass

    # Exit a parse tree produced by CPPParser#enumkey.
    def exitEnumkey(self, ctx:CPPParser.EnumkeyContext):
        pass


    # Enter a parse tree produced by CPPParser#enumbase.
    def enterEnumbase(self, ctx:CPPParser.EnumbaseContext):
        pass

    # Exit a parse tree produced by CPPParser#enumbase.
    def exitEnumbase(self, ctx:CPPParser.EnumbaseContext):
        pass


    # Enter a parse tree produced by CPPParser#enumeratorList.
    def enterEnumeratorList(self, ctx:CPPParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by CPPParser#enumeratorList.
    def exitEnumeratorList(self, ctx:CPPParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by CPPParser#enumeratorDefinition.
    def enterEnumeratorDefinition(self, ctx:CPPParser.EnumeratorDefinitionContext):
        pass

    # Exit a parse tree produced by CPPParser#enumeratorDefinition.
    def exitEnumeratorDefinition(self, ctx:CPPParser.EnumeratorDefinitionContext):
        pass


    # Enter a parse tree produced by CPPParser#enumerator.
    def enterEnumerator(self, ctx:CPPParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by CPPParser#enumerator.
    def exitEnumerator(self, ctx:CPPParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by CPPParser#namespaceName.
    def enterNamespaceName(self, ctx:CPPParser.NamespaceNameContext):
        pass

    # Exit a parse tree produced by CPPParser#namespaceName.
    def exitNamespaceName(self, ctx:CPPParser.NamespaceNameContext):
        pass


    # Enter a parse tree produced by CPPParser#originalNamespaceName.
    def enterOriginalNamespaceName(self, ctx:CPPParser.OriginalNamespaceNameContext):
        pass

    # Exit a parse tree produced by CPPParser#originalNamespaceName.
    def exitOriginalNamespaceName(self, ctx:CPPParser.OriginalNamespaceNameContext):
        pass


    # Enter a parse tree produced by CPPParser#namespaceDefinition.
    def enterNamespaceDefinition(self, ctx:CPPParser.NamespaceDefinitionContext):
        pass

    # Exit a parse tree produced by CPPParser#namespaceDefinition.
    def exitNamespaceDefinition(self, ctx:CPPParser.NamespaceDefinitionContext):
        pass


    # Enter a parse tree produced by CPPParser#namespaceAlias.
    def enterNamespaceAlias(self, ctx:CPPParser.NamespaceAliasContext):
        pass

    # Exit a parse tree produced by CPPParser#namespaceAlias.
    def exitNamespaceAlias(self, ctx:CPPParser.NamespaceAliasContext):
        pass


    # Enter a parse tree produced by CPPParser#namespaceAliasDefinition.
    def enterNamespaceAliasDefinition(self, ctx:CPPParser.NamespaceAliasDefinitionContext):
        pass

    # Exit a parse tree produced by CPPParser#namespaceAliasDefinition.
    def exitNamespaceAliasDefinition(self, ctx:CPPParser.NamespaceAliasDefinitionContext):
        pass


    # Enter a parse tree produced by CPPParser#qualifiednamespacespecifier.
    def enterQualifiednamespacespecifier(self, ctx:CPPParser.QualifiednamespacespecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#qualifiednamespacespecifier.
    def exitQualifiednamespacespecifier(self, ctx:CPPParser.QualifiednamespacespecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#usingDeclaration.
    def enterUsingDeclaration(self, ctx:CPPParser.UsingDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#usingDeclaration.
    def exitUsingDeclaration(self, ctx:CPPParser.UsingDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#usingDirective.
    def enterUsingDirective(self, ctx:CPPParser.UsingDirectiveContext):
        pass

    # Exit a parse tree produced by CPPParser#usingDirective.
    def exitUsingDirective(self, ctx:CPPParser.UsingDirectiveContext):
        pass


    # Enter a parse tree produced by CPPParser#asmDefinition.
    def enterAsmDefinition(self, ctx:CPPParser.AsmDefinitionContext):
        pass

    # Exit a parse tree produced by CPPParser#asmDefinition.
    def exitAsmDefinition(self, ctx:CPPParser.AsmDefinitionContext):
        pass


    # Enter a parse tree produced by CPPParser#linkageSpecification.
    def enterLinkageSpecification(self, ctx:CPPParser.LinkageSpecificationContext):
        pass

    # Exit a parse tree produced by CPPParser#linkageSpecification.
    def exitLinkageSpecification(self, ctx:CPPParser.LinkageSpecificationContext):
        pass


    # Enter a parse tree produced by CPPParser#attributeSpecifierSeq.
    def enterAttributeSpecifierSeq(self, ctx:CPPParser.AttributeSpecifierSeqContext):
        pass

    # Exit a parse tree produced by CPPParser#attributeSpecifierSeq.
    def exitAttributeSpecifierSeq(self, ctx:CPPParser.AttributeSpecifierSeqContext):
        pass


    # Enter a parse tree produced by CPPParser#attributeSpecifier.
    def enterAttributeSpecifier(self, ctx:CPPParser.AttributeSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#attributeSpecifier.
    def exitAttributeSpecifier(self, ctx:CPPParser.AttributeSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#alignmentspecifier.
    def enterAlignmentspecifier(self, ctx:CPPParser.AlignmentspecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#alignmentspecifier.
    def exitAlignmentspecifier(self, ctx:CPPParser.AlignmentspecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#attributeList.
    def enterAttributeList(self, ctx:CPPParser.AttributeListContext):
        pass

    # Exit a parse tree produced by CPPParser#attributeList.
    def exitAttributeList(self, ctx:CPPParser.AttributeListContext):
        pass


    # Enter a parse tree produced by CPPParser#attribute.
    def enterAttribute(self, ctx:CPPParser.AttributeContext):
        pass

    # Exit a parse tree produced by CPPParser#attribute.
    def exitAttribute(self, ctx:CPPParser.AttributeContext):
        pass


    # Enter a parse tree produced by CPPParser#attributeNamespace.
    def enterAttributeNamespace(self, ctx:CPPParser.AttributeNamespaceContext):
        pass

    # Exit a parse tree produced by CPPParser#attributeNamespace.
    def exitAttributeNamespace(self, ctx:CPPParser.AttributeNamespaceContext):
        pass


    # Enter a parse tree produced by CPPParser#attributeArgumentClause.
    def enterAttributeArgumentClause(self, ctx:CPPParser.AttributeArgumentClauseContext):
        pass

    # Exit a parse tree produced by CPPParser#attributeArgumentClause.
    def exitAttributeArgumentClause(self, ctx:CPPParser.AttributeArgumentClauseContext):
        pass


    # Enter a parse tree produced by CPPParser#balancedTokenSeq.
    def enterBalancedTokenSeq(self, ctx:CPPParser.BalancedTokenSeqContext):
        pass

    # Exit a parse tree produced by CPPParser#balancedTokenSeq.
    def exitBalancedTokenSeq(self, ctx:CPPParser.BalancedTokenSeqContext):
        pass


    # Enter a parse tree produced by CPPParser#balancedtoken.
    def enterBalancedtoken(self, ctx:CPPParser.BalancedtokenContext):
        pass

    # Exit a parse tree produced by CPPParser#balancedtoken.
    def exitBalancedtoken(self, ctx:CPPParser.BalancedtokenContext):
        pass


    # Enter a parse tree produced by CPPParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:CPPParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by CPPParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:CPPParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by CPPParser#initDeclarator.
    def enterInitDeclarator(self, ctx:CPPParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#initDeclarator.
    def exitInitDeclarator(self, ctx:CPPParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#declarator.
    def enterDeclarator(self, ctx:CPPParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#declarator.
    def exitDeclarator(self, ctx:CPPParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#pointerDeclarator.
    def enterPointerDeclarator(self, ctx:CPPParser.PointerDeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#pointerDeclarator.
    def exitPointerDeclarator(self, ctx:CPPParser.PointerDeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#noPointerDeclarator.
    def enterNoPointerDeclarator(self, ctx:CPPParser.NoPointerDeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#noPointerDeclarator.
    def exitNoPointerDeclarator(self, ctx:CPPParser.NoPointerDeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#parametersAndQualifiers.
    def enterParametersAndQualifiers(self, ctx:CPPParser.ParametersAndQualifiersContext):
        pass

    # Exit a parse tree produced by CPPParser#parametersAndQualifiers.
    def exitParametersAndQualifiers(self, ctx:CPPParser.ParametersAndQualifiersContext):
        pass


    # Enter a parse tree produced by CPPParser#trailingReturnType.
    def enterTrailingReturnType(self, ctx:CPPParser.TrailingReturnTypeContext):
        pass

    # Exit a parse tree produced by CPPParser#trailingReturnType.
    def exitTrailingReturnType(self, ctx:CPPParser.TrailingReturnTypeContext):
        pass


    # Enter a parse tree produced by CPPParser#pointerOperator.
    def enterPointerOperator(self, ctx:CPPParser.PointerOperatorContext):
        pass

    # Exit a parse tree produced by CPPParser#pointerOperator.
    def exitPointerOperator(self, ctx:CPPParser.PointerOperatorContext):
        pass


    # Enter a parse tree produced by CPPParser#cvqualifierseq.
    def enterCvqualifierseq(self, ctx:CPPParser.CvqualifierseqContext):
        pass

    # Exit a parse tree produced by CPPParser#cvqualifierseq.
    def exitCvqualifierseq(self, ctx:CPPParser.CvqualifierseqContext):
        pass


    # Enter a parse tree produced by CPPParser#cvQualifier.
    def enterCvQualifier(self, ctx:CPPParser.CvQualifierContext):
        pass

    # Exit a parse tree produced by CPPParser#cvQualifier.
    def exitCvQualifier(self, ctx:CPPParser.CvQualifierContext):
        pass


    # Enter a parse tree produced by CPPParser#refqualifier.
    def enterRefqualifier(self, ctx:CPPParser.RefqualifierContext):
        pass

    # Exit a parse tree produced by CPPParser#refqualifier.
    def exitRefqualifier(self, ctx:CPPParser.RefqualifierContext):
        pass


    # Enter a parse tree produced by CPPParser#declaratorid.
    def enterDeclaratorid(self, ctx:CPPParser.DeclaratoridContext):
        pass

    # Exit a parse tree produced by CPPParser#declaratorid.
    def exitDeclaratorid(self, ctx:CPPParser.DeclaratoridContext):
        pass


    # Enter a parse tree produced by CPPParser#theTypeId.
    def enterTheTypeId(self, ctx:CPPParser.TheTypeIdContext):
        pass

    # Exit a parse tree produced by CPPParser#theTypeId.
    def exitTheTypeId(self, ctx:CPPParser.TheTypeIdContext):
        pass


    # Enter a parse tree produced by CPPParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:CPPParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:CPPParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#pointerAbstractDeclarator.
    def enterPointerAbstractDeclarator(self, ctx:CPPParser.PointerAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#pointerAbstractDeclarator.
    def exitPointerAbstractDeclarator(self, ctx:CPPParser.PointerAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#noPointerAbstractDeclarator.
    def enterNoPointerAbstractDeclarator(self, ctx:CPPParser.NoPointerAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#noPointerAbstractDeclarator.
    def exitNoPointerAbstractDeclarator(self, ctx:CPPParser.NoPointerAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#abstractPackDeclarator.
    def enterAbstractPackDeclarator(self, ctx:CPPParser.AbstractPackDeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#abstractPackDeclarator.
    def exitAbstractPackDeclarator(self, ctx:CPPParser.AbstractPackDeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#noPointerAbstractPackDeclarator.
    def enterNoPointerAbstractPackDeclarator(self, ctx:CPPParser.NoPointerAbstractPackDeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#noPointerAbstractPackDeclarator.
    def exitNoPointerAbstractPackDeclarator(self, ctx:CPPParser.NoPointerAbstractPackDeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#parameterDeclarationClause.
    def enterParameterDeclarationClause(self, ctx:CPPParser.ParameterDeclarationClauseContext):
        pass

    # Exit a parse tree produced by CPPParser#parameterDeclarationClause.
    def exitParameterDeclarationClause(self, ctx:CPPParser.ParameterDeclarationClauseContext):
        pass


    # Enter a parse tree produced by CPPParser#parameterDeclarationList.
    def enterParameterDeclarationList(self, ctx:CPPParser.ParameterDeclarationListContext):
        pass

    # Exit a parse tree produced by CPPParser#parameterDeclarationList.
    def exitParameterDeclarationList(self, ctx:CPPParser.ParameterDeclarationListContext):
        pass


    # Enter a parse tree produced by CPPParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:CPPParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:CPPParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CPPParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CPPParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CPPParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CPPParser#functionBody.
    def enterFunctionBody(self, ctx:CPPParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by CPPParser#functionBody.
    def exitFunctionBody(self, ctx:CPPParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by CPPParser#initializer.
    def enterInitializer(self, ctx:CPPParser.InitializerContext):
        pass

    # Exit a parse tree produced by CPPParser#initializer.
    def exitInitializer(self, ctx:CPPParser.InitializerContext):
        pass


    # Enter a parse tree produced by CPPParser#braceOrEqualInitializer.
    def enterBraceOrEqualInitializer(self, ctx:CPPParser.BraceOrEqualInitializerContext):
        pass

    # Exit a parse tree produced by CPPParser#braceOrEqualInitializer.
    def exitBraceOrEqualInitializer(self, ctx:CPPParser.BraceOrEqualInitializerContext):
        pass


    # Enter a parse tree produced by CPPParser#initializerClause.
    def enterInitializerClause(self, ctx:CPPParser.InitializerClauseContext):
        pass

    # Exit a parse tree produced by CPPParser#initializerClause.
    def exitInitializerClause(self, ctx:CPPParser.InitializerClauseContext):
        pass


    # Enter a parse tree produced by CPPParser#initializerList.
    def enterInitializerList(self, ctx:CPPParser.InitializerListContext):
        pass

    # Exit a parse tree produced by CPPParser#initializerList.
    def exitInitializerList(self, ctx:CPPParser.InitializerListContext):
        pass


    # Enter a parse tree produced by CPPParser#bracedInitList.
    def enterBracedInitList(self, ctx:CPPParser.BracedInitListContext):
        pass

    # Exit a parse tree produced by CPPParser#bracedInitList.
    def exitBracedInitList(self, ctx:CPPParser.BracedInitListContext):
        pass


    # Enter a parse tree produced by CPPParser#className.
    def enterClassName(self, ctx:CPPParser.ClassNameContext):
        pass

    # Exit a parse tree produced by CPPParser#className.
    def exitClassName(self, ctx:CPPParser.ClassNameContext):
        pass


    # Enter a parse tree produced by CPPParser#classSpecifier.
    def enterClassSpecifier(self, ctx:CPPParser.ClassSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#classSpecifier.
    def exitClassSpecifier(self, ctx:CPPParser.ClassSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#classHead.
    def enterClassHead(self, ctx:CPPParser.ClassHeadContext):
        pass

    # Exit a parse tree produced by CPPParser#classHead.
    def exitClassHead(self, ctx:CPPParser.ClassHeadContext):
        pass


    # Enter a parse tree produced by CPPParser#classHeadName.
    def enterClassHeadName(self, ctx:CPPParser.ClassHeadNameContext):
        pass

    # Exit a parse tree produced by CPPParser#classHeadName.
    def exitClassHeadName(self, ctx:CPPParser.ClassHeadNameContext):
        pass


    # Enter a parse tree produced by CPPParser#classVirtSpecifier.
    def enterClassVirtSpecifier(self, ctx:CPPParser.ClassVirtSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#classVirtSpecifier.
    def exitClassVirtSpecifier(self, ctx:CPPParser.ClassVirtSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#classKey.
    def enterClassKey(self, ctx:CPPParser.ClassKeyContext):
        pass

    # Exit a parse tree produced by CPPParser#classKey.
    def exitClassKey(self, ctx:CPPParser.ClassKeyContext):
        pass


    # Enter a parse tree produced by CPPParser#memberSpecification.
    def enterMemberSpecification(self, ctx:CPPParser.MemberSpecificationContext):
        pass

    # Exit a parse tree produced by CPPParser#memberSpecification.
    def exitMemberSpecification(self, ctx:CPPParser.MemberSpecificationContext):
        pass


    # Enter a parse tree produced by CPPParser#memberdeclaration.
    def enterMemberdeclaration(self, ctx:CPPParser.MemberdeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#memberdeclaration.
    def exitMemberdeclaration(self, ctx:CPPParser.MemberdeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#memberDeclaratorList.
    def enterMemberDeclaratorList(self, ctx:CPPParser.MemberDeclaratorListContext):
        pass

    # Exit a parse tree produced by CPPParser#memberDeclaratorList.
    def exitMemberDeclaratorList(self, ctx:CPPParser.MemberDeclaratorListContext):
        pass


    # Enter a parse tree produced by CPPParser#memberDeclarator.
    def enterMemberDeclarator(self, ctx:CPPParser.MemberDeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#memberDeclarator.
    def exitMemberDeclarator(self, ctx:CPPParser.MemberDeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#virtualSpecifierSeq.
    def enterVirtualSpecifierSeq(self, ctx:CPPParser.VirtualSpecifierSeqContext):
        pass

    # Exit a parse tree produced by CPPParser#virtualSpecifierSeq.
    def exitVirtualSpecifierSeq(self, ctx:CPPParser.VirtualSpecifierSeqContext):
        pass


    # Enter a parse tree produced by CPPParser#virtualSpecifier.
    def enterVirtualSpecifier(self, ctx:CPPParser.VirtualSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#virtualSpecifier.
    def exitVirtualSpecifier(self, ctx:CPPParser.VirtualSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#pureSpecifier.
    def enterPureSpecifier(self, ctx:CPPParser.PureSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#pureSpecifier.
    def exitPureSpecifier(self, ctx:CPPParser.PureSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#baseClause.
    def enterBaseClause(self, ctx:CPPParser.BaseClauseContext):
        pass

    # Exit a parse tree produced by CPPParser#baseClause.
    def exitBaseClause(self, ctx:CPPParser.BaseClauseContext):
        pass


    # Enter a parse tree produced by CPPParser#baseSpecifierList.
    def enterBaseSpecifierList(self, ctx:CPPParser.BaseSpecifierListContext):
        pass

    # Exit a parse tree produced by CPPParser#baseSpecifierList.
    def exitBaseSpecifierList(self, ctx:CPPParser.BaseSpecifierListContext):
        pass


    # Enter a parse tree produced by CPPParser#baseSpecifier.
    def enterBaseSpecifier(self, ctx:CPPParser.BaseSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#baseSpecifier.
    def exitBaseSpecifier(self, ctx:CPPParser.BaseSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#classOrDeclType.
    def enterClassOrDeclType(self, ctx:CPPParser.ClassOrDeclTypeContext):
        pass

    # Exit a parse tree produced by CPPParser#classOrDeclType.
    def exitClassOrDeclType(self, ctx:CPPParser.ClassOrDeclTypeContext):
        pass


    # Enter a parse tree produced by CPPParser#baseTypeSpecifier.
    def enterBaseTypeSpecifier(self, ctx:CPPParser.BaseTypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#baseTypeSpecifier.
    def exitBaseTypeSpecifier(self, ctx:CPPParser.BaseTypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#accessSpecifier.
    def enterAccessSpecifier(self, ctx:CPPParser.AccessSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#accessSpecifier.
    def exitAccessSpecifier(self, ctx:CPPParser.AccessSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#conversionFunctionId.
    def enterConversionFunctionId(self, ctx:CPPParser.ConversionFunctionIdContext):
        pass

    # Exit a parse tree produced by CPPParser#conversionFunctionId.
    def exitConversionFunctionId(self, ctx:CPPParser.ConversionFunctionIdContext):
        pass


    # Enter a parse tree produced by CPPParser#conversionTypeId.
    def enterConversionTypeId(self, ctx:CPPParser.ConversionTypeIdContext):
        pass

    # Exit a parse tree produced by CPPParser#conversionTypeId.
    def exitConversionTypeId(self, ctx:CPPParser.ConversionTypeIdContext):
        pass


    # Enter a parse tree produced by CPPParser#conversionDeclarator.
    def enterConversionDeclarator(self, ctx:CPPParser.ConversionDeclaratorContext):
        pass

    # Exit a parse tree produced by CPPParser#conversionDeclarator.
    def exitConversionDeclarator(self, ctx:CPPParser.ConversionDeclaratorContext):
        pass


    # Enter a parse tree produced by CPPParser#constructorInitializer.
    def enterConstructorInitializer(self, ctx:CPPParser.ConstructorInitializerContext):
        pass

    # Exit a parse tree produced by CPPParser#constructorInitializer.
    def exitConstructorInitializer(self, ctx:CPPParser.ConstructorInitializerContext):
        pass


    # Enter a parse tree produced by CPPParser#memInitializerList.
    def enterMemInitializerList(self, ctx:CPPParser.MemInitializerListContext):
        pass

    # Exit a parse tree produced by CPPParser#memInitializerList.
    def exitMemInitializerList(self, ctx:CPPParser.MemInitializerListContext):
        pass


    # Enter a parse tree produced by CPPParser#memInitializer.
    def enterMemInitializer(self, ctx:CPPParser.MemInitializerContext):
        pass

    # Exit a parse tree produced by CPPParser#memInitializer.
    def exitMemInitializer(self, ctx:CPPParser.MemInitializerContext):
        pass


    # Enter a parse tree produced by CPPParser#meminitializerid.
    def enterMeminitializerid(self, ctx:CPPParser.MeminitializeridContext):
        pass

    # Exit a parse tree produced by CPPParser#meminitializerid.
    def exitMeminitializerid(self, ctx:CPPParser.MeminitializeridContext):
        pass


    # Enter a parse tree produced by CPPParser#operatorFunctionId.
    def enterOperatorFunctionId(self, ctx:CPPParser.OperatorFunctionIdContext):
        pass

    # Exit a parse tree produced by CPPParser#operatorFunctionId.
    def exitOperatorFunctionId(self, ctx:CPPParser.OperatorFunctionIdContext):
        pass


    # Enter a parse tree produced by CPPParser#literalOperatorId.
    def enterLiteralOperatorId(self, ctx:CPPParser.LiteralOperatorIdContext):
        pass

    # Exit a parse tree produced by CPPParser#literalOperatorId.
    def exitLiteralOperatorId(self, ctx:CPPParser.LiteralOperatorIdContext):
        pass


    # Enter a parse tree produced by CPPParser#templateDeclaration.
    def enterTemplateDeclaration(self, ctx:CPPParser.TemplateDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#templateDeclaration.
    def exitTemplateDeclaration(self, ctx:CPPParser.TemplateDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#templateparameterList.
    def enterTemplateparameterList(self, ctx:CPPParser.TemplateparameterListContext):
        pass

    # Exit a parse tree produced by CPPParser#templateparameterList.
    def exitTemplateparameterList(self, ctx:CPPParser.TemplateparameterListContext):
        pass


    # Enter a parse tree produced by CPPParser#templateParameter.
    def enterTemplateParameter(self, ctx:CPPParser.TemplateParameterContext):
        pass

    # Exit a parse tree produced by CPPParser#templateParameter.
    def exitTemplateParameter(self, ctx:CPPParser.TemplateParameterContext):
        pass


    # Enter a parse tree produced by CPPParser#typeParameter.
    def enterTypeParameter(self, ctx:CPPParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by CPPParser#typeParameter.
    def exitTypeParameter(self, ctx:CPPParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by CPPParser#simpleTemplateId.
    def enterSimpleTemplateId(self, ctx:CPPParser.SimpleTemplateIdContext):
        pass

    # Exit a parse tree produced by CPPParser#simpleTemplateId.
    def exitSimpleTemplateId(self, ctx:CPPParser.SimpleTemplateIdContext):
        pass


    # Enter a parse tree produced by CPPParser#templateId.
    def enterTemplateId(self, ctx:CPPParser.TemplateIdContext):
        pass

    # Exit a parse tree produced by CPPParser#templateId.
    def exitTemplateId(self, ctx:CPPParser.TemplateIdContext):
        pass


    # Enter a parse tree produced by CPPParser#templateName.
    def enterTemplateName(self, ctx:CPPParser.TemplateNameContext):
        pass

    # Exit a parse tree produced by CPPParser#templateName.
    def exitTemplateName(self, ctx:CPPParser.TemplateNameContext):
        pass


    # Enter a parse tree produced by CPPParser#templateArgumentList.
    def enterTemplateArgumentList(self, ctx:CPPParser.TemplateArgumentListContext):
        pass

    # Exit a parse tree produced by CPPParser#templateArgumentList.
    def exitTemplateArgumentList(self, ctx:CPPParser.TemplateArgumentListContext):
        pass


    # Enter a parse tree produced by CPPParser#templateArgument.
    def enterTemplateArgument(self, ctx:CPPParser.TemplateArgumentContext):
        pass

    # Exit a parse tree produced by CPPParser#templateArgument.
    def exitTemplateArgument(self, ctx:CPPParser.TemplateArgumentContext):
        pass


    # Enter a parse tree produced by CPPParser#typeNameSpecifier.
    def enterTypeNameSpecifier(self, ctx:CPPParser.TypeNameSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#typeNameSpecifier.
    def exitTypeNameSpecifier(self, ctx:CPPParser.TypeNameSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#explicitInstantiation.
    def enterExplicitInstantiation(self, ctx:CPPParser.ExplicitInstantiationContext):
        pass

    # Exit a parse tree produced by CPPParser#explicitInstantiation.
    def exitExplicitInstantiation(self, ctx:CPPParser.ExplicitInstantiationContext):
        pass


    # Enter a parse tree produced by CPPParser#explicitSpecialization.
    def enterExplicitSpecialization(self, ctx:CPPParser.ExplicitSpecializationContext):
        pass

    # Exit a parse tree produced by CPPParser#explicitSpecialization.
    def exitExplicitSpecialization(self, ctx:CPPParser.ExplicitSpecializationContext):
        pass


    # Enter a parse tree produced by CPPParser#tryBlock.
    def enterTryBlock(self, ctx:CPPParser.TryBlockContext):
        pass

    # Exit a parse tree produced by CPPParser#tryBlock.
    def exitTryBlock(self, ctx:CPPParser.TryBlockContext):
        pass


    # Enter a parse tree produced by CPPParser#functionTryBlock.
    def enterFunctionTryBlock(self, ctx:CPPParser.FunctionTryBlockContext):
        pass

    # Exit a parse tree produced by CPPParser#functionTryBlock.
    def exitFunctionTryBlock(self, ctx:CPPParser.FunctionTryBlockContext):
        pass


    # Enter a parse tree produced by CPPParser#handlerSeq.
    def enterHandlerSeq(self, ctx:CPPParser.HandlerSeqContext):
        pass

    # Exit a parse tree produced by CPPParser#handlerSeq.
    def exitHandlerSeq(self, ctx:CPPParser.HandlerSeqContext):
        pass


    # Enter a parse tree produced by CPPParser#handler.
    def enterHandler(self, ctx:CPPParser.HandlerContext):
        pass

    # Exit a parse tree produced by CPPParser#handler.
    def exitHandler(self, ctx:CPPParser.HandlerContext):
        pass


    # Enter a parse tree produced by CPPParser#exceptionDeclaration.
    def enterExceptionDeclaration(self, ctx:CPPParser.ExceptionDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#exceptionDeclaration.
    def exitExceptionDeclaration(self, ctx:CPPParser.ExceptionDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#throwExpression.
    def enterThrowExpression(self, ctx:CPPParser.ThrowExpressionContext):
        pass

    # Exit a parse tree produced by CPPParser#throwExpression.
    def exitThrowExpression(self, ctx:CPPParser.ThrowExpressionContext):
        pass


    # Enter a parse tree produced by CPPParser#exceptionSpecification.
    def enterExceptionSpecification(self, ctx:CPPParser.ExceptionSpecificationContext):
        pass

    # Exit a parse tree produced by CPPParser#exceptionSpecification.
    def exitExceptionSpecification(self, ctx:CPPParser.ExceptionSpecificationContext):
        pass


    # Enter a parse tree produced by CPPParser#dynamicExceptionSpecification.
    def enterDynamicExceptionSpecification(self, ctx:CPPParser.DynamicExceptionSpecificationContext):
        pass

    # Exit a parse tree produced by CPPParser#dynamicExceptionSpecification.
    def exitDynamicExceptionSpecification(self, ctx:CPPParser.DynamicExceptionSpecificationContext):
        pass


    # Enter a parse tree produced by CPPParser#typeIdList.
    def enterTypeIdList(self, ctx:CPPParser.TypeIdListContext):
        pass

    # Exit a parse tree produced by CPPParser#typeIdList.
    def exitTypeIdList(self, ctx:CPPParser.TypeIdListContext):
        pass


    # Enter a parse tree produced by CPPParser#noeExceptSpecification.
    def enterNoeExceptSpecification(self, ctx:CPPParser.NoeExceptSpecificationContext):
        pass

    # Exit a parse tree produced by CPPParser#noeExceptSpecification.
    def exitNoeExceptSpecification(self, ctx:CPPParser.NoeExceptSpecificationContext):
        pass


    # Enter a parse tree produced by CPPParser#theOperator.
    def enterTheOperator(self, ctx:CPPParser.TheOperatorContext):
        pass

    # Exit a parse tree produced by CPPParser#theOperator.
    def exitTheOperator(self, ctx:CPPParser.TheOperatorContext):
        pass


    # Enter a parse tree produced by CPPParser#literal.
    def enterLiteral(self, ctx:CPPParser.LiteralContext):
        pass

    # Exit a parse tree produced by CPPParser#literal.
    def exitLiteral(self, ctx:CPPParser.LiteralContext):
        pass



del CPPParser