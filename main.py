# main.py

from lex import lexer
from parser import parser
from interpreter import Interpreter

def run_dsl(script):
    interpreter = Interpreter()

    print("\n--- Running DSL Script ---\n")

    for line in script:
        line = line.strip()
        if not line:
            continue

        print(f"> {line}")

        command = parser.parse(line, lexer=lexer)
        interpreter.execute(command)

if __name__ == "__main__":
    dsl_script = [
        "load vector",
        "load model",
        "analyse dataset",       # triggers analyse_dataset() with dataset.csv
        "save results",          # saves results.txt
    ]

    run_dsl(dsl_script)