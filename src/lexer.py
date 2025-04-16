#! /usr/bin/env python

import re

class Rule:

    def __init__(self, name: str, pattern: str) -> None:
        '''
            Rule class to specify lexer rules for identifying tokens
        '''
        self.name = name # name of the token type
        self.pattern = pattern # regular expression pattern

    def match(self, text: str) -> bool:
        '''
            Check if the given text matches the rule's pattern
        '''
        if re.fullmatch(self.pattern, text):
            return True
        return False
    
class Lexer:
    def __init__(self):
        self.lexeme_buffer = [] # holds the lexemes from each lexer call
        self.rules = {} # list of lexer rules
    
    def add_rule(self, token_type: str, pattern: str) -> None:
        '''
            Adds the given rule to help in identifying tokens
        '''
        self.rules.append(Rule(token_type, pattern))

    def tokenize(self, line: str) -> list:
        '''
            Tokenizes the given text using the lexer rules
        '''
        # The grammar of an algorithm is that each line consists of lexemes separated by
        # whitespace as a delimiter, in which case text.split() helps.
        # In case expressions tend to stay close, we'll scan them line by line to 
        # Separate out the lexemes.

        self.lexeme_buffer = line.split() # splits the line about the whitespace
        tokens = []
        for lexeme in self.lexeme_buffer:
            for id, rule in self.rules:
                if rule.match(lexeme):
                    tokens.append((id, lexeme))
                else:
                    raise Exception(f"Unknown lexeme: {lexeme}")
                
    
