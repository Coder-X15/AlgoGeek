# main place where the compiler is being developed
from algogeek_grammar import *
            
def test():
    ###### TOKEN DEFINITIONS
    input_cmds = Group('input_command')
    output_cmds = Group('output_command')
    assignment_cmds = Group('assignment_command')
    math_operators = Group('math_operator')
    rel_operators = Group('relational_operator')
    assignment_op = Group('assignment_operator')
    augmented_assignment = Group('augmented_assignment_operator')
    # adding the output commands
    for cmd in 'print display output'.split():
        output_cmds.add(cmd)

    # adding the input commands
    for cmd in 'input read get'.split():
        input_cmds.add(cmd)

    # adding the assignment commands    
    for cmd in 'set assign let'.split():
        assignment_cmds.add(cmd)

    # adding the math operators    
    for cmd in '+ - * / % //'.split():
        math_operators.add(cmd)

    # adding the relational operators
    for cmd in '> < >= <= == !='.split():
        rel_operators.add(cmd)
        
    # adding the assignment operator    
    for cmd in '='.split():
        assignment_op.add(cmd)

    # adding the augmented assignment operators    
    for cmd in '+= -= /= *= %= //='.split():
        augmented_assignment.add(cmd)

    # adding the groups
    groups = [input_cmds, output_cmds, assignment_cmds, math_operators, rel_operators, assignment_op, augmented_assignment]

    ###### GRAMMAR DEFINITIONS
    # rules to output stuff
    display = Grammar_Rule('display')
    possible_ways = ['output_command string_literal',
                     'output_command number',
                     'output_command variable']
    for way in possible_ways:
        display.add(way)
    # rules to assign stuff
    assign = Grammar_Rule('assign')
    possible_ways = ['assignment_command variable assignment_operator string_literal',
                     'assignment_command variable assignment_operator number']
    for way in possible_ways:
        assign.add(way)
    # rules to input stuff
    inputs = Grammar_Rule('input')
    possible_ways = ['input_command variable']
    for way in possible_ways:
        inputs.add(way)
    

    rules = [display, assign, inputs]
    
##    try:
##        while True:
##            command = input("Type a step in an algorithm:")
##            print("Tokens:---------")
##            tokens = tokenise(command, groups)
##            for token in tokens:
##                print(f'    {token[0]} : {token[1]}')
##            print("Type of command", end = ':')
##            for rule in rules:
##                if rule.validate(tokens):
##                    print(rule.type)
##    except:
##        print("Invalid syntax.")
    while True:
            command = input("Type a step in an algorithm:")
            print("Tokens:---------")
            tokens = tokenise(command, groups)
            for token in tokens:
                print(f'    {token[0]} : {token[1]}')
            print("Type of command", end = ':')
            for rule in rules:
                if rule.validate(tokens):
                    print(rule.type)
if __name__ == '__main__':
    test()
