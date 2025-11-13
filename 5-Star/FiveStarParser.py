# Generated from FiveStar.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\7\2")
        buf.write("\17\n\2\f\2\16\2\22\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\7\4\36\n\4\f\4\16\4!\13\4\5\4#\n\4\3\4\5\4")
        buf.write("&\n\4\3\4\3\4\3\5\3\5\5\5,\n\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5\67\n\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5?\n")
        buf.write("\5\f\5\16\5B\13\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6J\n\6\3\6")
        buf.write("\2\3\b\7\2\4\6\b\n\2\5\3\2\20\24\3\2\25\26\3\2\27\31\2")
        buf.write("X\2\20\3\2\2\2\4\25\3\2\2\2\6\31\3\2\2\2\b\66\3\2\2\2")
        buf.write("\nI\3\2\2\2\f\17\5\4\3\2\r\17\5\b\5\2\16\f\3\2\2\2\16")
        buf.write("\r\3\2\2\2\17\22\3\2\2\2\20\16\3\2\2\2\20\21\3\2\2\2\21")
        buf.write("\23\3\2\2\2\22\20\3\2\2\2\23\24\7\2\2\3\24\3\3\2\2\2\25")
        buf.write("\26\7\17\2\2\26\27\t\2\2\2\27\30\5\b\5\2\30\5\3\2\2\2")
        buf.write("\31\"\7\3\2\2\32\37\5\b\5\2\33\34\7\4\2\2\34\36\5\b\5")
        buf.write("\2\35\33\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2")
        buf.write(" #\3\2\2\2!\37\3\2\2\2\"\32\3\2\2\2\"#\3\2\2\2#%\3\2\2")
        buf.write("\2$&\7\4\2\2%$\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\7\5\2\2")
        buf.write("(\7\3\2\2\2)+\b\5\1\2*,\t\3\2\2+*\3\2\2\2+,\3\2\2\2,-")
        buf.write("\3\2\2\2-\67\5\n\6\2.\67\7\17\2\2/\67\7\16\2\2\60\67\7")
        buf.write("\r\2\2\61\67\5\6\4\2\62\63\7\6\2\2\63\64\5\b\5\2\64\65")
        buf.write("\7\7\2\2\65\67\3\2\2\2\66)\3\2\2\2\66.\3\2\2\2\66/\3\2")
        buf.write("\2\2\66\60\3\2\2\2\66\61\3\2\2\2\66\62\3\2\2\2\67@\3\2")
        buf.write("\2\289\f\n\2\29:\t\4\2\2:?\5\b\5\13;<\f\t\2\2<=\t\3\2")
        buf.write("\2=?\5\b\5\n>8\3\2\2\2>;\3\2\2\2?B\3\2\2\2@>\3\2\2\2@")
        buf.write("A\3\2\2\2A\t\3\2\2\2B@\3\2\2\2CJ\7\13\2\2DJ\7\f\2\2EJ")
        buf.write("\7\r\2\2FJ\7\16\2\2GJ\7\17\2\2HJ\5\6\4\2IC\3\2\2\2ID\3")
        buf.write("\2\2\2IE\3\2\2\2IF\3\2\2\2IG\3\2\2\2IH\3\2\2\2J\13\3\2")
        buf.write("\2\2\f\16\20\37\"%+\66>@I")
        return buf.getvalue()


