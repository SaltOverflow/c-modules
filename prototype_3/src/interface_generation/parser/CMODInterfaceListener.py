# Generated from CMODInterface.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CMODInterfaceParser import CMODInterfaceParser
else:
    from CMODInterfaceParser import CMODInterfaceParser

# This class defines a complete listener for a parse tree produced by CMODInterfaceParser.
class CMODInterfaceListener(ParseTreeListener):

    # Enter a parse tree produced by CMODInterfaceParser#token.
    def enterToken(self, ctx:CMODInterfaceParser.TokenContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#token.
    def exitToken(self, ctx:CMODInterfaceParser.TokenContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#keyword.
    def enterKeyword(self, ctx:CMODInterfaceParser.KeywordContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#keyword.
    def exitKeyword(self, ctx:CMODInterfaceParser.KeywordContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#constant.
    def enterConstant(self, ctx:CMODInterfaceParser.ConstantContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#constant.
    def exitConstant(self, ctx:CMODInterfaceParser.ConstantContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#enumerationConstant.
    def enterEnumerationConstant(self, ctx:CMODInterfaceParser.EnumerationConstantContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#enumerationConstant.
    def exitEnumerationConstant(self, ctx:CMODInterfaceParser.EnumerationConstantContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#punctuator.
    def enterPunctuator(self, ctx:CMODInterfaceParser.PunctuatorContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#punctuator.
    def exitPunctuator(self, ctx:CMODInterfaceParser.PunctuatorContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#skipTokens.
    def enterSkipTokens(self, ctx:CMODInterfaceParser.SkipTokensContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#skipTokens.
    def exitSkipTokens(self, ctx:CMODInterfaceParser.SkipTokensContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#constantExpression.
    def enterConstantExpression(self, ctx:CMODInterfaceParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#constantExpression.
    def exitConstantExpression(self, ctx:CMODInterfaceParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:CMODInterfaceParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:CMODInterfaceParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#expression.
    def enterExpression(self, ctx:CMODInterfaceParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#expression.
    def exitExpression(self, ctx:CMODInterfaceParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#innerExpression.
    def enterInnerExpression(self, ctx:CMODInterfaceParser.InnerExpressionContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#innerExpression.
    def exitInnerExpression(self, ctx:CMODInterfaceParser.InnerExpressionContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#declaration.
    def enterDeclaration(self, ctx:CMODInterfaceParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#declaration.
    def exitDeclaration(self, ctx:CMODInterfaceParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:CMODInterfaceParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:CMODInterfaceParser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:CMODInterfaceParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:CMODInterfaceParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#initDeclarator.
    def enterInitDeclarator(self, ctx:CMODInterfaceParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#initDeclarator.
    def exitInitDeclarator(self, ctx:CMODInterfaceParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:CMODInterfaceParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:CMODInterfaceParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CMODInterfaceParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CMODInterfaceParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx:CMODInterfaceParser.StructOrUnionSpecifierContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx:CMODInterfaceParser.StructOrUnionSpecifierContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#structOrUnion.
    def enterStructOrUnion(self, ctx:CMODInterfaceParser.StructOrUnionContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#structOrUnion.
    def exitStructOrUnion(self, ctx:CMODInterfaceParser.StructOrUnionContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#structDeclaration.
    def enterStructDeclaration(self, ctx:CMODInterfaceParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#structDeclaration.
    def exitStructDeclaration(self, ctx:CMODInterfaceParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:CMODInterfaceParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:CMODInterfaceParser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx:CMODInterfaceParser.StructDeclaratorListContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx:CMODInterfaceParser.StructDeclaratorListContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#structDeclarator.
    def enterStructDeclarator(self, ctx:CMODInterfaceParser.StructDeclaratorContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#structDeclarator.
    def exitStructDeclarator(self, ctx:CMODInterfaceParser.StructDeclaratorContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:CMODInterfaceParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:CMODInterfaceParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#enumeratorList.
    def enterEnumeratorList(self, ctx:CMODInterfaceParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#enumeratorList.
    def exitEnumeratorList(self, ctx:CMODInterfaceParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#enumerator.
    def enterEnumerator(self, ctx:CMODInterfaceParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#enumerator.
    def exitEnumerator(self, ctx:CMODInterfaceParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#typeQualifier.
    def enterTypeQualifier(self, ctx:CMODInterfaceParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#typeQualifier.
    def exitTypeQualifier(self, ctx:CMODInterfaceParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:CMODInterfaceParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:CMODInterfaceParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#declarator.
    def enterDeclarator(self, ctx:CMODInterfaceParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#declarator.
    def exitDeclarator(self, ctx:CMODInterfaceParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:CMODInterfaceParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:CMODInterfaceParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#pointer.
    def enterPointer(self, ctx:CMODInterfaceParser.PointerContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#pointer.
    def exitPointer(self, ctx:CMODInterfaceParser.PointerContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:CMODInterfaceParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:CMODInterfaceParser.TypeQualifierListContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#typedefName.
    def enterTypedefName(self, ctx:CMODInterfaceParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#typedefName.
    def exitTypedefName(self, ctx:CMODInterfaceParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#initializer.
    def enterInitializer(self, ctx:CMODInterfaceParser.InitializerContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#initializer.
    def exitInitializer(self, ctx:CMODInterfaceParser.InitializerContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#initializerList.
    def enterInitializerList(self, ctx:CMODInterfaceParser.InitializerListContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#initializerList.
    def exitInitializerList(self, ctx:CMODInterfaceParser.InitializerListContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#designation.
    def enterDesignation(self, ctx:CMODInterfaceParser.DesignationContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#designation.
    def exitDesignation(self, ctx:CMODInterfaceParser.DesignationContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#designator.
    def enterDesignator(self, ctx:CMODInterfaceParser.DesignatorContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#designator.
    def exitDesignator(self, ctx:CMODInterfaceParser.DesignatorContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#compoundStatement.
    def enterCompoundStatement(self, ctx:CMODInterfaceParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#compoundStatement.
    def exitCompoundStatement(self, ctx:CMODInterfaceParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#compilationUnit.
    def enterCompilationUnit(self, ctx:CMODInterfaceParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#compilationUnit.
    def exitCompilationUnit(self, ctx:CMODInterfaceParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#translationUnit.
    def enterTranslationUnit(self, ctx:CMODInterfaceParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#translationUnit.
    def exitTranslationUnit(self, ctx:CMODInterfaceParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#moduleDeclaration.
    def enterModuleDeclaration(self, ctx:CMODInterfaceParser.ModuleDeclarationContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#moduleDeclaration.
    def exitModuleDeclaration(self, ctx:CMODInterfaceParser.ModuleDeclarationContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#importDeclaration.
    def enterImportDeclaration(self, ctx:CMODInterfaceParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#importDeclaration.
    def exitImportDeclaration(self, ctx:CMODInterfaceParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:CMODInterfaceParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:CMODInterfaceParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by CMODInterfaceParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CMODInterfaceParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CMODInterfaceParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CMODInterfaceParser.FunctionDefinitionContext):
        pass



del CMODInterfaceParser