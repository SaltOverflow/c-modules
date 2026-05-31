# Generated from parser/CMOD.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,231,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,1,1,1,5,1,
        42,8,1,10,1,12,1,45,9,1,1,1,5,1,48,8,1,10,1,12,1,51,9,1,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,4,3,4,62,8,4,1,4,1,4,3,4,66,8,4,1,4,1,
        4,3,4,70,8,4,1,4,1,4,3,4,74,8,4,1,4,1,4,3,4,78,8,4,1,5,1,5,1,5,1,
        5,5,5,84,8,5,10,5,12,5,87,9,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,109,8,8,1,8,1,
        8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,119,8,9,1,9,1,9,1,9,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,134,8,10,10,10,12,10,137,
        9,10,1,11,1,11,5,11,141,8,11,10,11,12,11,144,9,11,1,11,1,11,1,12,
        3,12,149,8,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,5,13,188,8,13,10,13,12,13,191,9,13,1,13,3,13,194,8,13,1,13,
        1,13,5,13,198,8,13,10,13,12,13,201,9,13,1,14,5,14,204,8,14,10,14,
        12,14,207,9,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,3,16,223,8,16,1,17,1,17,3,17,227,8,17,1,17,1,
        17,1,17,0,1,26,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,0,2,1,0,5,6,1,0,30,31,264,0,36,1,0,0,0,2,39,1,0,0,0,4,52,1,0,
        0,0,6,56,1,0,0,0,8,77,1,0,0,0,10,79,1,0,0,0,12,91,1,0,0,0,14,97,
        1,0,0,0,16,102,1,0,0,0,18,112,1,0,0,0,20,123,1,0,0,0,22,138,1,0,
        0,0,24,148,1,0,0,0,26,193,1,0,0,0,28,205,1,0,0,0,30,208,1,0,0,0,
        32,222,1,0,0,0,34,226,1,0,0,0,36,37,3,2,1,0,37,38,5,0,0,1,38,1,1,
        0,0,0,39,43,3,4,2,0,40,42,3,6,3,0,41,40,1,0,0,0,42,45,1,0,0,0,43,
        41,1,0,0,0,43,44,1,0,0,0,44,49,1,0,0,0,45,43,1,0,0,0,46,48,3,8,4,
        0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,3,1,
        0,0,0,51,49,1,0,0,0,52,53,5,1,0,0,53,54,5,39,0,0,54,55,5,2,0,0,55,
        5,1,0,0,0,56,57,5,3,0,0,57,58,5,39,0,0,58,59,5,2,0,0,59,7,1,0,0,
        0,60,62,5,4,0,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,78,
        3,10,5,0,64,66,5,4,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,
        67,78,3,14,7,0,68,70,5,4,0,0,69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,
        0,0,0,71,78,3,16,8,0,72,74,5,4,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,
        75,1,0,0,0,75,78,3,18,9,0,76,78,5,2,0,0,77,61,1,0,0,0,77,65,1,0,
        0,0,77,69,1,0,0,0,77,73,1,0,0,0,77,76,1,0,0,0,78,9,1,0,0,0,79,80,
        7,0,0,0,80,81,5,39,0,0,81,85,5,7,0,0,82,84,3,12,6,0,83,82,1,0,0,
        0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,
        1,0,0,0,88,89,5,8,0,0,89,90,5,2,0,0,90,11,1,0,0,0,91,92,3,28,14,
        0,92,93,3,32,16,0,93,94,3,28,14,0,94,95,3,34,17,0,95,96,5,2,0,0,
        96,13,1,0,0,0,97,98,5,9,0,0,98,99,3,26,13,0,99,100,5,39,0,0,100,
        101,5,2,0,0,101,15,1,0,0,0,102,103,3,28,14,0,103,104,3,32,16,0,104,
        105,3,28,14,0,105,108,3,34,17,0,106,107,5,10,0,0,107,109,3,26,13,
        0,108,106,1,0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,110,111,5,2,0,
        0,111,17,1,0,0,0,112,113,3,28,14,0,113,114,3,32,16,0,114,115,3,28,
        14,0,115,116,3,34,17,0,116,118,5,11,0,0,117,119,3,20,10,0,118,117,
        1,0,0,0,118,119,1,0,0,0,119,120,1,0,0,0,120,121,5,12,0,0,121,122,
        3,22,11,0,122,19,1,0,0,0,123,124,3,28,14,0,124,125,3,32,16,0,125,
        126,3,28,14,0,126,135,3,34,17,0,127,128,5,13,0,0,128,129,3,28,14,
        0,129,130,3,32,16,0,130,131,3,28,14,0,131,132,3,34,17,0,132,134,
        1,0,0,0,133,127,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,
        1,0,0,0,136,21,1,0,0,0,137,135,1,0,0,0,138,142,5,7,0,0,139,141,3,
        24,12,0,140,139,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,
        1,0,0,0,143,145,1,0,0,0,144,142,1,0,0,0,145,146,5,8,0,0,146,23,1,
        0,0,0,147,149,5,9,0,0,148,147,1,0,0,0,148,149,1,0,0,0,149,150,1,
        0,0,0,150,151,3,26,13,0,151,152,5,2,0,0,152,25,1,0,0,0,153,154,6,
        13,-1,0,154,194,5,13,0,0,155,194,5,14,0,0,156,194,5,15,0,0,157,194,
        5,16,0,0,158,194,5,17,0,0,159,194,5,18,0,0,160,194,5,19,0,0,161,
        194,5,20,0,0,162,194,5,21,0,0,163,194,5,22,0,0,164,194,5,23,0,0,
        165,194,5,24,0,0,166,194,5,25,0,0,167,194,5,10,0,0,168,194,5,26,
        0,0,169,194,5,27,0,0,170,171,5,11,0,0,171,172,3,26,13,0,172,173,
        5,12,0,0,173,194,1,0,0,0,174,175,5,28,0,0,175,176,3,26,13,0,176,
        177,5,29,0,0,177,194,1,0,0,0,178,179,5,7,0,0,179,180,3,26,13,0,180,
        181,5,8,0,0,181,194,1,0,0,0,182,194,5,42,0,0,183,194,5,41,0,0,184,
        194,5,40,0,0,185,189,3,32,16,0,186,188,5,16,0,0,187,186,1,0,0,0,
        188,191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,194,1,0,0,0,
        191,189,1,0,0,0,192,194,3,30,15,0,193,153,1,0,0,0,193,155,1,0,0,
        0,193,156,1,0,0,0,193,157,1,0,0,0,193,158,1,0,0,0,193,159,1,0,0,
        0,193,160,1,0,0,0,193,161,1,0,0,0,193,162,1,0,0,0,193,163,1,0,0,
        0,193,164,1,0,0,0,193,165,1,0,0,0,193,166,1,0,0,0,193,167,1,0,0,
        0,193,168,1,0,0,0,193,169,1,0,0,0,193,170,1,0,0,0,193,174,1,0,0,
        0,193,178,1,0,0,0,193,182,1,0,0,0,193,183,1,0,0,0,193,184,1,0,0,
        0,193,185,1,0,0,0,193,192,1,0,0,0,194,199,1,0,0,0,195,196,10,25,
        0,0,196,198,3,26,13,26,197,195,1,0,0,0,198,201,1,0,0,0,199,197,1,
        0,0,0,199,200,1,0,0,0,200,27,1,0,0,0,201,199,1,0,0,0,202,204,3,30,
        15,0,203,202,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,
        0,0,206,29,1,0,0,0,207,205,1,0,0,0,208,209,7,1,0,0,209,31,1,0,0,
        0,210,223,5,32,0,0,211,223,5,33,0,0,212,223,5,34,0,0,213,223,5,35,
        0,0,214,223,5,36,0,0,215,223,5,37,0,0,216,223,5,38,0,0,217,218,5,
        5,0,0,218,223,5,39,0,0,219,220,5,6,0,0,220,223,5,39,0,0,221,223,
        5,39,0,0,222,210,1,0,0,0,222,211,1,0,0,0,222,212,1,0,0,0,222,213,
        1,0,0,0,222,214,1,0,0,0,222,215,1,0,0,0,222,216,1,0,0,0,222,217,
        1,0,0,0,222,219,1,0,0,0,222,221,1,0,0,0,223,33,1,0,0,0,224,225,5,
        16,0,0,225,227,3,28,14,0,226,224,1,0,0,0,226,227,1,0,0,0,227,228,
        1,0,0,0,228,229,5,39,0,0,229,35,1,0,0,0,19,43,49,61,65,69,73,77,
        85,108,118,135,142,148,189,193,199,205,222,226
    ]

