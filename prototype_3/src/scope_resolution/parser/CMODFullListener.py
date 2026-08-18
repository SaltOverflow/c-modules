# Generated from CMODFull.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CMODFullParser import CMODFullParser
else:
    from CMODFullParser import CMODFullParser

from src.scope_resolution.symbolTable import pushScope, popScope, addSymbol, getSymbol
from src.interface_generation.ListenerExtractSymbolDefinitions import SymbolType


# This class defines a complete listener for a parse tree produced by CMODFullParser.
class CMODFullListener(ParseTreeListener):

    # Enter a parse tree produced by CMODFullParser#token.
    def enterToken(self, ctx:CMODFullParser.TokenContext):
        pass

    # Exit a parse tree produced by CMODFullParser#token.
    def exitToken(self, ctx:CMODFullParser.TokenContext):
        pass


    # Enter a parse tree produced by CMODFullParser#keyword.
    def enterKeyword(self, ctx:CMODFullParser.KeywordContext):
        pass

    # Exit a parse tree produced by CMODFullParser#keyword.
    def exitKeyword(self, ctx:CMODFullParser.KeywordContext):
        pass


    # Enter a parse tree produced by CMODFullParser#constant.
    def enterConstant(self, ctx:CMODFullParser.ConstantContext):
        pass

    # Exit a parse tree produced by CMODFullParser#constant.
    def exitConstant(self, ctx:CMODFullParser.ConstantContext):
        pass


    # Enter a parse tree produced by CMODFullParser#enumerationConstant.
    def enterEnumerationConstant(self, ctx:CMODFullParser.EnumerationConstantContext):
        pass

    # Exit a parse tree produced by CMODFullParser#enumerationConstant.
    def exitEnumerationConstant(self, ctx:CMODFullParser.EnumerationConstantContext):
        pass


    # Enter a parse tree produced by CMODFullParser#punctuator.
    def enterPunctuator(self, ctx:CMODFullParser.PunctuatorContext):
        pass

    # Exit a parse tree produced by CMODFullParser#punctuator.
    def exitPunctuator(self, ctx:CMODFullParser.PunctuatorContext):
        pass


    # Enter a parse tree produced by CMODFullParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:CMODFullParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:CMODFullParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#postfixExpression.
    def enterPostfixExpression(self, ctx:CMODFullParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#postfixExpression.
    def exitPostfixExpression(self, ctx:CMODFullParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:CMODFullParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by CMODFullParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:CMODFullParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by CMODFullParser#unaryExpression.
    def enterUnaryExpression(self, ctx:CMODFullParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#unaryExpression.
    def exitUnaryExpression(self, ctx:CMODFullParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#unaryOperator.
    def enterUnaryOperator(self, ctx:CMODFullParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by CMODFullParser#unaryOperator.
    def exitUnaryOperator(self, ctx:CMODFullParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by CMODFullParser#castExpression.
    def enterCastExpression(self, ctx:CMODFullParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#castExpression.
    def exitCastExpression(self, ctx:CMODFullParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:CMODFullParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:CMODFullParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:CMODFullParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:CMODFullParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#shiftExpression.
    def enterShiftExpression(self, ctx:CMODFullParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#shiftExpression.
    def exitShiftExpression(self, ctx:CMODFullParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#relationalExpression.
    def enterRelationalExpression(self, ctx:CMODFullParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#relationalExpression.
    def exitRelationalExpression(self, ctx:CMODFullParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#equalityExpression.
    def enterEqualityExpression(self, ctx:CMODFullParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#equalityExpression.
    def exitEqualityExpression(self, ctx:CMODFullParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#andExpression.
    def enterAndExpression(self, ctx:CMODFullParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#andExpression.
    def exitAndExpression(self, ctx:CMODFullParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:CMODFullParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:CMODFullParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:CMODFullParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:CMODFullParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:CMODFullParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:CMODFullParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:CMODFullParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:CMODFullParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:CMODFullParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:CMODFullParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:CMODFullParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:CMODFullParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:CMODFullParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by CMODFullParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:CMODFullParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by CMODFullParser#expression.
    def enterExpression(self, ctx:CMODFullParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#expression.
    def exitExpression(self, ctx:CMODFullParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#constantExpression.
    def enterConstantExpression(self, ctx:CMODFullParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#constantExpression.
    def exitConstantExpression(self, ctx:CMODFullParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#declaration.
    def enterDeclaration(self, ctx:CMODFullParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CMODFullParser#declaration.
    def exitDeclaration(self, ctx:CMODFullParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CMODFullParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:CMODFullParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by CMODFullParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:CMODFullParser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by CMODFullParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:CMODFullParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by CMODFullParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:CMODFullParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by CMODFullParser#initDeclarator.
    def enterInitDeclarator(self, ctx:CMODFullParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by CMODFullParser#initDeclarator.
    def exitInitDeclarator(self, ctx:CMODFullParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by CMODFullParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:CMODFullParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by CMODFullParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:CMODFullParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by CMODFullParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CMODFullParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CMODFullParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CMODFullParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CMODFullParser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx:CMODFullParser.StructOrUnionSpecifierContext):
        pass

    # Exit a parse tree produced by CMODFullParser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx:CMODFullParser.StructOrUnionSpecifierContext):
        pass


    # Enter a parse tree produced by CMODFullParser#structOrUnion.
    def enterStructOrUnion(self, ctx:CMODFullParser.StructOrUnionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#structOrUnion.
    def exitStructOrUnion(self, ctx:CMODFullParser.StructOrUnionContext):
        pass


    # Enter a parse tree produced by CMODFullParser#structDeclaration.
    def enterStructDeclaration(self, ctx:CMODFullParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by CMODFullParser#structDeclaration.
    def exitStructDeclaration(self, ctx:CMODFullParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by CMODFullParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:CMODFullParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by CMODFullParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:CMODFullParser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by CMODFullParser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx:CMODFullParser.StructDeclaratorListContext):
        pass

    # Exit a parse tree produced by CMODFullParser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx:CMODFullParser.StructDeclaratorListContext):
        pass


    # Enter a parse tree produced by CMODFullParser#structDeclarator.
    def enterStructDeclarator(self, ctx:CMODFullParser.StructDeclaratorContext):
        pass

    # Exit a parse tree produced by CMODFullParser#structDeclarator.
    def exitStructDeclarator(self, ctx:CMODFullParser.StructDeclaratorContext):
        pass


    # Enter a parse tree produced by CMODFullParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:CMODFullParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by CMODFullParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:CMODFullParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by CMODFullParser#enumeratorList.
    def enterEnumeratorList(self, ctx:CMODFullParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by CMODFullParser#enumeratorList.
    def exitEnumeratorList(self, ctx:CMODFullParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by CMODFullParser#enumerator.
    def enterEnumerator(self, ctx:CMODFullParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by CMODFullParser#enumerator.
    def exitEnumerator(self, ctx:CMODFullParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by CMODFullParser#typeQualifier.
    def enterTypeQualifier(self, ctx:CMODFullParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by CMODFullParser#typeQualifier.
    def exitTypeQualifier(self, ctx:CMODFullParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by CMODFullParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:CMODFullParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by CMODFullParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:CMODFullParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by CMODFullParser#declarator.
    def enterDeclarator(self, ctx:CMODFullParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CMODFullParser#declarator.
    def exitDeclarator(self, ctx:CMODFullParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by CMODFullParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:CMODFullParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by CMODFullParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:CMODFullParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by CMODFullParser#pointer.
    def enterPointer(self, ctx:CMODFullParser.PointerContext):
        pass

    # Exit a parse tree produced by CMODFullParser#pointer.
    def exitPointer(self, ctx:CMODFullParser.PointerContext):
        pass


    # Enter a parse tree produced by CMODFullParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:CMODFullParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by CMODFullParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:CMODFullParser.TypeQualifierListContext):
        pass


    # Enter a parse tree produced by CMODFullParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:CMODFullParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by CMODFullParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:CMODFullParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by CMODFullParser#parameterList.
    def enterParameterList(self, ctx:CMODFullParser.ParameterListContext):
        pass

    # Exit a parse tree produced by CMODFullParser#parameterList.
    def exitParameterList(self, ctx:CMODFullParser.ParameterListContext):
        pass


    # Enter a parse tree produced by CMODFullParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:CMODFullParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by CMODFullParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:CMODFullParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by CMODFullParser#typeName.
    def enterTypeName(self, ctx:CMODFullParser.TypeNameContext):
        pass

    # Exit a parse tree produced by CMODFullParser#typeName.
    def exitTypeName(self, ctx:CMODFullParser.TypeNameContext):
        pass


    # Enter a parse tree produced by CMODFullParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:CMODFullParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by CMODFullParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:CMODFullParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by CMODFullParser#directAbstractDeclarator.
    def enterDirectAbstractDeclarator(self, ctx:CMODFullParser.DirectAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by CMODFullParser#directAbstractDeclarator.
    def exitDirectAbstractDeclarator(self, ctx:CMODFullParser.DirectAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by CMODFullParser#directAbstractDeclaratorAfter.
    def enterDirectAbstractDeclaratorAfter(self, ctx:CMODFullParser.DirectAbstractDeclaratorAfterContext):
        pass

    # Exit a parse tree produced by CMODFullParser#directAbstractDeclaratorAfter.
    def exitDirectAbstractDeclaratorAfter(self, ctx:CMODFullParser.DirectAbstractDeclaratorAfterContext):
        pass


    # Enter a parse tree produced by CMODFullParser#typedefName.
    def enterTypedefName(self, ctx:CMODFullParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by CMODFullParser#typedefName.
    def exitTypedefName(self, ctx:CMODFullParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by CMODFullParser#initializer.
    def enterInitializer(self, ctx:CMODFullParser.InitializerContext):
        pass

    # Exit a parse tree produced by CMODFullParser#initializer.
    def exitInitializer(self, ctx:CMODFullParser.InitializerContext):
        pass


    # Enter a parse tree produced by CMODFullParser#initializerList.
    def enterInitializerList(self, ctx:CMODFullParser.InitializerListContext):
        pass

    # Exit a parse tree produced by CMODFullParser#initializerList.
    def exitInitializerList(self, ctx:CMODFullParser.InitializerListContext):
        pass


    # Enter a parse tree produced by CMODFullParser#designation.
    def enterDesignation(self, ctx:CMODFullParser.DesignationContext):
        pass

    # Exit a parse tree produced by CMODFullParser#designation.
    def exitDesignation(self, ctx:CMODFullParser.DesignationContext):
        pass


    # Enter a parse tree produced by CMODFullParser#designator.
    def enterDesignator(self, ctx:CMODFullParser.DesignatorContext):
        pass

    # Exit a parse tree produced by CMODFullParser#designator.
    def exitDesignator(self, ctx:CMODFullParser.DesignatorContext):
        pass


    # Enter a parse tree produced by CMODFullParser#statement.
    def enterStatement(self, ctx:CMODFullParser.StatementContext):
        pass

    # Exit a parse tree produced by CMODFullParser#statement.
    def exitStatement(self, ctx:CMODFullParser.StatementContext):
        pass


    # Enter a parse tree produced by CMODFullParser#labeledStatement.
    def enterLabeledStatement(self, ctx:CMODFullParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by CMODFullParser#labeledStatement.
    def exitLabeledStatement(self, ctx:CMODFullParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by CMODFullParser#compoundStatement.
    def enterCompoundStatement(self, ctx:CMODFullParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by CMODFullParser#compoundStatement.
    def exitCompoundStatement(self, ctx:CMODFullParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by CMODFullParser#blockItemList.
    def enterBlockItemList(self, ctx:CMODFullParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by CMODFullParser#blockItemList.
    def exitBlockItemList(self, ctx:CMODFullParser.BlockItemListContext):
        pass


    # Enter a parse tree produced by CMODFullParser#blockItem.
    def enterBlockItem(self, ctx:CMODFullParser.BlockItemContext):
        pass

    # Exit a parse tree produced by CMODFullParser#blockItem.
    def exitBlockItem(self, ctx:CMODFullParser.BlockItemContext):
        pass


    # Enter a parse tree produced by CMODFullParser#expressionStatement.
    def enterExpressionStatement(self, ctx:CMODFullParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by CMODFullParser#expressionStatement.
    def exitExpressionStatement(self, ctx:CMODFullParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by CMODFullParser#selectionStatement.
    def enterSelectionStatement(self, ctx:CMODFullParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by CMODFullParser#selectionStatement.
    def exitSelectionStatement(self, ctx:CMODFullParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by CMODFullParser#iterationStatement.
    def enterIterationStatement(self, ctx:CMODFullParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by CMODFullParser#iterationStatement.
    def exitIterationStatement(self, ctx:CMODFullParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by CMODFullParser#jumpStatement.
    def enterJumpStatement(self, ctx:CMODFullParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by CMODFullParser#jumpStatement.
    def exitJumpStatement(self, ctx:CMODFullParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by CMODFullParser#compilationUnit.
    def enterCompilationUnit(self, ctx:CMODFullParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CMODFullParser#compilationUnit.
    def exitCompilationUnit(self, ctx:CMODFullParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by CMODFullParser#translationUnit.
    def enterTranslationUnit(self, ctx:CMODFullParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by CMODFullParser#translationUnit.
    def exitTranslationUnit(self, ctx:CMODFullParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by CMODFullParser#moduleDeclaration.
    def enterModuleDeclaration(self, ctx:CMODFullParser.ModuleDeclarationContext):
        pass

    # Exit a parse tree produced by CMODFullParser#moduleDeclaration.
    def exitModuleDeclaration(self, ctx:CMODFullParser.ModuleDeclarationContext):
        pass


    # Enter a parse tree produced by CMODFullParser#importDeclaration.
    def enterImportDeclaration(self, ctx:CMODFullParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by CMODFullParser#importDeclaration.
    def exitImportDeclaration(self, ctx:CMODFullParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by CMODFullParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:CMODFullParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by CMODFullParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:CMODFullParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by CMODFullParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CMODFullParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CMODFullParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CMODFullParser.FunctionDefinitionContext):
        pass



del CMODFullParser