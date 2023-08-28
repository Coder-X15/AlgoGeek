# execution handler

from algogeek_grammar import *

data = {} # where program data is held
commands = [] # where instructions as token-lists are stacked up
counter = 0 # a counter to help keeping track of steps

######## GRAMMAR SETUP ###########
###### TOKEN DEFINITIONS
input_cmds = Group('input_command')
output_cmds = Group('output_command')
assignment_cmds = Group('assignment_command')
flow_cmds = Group('flow_command')
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

for cmd in 'start begin stop end'.split():
    flow_cmds.add(cmd)

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
groups = [input_cmds, output_cmds, assignment_cmds,flow_cmds, math_operators, rel_operators, assignment_op, augmented_assignment]

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
    
# the start/stop stuff
flow = Grammar_Rule('flow')
possible_ways = ['flow_command']
for way in possible_ways:
    flow.add(way)

# rule to evaluate math expressions
math = Expression('math')
math.add('number variable math_operator')

# rule to evaluate comparisons
# adding the rules to the rulebook
rules = [display, assign, inputs, flow, math]
##################################

def evaluate(expression_parts):
    '''trying to get long math expressions evaluated'''
    eval_string = ''
    for token in expression_parts:
        if token[1] == 'variable':
            eval_string += str(data[token[0]])
        elif token[1] not in ('number','math_operator'):
            raise ValueError("Each operand must either be a number or a variable.")
        else:
            eval_string += str(token[0])
    return eval(eval_string)

    
def update_data(key, value, type_of_val):
    '''updates the data dictionary based on the type'''
    if type_of_val == 'number':
        data[key] = float(value)
    elif type_of_val == 'string_literal':
        data[key] = eval(value)
    elif type_of_val == 'variable':
        data[key] = data[value]
    else:
        raise ValueError("Invalid argument for 'type_of_val'; possible ones are 'number', 'variable', 'string_literal'")

def display(value, type_of_val):
    '''displays data'''
    if type_of_val == 'number':
        print(float(value))
    elif type_of_val == 'string_literal':
        print(eval(value))
    elif type_of_val == 'variable':
        print(data[value])
    else:
        raise ValueError("Invalid argument for 'type_of_val'; possible ones are 'number', 'variable', 'string_literal'")

def input_data(value, type_of_val):
    '''reads values from the command line and assigns to the variable 'value' '''
    if type_of_val != 'variable':
        raise ValueError("Only variables can be used to read data into.")
    data[value] = eval(input())

def add_step(sentence):
    '''adds a sentence to the algorithm'''
    tokens = tokenise(sentence, groups)
    for rule in rules:
        if rule.validate(tokens):
            commands.append(tokens)
            break
    else:
        raise SyntaxError("Incorrect sytax for the line: '", sentence, "'")

def execute():
    '''executes the algorithm'''
    global counter
    if commands[0][0][0] not in 'start begin' or commands[-1][0][0] not in 'stop end':
        raise Exception("Every algorithm must start with a start step and end with a stop step.")
    for line in commands:
        if line[0][0] in output_cmds:
            display(line[1][0], line[1][1])
        elif line[0][0] in input_cmds:
            input_data(line[1][0], line[1][1])
        elif line[0][0] in assignment_cmds:
            if len(line) <= 4:
                update_data(line[1][0], line[3][0], line[3][1])
            else:
                value = evaluate(line[3:])
                line = line[:3] + [(value, 'number')]
                update_data(line[1][0], line[3][0], line[3][1])
        else:
            pass
        counter += 1
            
if __name__ == "__main__":
    N = int(input("Enter the number of steps:"))
    for i in range(N):
        add_step(input(f'step {i + 1}:'))
    execute()
    