class CMODParser ( Parser ):

    grammarFileName = "CMOD.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'module'", "';'", "'import'", "'export'", 
                     "'struct'", "'union'", "'{'", "'}'", "'typedef'", "'='", 
                     "'('", "')'", "','", "'.'", "'->'", "'*'", "'/'", "'+'", 
                     "'-'", "'!'", "'~'", "'&'", "'|'", "'?'", "':'", "'<'", 
                     "'>'", "'['", "']'", "'const'", "'volatile'", "'void'", 
                     "'char'", "'short'", "'int'", "'long'", "'float'", 
                     "'double'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Identifier", 
                      "Number", "CharLiteral", "StringLiteral", "Whitespace", 
                      "Newline", "BlockComment", "LineComment" ]

    RULE_compilationUnit = 0
    RULE_translationUnit = 1
    RULE_moduleDeclaration = 2
    RULE_importDeclaration = 3
    RULE_externalDeclaration = 4
    RULE_structUnionDefinition = 5
    RULE_structField = 6
    RULE_typedefDefinition = 7
    RULE_globalDefinition = 8
    RULE_functionDefinition = 9
    RULE_parameterList = 10
    RULE_compoundStatement = 11
    RULE_statement = 12
    RULE_expression = 13
    RULE_typeQualifierList = 14
    RULE_typeQualifier = 15
    RULE_typeSpecifier = 16
    RULE_declarator = 17

    ruleNames =  [ "compilationUnit", "translationUnit", "moduleDeclaration", 
                   "importDeclaration", "externalDeclaration", "structUnionDefinition", 
                   "structField", "typedefDefinition", "globalDefinition", 
                   "functionDefinition", "parameterList", "compoundStatement", 
                   "statement", "expression", "typeQualifierList", "typeQualifier", 
                   "typeSpecifier", "declarator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    Identifier=39
    Number=40
    CharLiteral=41
    StringLiteral=42
    Whitespace=43
    Newline=44
    BlockComment=45
    LineComment=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def translationUnit(self):
            return self.getTypedRuleContext(CMODParser.TranslationUnitContext,0)


        def EOF(self):
            return self.getToken(CMODParser.EOF, 0)

        def getRuleIndex(self):
            return CMODParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)




    def compilationUnit(self):

        localctx = CMODParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.translationUnit()
            self.state = 37
            self.match(CMODParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TranslationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moduleDeclaration(self):
            return self.getTypedRuleContext(CMODParser.ModuleDeclarationContext,0)


        def importDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.ImportDeclarationContext)
            else:
                return self.getTypedRuleContext(CMODParser.ImportDeclarationContext,i)


        def externalDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.ExternalDeclarationContext)
            else:
                return self.getTypedRuleContext(CMODParser.ExternalDeclarationContext,i)


        def getRuleIndex(self):
            return CMODParser.RULE_translationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTranslationUnit" ):
                listener.enterTranslationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTranslationUnit" ):
                listener.exitTranslationUnit(self)




    def translationUnit(self):

        localctx = CMODParser.TranslationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_translationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.moduleDeclaration()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 40
                self.importDeclaration()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1098437886580) != 0):
                self.state = 46
                self.externalDeclaration()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModuleDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CMODParser.Identifier, 0)

        def getRuleIndex(self):
            return CMODParser.RULE_moduleDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModuleDeclaration" ):
                listener.enterModuleDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModuleDeclaration" ):
                listener.exitModuleDeclaration(self)




    def moduleDeclaration(self):

        localctx = CMODParser.ModuleDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_moduleDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(CMODParser.T__0)
            self.state = 53
            self.match(CMODParser.Identifier)
            self.state = 54
            self.match(CMODParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CMODParser.Identifier, 0)

        def getRuleIndex(self):
            return CMODParser.RULE_importDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportDeclaration" ):
                listener.enterImportDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportDeclaration" ):
                listener.exitImportDeclaration(self)




    def importDeclaration(self):

        localctx = CMODParser.ImportDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_importDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(CMODParser.T__2)
            self.state = 57
            self.match(CMODParser.Identifier)
            self.state = 58
            self.match(CMODParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExternalDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structUnionDefinition(self):
            return self.getTypedRuleContext(CMODParser.StructUnionDefinitionContext,0)


        def typedefDefinition(self):
            return self.getTypedRuleContext(CMODParser.TypedefDefinitionContext,0)


        def globalDefinition(self):
            return self.getTypedRuleContext(CMODParser.GlobalDefinitionContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(CMODParser.FunctionDefinitionContext,0)


        def getRuleIndex(self):
            return CMODParser.RULE_externalDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExternalDeclaration" ):
                listener.enterExternalDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExternalDeclaration" ):
                listener.exitExternalDeclaration(self)




    def externalDeclaration(self):

        localctx = CMODParser.ExternalDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_externalDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 60
                    self.match(CMODParser.T__3)


                self.state = 63
                self.structUnionDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 64
                    self.match(CMODParser.T__3)


                self.state = 67
                self.typedefDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 68
                    self.match(CMODParser.T__3)


                self.state = 71
                self.globalDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 72
                    self.match(CMODParser.T__3)


                self.state = 75
                self.functionDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.match(CMODParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructUnionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CMODParser.Identifier, 0)

        def structField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.StructFieldContext)
            else:
                return self.getTypedRuleContext(CMODParser.StructFieldContext,i)


        def getRuleIndex(self):
            return CMODParser.RULE_structUnionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructUnionDefinition" ):
                listener.enterStructUnionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructUnionDefinition" ):
                listener.exitStructUnionDefinition(self)




    def structUnionDefinition(self):

        localctx = CMODParser.StructUnionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_structUnionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 80
            self.match(CMODParser.Identifier)
            self.state = 81
            self.match(CMODParser.T__6)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1098437886048) != 0):
                self.state = 82
                self.structField()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(CMODParser.T__7)
            self.state = 89
            self.match(CMODParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeQualifierList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.TypeQualifierListContext)
            else:
                return self.getTypedRuleContext(CMODParser.TypeQualifierListContext,i)


        def typeSpecifier(self):
            return self.getTypedRuleContext(CMODParser.TypeSpecifierContext,0)


        def declarator(self):
            return self.getTypedRuleContext(CMODParser.DeclaratorContext,0)


        def getRuleIndex(self):
            return CMODParser.RULE_structField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructField" ):
                listener.enterStructField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructField" ):
                listener.exitStructField(self)




    def structField(self):

        localctx = CMODParser.StructFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_structField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.typeQualifierList()
            self.state = 92
            self.typeSpecifier()
            self.state = 93
            self.typeQualifierList()
            self.state = 94
            self.declarator()
            self.state = 95
            self.match(CMODParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedefDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CMODParser.ExpressionContext,0)


        def Identifier(self):
            return self.getToken(CMODParser.Identifier, 0)

        def getRuleIndex(self):
            return CMODParser.RULE_typedefDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedefDefinition" ):
                listener.enterTypedefDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedefDefinition" ):
                listener.exitTypedefDefinition(self)




    def typedefDefinition(self):

        localctx = CMODParser.TypedefDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typedefDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(CMODParser.T__8)
            self.state = 98
            self.expression(0)
            self.state = 99
            self.match(CMODParser.Identifier)
            self.state = 100
            self.match(CMODParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeQualifierList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.TypeQualifierListContext)
            else:
                return self.getTypedRuleContext(CMODParser.TypeQualifierListContext,i)


        def typeSpecifier(self):
            return self.getTypedRuleContext(CMODParser.TypeSpecifierContext,0)


        def declarator(self):
            return self.getTypedRuleContext(CMODParser.DeclaratorContext,0)


        def expression(self):
            return self.getTypedRuleContext(CMODParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CMODParser.RULE_globalDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalDefinition" ):
                listener.enterGlobalDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalDefinition" ):
                listener.exitGlobalDefinition(self)




    def globalDefinition(self):

        localctx = CMODParser.GlobalDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_globalDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.typeQualifierList()
            self.state = 103
            self.typeSpecifier()
            self.state = 104
            self.typeQualifierList()
            self.state = 105
            self.declarator()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 106
                self.match(CMODParser.T__9)
                self.state = 107
                self.expression(0)


            self.state = 110
            self.match(CMODParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeQualifierList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.TypeQualifierListContext)
            else:
                return self.getTypedRuleContext(CMODParser.TypeQualifierListContext,i)


        def typeSpecifier(self):
            return self.getTypedRuleContext(CMODParser.TypeSpecifierContext,0)


        def declarator(self):
            return self.getTypedRuleContext(CMODParser.DeclaratorContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(CMODParser.CompoundStatementContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(CMODParser.ParameterListContext,0)


        def getRuleIndex(self):
            return CMODParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = CMODParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.typeQualifierList()
            self.state = 113
            self.typeSpecifier()
            self.state = 114
            self.typeQualifierList()
            self.state = 115
            self.declarator()
            self.state = 116
            self.match(CMODParser.T__10)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1098437886048) != 0):
                self.state = 117
                self.parameterList()


            self.state = 120
            self.match(CMODParser.T__11)
            self.state = 121
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeQualifierList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.TypeQualifierListContext)
            else:
                return self.getTypedRuleContext(CMODParser.TypeQualifierListContext,i)


        def typeSpecifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.TypeSpecifierContext)
            else:
                return self.getTypedRuleContext(CMODParser.TypeSpecifierContext,i)


        def declarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.DeclaratorContext)
            else:
                return self.getTypedRuleContext(CMODParser.DeclaratorContext,i)


        def getRuleIndex(self):
            return CMODParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = CMODParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.typeQualifierList()
            self.state = 124
            self.typeSpecifier()
            self.state = 125
            self.typeQualifierList()
            self.state = 126
            self.declarator()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 127
                self.match(CMODParser.T__12)
                self.state = 128
                self.typeQualifierList()
                self.state = 129
                self.typeSpecifier()
                self.state = 130
                self.typeQualifierList()
                self.state = 131
                self.declarator()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.StatementContext)
            else:
                return self.getTypedRuleContext(CMODParser.StatementContext,i)


        def getRuleIndex(self):
            return CMODParser.RULE_compoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStatement" ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStatement" ):
                listener.exitCompoundStatement(self)




    def compoundStatement(self):

        localctx = CMODParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(CMODParser.T__6)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8795556146912) != 0):
                self.state = 139
                self.statement()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 145
            self.match(CMODParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CMODParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CMODParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = CMODParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 147
                self.match(CMODParser.T__8)


            self.state = 150
            self.expression(0)
            self.state = 151
            self.match(CMODParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CMODParser.ExpressionContext,i)


        def StringLiteral(self):
            return self.getToken(CMODParser.StringLiteral, 0)

        def CharLiteral(self):
            return self.getToken(CMODParser.CharLiteral, 0)

        def Number(self):
            return self.getToken(CMODParser.Number, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(CMODParser.TypeSpecifierContext,0)


        def typeQualifier(self):
            return self.getTypedRuleContext(CMODParser.TypeQualifierContext,0)


        def getRuleIndex(self):
            return CMODParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CMODParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 154
                self.match(CMODParser.T__12)
                pass
            elif token in [14]:
                self.state = 155
                self.match(CMODParser.T__13)
                pass
            elif token in [15]:
                self.state = 156
                self.match(CMODParser.T__14)
                pass
            elif token in [16]:
                self.state = 157
                self.match(CMODParser.T__15)
                pass
            elif token in [17]:
                self.state = 158
                self.match(CMODParser.T__16)
                pass
            elif token in [18]:
                self.state = 159
                self.match(CMODParser.T__17)
                pass
            elif token in [19]:
                self.state = 160
                self.match(CMODParser.T__18)
                pass
            elif token in [20]:
                self.state = 161
                self.match(CMODParser.T__19)
                pass
            elif token in [21]:
                self.state = 162
                self.match(CMODParser.T__20)
                pass
            elif token in [22]:
                self.state = 163
                self.match(CMODParser.T__21)
                pass
            elif token in [23]:
                self.state = 164
                self.match(CMODParser.T__22)
                pass
            elif token in [24]:
                self.state = 165
                self.match(CMODParser.T__23)
                pass
            elif token in [25]:
                self.state = 166
                self.match(CMODParser.T__24)
                pass
            elif token in [10]:
                self.state = 167
                self.match(CMODParser.T__9)
                pass
            elif token in [26]:
                self.state = 168
                self.match(CMODParser.T__25)
                pass
            elif token in [27]:
                self.state = 169
                self.match(CMODParser.T__26)
                pass
            elif token in [11]:
                self.state = 170
                self.match(CMODParser.T__10)
                self.state = 171
                self.expression(0)
                self.state = 172
                self.match(CMODParser.T__11)
                pass
            elif token in [28]:
                self.state = 174
                self.match(CMODParser.T__27)
                self.state = 175
                self.expression(0)
                self.state = 176
                self.match(CMODParser.T__28)
                pass
            elif token in [7]:
                self.state = 178
                self.match(CMODParser.T__6)
                self.state = 179
                self.expression(0)
                self.state = 180
                self.match(CMODParser.T__7)
                pass
            elif token in [42]:
                self.state = 182
                self.match(CMODParser.StringLiteral)
                pass
            elif token in [41]:
                self.state = 183
                self.match(CMODParser.CharLiteral)
                pass
            elif token in [40]:
                self.state = 184
                self.match(CMODParser.Number)
                pass
            elif token in [5, 6, 32, 33, 34, 35, 36, 37, 38, 39]:
                self.state = 185
                self.typeSpecifier()
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 186
                        self.match(CMODParser.T__15) 
                    self.state = 191
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass
            elif token in [30, 31]:
                self.state = 192
                self.typeQualifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CMODParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 195
                    if not self.precpred(self._ctx, 25):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                    self.state = 196
                    self.expression(26) 
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeQualifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeQualifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.TypeQualifierContext)
            else:
                return self.getTypedRuleContext(CMODParser.TypeQualifierContext,i)


        def getRuleIndex(self):
            return CMODParser.RULE_typeQualifierList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeQualifierList" ):
                listener.enterTypeQualifierList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeQualifierList" ):
                listener.exitTypeQualifierList(self)




    def typeQualifierList(self):

        localctx = CMODParser.TypeQualifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_typeQualifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 202
                self.typeQualifier()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CMODParser.RULE_typeQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeQualifier" ):
                listener.enterTypeQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeQualifier" ):
                listener.exitTypeQualifier(self)




    def typeQualifier(self):

        localctx = CMODParser.TypeQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_typeQualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            _la = self._input.LA(1)
            if not(_la==30 or _la==31):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CMODParser.Identifier, 0)

        def getRuleIndex(self):
            return CMODParser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)




    def typeSpecifier(self):

        localctx = CMODParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_typeSpecifier)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(CMODParser.T__31)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(CMODParser.T__32)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                self.match(CMODParser.T__33)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 213
                self.match(CMODParser.T__34)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 5)
                self.state = 214
                self.match(CMODParser.T__35)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 6)
                self.state = 215
                self.match(CMODParser.T__36)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 7)
                self.state = 216
                self.match(CMODParser.T__37)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 8)
                self.state = 217
                self.match(CMODParser.T__4)
                self.state = 218
                self.match(CMODParser.Identifier)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 9)
                self.state = 219
                self.match(CMODParser.T__5)
                self.state = 220
                self.match(CMODParser.Identifier)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 10)
                self.state = 221
                self.match(CMODParser.Identifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CMODParser.Identifier, 0)

        def typeQualifierList(self):
            return self.getTypedRuleContext(CMODParser.TypeQualifierListContext,0)


        def getRuleIndex(self):
            return CMODParser.RULE_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarator" ):
                listener.enterDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarator" ):
                listener.exitDeclarator(self)




    def declarator(self):

        localctx = CMODParser.DeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 224
                self.match(CMODParser.T__15)
                self.state = 225
                self.typeQualifierList()


            self.state = 228
            self.match(CMODParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 25)
         




