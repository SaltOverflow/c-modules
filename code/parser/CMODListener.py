# Generated from parser/CMOD.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CMODParser import CMODParser
else:
    from CMODParser import CMODParser

# This class defines a complete listener for a parse tree produced by CMODParser.
class CMODListener(ParseTreeListener):

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


    # Enter a parse tree produced by CMODParser#limitedFunctionDefinition.
    def enterLimitedFunctionDefinition(self, ctx:CMODParser.LimitedFunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CMODParser#limitedFunctionDefinition.
    def exitLimitedFunctionDefinition(self, ctx:CMODParser.LimitedFunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CMODParser#limitedTypeSpecifier.
    def enterLimitedTypeSpecifier(self, ctx:CMODParser.LimitedTypeSpecifierContext):
        pass

    # Exit a parse tree produced by CMODParser#limitedTypeSpecifier.
    def exitLimitedTypeSpecifier(self, ctx:CMODParser.LimitedTypeSpecifierContext):
        pass


    # Enter a parse tree produced by CMODParser#limitedDeclarator.
    def enterLimitedDeclarator(self, ctx:CMODParser.LimitedDeclaratorContext):
        pass

    # Exit a parse tree produced by CMODParser#limitedDeclarator.
    def exitLimitedDeclarator(self, ctx:CMODParser.LimitedDeclaratorContext):
        pass


    # Enter a parse tree produced by CMODParser#limitedParameterList.
    def enterLimitedParameterList(self, ctx:CMODParser.LimitedParameterListContext):
        pass

    # Exit a parse tree produced by CMODParser#limitedParameterList.
    def exitLimitedParameterList(self, ctx:CMODParser.LimitedParameterListContext):
        pass


    # Enter a parse tree produced by CMODParser#limitedCompoundStatement.
    def enterLimitedCompoundStatement(self, ctx:CMODParser.LimitedCompoundStatementContext):
        pass

    # Exit a parse tree produced by CMODParser#limitedCompoundStatement.
    def exitLimitedCompoundStatement(self, ctx:CMODParser.LimitedCompoundStatementContext):
        pass


    # Enter a parse tree produced by CMODParser#limitedStatement.
    def enterLimitedStatement(self, ctx:CMODParser.LimitedStatementContext):
        pass

    # Exit a parse tree produced by CMODParser#limitedStatement.
    def exitLimitedStatement(self, ctx:CMODParser.LimitedStatementContext):
        pass


    # Enter a parse tree produced by CMODParser#limitedGlobal.
    def enterLimitedGlobal(self, ctx:CMODParser.LimitedGlobalContext):
        pass

    # Exit a parse tree produced by CMODParser#limitedGlobal.
    def exitLimitedGlobal(self, ctx:CMODParser.LimitedGlobalContext):
        pass


    # Enter a parse tree produced by CMODParser#limitedInitializer.
    def enterLimitedInitializer(self, ctx:CMODParser.LimitedInitializerContext):
        pass

    # Exit a parse tree produced by CMODParser#limitedInitializer.
    def exitLimitedInitializer(self, ctx:CMODParser.LimitedInitializerContext):
        pass


    # Enter a parse tree produced by CMODParser#limitedStruct.
    def enterLimitedStruct(self, ctx:CMODParser.LimitedStructContext):
        pass

    # Exit a parse tree produced by CMODParser#limitedStruct.
    def exitLimitedStruct(self, ctx:CMODParser.LimitedStructContext):
        pass



del CMODParser