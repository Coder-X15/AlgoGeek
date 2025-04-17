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

# Step 1: Create a class to represent the grammar rules for each kind
# Strategy - we start off with a single class that represents the whole grammar