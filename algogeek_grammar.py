# a grammar handler for an algorithm compiler

class Group:
    def __init__(self, group_name):
        '''class to handle command or operator groups/types'''
        self.name = group_name
        self.commands = []
    def __contains__(self, x):
        '''Group.__contains__(x) <=> x in Group'''
        return x in self.commands
    def add(self, command):
        '''adds commands to the group if commands'''
        self.commands.append(command)

        
def tokenise(sentence, groups):
    '''a function to categorse parts of a sentence in the algorithm to the classes as given in the groups'''
    parts = sentence.split()
    types = []
    string_val = ''
    add = False
    for part in parts:
        for group in groups:
            if part.lower() in group:
                types.append((part, group.name))
                break
        else:
            if part.startswith('"') and part.endswith('"'):
                types.append((part, 'string_literal'))
            elif part.startswith('"'):
                add = True
                string_val += part
            elif add == True:
                string_val += ' '+ part
                if part.endswith('"'):
                    add = False
                    types.append((string_val, 'string_literal'))
                
            elif part.isdigit() or (False not in [u.isdigit() for u in part.split('.')]):
                types.append((int(part), 'number'))
            elif ',' in part:
                sub = part.split(',')
                for item in sub:
                    types.append((item, 'variable'))
            else:
                types.append((part, 'variable'))
                
    return types

class Grammar_Rule:
    def __init__(self, structure_type):
        '''basic class to denote a rule in the compiler's grammar'''
        self.structures = []
        self.type = structure_type
    def add(self, rule):
        '''updates self.structure'''
        self.structures.append(rule.split())
    def validate(self, token_list):
        '''validates if the sentence structure is correct from the list of tokens extracted from the sentence'''
        if [token[1] for token in token_list]  in self.structures:
            return True
        else:
            return False
