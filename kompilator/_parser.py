import ply.yacc as yacc
from lexer import tokens
from generate_code import generator

generator = generator()

# Define precedence
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
    ('left', 'MOD'),
)

# Define the start symbol
start = 'program_all'

# Define the grammar rules
def p_program_all(p):
    # '''program_all : procedures main'''
    '''program_all : main'''
    generator.program_start(p[1])

# def p_procedures(p):
#     '''procedures : procedures PROCEDURE proc_head IS declarations IN commands END
#                   | procedures PROCEDURE proc_head IS IN commands END
#                   |'''
#     # Implementation goes here

def p_main(p):
    '''main : PROGRAM IS declarations IN commands END
            | PROGRAM IS IN commands END'''
    p[0] = generator.main_start

# def p_commands(p):
#     '''commands : commands command
#                 | command'''
#     # Implementation goes here
    
def p_commands(p):
    '''commands : command'''
    p[0] = None

# def p_command(p):
#     '''command : identifier ASSIGN expression SEMICOLON
#                | IF condition THEN commands ELSE commands ENDIF
#                | IF condition THEN commands ENDIF
#                | WHILE condition DO commands ENDWHILE
#                | REPEAT commands UNTIL condition SEMICOLON
#                | proc_call SEMICOLON
#                | READ identifier SEMICOLON
#                | WRITE value SEMICOLON'''
#     # Implementation goes here

def p_command(p):
    '''command : identifier ASSIGN expression SEMICOLON'''
    generator.assign(p[1], p[3])

# def p_command(p):
#     '''command : READ identifier SEMICOLONN'''
#     # Implementation goes here\
        
# def p_command(p):
#     '''command : WRITE value SEMICOLON'''
#     # Implementation goes here

# def p_proc_head(p):
#     '''proc_head : pidentifier OPEN_PAREN args_decl CLOSE_PAREN'''
#     # Implementation goes here

# def p_proc_call(p):
#     '''proc_call : pidentifier OPEN_PAREN args CLOSE_PAREN'''
#     # Implementation goes here

# def p_declarations(p):
#     '''declarations : declarations COMMA pidentifier
#                     | declarations COMMA pidentifier OPEN_BRACKET num CLOSE_BRACKET
#                     | pidentifier
#                     | pidentifier OPEN_BRACKET num CLOSE_BRACKET'''
#     # Implementation goes here

def p_declarations(p):
    '''declarations : IDENTIFIER'''
    generator.add_variable(p[1])
                    
def p_mult_declarations(p):
    '''declarations : declarations COMMA IDENTIFIER'''
    generator.add_variable(p[3])

# def p_args_decl(p):
#     '''args_decl : args_decl COMMA pidentifier
#                  | args_decl COMMA T pidentifier
#                  | pidentifier
#                  | T pidentifier'''
#     # Implementation goes here

# def p_args(p):
#     '''args : args COMMA pidentifier
#             | pidentifier'''
#     # Implementation goes here

# def p_expression(p):
#     '''expression : value
#                   | value PLUS value
#                   | value MINUS value
#                   | value TIMES value
#                   | value DIVIDE value
#                   | value MOD value'''
#     # Implementation goes here

def p_expression(p):
    '''expression : value'''
    p[0] = int(p[1])

# def p_condition(p):
#     '''condition : value EQ value
#                  | value NEQ value
#                  | value GT value
#                  | value LT value
#                  | value GE value
#                  | value LE value'''
#     # Implementation goes here

def p_value(p):
    '''value : NUM
             | identifier'''
    p[0] = p[1]

# def p_identifier(p):
#     '''identifier : pidentifier
#                   | pidentifier OPEN_BRACKET NUM CLOSE_BRACKET
#                   | pidentifier OPEN_BRACKET pidentifier CLOSE_BRACKET'''
#     # Implementation goes here

def p_identifier(p):
    '''identifier : IDENTIFIER'''
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")

# Build the parser
parser = yacc.yacc()

def get_generated_code(code):
    parser.parse(code)
    return generator.cmd