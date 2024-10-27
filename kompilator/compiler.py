import sys
import os
from lexer import lexer
from _parser import parser, get_generated_code
def main():
    if len(sys.argv) != 3:
        print("python compiler.py <input_file.imp> <output_file.mr>")
        exit()
    
    with open(sys.argv[1], "r") as f:
        code = f.read()
        lexer.input(code)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
            
    output = get_generated_code(code)
    with open(sys.argv[2], "w") as f:
        for inst in output:
            f.write(inst + '\n')
    
if __name__ == "__main__":
    main()