class FiveStarParser ( Parser ):

    grammarFileName = "FiveStar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "','", "']'", "'('", "')'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='", "'+='", 
                     "'-='", "'*='", "'/='", "'+'", "'-'", "'*'", "'%'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NEWLINE", "COMMENT", "WS", 
                      "INTEGER", "DOUBLE", "STRING", "BOOLEAN", "ID", "ASSIGN", 
                      "ADD_ASSIGN", "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                      "PLUS", "MINUS", "TIMES", "MOD", "OVER" ]

    RULE_program = 0
    RULE_assignment = 1
    RULE_list = 2
    RULE_expression = 3
    RULE_value = 4

    ruleNames =  [ "program", "assignment", "list", "expression", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NEWLINE=6
    COMMENT=7
    WS=8
    INTEGER=9
    DOUBLE=10
    STRING=11
    BOOLEAN=12
    ID=13
    ASSIGN=14
    ADD_ASSIGN=15
    MINUS_ASSIGN=16
    MUL_ASSIGN=17
    DIV_ASSIGN=18
    PLUS=19
    MINUS=20
    TIMES=21
    MOD=22
    OVER=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(FiveStarParser.EOF, 0)

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FiveStarParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(FiveStarParser.AssignmentContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FiveStarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FiveStarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return FiveStarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = FiveStarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FiveStarParser.T__0) | (1 << FiveStarParser.T__3) | (1 << FiveStarParser.INTEGER) | (1 << FiveStarParser.DOUBLE) | (1 << FiveStarParser.STRING) | (1 << FiveStarParser.BOOLEAN) | (1 << FiveStarParser.ID) | (1 << FiveStarParser.PLUS) | (1 << FiveStarParser.MINUS))) != 0):
                self.state = 12
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 10
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 11
                    self.expression(0)
                    pass


                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 17
            self.match(FiveStarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FiveStarParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(FiveStarParser.ExpressionContext,0)


        def ASSIGN(self):
            return self.getToken(FiveStarParser.ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(FiveStarParser.ADD_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(FiveStarParser.MINUS_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(FiveStarParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(FiveStarParser.DIV_ASSIGN, 0)

        def getRuleIndex(self):
            return FiveStarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = FiveStarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(FiveStarParser.ID)
            self.state = 20
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FiveStarParser.ASSIGN) | (1 << FiveStarParser.ADD_ASSIGN) | (1 << FiveStarParser.MINUS_ASSIGN) | (1 << FiveStarParser.MUL_ASSIGN) | (1 << FiveStarParser.DIV_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 21
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FiveStarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FiveStarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return FiveStarParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list(self):

        localctx = FiveStarParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(FiveStarParser.T__0)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FiveStarParser.T__0) | (1 << FiveStarParser.T__3) | (1 << FiveStarParser.INTEGER) | (1 << FiveStarParser.DOUBLE) | (1 << FiveStarParser.STRING) | (1 << FiveStarParser.BOOLEAN) | (1 << FiveStarParser.ID) | (1 << FiveStarParser.PLUS) | (1 << FiveStarParser.MINUS))) != 0):
                self.state = 24
                self.expression(0)
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 25
                        self.match(FiveStarParser.T__1)
                        self.state = 26
                        self.expression(0) 
                    self.state = 31
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)



            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FiveStarParser.T__1:
                self.state = 34
                self.match(FiveStarParser.T__1)


            self.state = 37
            self.match(FiveStarParser.T__2)
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

        def value(self):
            return self.getTypedRuleContext(FiveStarParser.ValueContext,0)


        def PLUS(self):
            return self.getToken(FiveStarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(FiveStarParser.MINUS, 0)

        def ID(self):
            return self.getToken(FiveStarParser.ID, 0)

        def BOOLEAN(self):
            return self.getToken(FiveStarParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(FiveStarParser.STRING, 0)

        def list(self):
            return self.getTypedRuleContext(FiveStarParser.ListContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FiveStarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FiveStarParser.ExpressionContext,i)


        def TIMES(self):
            return self.getToken(FiveStarParser.TIMES, 0)

        def MOD(self):
            return self.getToken(FiveStarParser.MOD, 0)

        def OVER(self):
            return self.getToken(FiveStarParser.OVER, 0)

        def getRuleIndex(self):
            return FiveStarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FiveStarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==FiveStarParser.PLUS or _la==FiveStarParser.MINUS:
                    self.state = 40
                    _la = self._input.LA(1)
                    if not(_la==FiveStarParser.PLUS or _la==FiveStarParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 43
                self.value()
                pass

            elif la_ == 2:
                self.state = 44
                self.match(FiveStarParser.ID)
                pass

            elif la_ == 3:
                self.state = 45
                self.match(FiveStarParser.BOOLEAN)
                pass

            elif la_ == 4:
                self.state = 46
                self.match(FiveStarParser.STRING)
                pass

            elif la_ == 5:
                self.state = 47
                self.list()
                pass

            elif la_ == 6:
                self.state = 48
                self.match(FiveStarParser.T__3)
                self.state = 49
                self.expression(0)
                self.state = 50
                self.match(FiveStarParser.T__4)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 60
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = FiveStarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 54
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 55
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FiveStarParser.TIMES) | (1 << FiveStarParser.MOD) | (1 << FiveStarParser.OVER))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = FiveStarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 57
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 58
                        _la = self._input.LA(1)
                        if not(_la==FiveStarParser.PLUS or _la==FiveStarParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        self.expression(8)
                        pass

             
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(FiveStarParser.INTEGER, 0)

        def DOUBLE(self):
            return self.getToken(FiveStarParser.DOUBLE, 0)

        def STRING(self):
            return self.getToken(FiveStarParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(FiveStarParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(FiveStarParser.ID, 0)

        def list(self):
            return self.getTypedRuleContext(FiveStarParser.ListContext,0)


        def getRuleIndex(self):
            return FiveStarParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = FiveStarParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FiveStarParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(FiveStarParser.INTEGER)
                pass
            elif token in [FiveStarParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(FiveStarParser.DOUBLE)
                pass
            elif token in [FiveStarParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.match(FiveStarParser.STRING)
                pass
            elif token in [FiveStarParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.match(FiveStarParser.BOOLEAN)
                pass
            elif token in [FiveStarParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.match(FiveStarParser.ID)
                pass
            elif token in [FiveStarParser.T__0]:
                self.enterOuterAlt(localctx, 6)
                self.state = 70
                self.list()
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         




