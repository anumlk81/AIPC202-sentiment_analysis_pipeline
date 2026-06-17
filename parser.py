import ply.yacc as yacc
from lex import tokens

def p_command(p):
    '''command : LOAD VECTOR
               | SAVE VECTOR
               | LOAD MODEL
               | SAVE MODEL
                | ANALYSE DATASET
               | SAVE RESULTS
               | sentiment'''
    if len(p)==3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_sentiment(p):
    '''sentiment : POSITIVE
                 | NEGATIVE
                 | NEUTRAL'''
    p[0] = ('sentiment', p[1])

def p_error(p):
    if p:
        print(f"syntax error at'{p.value}'")
    else:
        print("syntax error at EOF")

parser = yacc.yacc()

if __name__ == '__main__':
    test_input = ["load vector",
                   "save model", 
                   "positive", "negative", "neutral", "invalid command"]
    from lex import lexer
    for test in test_input:
        result = parser.parse(test, lexer=lexer)
        print(f"Input: '{test}' -> Parsed: {result}")