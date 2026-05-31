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


    # Enter a parse tree produced by CMODParser#structUnionDefinition.
    def enterStructUnionDefinition(self, ctx:CMODParser.StructUnionDefinitionContext):
        pass

    # Exit a parse tree produced by CMODParser#structUnionDefinition.
    def exitStructUnionDefinition(self, ctx:CMODParser.StructUnionDefinitionContext):
        pass


    # Enter a parse tree produced by CMODParser#structField.
    def enterStructField(self, ctx:CMODParser.StructFieldContext):
        pass

    # Exit a parse tree produced by CMODParser#structField.
    def exitStructField(self, ctx:CMODParser.StructFieldContext):
        pass


    # Enter a parse tree produced by CMODParser#typedefDefinition.
    def enterTypedefDefinition(self, ctx:CMODParser.TypedefDefinitionContext):
        pass

    # Exit a parse tree produced by CMODParser#typedefDefinition.
    def exitTypedefDefinition(self, ctx:CMODParser.TypedefDefinitionContext):
        pass


    # Enter a parse tree produced by CMODParser#globalDefinition.
    def enterGlobalDefinition(self, ctx:CMODParser.GlobalDefinitionContext):
        pass

    # Exit a parse tree produced by CMODParser#globalDefinition.
    def exitGlobalDefinition(self, ctx:CMODParser.GlobalDefinitionContext):
        pass


    # Enter a parse tree produced by CMODParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CMODParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CMODParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CMODParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CMODParser#parameterList.
    def enterParameterList(self, ctx:CMODParser.ParameterListContext):
        pass

    # Exit a parse tree produced by CMODParser#parameterList.
    def exitParameterList(self, ctx:CMODParser.ParameterListContext):
        pass


    # Enter a parse tree produced by CMODParser#compoundStatement.
    def enterCompoundStatement(self, ctx:CMODParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by CMODParser#compoundStatement.
    def exitCompoundStatement(self, ctx:CMODParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by CMODParser#statement.
    def enterStatement(self, ctx:CMODParser.StatementContext):
        pass

    # Exit a parse tree produced by CMODParser#statement.
    def exitStatement(self, ctx:CMODParser.StatementContext):
        pass


    # Enter a parse tree produced by CMODParser#expression.
    def enterExpression(self, ctx:CMODParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CMODParser#expression.
    def exitExpression(self, ctx:CMODParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CMODParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CMODParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CMODParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CMODParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CMODParser#declarator.
    def enterDeclarator(self, ctx:CMODParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CMODParser#declarator.
    def exitDeclarator(self, ctx:CMODParser.DeclaratorContext):
        pass



del CMODParser