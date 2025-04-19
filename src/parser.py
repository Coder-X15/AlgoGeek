#!/usr/bin/env python

# we'll slowly implement the parser here
# first we'll document the rules that we'll implement [NB: S is the starting state]
#  1. Start/Stop:
#    S -> start
#    S -> stop
#  2. Standard input/ output
#    A) Output
#      S -> stdout EXPR
#      EXPR -> EXPR VAR EXPR | string
#      VAR -> int
#      VAR -> float
#      VAR -> string
#      VAR -> bool
#    B) Input
#      S -> stdin VAR
#      VAR -> id | VAR , VAR
#  3. Expressions:
#    S -> EXPR
#    EXPR -> EXPR OP EXPR | (EXPR) | FACTOR | id
#    OP -> + | - | * | / | % | ** | == | != | && | || | < | > | <= | >=
#    FACTOR -> int | float | str
#  4. Conditionals
#    S -> if EXPR then goto int else goto int
#  5. Loops
#    S -> while EXPR goto int | for id from int to int goto int
#  6. Goto stataments
#    S -> goto int

# Step 1: Create functions to validate each basic token

def isStart(token: tuple) -> bool:
    ''' validates the start token'''
    return token[0] == 'start'

def isStop(token: tuple) -> bool:
    ''' validates the stop token '''
    return token[0] == 'stop'

# Step 2: Construct mechanism to parse expressions
# This will involve creating the postfix order of the expression tokens, and then evaluating their order

# Step 3: Implement the parser functions for the rest of the rules

def isExpression(token_stream: list) -> bool:
    ''' validates the expression token stream '''
    return True # yet to implement the logic of

def isGoto(token_stream: list) -> bool:
    ''' validates the goto token stream '''
    return len(token_stream) == 2 and (token_stream[0][0] == 'goto' and token_stream[1][0] == 'int')

def isConditional(token_stream: list) -> bool:
    ''' validates the token stream for conditional statements'''
    def If(token: tuple) -> bool:
        return token[0] == 'if'
    def Then(token: tuple) -> bool:
        return token[0] == 'then'
    def Else(token: tuple) -> bool:
        return token[0] == 'else'
    
    pattern = [
        If, isExpression, Then, isGoto, Else, isGoto
    ]



