from antlr4 import *

class ParseTreeListenerWithPruning(ParseTreeListener):
    def shouldContinue(self) -> bool:
        raise NotImplementedError("shouldContinue() should be overriden")

class ParseTreeWalkerWithPruning(ParseTreeWalker):
    def walk(self, listener: ParseTreeListenerWithPruning, t: ParserRuleContext):
        # Same thing as before, but with shouldContinue() call
        if isinstance(t, ErrorNode):
            listener.visitErrorNode(t)
            return
        elif isinstance(t, TerminalNode):
            listener.visitTerminal(t)
            return
        self.enterRule(listener, t)
        if listener.shouldContinue():
            for child in t.getChildren():
                self.walk(listener, child)
        self.exitRule(listener, t)
