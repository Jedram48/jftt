import ply.lex as lex
import ply.yacc as yacc

TOP = 1234577
rpn = ""

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POWER',
    'LPAREN',
    'RPAREN',
    'MOD',
)

t_ignore = ' \t'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Nieznany znak: {t.value[0]}")
    t.lexer.skip(1)

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'UMINUS'),
    ('right', 'POWER'),
)

def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression POWER expression
               | expression MOD expression
               | LPAREN expression RPAREN
               | MINUS NUMBER %prec UMINUS
               | NUMBER
    '''
    global rpn
    if len(p) == 2:
        p[0] = GF(p[1])
        rpn += str(p[0]) + " "
    elif p[1] == '(':
        p[0] = p[2]
    elif p[1] == '-':
        p[0] = -(p[2])
        rpn += str(GF(p[0])) + " "
    else:
        p[0] = calculate(p[2], p[1], p[3])
        rpn += str(p[2]) + " "

def GF(a):
    neg = False
    if a < 0:
        neg = True
    a = abs(a)
    while a > TOP:
        a -= TOP
    if neg:
        return TOP - a
    return a

def modinv(a, p):
    m0 = p
    t, q = 0, 0
    x0, x1 = 0, 1
    if p == 1:
        return 0
    while a > 1:
        q = a // p
        t = p
        p = a % p
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if x1 < 0:
        x1 += m0
    return x1

def divide(a, b):
    b_inverse = modinv(GF(b), TOP)
    if b_inverse == 0:
        print("Dzielenie przez 0!")
        return 0
    result = (a * b_inverse) % TOP
    return GF(result)

def potengowanie(a, b):
    result = a
    neg = b < 0
    b = abs(b)
    while b > 1:
        result *= a
        b -= 1
        if result > TOP:
            result -= TOP
    if neg:
        return divide(1, result)
    return result

def calculate(op, a, b):
    if op == '+':
        return GF(a + b)
    elif op == '-':
        return GF(a - b)
    elif op == '*':
        return GF(a * b)
    elif op == '/':
        if b == 0:
            yacc.yacc().error("Cannot divide by zero")
        else:
            return GF(divide(a, b))
    elif op == '%':
        if b == 0:
            yacc.yacc().error("Cannot mod by zero")
        else:
            return GF(a % b)
    elif op == '^':
        return GF(potengowanie(a, b))

def p_error(p):
    print("Błąd składni")

lexer = lex.lex()
parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        try:
            rpn = ""
            input_line = input("Podaj wyrażenie (lub 'exit' aby wyjść): ")
            if input_line.lower() == 'exit':
                break
            if not input_line or input_line.startswith('#'):
                continue

            result = GF(parser.parse(input_line, lexer=lexer))
            print(rpn)
            print(f"Wynik: {result}")

        except Exception as e:
            print(f"Błąd: {e}")
