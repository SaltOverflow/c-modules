# Generated from parser/CMOD.g4 by ANTLR 4.12.0
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
        4,1,39,188,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,1,1,5,
        1,42,8,1,10,1,12,1,45,9,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,3,
        4,56,8,4,1,4,1,4,3,4,60,8,4,1,4,1,4,3,4,64,8,4,1,4,1,4,3,4,68,8,
        4,1,5,1,5,1,5,1,5,5,5,74,8,5,10,5,12,5,77,9,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,90,8,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,
        98,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,109,8,9,10,9,12,9,
        112,9,9,1,10,1,10,5,10,116,8,10,10,10,12,10,119,9,10,1,10,1,10,1,
        11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,157,8,12,10,12,12,12,
        160,9,12,1,12,3,12,163,8,12,1,12,1,12,5,12,167,8,12,10,12,12,12,
        170,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,181,8,
        13,1,14,3,14,184,8,14,1,14,1,14,1,14,0,1,24,15,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,0,0,215,0,30,1,0,0,0,2,33,1,0,0,0,4,46,1,0,
        0,0,6,50,1,0,0,0,8,67,1,0,0,0,10,69,1,0,0,0,12,81,1,0,0,0,14,85,
        1,0,0,0,16,93,1,0,0,0,18,102,1,0,0,0,20,113,1,0,0,0,22,122,1,0,0,
        0,24,162,1,0,0,0,26,180,1,0,0,0,28,183,1,0,0,0,30,31,3,2,1,0,31,
        32,5,0,0,1,32,1,1,0,0,0,33,37,3,4,2,0,34,36,3,6,3,0,35,34,1,0,0,
        0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,43,1,0,0,0,39,37,
        1,0,0,0,40,42,3,8,4,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,
        43,44,1,0,0,0,44,3,1,0,0,0,45,43,1,0,0,0,46,47,5,1,0,0,47,48,5,33,
        0,0,48,49,5,2,0,0,49,5,1,0,0,0,50,51,5,3,0,0,51,52,5,33,0,0,52,53,
        5,2,0,0,53,7,1,0,0,0,54,56,5,4,0,0,55,54,1,0,0,0,55,56,1,0,0,0,56,
        57,1,0,0,0,57,68,3,10,5,0,58,60,5,4,0,0,59,58,1,0,0,0,59,60,1,0,
        0,0,60,61,1,0,0,0,61,68,3,14,7,0,62,64,5,4,0,0,63,62,1,0,0,0,63,
        64,1,0,0,0,64,65,1,0,0,0,65,68,3,16,8,0,66,68,5,2,0,0,67,55,1,0,
        0,0,67,59,1,0,0,0,67,63,1,0,0,0,67,66,1,0,0,0,68,9,1,0,0,0,69,70,
        5,5,0,0,70,71,5,33,0,0,71,75,5,6,0,0,72,74,3,12,6,0,73,72,1,0,0,
        0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,75,
        1,0,0,0,78,79,5,7,0,0,79,80,5,2,0,0,80,11,1,0,0,0,81,82,3,26,13,
        0,82,83,3,28,14,0,83,84,5,2,0,0,84,13,1,0,0,0,85,86,3,26,13,0,86,
        89,3,28,14,0,87,88,5,8,0,0,88,90,3,24,12,0,89,87,1,0,0,0,89,90,1,
        0,0,0,90,91,1,0,0,0,91,92,5,2,0,0,92,15,1,0,0,0,93,94,3,26,13,0,
        94,95,3,28,14,0,95,97,5,9,0,0,96,98,3,18,9,0,97,96,1,0,0,0,97,98,
        1,0,0,0,98,99,1,0,0,0,99,100,5,10,0,0,100,101,3,20,10,0,101,17,1,
        0,0,0,102,103,3,26,13,0,103,110,3,28,14,0,104,105,5,11,0,0,105,106,
        3,26,13,0,106,107,3,28,14,0,107,109,1,0,0,0,108,104,1,0,0,0,109,
        112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,19,1,0,0,0,112,110,
        1,0,0,0,113,117,5,6,0,0,114,116,3,22,11,0,115,114,1,0,0,0,116,119,
        1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,120,1,0,0,0,119,117,
        1,0,0,0,120,121,5,7,0,0,121,21,1,0,0,0,122,123,3,24,12,0,123,124,
        5,2,0,0,124,23,1,0,0,0,125,126,6,12,-1,0,126,163,5,11,0,0,127,163,
        5,12,0,0,128,163,5,13,0,0,129,163,5,14,0,0,130,163,5,15,0,0,131,
        163,5,16,0,0,132,163,5,17,0,0,133,163,5,18,0,0,134,163,5,19,0,0,
        135,163,5,20,0,0,136,163,5,21,0,0,137,163,5,8,0,0,138,163,5,22,0,
        0,139,163,5,23,0,0,140,141,5,9,0,0,141,142,3,24,12,0,142,143,5,10,
        0,0,143,163,1,0,0,0,144,145,5,24,0,0,145,146,3,24,12,0,146,147,5,
        25,0,0,147,163,1,0,0,0,148,149,5,6,0,0,149,150,3,24,12,0,150,151,
        5,7,0,0,151,163,1,0,0,0,152,163,5,35,0,0,153,163,5,34,0,0,154,158,
        3,26,13,0,155,157,5,14,0,0,156,155,1,0,0,0,157,160,1,0,0,0,158,156,
        1,0,0,0,158,159,1,0,0,0,159,163,1,0,0,0,160,158,1,0,0,0,161,163,
        5,33,0,0,162,125,1,0,0,0,162,127,1,0,0,0,162,128,1,0,0,0,162,129,
        1,0,0,0,162,130,1,0,0,0,162,131,1,0,0,0,162,132,1,0,0,0,162,133,
        1,0,0,0,162,134,1,0,0,0,162,135,1,0,0,0,162,136,1,0,0,0,162,137,
        1,0,0,0,162,138,1,0,0,0,162,139,1,0,0,0,162,140,1,0,0,0,162,144,
        1,0,0,0,162,148,1,0,0,0,162,152,1,0,0,0,162,153,1,0,0,0,162,154,
        1,0,0,0,162,161,1,0,0,0,163,168,1,0,0,0,164,165,10,22,0,0,165,167,
        3,24,12,23,166,164,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,
        1,0,0,0,169,25,1,0,0,0,170,168,1,0,0,0,171,181,5,26,0,0,172,181,
        5,27,0,0,173,181,5,28,0,0,174,181,5,29,0,0,175,181,5,30,0,0,176,
        181,5,31,0,0,177,181,5,32,0,0,178,179,5,5,0,0,179,181,5,33,0,0,180,
        171,1,0,0,0,180,172,1,0,0,0,180,173,1,0,0,0,180,174,1,0,0,0,180,
        175,1,0,0,0,180,176,1,0,0,0,180,177,1,0,0,0,180,178,1,0,0,0,181,
        27,1,0,0,0,182,184,5,14,0,0,183,182,1,0,0,0,183,184,1,0,0,0,184,
        185,1,0,0,0,185,186,5,33,0,0,186,29,1,0,0,0,16,37,43,55,59,63,67,
        75,89,97,110,117,158,162,168,180,183
    ]

