# main.py

from lex import lexer
from parser import parser
from interpreter import Interpreter

def run_dsl(script):
    interpreter = Interpreter()
    print("\n--- Running DSL Script ---\n")

    for line in script:
        line = line.strip()

        # skip empty lines and comments
        if not line or line.startswith("#"):
            continue

        print(f"> {line}")
        command = parser.parse(line, lexer=lexer)
        interpreter.execute(command)

def run_dsl_file(filepath):
    print(f"\n[DSL] Reading script: {filepath}")
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
        run_dsl(lines)
    except FileNotFoundError:
        print(f"[DSL] Error: file '{filepath}' not found.")

if __name__ == "__main__":
    run_dsl_file("sentiment_pipeline.dsl")