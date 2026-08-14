# Generated from src/interface_generation/parser/CMOD.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CMODParser import CMODParser
else:
    from CMODParser import CMODParser

# This class defines a complete listener for a parse tree produced by CMODParser.
class CMODListener(ParseTreeListener):

    # Enter a parse tree produced by CMODParser#token.
    def enterToken(self, ctx:CMODParser.TokenContext):
        pass

    # Exit a parse tree produced by CMODParser#token.
    def exitToken(self, ctx:CMODParser.TokenContext):
        pass


    # Enter a parse tree produced by CMODParser#keyword.
    def enterKeyword(self, ctx:CMODParser.KeywordContext):
        pass

    # Exit a parse tree produced by CMODParser#keyword.
    def exitKeyword(self, ctx:CMODParser.KeywordContext):
        pass


    # Enter a parse tree produced by CMODParser#constant.
    def enterConstant(self, ctx:CMODParser.ConstantContext):
        pass

    # Exit a parse tree produced by CMODParser#constant.
    def exitConstant(self, ctx:CMODParser.ConstantContext):
        pass


    # Enter a parse tree produced by CMODParser#enumerationConstant.
    def enterEnumerationConstant(self, ctx:CMODParser.EnumerationConstantContext):
        pass

    # Exit a parse tree produced by CMODParser#enumerationConstant.
    def exitEnumerationConstant(self, ctx:CMODParser.EnumerationConstantContext):
        pass


    # Enter a parse tree produced by CMODParser#punctuator.
    def enterPunctuator(self, ctx:CMODParser.PunctuatorContext):
        pass

    # Exit a parse tree produced by CMODParser#punctuator.
    def exitPunctuator(self, ctx:CMODParser.PunctuatorContext):
        pass


    # Enter a parse tree produced by CMODParser#skipTokens.
    def enterSkipTokens(self, ctx:CMODParser.SkipTokensContext):
        pass

    # Exit a parse tree produced by CMODParser#skipTokens.
    def exitSkipTokens(self, ctx:CMODParser.SkipTokensContext):
        pass


    # Enter a parse tree produced by CMODParser#constantExpression.
    def enterConstantExpression(self, ctx:CMODParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by CMODParser#constantExpression.
    def exitConstantExpression(self, ctx:CMODParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by CMODParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:CMODParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by CMODParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:CMODParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by CMODParser#expression.
    def enterExpression(self, ctx:CMODParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CMODParser#expression.
    def exitExpression(self, ctx:CMODParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CMODParser#innerExpression.
    def enterInnerExpression(self, ctx:CMODParser.InnerExpressionContext):
        pass

    # Exit a parse tree produced by CMODParser#innerExpression.
    def exitInnerExpression(self, ctx:CMODParser.InnerExpressionContext):
        pass


    # Enter a parse tree produced by CMODParser#declaration.
    def enterDeclaration(self, ctx:CMODParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CMODParser#declaration.
    def exitDeclaration(self, ctx:CMODParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CMODParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:CMODParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by CMODParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:CMODParser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by CMODParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:CMODParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by CMODParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:CMODParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by CMODParser#initDeclarator.
    def enterInitDeclarator(self, ctx:CMODParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by CMODParser#initDeclarator.
    def exitInitDeclarator(self, ctx:CMODParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by CMODParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:CMODParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by CMODParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:CMODParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by CMODParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CMODParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CMODParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CMODParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CMODParser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx:CMODParser.StructOrUnionSpecifierContext):
        pass

    # Exit a parse tree produced by CMODParser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx:CMODParser.StructOrUnionSpecifierContext):
        pass


    # Enter a parse tree produced by CMODParser#structOrUnion.
    def enterStructOrUnion(self, ctx:CMODParser.StructOrUnionContext):
        pass

    # Exit a parse tree produced by CMODParser#structOrUnion.
    def exitStructOrUnion(self, ctx:CMODParser.StructOrUnionContext):
        pass


    # Enter a parse tree produced by CMODParser#structDeclaration.
    def enterStructDeclaration(self, ctx:CMODParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by CMODParser#structDeclaration.
    def exitStructDeclaration(self, ctx:CMODParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by CMODParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:CMODParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by CMODParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:CMODParser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by CMODParser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx:CMODParser.StructDeclaratorListContext):
        pass

    # Exit a parse tree produced by CMODParser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx:CMODParser.StructDeclaratorListContext):
        pass


    # Enter a parse tree produced by CMODParser#structDeclarator.
    def enterStructDeclarator(self, ctx:CMODParser.StructDeclaratorContext):
        pass

    # Exit a parse tree produced by CMODParser#structDeclarator.
    def exitStructDeclarator(self, ctx:CMODParser.StructDeclaratorContext):
        pass


    # Enter a parse tree produced by CMODParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:CMODParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by CMODParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:CMODParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by CMODParser#enumeratorList.
    def enterEnumeratorList(self, ctx:CMODParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by CMODParser#enumeratorList.
    def exitEnumeratorList(self, ctx:CMODParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by CMODParser#enumerator.
    def enterEnumerator(self, ctx:CMODParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by CMODParser#enumerator.
    def exitEnumerator(self, ctx:CMODParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by CMODParser#typeQualifier.
    def enterTypeQualifier(self, ctx:CMODParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by CMODParser#typeQualifier.
    def exitTypeQualifier(self, ctx:CMODParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by CMODParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:CMODParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by CMODParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:CMODParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by CMODParser#declarator.
    def enterDeclarator(self, ctx:CMODParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CMODParser#declarator.
    def exitDeclarator(self, ctx:CMODParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by CMODParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:CMODParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by CMODParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:CMODParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by CMODParser#pointer.
    def enterPointer(self, ctx:CMODParser.PointerContext):
        pass

    # Exit a parse tree produced by CMODParser#pointer.
    def exitPointer(self, ctx:CMODParser.PointerContext):
        pass


    # Enter a parse tree produced by CMODParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:CMODParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by CMODParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:CMODParser.TypeQualifierListContext):
        pass


    # Enter a parse tree produced by CMODParser#typedefName.
    def enterTypedefName(self, ctx:CMODParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by CMODParser#typedefName.
    def exitTypedefName(self, ctx:CMODParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by CMODParser#initializer.
    def enterInitializer(self, ctx:CMODParser.InitializerContext):
        pass

    # Exit a parse tree produced by CMODParser#initializer.
    def exitInitializer(self, ctx:CMODParser.InitializerContext):
        pass


    # Enter a parse tree produced by CMODParser#initializerList.
    def enterInitializerList(self, ctx:CMODParser.InitializerListContext):
        pass

    # Exit a parse tree produced by CMODParser#initializerList.
    def exitInitializerList(self, ctx:CMODParser.InitializerListContext):
        pass


    # Enter a parse tree produced by CMODParser#designation.
    def enterDesignation(self, ctx:CMODParser.DesignationContext):
        pass

    # Exit a parse tree produced by CMODParser#designation.
    def exitDesignation(self, ctx:CMODParser.DesignationContext):
        pass


    # Enter a parse tree produced by CMODParser#designator.
    def enterDesignator(self, ctx:CMODParser.DesignatorContext):
        pass

    # Exit a parse tree produced by CMODParser#designator.
    def exitDesignator(self, ctx:CMODParser.DesignatorContext):
        pass


    # Enter a parse tree produced by CMODParser#compoundStatement.
    def enterCompoundStatement(self, ctx:CMODParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by CMODParser#compoundStatement.
    def exitCompoundStatement(self, ctx:CMODParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by CMODParser#compilationUnit.
    def enterCompilationUnit(self, ctx:CMODParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CMODParser#compilationUnit.
    def exitCompilationUnit(self, ctx:CMODParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by CMODParser#translationUnit.
    def enterTranslationUnit(self, ctx:CMODParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by CMODParser#translationUnit.
    def exitTranslationUnit(self, ctx:CMODParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by CMODParser#moduleDeclaration.
    def enterModuleDeclaration(self, ctx:CMODParser.ModuleDeclarationContext):
        pass

    # Exit a parse tree produced by CMODParser#moduleDeclaration.
    def exitModuleDeclaration(self, ctx:CMODParser.ModuleDeclarationContext):
        pass


    # Enter a parse tree produced by CMODParser#importDeclaration.
    def enterImportDeclaration(self, ctx:CMODParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by CMODParser#importDeclaration.
    def exitImportDeclaration(self, ctx:CMODParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by CMODParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:CMODParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by CMODParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:CMODParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by CMODParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CMODParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CMODParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CMODParser.FunctionDefinitionContext):
        pass



del CMODParser