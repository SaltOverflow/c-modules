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
        4,1,44,207,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,1,1,1,5,1,38,8,1,10,1,12,1,41,
        9,1,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,4,3,4,58,8,4,1,4,1,4,3,4,62,8,4,1,4,1,4,3,4,66,8,4,1,4,1,4,
        3,4,70,8,4,1,4,1,4,3,4,74,8,4,1,5,1,5,1,5,1,5,5,5,80,8,5,10,5,12,
        5,83,9,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,3,8,101,8,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,109,8,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,120,8,10,10,10,12,10,123,
        9,10,1,11,1,11,5,11,127,8,11,10,11,12,11,130,9,11,1,11,1,11,1,12,
        3,12,135,8,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,5,13,174,8,13,10,13,12,13,177,9,13,3,13,179,8,13,1,13,1,13,
        5,13,183,8,13,10,13,12,13,186,9,13,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,3,14,200,8,14,1,15,3,15,203,8,15,1,
        15,1,15,1,15,0,1,26,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        0,1,1,0,5,6,240,0,32,1,0,0,0,2,35,1,0,0,0,4,48,1,0,0,0,6,52,1,0,
        0,0,8,73,1,0,0,0,10,75,1,0,0,0,12,87,1,0,0,0,14,91,1,0,0,0,16,96,
        1,0,0,0,18,104,1,0,0,0,20,113,1,0,0,0,22,124,1,0,0,0,24,134,1,0,
        0,0,26,178,1,0,0,0,28,199,1,0,0,0,30,202,1,0,0,0,32,33,3,2,1,0,33,
        34,5,0,0,1,34,1,1,0,0,0,35,39,3,4,2,0,36,38,3,6,3,0,37,36,1,0,0,
        0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,45,1,0,0,0,41,39,
        1,0,0,0,42,44,3,8,4,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,
        45,46,1,0,0,0,46,3,1,0,0,0,47,45,1,0,0,0,48,49,5,1,0,0,49,50,5,37,
        0,0,50,51,5,2,0,0,51,5,1,0,0,0,52,53,5,3,0,0,53,54,5,37,0,0,54,55,
        5,2,0,0,55,7,1,0,0,0,56,58,5,4,0,0,57,56,1,0,0,0,57,58,1,0,0,0,58,
        59,1,0,0,0,59,74,3,10,5,0,60,62,5,4,0,0,61,60,1,0,0,0,61,62,1,0,
        0,0,62,63,1,0,0,0,63,74,3,14,7,0,64,66,5,4,0,0,65,64,1,0,0,0,65,
        66,1,0,0,0,66,67,1,0,0,0,67,74,3,16,8,0,68,70,5,4,0,0,69,68,1,0,
        0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,74,3,18,9,0,72,74,5,2,0,0,73,
        57,1,0,0,0,73,61,1,0,0,0,73,65,1,0,0,0,73,69,1,0,0,0,73,72,1,0,0,
        0,74,9,1,0,0,0,75,76,7,0,0,0,76,77,5,37,0,0,77,81,5,7,0,0,78,80,
        3,12,6,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,
        82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,8,0,0,85,86,5,2,0,0,86,11,1,
        0,0,0,87,88,3,28,14,0,88,89,3,30,15,0,89,90,5,2,0,0,90,13,1,0,0,
        0,91,92,5,9,0,0,92,93,3,26,13,0,93,94,5,37,0,0,94,95,5,2,0,0,95,
        15,1,0,0,0,96,97,3,28,14,0,97,100,3,30,15,0,98,99,5,10,0,0,99,101,
        3,26,13,0,100,98,1,0,0,0,100,101,1,0,0,0,101,102,1,0,0,0,102,103,
        5,2,0,0,103,17,1,0,0,0,104,105,3,28,14,0,105,106,3,30,15,0,106,108,
        5,11,0,0,107,109,3,20,10,0,108,107,1,0,0,0,108,109,1,0,0,0,109,110,
        1,0,0,0,110,111,5,12,0,0,111,112,3,22,11,0,112,19,1,0,0,0,113,114,
        3,28,14,0,114,121,3,30,15,0,115,116,5,13,0,0,116,117,3,28,14,0,117,
        118,3,30,15,0,118,120,1,0,0,0,119,115,1,0,0,0,120,123,1,0,0,0,121,
        119,1,0,0,0,121,122,1,0,0,0,122,21,1,0,0,0,123,121,1,0,0,0,124,128,
        5,7,0,0,125,127,3,24,12,0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,
        1,0,0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,132,
        5,8,0,0,132,23,1,0,0,0,133,135,5,9,0,0,134,133,1,0,0,0,134,135,1,
        0,0,0,135,136,1,0,0,0,136,137,3,26,13,0,137,138,5,2,0,0,138,25,1,
        0,0,0,139,140,6,13,-1,0,140,179,5,13,0,0,141,179,5,14,0,0,142,179,
        5,15,0,0,143,179,5,16,0,0,144,179,5,17,0,0,145,179,5,18,0,0,146,
        179,5,19,0,0,147,179,5,20,0,0,148,179,5,21,0,0,149,179,5,22,0,0,
        150,179,5,23,0,0,151,179,5,24,0,0,152,179,5,25,0,0,153,179,5,10,
        0,0,154,179,5,26,0,0,155,179,5,27,0,0,156,157,5,11,0,0,157,158,3,
        26,13,0,158,159,5,12,0,0,159,179,1,0,0,0,160,161,5,28,0,0,161,162,
        3,26,13,0,162,163,5,29,0,0,163,179,1,0,0,0,164,165,5,7,0,0,165,166,
        3,26,13,0,166,167,5,8,0,0,167,179,1,0,0,0,168,179,5,40,0,0,169,179,
        5,39,0,0,170,179,5,38,0,0,171,175,3,28,14,0,172,174,5,16,0,0,173,
        172,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,
        179,1,0,0,0,177,175,1,0,0,0,178,139,1,0,0,0,178,141,1,0,0,0,178,
        142,1,0,0,0,178,143,1,0,0,0,178,144,1,0,0,0,178,145,1,0,0,0,178,
        146,1,0,0,0,178,147,1,0,0,0,178,148,1,0,0,0,178,149,1,0,0,0,178,
        150,1,0,0,0,178,151,1,0,0,0,178,152,1,0,0,0,178,153,1,0,0,0,178,
        154,1,0,0,0,178,155,1,0,0,0,178,156,1,0,0,0,178,160,1,0,0,0,178,
        164,1,0,0,0,178,168,1,0,0,0,178,169,1,0,0,0,178,170,1,0,0,0,178,
        171,1,0,0,0,179,184,1,0,0,0,180,181,10,24,0,0,181,183,3,26,13,25,
        182,180,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,
        185,27,1,0,0,0,186,184,1,0,0,0,187,200,5,30,0,0,188,200,5,31,0,0,
        189,200,5,32,0,0,190,200,5,33,0,0,191,200,5,34,0,0,192,200,5,35,
        0,0,193,200,5,36,0,0,194,195,5,5,0,0,195,200,5,37,0,0,196,197,5,
        6,0,0,197,200,5,37,0,0,198,200,5,37,0,0,199,187,1,0,0,0,199,188,
        1,0,0,0,199,189,1,0,0,0,199,190,1,0,0,0,199,191,1,0,0,0,199,192,
        1,0,0,0,199,193,1,0,0,0,199,194,1,0,0,0,199,196,1,0,0,0,199,198,
        1,0,0,0,200,29,1,0,0,0,201,203,5,16,0,0,202,201,1,0,0,0,202,203,
        1,0,0,0,203,204,1,0,0,0,204,205,5,37,0,0,205,31,1,0,0,0,18,39,45,
        57,61,65,69,73,81,100,108,121,128,134,175,178,184,199,202
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
                     "'>'", "'['", "']'", "'void'", "'char'", "'short'", 
                     "'int'", "'long'", "'float'", "'double'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Identifier", "Number", "CharLiteral", 
                      "StringLiteral", "Whitespace", "Newline", "BlockComment", 
                      "LineComment" ]

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
    RULE_typeSpecifier = 14
    RULE_declarator = 15

    ruleNames =  [ "compilationUnit", "translationUnit", "moduleDeclaration", 
                   "importDeclaration", "externalDeclaration", "structUnionDefinition", 
                   "structField", "typedefDefinition", "globalDefinition", 
                   "functionDefinition", "parameterList", "compoundStatement", 
                   "statement", "expression", "typeSpecifier", "declarator" ]

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
    Identifier=37
    Number=38
    CharLiteral=39
    StringLiteral=40
    Whitespace=41
    Newline=42
    BlockComment=43
    LineComment=44

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
            self.state = 32
            self.translationUnit()
            self.state = 33
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
            self.state = 35
            self.moduleDeclaration()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 36
                self.importDeclaration()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 273804165748) != 0):
                self.state = 42
                self.externalDeclaration()
                self.state = 47
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
            self.state = 48
            self.match(CMODParser.T__0)
            self.state = 49
            self.match(CMODParser.Identifier)
            self.state = 50
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
            self.state = 52
            self.match(CMODParser.T__2)
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
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 56
                    self.match(CMODParser.T__3)


                self.state = 59
                self.structUnionDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 60
                    self.match(CMODParser.T__3)


                self.state = 63
                self.typedefDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 64
                    self.match(CMODParser.T__3)


                self.state = 67
                self.globalDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 68
                    self.match(CMODParser.T__3)


                self.state = 71
                self.functionDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
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
            self.state = 75
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 76
            self.match(CMODParser.Identifier)
            self.state = 77
            self.match(CMODParser.T__6)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 273804165216) != 0):
                self.state = 78
                self.structField()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(CMODParser.T__7)
            self.state = 85
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
            self.state = 87
            self.typeSpecifier()
            self.state = 88
            self.declarator()
            self.state = 89
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
            self.state = 91
            self.match(CMODParser.T__8)
            self.state = 92
            self.expression(0)
            self.state = 93
            self.match(CMODParser.Identifier)
            self.state = 94
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
            self.state = 96
            self.typeSpecifier()
            self.state = 97
            self.declarator()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 98
                self.match(CMODParser.T__9)
                self.state = 99
                self.expression(0)


            self.state = 102
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
            self.state = 104
            self.typeSpecifier()
            self.state = 105
            self.declarator()
            self.state = 106
            self.match(CMODParser.T__10)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 273804165216) != 0):
                self.state = 107
                self.parameterList()


            self.state = 110
            self.match(CMODParser.T__11)
            self.state = 111
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
            self.state = 113
            self.typeSpecifier()
            self.state = 114
            self.declarator()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 115
                self.match(CMODParser.T__12)
                self.state = 116
                self.typeSpecifier()
                self.state = 117
                self.declarator()
                self.state = 123
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
            self.state = 124
            self.match(CMODParser.T__6)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2198486380256) != 0):
                self.state = 125
                self.statement()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
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
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 133
                self.match(CMODParser.T__8)


            self.state = 136
            self.expression(0)
            self.state = 137
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
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 140
                self.match(CMODParser.T__12)
                pass
            elif token in [14]:
                self.state = 141
                self.match(CMODParser.T__13)
                pass
            elif token in [15]:
                self.state = 142
                self.match(CMODParser.T__14)
                pass
            elif token in [16]:
                self.state = 143
                self.match(CMODParser.T__15)
                pass
            elif token in [17]:
                self.state = 144
                self.match(CMODParser.T__16)
                pass
            elif token in [18]:
                self.state = 145
                self.match(CMODParser.T__17)
                pass
            elif token in [19]:
                self.state = 146
                self.match(CMODParser.T__18)
                pass
            elif token in [20]:
                self.state = 147
                self.match(CMODParser.T__19)
                pass
            elif token in [21]:
                self.state = 148
                self.match(CMODParser.T__20)
                pass
            elif token in [22]:
                self.state = 149
                self.match(CMODParser.T__21)
                pass
            elif token in [23]:
                self.state = 150
                self.match(CMODParser.T__22)
                pass
            elif token in [24]:
                self.state = 151
                self.match(CMODParser.T__23)
                pass
            elif token in [25]:
                self.state = 152
                self.match(CMODParser.T__24)
                pass
            elif token in [10]:
                self.state = 153
                self.match(CMODParser.T__9)
                pass
            elif token in [26]:
                self.state = 154
                self.match(CMODParser.T__25)
                pass
            elif token in [27]:
                self.state = 155
                self.match(CMODParser.T__26)
                pass
            elif token in [11]:
                self.state = 156
                self.match(CMODParser.T__10)
                self.state = 157
                self.expression(0)
                self.state = 158
                self.match(CMODParser.T__11)
                pass
            elif token in [28]:
                self.state = 160
                self.match(CMODParser.T__27)
                self.state = 161
                self.expression(0)
                self.state = 162
                self.match(CMODParser.T__28)
                pass
            elif token in [7]:
                self.state = 164
                self.match(CMODParser.T__6)
                self.state = 165
                self.expression(0)
                self.state = 166
                self.match(CMODParser.T__7)
                pass
            elif token in [40]:
                self.state = 168
                self.match(CMODParser.StringLiteral)
                pass
            elif token in [39]:
                self.state = 169
                self.match(CMODParser.CharLiteral)
                pass
            elif token in [38]:
                self.state = 170
                self.match(CMODParser.Number)
                pass
            elif token in [5, 6, 30, 31, 32, 33, 34, 35, 36, 37]:
                self.state = 171
                self.typeSpecifier()
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 172
                        self.match(CMODParser.T__15) 
                    self.state = 177
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CMODParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 180
                    if not self.precpred(self._ctx, 24):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                    self.state = 181
                    self.expression(25) 
                self.state = 186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 28, self.RULE_typeSpecifier)
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(CMODParser.T__29)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(CMODParser.T__30)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.match(CMODParser.T__31)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 190
                self.match(CMODParser.T__32)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 5)
                self.state = 191
                self.match(CMODParser.T__33)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 6)
                self.state = 192
                self.match(CMODParser.T__34)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 7)
                self.state = 193
                self.match(CMODParser.T__35)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 8)
                self.state = 194
                self.match(CMODParser.T__4)
                self.state = 195
                self.match(CMODParser.Identifier)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 9)
                self.state = 196
                self.match(CMODParser.T__5)
                self.state = 197
                self.match(CMODParser.Identifier)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 10)
                self.state = 198
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
        self.enterRule(localctx, 30, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 201
                self.match(CMODParser.T__15)


            self.state = 204
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
                return self.precpred(self._ctx, 24)
         




