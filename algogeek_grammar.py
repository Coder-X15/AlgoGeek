# a grammar handler for an algorithm compiler

class Group:
    def __init__(self, group_name):
        self.name = group_name
        self.commands = []
    def __contains__(self, x):
        return x in self.commands
    def add(self, command):
        self.commands.append(command)

        
def tokenise(sentence, groups):
    '''a function to categorse parts of a sentence in the algorithm to the classes as given in the groups'''
    parts = sentence.split()
    types = []
    string_val = ''
    add = False
    for part in parts:
        for group in groups:
            if part in group:
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
            elif part in ['+','-','/','*','//','%','>','<','>=','<=','==','!=','=','+=','-=','*=','/=','//=','%=']:
                types.append((part, 'operator'))
            elif ',' in part:
                sub = part.split(',')
                for item in sub:
                    types.append((item, 'variable'))
            else:
                types.append((part, 'variable'))
                
    return types

input_cmds = Group('input_command')
output_cmds = Group('output_command')
assignment_cmds = Group('assignment_command')
for cmd in 'print display output'.split():
    output_cmds.add(cmd)

for cmd in 'input read get'.split():
    input_cmds.add(cmd)
for cmd in 'set assign let'.split():
    assignment_cmds.add(cmd)
cmd_groups = [input_cmds, output_cmds, assignment_cmds]
                
