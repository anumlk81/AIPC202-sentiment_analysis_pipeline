import ply.lex as lex

#tokens for sentiment analysis
tokens = (
    'POSITIVE',
    'NEGATIVE',
    'NEUTRAL',
    'LOAD',
    'SAVE',
    'VECTOR',
    'MODEL',


)

#regural expressions for tokens
t_POSITIVE = r'\b(positive|good|great|excellent|amazing|fantastic|happy|love)\b'
t_NEGATIVE = r'\b(negative|bad|terrible|awful|horrible|sad|hate)\b'
t_NEUTRAL = r'\b(neutral|okay|fine|average|mediocre)\b'
t_LOAD = r'\bload\b'
t_SAVE = r'\bsave\b'
t_VECTOR = r'\bvector\b'
t_MODEL = r'\bmodel\b'

#A regular expression with some action code. 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

#Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

#Build the lexer
lexer = lex.lex()