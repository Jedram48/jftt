from sly import Lexer, Parser

# Definicja leksera
class CalcLexer(Lexer):
    tokens = {NUMBER, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, POWER}
    ignore = ' \t'

    # Tokeny
    NUMBER = r'\d+'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    LPAREN = r'\('
    RPAREN = r'\)'
    POWER = r'\^'

    # Obsługa tokenów
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value) % 1234577
        return t

# Definicja parsera
class CalcParser(Parser):
    tokens = CalcLexer.tokens
    rpn = ""

    def get_rpn():
        return rpn

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
        ('right', UMINUS),
        ('left', POWER)
    )

    # Produkcje
    @_('expr PLUS expr',
       'expr MINUS expr',
       'expr TIMES expr',
       'expr DIVIDE expr',
       'expr POWER expr')
    def expr(self, p):
        rpn += str(p[1]) + " "
        if p[1] == '+':
            return (p[0] + p[2]) % 1234577
        elif p[1] == '-':
            return (p[0] - p[2]) % 1234577
        elif p[1] == '*':
            return (p[0] * p[2]) % 1234577
        elif p[1] == '/':
            return (p[0] // p[2]) % 1234577
        elif p[1] == '^':
            return pow(p[0], p[2], 1234577)

    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        rpn += str((-p[1]) % 1234577) + " "
        return (-p[1]) % 1234577

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p[1]

    @_('NUMBER')
    def expr(self, p):
        rpn += str(p[0]) + " "
        return p[0]

class InputHandler:
    def __init__(self):
        self.current_line = ''
        self.lines = []

    def process_input(self, line):
        if line.startswith('#'):
            return
        if line.endswith('\\'):
            self.current_line += line[:-1]
        else:
            self.current_line += line
            self.lines.append(self.current_line)
            self.current_line = ''

def infix_to_rpn(expression):
    def precedence(operator):
        precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence_dict.get(operator, 0)

    def is_operator(char):
        operators = {'+', '-', '*', '/', '^'}
        return char in operators

    def to_rpn(infix_tokens):
        output = []
        stack = []

        for token in infix_tokens:
            if token.isalnum():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif is_operator(token):
                while stack and is_operator(stack[-1]) and precedence(stack[-1]) >= precedence(token):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return output

    expression_tokens = expression.replace(' ', '').replace('^', '**').replace('(-', '(0-').split()

    rpn_tokens = to_rpn(expression_tokens)

    rpn_expression = ' '.join(rpn_tokens)

    return rpn_expression

lexer = CalcLexer()
parser = CalcParser()
input_handler = InputHandler()

try:
    while True:
        try:
            line = input("Podaj wyrażenie (CTRL+C aby zakończyć): ")
        except KeyboardInterrupt:
            print("\nZakończono program.")
            break

        input_handler.process_input(line)

        for line in input_handler.lines:
            tokens = lexer.tokenize(line)
            result = parser.parse(tokens)
            rpn_expr = parser.get_rpn()
            print(f"{line}\nONP: {rpn_expr}\nWynik: {result % 1234577}")

        input_handler.lines = []  # Wyczyść listę po przetworzeniu
except EOFError:
    pass