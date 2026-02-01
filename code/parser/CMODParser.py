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
        4,1,28,157,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,3,0,30,8,0,1,0,1,0,1,1,3,1,35,8,1,1,1,5,1,38,8,1,10,1,12,1,41,
        9,1,1,1,4,1,44,8,1,11,1,12,1,45,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        5,3,56,8,3,10,3,12,3,59,9,3,3,3,61,8,3,1,3,1,3,1,4,3,4,66,8,4,1,
        4,1,4,3,4,70,8,4,1,4,1,4,3,4,74,8,4,1,4,1,4,3,4,78,8,4,1,5,1,5,1,
        5,1,5,3,5,84,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        3,6,98,8,6,1,7,3,7,101,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,111,
        8,8,10,8,12,8,114,9,8,1,9,1,9,5,9,118,8,9,10,9,12,9,121,9,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,134,8,10,1,
        11,1,11,1,11,1,11,3,11,140,8,11,1,11,1,11,1,12,1,12,1,12,5,12,147,
        8,12,10,12,12,12,150,9,12,1,13,1,13,1,13,1,13,1,13,1,13,0,0,14,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,0,0,169,0,29,1,0,0,0,2,34,1,0,
        0,0,4,47,1,0,0,0,6,50,1,0,0,0,8,77,1,0,0,0,10,79,1,0,0,0,12,97,1,
        0,0,0,14,100,1,0,0,0,16,104,1,0,0,0,18,115,1,0,0,0,20,133,1,0,0,
        0,22,135,1,0,0,0,24,143,1,0,0,0,26,151,1,0,0,0,28,30,3,2,1,0,29,
        28,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,5,0,0,1,32,1,1,0,0,
        0,33,35,3,4,2,0,34,33,1,0,0,0,34,35,1,0,0,0,35,39,1,0,0,0,36,38,
        3,6,3,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,
        40,43,1,0,0,0,41,39,1,0,0,0,42,44,3,8,4,0,43,42,1,0,0,0,44,45,1,
        0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,3,1,0,0,0,47,48,5,1,0,0,48,
        49,5,2,0,0,49,5,1,0,0,0,50,60,5,3,0,0,51,61,5,24,0,0,52,57,5,23,
        0,0,53,54,5,4,0,0,54,56,5,23,0,0,55,53,1,0,0,0,56,59,1,0,0,0,57,
        55,1,0,0,0,57,58,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,60,51,1,0,0,
        0,60,52,1,0,0,0,61,62,1,0,0,0,62,63,5,2,0,0,63,7,1,0,0,0,64,66,5,
        5,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,78,3,10,5,0,68,
        70,5,5,0,0,69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,78,3,22,
        11,0,72,74,5,5,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,
        78,3,26,13,0,76,78,5,2,0,0,77,65,1,0,0,0,77,69,1,0,0,0,77,73,1,0,
        0,0,77,76,1,0,0,0,78,9,1,0,0,0,79,80,3,12,6,0,80,81,3,14,7,0,81,
        83,5,6,0,0,82,84,3,16,8,0,83,82,1,0,0,0,83,84,1,0,0,0,84,85,1,0,
        0,0,85,86,5,7,0,0,86,87,3,18,9,0,87,11,1,0,0,0,88,98,5,8,0,0,89,
        98,5,9,0,0,90,98,5,10,0,0,91,98,5,11,0,0,92,98,5,12,0,0,93,98,5,
        13,0,0,94,98,5,14,0,0,95,96,5,15,0,0,96,98,5,23,0,0,97,88,1,0,0,
        0,97,89,1,0,0,0,97,90,1,0,0,0,97,91,1,0,0,0,97,92,1,0,0,0,97,93,
        1,0,0,0,97,94,1,0,0,0,97,95,1,0,0,0,98,13,1,0,0,0,99,101,5,16,0,
        0,100,99,1,0,0,0,100,101,1,0,0,0,101,102,1,0,0,0,102,103,5,23,0,
        0,103,15,1,0,0,0,104,105,3,12,6,0,105,112,3,14,7,0,106,107,5,17,
        0,0,107,108,3,12,6,0,108,109,3,14,7,0,109,111,1,0,0,0,110,106,1,
        0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,17,1,0,
        0,0,114,112,1,0,0,0,115,119,5,18,0,0,116,118,3,20,10,0,117,116,1,
        0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,122,1,
        0,0,0,121,119,1,0,0,0,122,123,5,19,0,0,123,19,1,0,0,0,124,125,5,
        23,0,0,125,134,5,2,0,0,126,127,5,20,0,0,127,128,5,23,0,0,128,134,
        5,2,0,0,129,130,5,20,0,0,130,131,5,16,0,0,131,132,5,23,0,0,132,134,
        5,2,0,0,133,124,1,0,0,0,133,126,1,0,0,0,133,129,1,0,0,0,134,21,1,
        0,0,0,135,136,3,12,6,0,136,139,3,14,7,0,137,138,5,21,0,0,138,140,
        3,24,12,0,139,137,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,142,
        5,2,0,0,142,23,1,0,0,0,143,148,5,23,0,0,144,145,5,22,0,0,145,147,
        5,23,0,0,146,144,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,
        1,0,0,0,149,25,1,0,0,0,150,148,1,0,0,0,151,152,5,15,0,0,152,153,
        5,23,0,0,153,154,3,18,9,0,154,155,5,2,0,0,155,27,1,0,0,0,18,29,34,
        39,45,57,60,65,69,73,77,83,97,100,112,119,133,139,148
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

        def EOF(self):
            return self.getToken(CMODParser.EOF, 0)

        def translationUnit(self):
            return self.getTypedRuleContext(CMODParser.TranslationUnitContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 65326) != 0):
                self.state = 28
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
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 33
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

            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.externalDeclaration()
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 65316) != 0)):
                    break

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
            self.state = 47
            self.match(CMODParser.T__0)
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
            self.state = 50
            self.match(CMODParser.T__2)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 51
                self.match(CMODParser.StringLiteral)
                pass
            elif token in [23]:
                self.state = 52
                self.match(CMODParser.Identifier)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 53
                    self.match(CMODParser.T__3)
                    self.state = 54
                    self.match(CMODParser.Identifier)
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 62
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
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 64
                    self.match(CMODParser.T__4)


                self.state = 67
                self.limitedFunctionDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 68
                    self.match(CMODParser.T__4)


                self.state = 71
                self.limitedGlobal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 72
                    self.match(CMODParser.T__4)


                self.state = 75
                self.limitedStruct()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
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
            self.state = 79
            self.limitedTypeSpecifier()
            self.state = 80
            self.limitedDeclarator()
            self.state = 81
            self.match(CMODParser.T__5)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 65280) != 0):
                self.state = 82
                self.limitedParameterList()


            self.state = 85
            self.match(CMODParser.T__6)
            self.state = 86
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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(CMODParser.T__7)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(CMODParser.T__8)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.match(CMODParser.T__9)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.match(CMODParser.T__10)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.match(CMODParser.T__11)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 93
                self.match(CMODParser.T__12)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 94
                self.match(CMODParser.T__13)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 8)
                self.state = 95
                self.match(CMODParser.T__14)
                self.state = 96
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
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 99
                self.match(CMODParser.T__15)


            self.state = 102
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
            self.state = 104
            self.limitedTypeSpecifier()
            self.state = 105
            self.limitedDeclarator()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 106
                self.match(CMODParser.T__16)
                self.state = 107
                self.limitedTypeSpecifier()
                self.state = 108
                self.limitedDeclarator()
                self.state = 114
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
            self.state = 115
            self.match(CMODParser.T__17)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==23:
                self.state = 116
                self.limitedStatement()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
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
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(CMODParser.Identifier)
                self.state = 125
                self.match(CMODParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.match(CMODParser.T__19)
                self.state = 127
                self.match(CMODParser.Identifier)
                self.state = 128
                self.match(CMODParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.match(CMODParser.T__19)
                self.state = 130
                self.match(CMODParser.T__15)
                self.state = 131
                self.match(CMODParser.Identifier)
                self.state = 132
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
            self.state = 135
            self.limitedTypeSpecifier()
            self.state = 136
            self.limitedDeclarator()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 137
                self.match(CMODParser.T__20)
                self.state = 138
                self.limitedInitializer()


            self.state = 141
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
            self.state = 143
            self.match(CMODParser.Identifier)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 144
                self.match(CMODParser.T__21)
                self.state = 145
                self.match(CMODParser.Identifier)
                self.state = 150
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
            self.state = 151
            self.match(CMODParser.T__14)
            self.state = 152
            self.match(CMODParser.Identifier)
            self.state = 153
            self.limitedCompoundStatement()
            self.state = 154
            self.match(CMODParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





