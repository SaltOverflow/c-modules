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
        4,1,28,154,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,1,1,1,5,1,34,8,1,10,1,12,1,37,9,1,1,1,5,1,40,8,1,10,
        1,12,1,43,9,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,53,8,3,10,3,12,
        3,56,9,3,3,3,58,8,3,1,3,1,3,1,4,3,4,63,8,4,1,4,1,4,3,4,67,8,4,1,
        4,1,4,3,4,71,8,4,1,4,1,4,3,4,75,8,4,1,5,1,5,1,5,1,5,3,5,81,8,5,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,95,8,6,1,7,3,7,
        98,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,108,8,8,10,8,12,8,111,
        9,8,1,9,1,9,5,9,115,8,9,10,9,12,9,118,9,9,1,9,1,9,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,3,10,131,8,10,1,11,1,11,1,11,1,11,
        3,11,137,8,11,1,11,1,11,1,12,1,12,1,12,5,12,144,8,12,10,12,12,12,
        147,9,12,1,13,1,13,1,13,1,13,1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,0,0,164,0,28,1,0,0,0,2,31,1,0,0,0,4,44,1,0,0,0,
        6,47,1,0,0,0,8,74,1,0,0,0,10,76,1,0,0,0,12,94,1,0,0,0,14,97,1,0,
        0,0,16,101,1,0,0,0,18,112,1,0,0,0,20,130,1,0,0,0,22,132,1,0,0,0,
        24,140,1,0,0,0,26,148,1,0,0,0,28,29,3,2,1,0,29,30,5,0,0,1,30,1,1,
        0,0,0,31,35,3,4,2,0,32,34,3,6,3,0,33,32,1,0,0,0,34,37,1,0,0,0,35,
        33,1,0,0,0,35,36,1,0,0,0,36,41,1,0,0,0,37,35,1,0,0,0,38,40,3,8,4,
        0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,3,1,
        0,0,0,43,41,1,0,0,0,44,45,5,1,0,0,45,46,5,2,0,0,46,5,1,0,0,0,47,
        57,5,3,0,0,48,58,5,24,0,0,49,54,5,23,0,0,50,51,5,4,0,0,51,53,5,23,
        0,0,52,50,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,58,
        1,0,0,0,56,54,1,0,0,0,57,48,1,0,0,0,57,49,1,0,0,0,58,59,1,0,0,0,
        59,60,5,2,0,0,60,7,1,0,0,0,61,63,5,5,0,0,62,61,1,0,0,0,62,63,1,0,
        0,0,63,64,1,0,0,0,64,75,3,10,5,0,65,67,5,5,0,0,66,65,1,0,0,0,66,
        67,1,0,0,0,67,68,1,0,0,0,68,75,3,22,11,0,69,71,5,5,0,0,70,69,1,0,
        0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,75,3,26,13,0,73,75,5,2,0,0,74,
        62,1,0,0,0,74,66,1,0,0,0,74,70,1,0,0,0,74,73,1,0,0,0,75,9,1,0,0,
        0,76,77,3,12,6,0,77,78,3,14,7,0,78,80,5,6,0,0,79,81,3,16,8,0,80,
        79,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,5,7,0,0,83,84,3,18,
        9,0,84,11,1,0,0,0,85,95,5,8,0,0,86,95,5,9,0,0,87,95,5,10,0,0,88,
        95,5,11,0,0,89,95,5,12,0,0,90,95,5,13,0,0,91,95,5,14,0,0,92,93,5,
        15,0,0,93,95,5,23,0,0,94,85,1,0,0,0,94,86,1,0,0,0,94,87,1,0,0,0,
        94,88,1,0,0,0,94,89,1,0,0,0,94,90,1,0,0,0,94,91,1,0,0,0,94,92,1,
        0,0,0,95,13,1,0,0,0,96,98,5,16,0,0,97,96,1,0,0,0,97,98,1,0,0,0,98,
        99,1,0,0,0,99,100,5,23,0,0,100,15,1,0,0,0,101,102,3,12,6,0,102,109,
        3,14,7,0,103,104,5,17,0,0,104,105,3,12,6,0,105,106,3,14,7,0,106,
        108,1,0,0,0,107,103,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,
        110,1,0,0,0,110,17,1,0,0,0,111,109,1,0,0,0,112,116,5,18,0,0,113,
        115,3,20,10,0,114,113,1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,
        117,1,0,0,0,117,119,1,0,0,0,118,116,1,0,0,0,119,120,5,19,0,0,120,
        19,1,0,0,0,121,122,5,23,0,0,122,131,5,2,0,0,123,124,5,20,0,0,124,
        125,5,23,0,0,125,131,5,2,0,0,126,127,5,20,0,0,127,128,5,16,0,0,128,
        129,5,23,0,0,129,131,5,2,0,0,130,121,1,0,0,0,130,123,1,0,0,0,130,
        126,1,0,0,0,131,21,1,0,0,0,132,133,3,12,6,0,133,136,3,14,7,0,134,
        135,5,21,0,0,135,137,3,24,12,0,136,134,1,0,0,0,136,137,1,0,0,0,137,
        138,1,0,0,0,138,139,5,2,0,0,139,23,1,0,0,0,140,145,5,23,0,0,141,
        142,5,22,0,0,142,144,5,23,0,0,143,141,1,0,0,0,144,147,1,0,0,0,145,
        143,1,0,0,0,145,146,1,0,0,0,146,25,1,0,0,0,147,145,1,0,0,0,148,149,
        5,15,0,0,149,150,5,23,0,0,150,151,3,18,9,0,151,152,5,2,0,0,152,27,
        1,0,0,0,16,35,41,54,57,62,66,70,74,80,94,97,109,116,130,136,145
    ]