class CMODParser ( Parser ):

    grammarFileName = "CMOD.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'module'", "';'", "'import'", "'export'", 
                     "'struct'", "'{'", "'}'", "'='", "'('", "')'", "','", 
                     "'.'", "'->'", "'*'", "'/'", "'+'", "'-'", "'&'", "'|'", 
                     "'?'", "':'", "'<'", "'>'", "'['", "']'", "'void'", 
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
                      "<INVALID>", "Identifier", "Number", "StringLiteral", 
                      "Whitespace", "Newline", "BlockComment", "LineComment" ]

    RULE_compilationUnit = 0
    RULE_translationUnit = 1
    RULE_moduleDeclaration = 2
    RULE_importDeclaration = 3
    RULE_externalDeclaration = 4
    RULE_structDefinition = 5
    RULE_structField = 6
    RULE_globalDefinition = 7
    RULE_functionDefinition = 8
    RULE_parameterList = 9
    RULE_compoundStatement = 10
    RULE_statement = 11
    RULE_expression = 12
    RULE_typeSpecifier = 13
    RULE_declarator = 14

    ruleNames =  [ "compilationUnit", "translationUnit", "moduleDeclaration", 
                   "importDeclaration", "externalDeclaration", "structDefinition", 
                   "structField", "globalDefinition", "functionDefinition", 
                   "parameterList", "compoundStatement", "statement", "expression", 
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
    Identifier=33
    Number=34
    StringLiteral=35
    Whitespace=36
    Newline=37
    BlockComment=38
    LineComment=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
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
            self.state = 30
            self.translationUnit()
            self.state = 31
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
            self.state = 33
            self.moduleDeclaration()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 34
                self.importDeclaration()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8522825780) != 0):
                self.state = 40
                self.externalDeclaration()
                self.state = 45
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
            self.state = 46
            self.match(CMODParser.T__0)
            self.state = 47
            self.match(CMODParser.Identifier)
            self.state = 48
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
            self.state = 50
            self.match(CMODParser.T__2)
            self.state = 51
            self.match(CMODParser.Identifier)
            self.state = 52
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

        def structDefinition(self):
            return self.getTypedRuleContext(CMODParser.StructDefinitionContext,0)


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
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 54
                    self.match(CMODParser.T__3)


                self.state = 57
                self.structDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 58
                    self.match(CMODParser.T__3)


                self.state = 61
                self.globalDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 62
                    self.match(CMODParser.T__3)


                self.state = 65
                self.functionDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.match(CMODParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDefinitionContext(ParserRuleContext):
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
            return CMODParser.RULE_structDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructDefinition" ):
                listener.enterStructDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructDefinition" ):
                listener.exitStructDefinition(self)




    def structDefinition(self):

        localctx = CMODParser.StructDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_structDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(CMODParser.T__4)
            self.state = 70
            self.match(CMODParser.Identifier)
            self.state = 71
            self.match(CMODParser.T__5)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8522825760) != 0):
                self.state = 72
                self.structField()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(CMODParser.T__6)
            self.state = 79
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
            self.state = 81
            self.typeSpecifier()
            self.state = 82
            self.declarator()
            self.state = 83
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
        self.enterRule(localctx, 14, self.RULE_globalDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.typeSpecifier()
            self.state = 86
            self.declarator()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 87
                self.match(CMODParser.T__7)
                self.state = 88
                self.expression(0)


            self.state = 91
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
        self.enterRule(localctx, 16, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.typeSpecifier()
            self.state = 94
            self.declarator()
            self.state = 95
            self.match(CMODParser.T__8)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8522825760) != 0):
                self.state = 96
                self.parameterList()


            self.state = 99
            self.match(CMODParser.T__9)
            self.state = 100
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
        self.enterRule(localctx, 18, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.typeSpecifier()
            self.state = 103
            self.declarator()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 104
                self.match(CMODParser.T__10)
                self.state = 105
                self.typeSpecifier()
                self.state = 106
                self.declarator()
                self.state = 112
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
        self.enterRule(localctx, 20, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(CMODParser.T__5)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68685921120) != 0):
                self.state = 114
                self.statement()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(CMODParser.T__6)
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
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.expression(0)
            self.state = 123
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

        def Number(self):
            return self.getToken(CMODParser.Number, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(CMODParser.TypeSpecifierContext,0)


        def Identifier(self):
            return self.getToken(CMODParser.Identifier, 0)

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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 126
                self.match(CMODParser.T__10)
                pass
            elif token in [12]:
                self.state = 127
                self.match(CMODParser.T__11)
                pass
            elif token in [13]:
                self.state = 128
                self.match(CMODParser.T__12)
                pass
            elif token in [14]:
                self.state = 129
                self.match(CMODParser.T__13)
                pass
            elif token in [15]:
                self.state = 130
                self.match(CMODParser.T__14)
                pass
            elif token in [16]:
                self.state = 131
                self.match(CMODParser.T__15)
                pass
            elif token in [17]:
                self.state = 132
                self.match(CMODParser.T__16)
                pass
            elif token in [18]:
                self.state = 133
                self.match(CMODParser.T__17)
                pass
            elif token in [19]:
                self.state = 134
                self.match(CMODParser.T__18)
                pass
            elif token in [20]:
                self.state = 135
                self.match(CMODParser.T__19)
                pass
            elif token in [21]:
                self.state = 136
                self.match(CMODParser.T__20)
                pass
            elif token in [8]:
                self.state = 137
                self.match(CMODParser.T__7)
                pass
            elif token in [22]:
                self.state = 138
                self.match(CMODParser.T__21)
                pass
            elif token in [23]:
                self.state = 139
                self.match(CMODParser.T__22)
                pass
            elif token in [9]:
                self.state = 140
                self.match(CMODParser.T__8)
                self.state = 141
                self.expression(0)
                self.state = 142
                self.match(CMODParser.T__9)
                pass
            elif token in [24]:
                self.state = 144
                self.match(CMODParser.T__23)
                self.state = 145
                self.expression(0)
                self.state = 146
                self.match(CMODParser.T__24)
                pass
            elif token in [6]:
                self.state = 148
                self.match(CMODParser.T__5)
                self.state = 149
                self.expression(0)
                self.state = 150
                self.match(CMODParser.T__6)
                pass
            elif token in [35]:
                self.state = 152
                self.match(CMODParser.StringLiteral)
                pass
            elif token in [34]:
                self.state = 153
                self.match(CMODParser.Number)
                pass
            elif token in [5, 26, 27, 28, 29, 30, 31, 32]:
                self.state = 154
                self.typeSpecifier()
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 155
                        self.match(CMODParser.T__13) 
                    self.state = 160
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass
            elif token in [33]:
                self.state = 161
                self.match(CMODParser.Identifier)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CMODParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 164
                    if not self.precpred(self._ctx, 22):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                    self.state = 165
                    self.expression(23) 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_typeSpecifier)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(CMODParser.T__25)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(CMODParser.T__26)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(CMODParser.T__27)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.match(CMODParser.T__28)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                self.match(CMODParser.T__29)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 6)
                self.state = 176
                self.match(CMODParser.T__30)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 7)
                self.state = 177
                self.match(CMODParser.T__31)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 8)
                self.state = 178
                self.match(CMODParser.T__4)
                self.state = 179
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
        self.enterRule(localctx, 28, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 182
                self.match(CMODParser.T__13)


            self.state = 185
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
        self._predicates[12] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 22)
         




