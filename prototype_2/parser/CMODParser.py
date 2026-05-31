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
        4,1,46,251,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        1,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,1,5,1,50,8,1,10,1,12,1,53,9,
        1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,3,4,64,8,4,1,4,1,4,3,4,68,
        8,4,1,4,1,4,3,4,72,8,4,1,4,1,4,3,4,76,8,4,1,4,1,4,3,4,80,8,4,1,5,
        1,5,1,5,1,5,5,5,86,8,5,10,5,12,5,89,9,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,111,
        8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,121,8,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,136,8,10,10,10,
        12,10,139,9,10,1,11,1,11,5,11,143,8,11,10,11,12,11,146,9,11,1,11,
        1,11,1,12,3,12,151,8,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,176,8,13,10,13,12,13,179,9,13,1,13,1,13,1,13,3,13,
        184,8,13,1,13,1,13,1,13,3,13,189,8,13,1,13,1,13,1,13,1,13,1,13,1,
        13,5,13,197,8,13,10,13,12,13,200,9,13,1,13,3,13,203,8,13,1,13,1,
        13,5,13,207,8,13,10,13,12,13,210,9,13,1,14,5,14,213,8,14,10,14,12,
        14,216,9,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,3,16,232,8,16,1,17,1,17,3,17,236,8,17,1,17,1,17,
        5,17,240,8,17,10,17,12,17,243,9,17,1,18,1,18,3,18,247,8,18,1,18,
        1,18,1,18,0,1,26,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,0,2,1,0,5,6,1,0,30,31,289,0,38,1,0,0,0,2,41,1,0,0,0,4,54,1,
        0,0,0,6,58,1,0,0,0,8,79,1,0,0,0,10,81,1,0,0,0,12,93,1,0,0,0,14,99,
        1,0,0,0,16,104,1,0,0,0,18,114,1,0,0,0,20,125,1,0,0,0,22,140,1,0,
        0,0,24,150,1,0,0,0,26,202,1,0,0,0,28,214,1,0,0,0,30,217,1,0,0,0,
        32,231,1,0,0,0,34,235,1,0,0,0,36,244,1,0,0,0,38,39,3,2,1,0,39,40,
        5,0,0,1,40,1,1,0,0,0,41,45,3,4,2,0,42,44,3,6,3,0,43,42,1,0,0,0,44,
        47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,51,1,0,0,0,47,45,1,0,0,
        0,48,50,3,8,4,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,
        1,0,0,0,52,3,1,0,0,0,53,51,1,0,0,0,54,55,5,1,0,0,55,56,5,39,0,0,
        56,57,5,2,0,0,57,5,1,0,0,0,58,59,5,3,0,0,59,60,5,39,0,0,60,61,5,
        2,0,0,61,7,1,0,0,0,62,64,5,4,0,0,63,62,1,0,0,0,63,64,1,0,0,0,64,
        65,1,0,0,0,65,80,3,10,5,0,66,68,5,4,0,0,67,66,1,0,0,0,67,68,1,0,
        0,0,68,69,1,0,0,0,69,80,3,14,7,0,70,72,5,4,0,0,71,70,1,0,0,0,71,
        72,1,0,0,0,72,73,1,0,0,0,73,80,3,16,8,0,74,76,5,4,0,0,75,74,1,0,
        0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,80,3,18,9,0,78,80,5,2,0,0,79,
        63,1,0,0,0,79,67,1,0,0,0,79,71,1,0,0,0,79,75,1,0,0,0,79,78,1,0,0,
        0,80,9,1,0,0,0,81,82,7,0,0,0,82,83,5,39,0,0,83,87,5,7,0,0,84,86,
        3,12,6,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,
        88,90,1,0,0,0,89,87,1,0,0,0,90,91,5,8,0,0,91,92,5,2,0,0,92,11,1,
        0,0,0,93,94,3,28,14,0,94,95,3,32,16,0,95,96,3,28,14,0,96,97,3,34,
        17,0,97,98,5,2,0,0,98,13,1,0,0,0,99,100,5,9,0,0,100,101,3,26,13,
        0,101,102,5,39,0,0,102,103,5,2,0,0,103,15,1,0,0,0,104,105,3,28,14,
        0,105,106,3,32,16,0,106,107,3,28,14,0,107,110,3,34,17,0,108,109,
        5,10,0,0,109,111,3,26,13,0,110,108,1,0,0,0,110,111,1,0,0,0,111,112,
        1,0,0,0,112,113,5,2,0,0,113,17,1,0,0,0,114,115,3,28,14,0,115,116,
        3,32,16,0,116,117,3,28,14,0,117,118,3,34,17,0,118,120,5,11,0,0,119,
        121,3,20,10,0,120,119,1,0,0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,
        123,5,12,0,0,123,124,3,22,11,0,124,19,1,0,0,0,125,126,3,28,14,0,
        126,127,3,32,16,0,127,128,3,28,14,0,128,137,3,34,17,0,129,130,5,
        13,0,0,130,131,3,28,14,0,131,132,3,32,16,0,132,133,3,28,14,0,133,
        134,3,34,17,0,134,136,1,0,0,0,135,129,1,0,0,0,136,139,1,0,0,0,137,
        135,1,0,0,0,137,138,1,0,0,0,138,21,1,0,0,0,139,137,1,0,0,0,140,144,
        5,7,0,0,141,143,3,24,12,0,142,141,1,0,0,0,143,146,1,0,0,0,144,142,
        1,0,0,0,144,145,1,0,0,0,145,147,1,0,0,0,146,144,1,0,0,0,147,148,
        5,8,0,0,148,23,1,0,0,0,149,151,5,9,0,0,150,149,1,0,0,0,150,151,1,
        0,0,0,151,152,1,0,0,0,152,153,3,26,13,0,153,154,5,2,0,0,154,25,1,
        0,0,0,155,156,6,13,-1,0,156,203,5,13,0,0,157,203,5,14,0,0,158,203,
        5,15,0,0,159,203,5,16,0,0,160,203,5,17,0,0,161,203,5,18,0,0,162,
        203,5,19,0,0,163,203,5,20,0,0,164,203,5,21,0,0,165,203,5,22,0,0,
        166,203,5,23,0,0,167,203,5,24,0,0,168,203,5,25,0,0,169,203,5,10,
        0,0,170,203,5,26,0,0,171,203,5,27,0,0,172,177,5,11,0,0,173,176,3,
        26,13,0,174,176,5,2,0,0,175,173,1,0,0,0,175,174,1,0,0,0,176,179,
        1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,177,
        1,0,0,0,180,203,5,12,0,0,181,183,5,28,0,0,182,184,3,26,13,0,183,
        182,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,203,5,29,0,0,186,
        188,5,7,0,0,187,189,3,26,13,0,188,187,1,0,0,0,188,189,1,0,0,0,189,
        190,1,0,0,0,190,203,5,8,0,0,191,203,5,42,0,0,192,203,5,41,0,0,193,
        203,5,40,0,0,194,198,3,32,16,0,195,197,5,16,0,0,196,195,1,0,0,0,
        197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,203,1,0,0,0,
        200,198,1,0,0,0,201,203,3,30,15,0,202,155,1,0,0,0,202,157,1,0,0,
        0,202,158,1,0,0,0,202,159,1,0,0,0,202,160,1,0,0,0,202,161,1,0,0,
        0,202,162,1,0,0,0,202,163,1,0,0,0,202,164,1,0,0,0,202,165,1,0,0,
        0,202,166,1,0,0,0,202,167,1,0,0,0,202,168,1,0,0,0,202,169,1,0,0,
        0,202,170,1,0,0,0,202,171,1,0,0,0,202,172,1,0,0,0,202,181,1,0,0,
        0,202,186,1,0,0,0,202,191,1,0,0,0,202,192,1,0,0,0,202,193,1,0,0,
        0,202,194,1,0,0,0,202,201,1,0,0,0,203,208,1,0,0,0,204,205,10,25,
        0,0,205,207,3,26,13,26,206,204,1,0,0,0,207,210,1,0,0,0,208,206,1,
        0,0,0,208,209,1,0,0,0,209,27,1,0,0,0,210,208,1,0,0,0,211,213,3,30,
        15,0,212,211,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,215,1,0,
        0,0,215,29,1,0,0,0,216,214,1,0,0,0,217,218,7,1,0,0,218,31,1,0,0,
        0,219,232,5,32,0,0,220,232,5,33,0,0,221,232,5,34,0,0,222,232,5,35,
        0,0,223,232,5,36,0,0,224,232,5,37,0,0,225,232,5,38,0,0,226,227,5,
        5,0,0,227,232,5,39,0,0,228,229,5,6,0,0,229,232,5,39,0,0,230,232,
        5,39,0,0,231,219,1,0,0,0,231,220,1,0,0,0,231,221,1,0,0,0,231,222,
        1,0,0,0,231,223,1,0,0,0,231,224,1,0,0,0,231,225,1,0,0,0,231,226,
        1,0,0,0,231,228,1,0,0,0,231,230,1,0,0,0,232,33,1,0,0,0,233,234,5,
        16,0,0,234,236,3,28,14,0,235,233,1,0,0,0,235,236,1,0,0,0,236,237,
        1,0,0,0,237,241,5,39,0,0,238,240,3,36,18,0,239,238,1,0,0,0,240,243,
        1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,35,1,0,0,0,243,241,1,
        0,0,0,244,246,5,28,0,0,245,247,3,26,13,0,246,245,1,0,0,0,246,247,
        1,0,0,0,247,248,1,0,0,0,248,249,5,29,0,0,249,37,1,0,0,0,25,45,51,
        63,67,71,75,79,87,110,120,137,144,150,175,177,183,188,198,202,208,
        214,231,235,241,246
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
    RULE_arraySuffix = 18

    ruleNames =  [ "compilationUnit", "translationUnit", "moduleDeclaration", 
                   "importDeclaration", "externalDeclaration", "structUnionDefinition", 
                   "structField", "typedefDefinition", "globalDefinition", 
                   "functionDefinition", "parameterList", "compoundStatement", 
                   "statement", "expression", "typeQualifierList", "typeQualifier", 
                   "typeSpecifier", "declarator", "arraySuffix" ]

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
            self.state = 38
            self.translationUnit()
            self.state = 39
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
            self.state = 41
            self.moduleDeclaration()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 42
                self.importDeclaration()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1098437886580) != 0):
                self.state = 48
                self.externalDeclaration()
                self.state = 53
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
            self.state = 54
            self.match(CMODParser.T__0)
            self.state = 55
            self.match(CMODParser.Identifier)
            self.state = 56
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
            self.state = 58
            self.match(CMODParser.T__2)
            self.state = 59
            self.match(CMODParser.Identifier)
            self.state = 60
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
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 62
                    self.match(CMODParser.T__3)


                self.state = 65
                self.structUnionDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 66
                    self.match(CMODParser.T__3)


                self.state = 69
                self.typedefDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 70
                    self.match(CMODParser.T__3)


                self.state = 73
                self.globalDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 74
                    self.match(CMODParser.T__3)


                self.state = 77
                self.functionDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
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
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 82
            self.match(CMODParser.Identifier)
            self.state = 83
            self.match(CMODParser.T__6)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1098437886048) != 0):
                self.state = 84
                self.structField()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(CMODParser.T__7)
            self.state = 91
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
            self.state = 93
            self.typeQualifierList()
            self.state = 94
            self.typeSpecifier()
            self.state = 95
            self.typeQualifierList()
            self.state = 96
            self.declarator()
            self.state = 97
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
            self.state = 99
            self.match(CMODParser.T__8)
            self.state = 100
            self.expression(0)
            self.state = 101
            self.match(CMODParser.Identifier)
            self.state = 102
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
            self.state = 104
            self.typeQualifierList()
            self.state = 105
            self.typeSpecifier()
            self.state = 106
            self.typeQualifierList()
            self.state = 107
            self.declarator()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 108
                self.match(CMODParser.T__9)
                self.state = 109
                self.expression(0)


            self.state = 112
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
            self.state = 114
            self.typeQualifierList()
            self.state = 115
            self.typeSpecifier()
            self.state = 116
            self.typeQualifierList()
            self.state = 117
            self.declarator()
            self.state = 118
            self.match(CMODParser.T__10)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1098437886048) != 0):
                self.state = 119
                self.parameterList()


            self.state = 122
            self.match(CMODParser.T__11)
            self.state = 123
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
            self.state = 125
            self.typeQualifierList()
            self.state = 126
            self.typeSpecifier()
            self.state = 127
            self.typeQualifierList()
            self.state = 128
            self.declarator()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 129
                self.match(CMODParser.T__12)
                self.state = 130
                self.typeQualifierList()
                self.state = 131
                self.typeSpecifier()
                self.state = 132
                self.typeQualifierList()
                self.state = 133
                self.declarator()
                self.state = 139
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
            self.state = 140
            self.match(CMODParser.T__6)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8795556146912) != 0):
                self.state = 141
                self.statement()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
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
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 149
                self.match(CMODParser.T__8)


            self.state = 152
            self.expression(0)
            self.state = 153
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 156
                self.match(CMODParser.T__12)
                pass
            elif token in [14]:
                self.state = 157
                self.match(CMODParser.T__13)
                pass
            elif token in [15]:
                self.state = 158
                self.match(CMODParser.T__14)
                pass
            elif token in [16]:
                self.state = 159
                self.match(CMODParser.T__15)
                pass
            elif token in [17]:
                self.state = 160
                self.match(CMODParser.T__16)
                pass
            elif token in [18]:
                self.state = 161
                self.match(CMODParser.T__17)
                pass
            elif token in [19]:
                self.state = 162
                self.match(CMODParser.T__18)
                pass
            elif token in [20]:
                self.state = 163
                self.match(CMODParser.T__19)
                pass
            elif token in [21]:
                self.state = 164
                self.match(CMODParser.T__20)
                pass
            elif token in [22]:
                self.state = 165
                self.match(CMODParser.T__21)
                pass
            elif token in [23]:
                self.state = 166
                self.match(CMODParser.T__22)
                pass
            elif token in [24]:
                self.state = 167
                self.match(CMODParser.T__23)
                pass
            elif token in [25]:
                self.state = 168
                self.match(CMODParser.T__24)
                pass
            elif token in [10]:
                self.state = 169
                self.match(CMODParser.T__9)
                pass
            elif token in [26]:
                self.state = 170
                self.match(CMODParser.T__25)
                pass
            elif token in [27]:
                self.state = 171
                self.match(CMODParser.T__26)
                pass
            elif token in [11]:
                self.state = 172
                self.match(CMODParser.T__10)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8795556146404) != 0):
                    self.state = 175
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [5, 6, 7, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]:
                        self.state = 173
                        self.expression(0)
                        pass
                    elif token in [2]:
                        self.state = 174
                        self.match(CMODParser.T__1)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 180
                self.match(CMODParser.T__11)
                pass
            elif token in [28]:
                self.state = 181
                self.match(CMODParser.T__27)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8795556146400) != 0):
                    self.state = 182
                    self.expression(0)


                self.state = 185
                self.match(CMODParser.T__28)
                pass
            elif token in [7]:
                self.state = 186
                self.match(CMODParser.T__6)
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8795556146400) != 0):
                    self.state = 187
                    self.expression(0)


                self.state = 190
                self.match(CMODParser.T__7)
                pass
            elif token in [42]:
                self.state = 191
                self.match(CMODParser.StringLiteral)
                pass
            elif token in [41]:
                self.state = 192
                self.match(CMODParser.CharLiteral)
                pass
            elif token in [40]:
                self.state = 193
                self.match(CMODParser.Number)
                pass
            elif token in [5, 6, 32, 33, 34, 35, 36, 37, 38, 39]:
                self.state = 194
                self.typeSpecifier()
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 195
                        self.match(CMODParser.T__15) 
                    self.state = 200
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass
            elif token in [30, 31]:
                self.state = 201
                self.typeQualifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CMODParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 204
                    if not self.precpred(self._ctx, 25):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                    self.state = 205
                    self.expression(26) 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 211
                self.typeQualifier()
                self.state = 216
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
            self.state = 217
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
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(CMODParser.T__31)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(CMODParser.T__32)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(CMODParser.T__33)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.match(CMODParser.T__34)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 5)
                self.state = 223
                self.match(CMODParser.T__35)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 6)
                self.state = 224
                self.match(CMODParser.T__36)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 7)
                self.state = 225
                self.match(CMODParser.T__37)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 8)
                self.state = 226
                self.match(CMODParser.T__4)
                self.state = 227
                self.match(CMODParser.Identifier)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 9)
                self.state = 228
                self.match(CMODParser.T__5)
                self.state = 229
                self.match(CMODParser.Identifier)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 10)
                self.state = 230
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


        def arraySuffix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.ArraySuffixContext)
            else:
                return self.getTypedRuleContext(CMODParser.ArraySuffixContext,i)


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
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 233
                self.match(CMODParser.T__15)
                self.state = 234
                self.typeQualifierList()


            self.state = 237
            self.match(CMODParser.Identifier)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 238
                self.arraySuffix()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraySuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CMODParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CMODParser.RULE_arraySuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArraySuffix" ):
                listener.enterArraySuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArraySuffix" ):
                listener.exitArraySuffix(self)




    def arraySuffix(self):

        localctx = CMODParser.ArraySuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arraySuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(CMODParser.T__27)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8795556146400) != 0):
                self.state = 245
                self.expression(0)


            self.state = 248
            self.match(CMODParser.T__28)
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
         