class CMODParser ( Parser ):

    grammarFileName = "CMOD.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'module'", "';'", "'import'", "'/'", 
                     "'export'", "'('", "')'", "'void'", "'char'", "'short'", 
                     "'int'", "'long'", "'float'", "'double'", "'struct'", 
                     "'*'", "','", "'{'", "'}'", "'type'", "'='", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Identifier", 
                      "StringLiteral", "Whitespace", "Newline", "BlockComment", 
                      "LineComment" ]

    RULE_compilationUnit = 0
    RULE_translationUnit = 1
    RULE_moduleDeclaration = 2
    RULE_importDeclaration = 3
    RULE_externalDeclaration = 4
    RULE_limitedFunctionDefinition = 5
    RULE_limitedTypeSpecifier = 6
    RULE_limitedDeclarator = 7
    RULE_limitedParameterList = 8
    RULE_limitedCompoundStatement = 9
    RULE_limitedStatement = 10
    RULE_limitedGlobal = 11
    RULE_limitedInitializer = 12
    RULE_limitedStruct = 13

    ruleNames =  [ "compilationUnit", "translationUnit", "moduleDeclaration", 
                   "importDeclaration", "externalDeclaration", "limitedFunctionDefinition", 
                   "limitedTypeSpecifier", "limitedDeclarator", "limitedParameterList", 
                   "limitedCompoundStatement", "limitedStatement", "limitedGlobal", 
                   "limitedInitializer", "limitedStruct" ]

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
    Identifier=23
    StringLiteral=24
    Whitespace=25
    Newline=26
    BlockComment=27
    LineComment=28

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
            self.state = 28
            self.translationUnit()
            self.state = 29
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
            self.state = 31
            self.moduleDeclaration()
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 32
                self.importDeclaration()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 65316) != 0):
                self.state = 38
                self.externalDeclaration()
                self.state = 43
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
            self.state = 44
            self.match(CMODParser.T__0)
            self.state = 45
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

        def StringLiteral(self):
            return self.getToken(CMODParser.StringLiteral, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(CMODParser.Identifier)
            else:
                return self.getToken(CMODParser.Identifier, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(CMODParser.T__2)
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 48
                self.match(CMODParser.StringLiteral)
                pass
            elif token in [23]:
                self.state = 49
                self.match(CMODParser.Identifier)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 50
                    self.match(CMODParser.T__3)
                    self.state = 51
                    self.match(CMODParser.Identifier)
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 59
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

        def limitedFunctionDefinition(self):
            return self.getTypedRuleContext(CMODParser.LimitedFunctionDefinitionContext,0)


        def limitedGlobal(self):
            return self.getTypedRuleContext(CMODParser.LimitedGlobalContext,0)


        def limitedStruct(self):
            return self.getTypedRuleContext(CMODParser.LimitedStructContext,0)


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
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 61
                    self.match(CMODParser.T__4)


                self.state = 64
                self.limitedFunctionDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 65
                    self.match(CMODParser.T__4)


                self.state = 68
                self.limitedGlobal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 69
                    self.match(CMODParser.T__4)


                self.state = 72
                self.limitedStruct()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.match(CMODParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitedFunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def limitedTypeSpecifier(self):
            return self.getTypedRuleContext(CMODParser.LimitedTypeSpecifierContext,0)


        def limitedDeclarator(self):
            return self.getTypedRuleContext(CMODParser.LimitedDeclaratorContext,0)


        def limitedCompoundStatement(self):
            return self.getTypedRuleContext(CMODParser.LimitedCompoundStatementContext,0)


        def limitedParameterList(self):
            return self.getTypedRuleContext(CMODParser.LimitedParameterListContext,0)


        def getRuleIndex(self):
            return CMODParser.RULE_limitedFunctionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitedFunctionDefinition" ):
                listener.enterLimitedFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitedFunctionDefinition" ):
                listener.exitLimitedFunctionDefinition(self)




    def limitedFunctionDefinition(self):

        localctx = CMODParser.LimitedFunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_limitedFunctionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.limitedTypeSpecifier()
            self.state = 77
            self.limitedDeclarator()
            self.state = 78
            self.match(CMODParser.T__5)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 65280) != 0):
                self.state = 79
                self.limitedParameterList()


            self.state = 82
            self.match(CMODParser.T__6)
            self.state = 83
            self.limitedCompoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitedTypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CMODParser.Identifier, 0)

        def getRuleIndex(self):
            return CMODParser.RULE_limitedTypeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitedTypeSpecifier" ):
                listener.enterLimitedTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitedTypeSpecifier" ):
                listener.exitLimitedTypeSpecifier(self)




    def limitedTypeSpecifier(self):

        localctx = CMODParser.LimitedTypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_limitedTypeSpecifier)
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(CMODParser.T__7)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(CMODParser.T__8)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.match(CMODParser.T__9)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.match(CMODParser.T__10)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.match(CMODParser.T__11)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 90
                self.match(CMODParser.T__12)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 91
                self.match(CMODParser.T__13)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 8)
                self.state = 92
                self.match(CMODParser.T__14)
                self.state = 93
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


    class LimitedDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CMODParser.Identifier, 0)

        def getRuleIndex(self):
            return CMODParser.RULE_limitedDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitedDeclarator" ):
                listener.enterLimitedDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitedDeclarator" ):
                listener.exitLimitedDeclarator(self)




    def limitedDeclarator(self):

        localctx = CMODParser.LimitedDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_limitedDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 96
                self.match(CMODParser.T__15)


            self.state = 99
            self.match(CMODParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitedParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def limitedTypeSpecifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.LimitedTypeSpecifierContext)
            else:
                return self.getTypedRuleContext(CMODParser.LimitedTypeSpecifierContext,i)


        def limitedDeclarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.LimitedDeclaratorContext)
            else:
                return self.getTypedRuleContext(CMODParser.LimitedDeclaratorContext,i)


        def getRuleIndex(self):
            return CMODParser.RULE_limitedParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitedParameterList" ):
                listener.enterLimitedParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitedParameterList" ):
                listener.exitLimitedParameterList(self)




    def limitedParameterList(self):

        localctx = CMODParser.LimitedParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_limitedParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.limitedTypeSpecifier()
            self.state = 102
            self.limitedDeclarator()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 103
                self.match(CMODParser.T__16)
                self.state = 104
                self.limitedTypeSpecifier()
                self.state = 105
                self.limitedDeclarator()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitedCompoundStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def limitedStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMODParser.LimitedStatementContext)
            else:
                return self.getTypedRuleContext(CMODParser.LimitedStatementContext,i)


        def getRuleIndex(self):
            return CMODParser.RULE_limitedCompoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitedCompoundStatement" ):
                listener.enterLimitedCompoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitedCompoundStatement" ):
                listener.exitLimitedCompoundStatement(self)




    def limitedCompoundStatement(self):

        localctx = CMODParser.LimitedCompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_limitedCompoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(CMODParser.T__17)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==23:
                self.state = 113
                self.limitedStatement()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self.match(CMODParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitedStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CMODParser.Identifier, 0)

        def getRuleIndex(self):
            return CMODParser.RULE_limitedStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitedStatement" ):
                listener.enterLimitedStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitedStatement" ):
                listener.exitLimitedStatement(self)




    def limitedStatement(self):

        localctx = CMODParser.LimitedStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_limitedStatement)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(CMODParser.Identifier)
                self.state = 122
                self.match(CMODParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(CMODParser.T__19)
                self.state = 124
                self.match(CMODParser.Identifier)
                self.state = 125
                self.match(CMODParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.match(CMODParser.T__19)
                self.state = 127
                self.match(CMODParser.T__15)
                self.state = 128
                self.match(CMODParser.Identifier)
                self.state = 129
                self.match(CMODParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitedGlobalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def limitedTypeSpecifier(self):
            return self.getTypedRuleContext(CMODParser.LimitedTypeSpecifierContext,0)


        def limitedDeclarator(self):
            return self.getTypedRuleContext(CMODParser.LimitedDeclaratorContext,0)


        def limitedInitializer(self):
            return self.getTypedRuleContext(CMODParser.LimitedInitializerContext,0)


        def getRuleIndex(self):
            return CMODParser.RULE_limitedGlobal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitedGlobal" ):
                listener.enterLimitedGlobal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitedGlobal" ):
                listener.exitLimitedGlobal(self)




    def limitedGlobal(self):

        localctx = CMODParser.LimitedGlobalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_limitedGlobal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.limitedTypeSpecifier()
            self.state = 133
            self.limitedDeclarator()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 134
                self.match(CMODParser.T__20)
                self.state = 135
                self.limitedInitializer()


            self.state = 138
            self.match(CMODParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitedInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(CMODParser.Identifier)
            else:
                return self.getToken(CMODParser.Identifier, i)

        def getRuleIndex(self):
            return CMODParser.RULE_limitedInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitedInitializer" ):
                listener.enterLimitedInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitedInitializer" ):
                listener.exitLimitedInitializer(self)




    def limitedInitializer(self):

        localctx = CMODParser.LimitedInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_limitedInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(CMODParser.Identifier)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 141
                self.match(CMODParser.T__21)
                self.state = 142
                self.match(CMODParser.Identifier)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitedStructContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CMODParser.Identifier, 0)

        def limitedCompoundStatement(self):
            return self.getTypedRuleContext(CMODParser.LimitedCompoundStatementContext,0)


        def getRuleIndex(self):
            return CMODParser.RULE_limitedStruct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitedStruct" ):
                listener.enterLimitedStruct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitedStruct" ):
                listener.exitLimitedStruct(self)




    def limitedStruct(self):

        localctx = CMODParser.LimitedStructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_limitedStruct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(CMODParser.T__14)
            self.state = 149
            self.match(CMODParser.Identifier)
            self.state = 150
            self.limitedCompoundStatement()
            self.state = 151
            self.match(CMODParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





