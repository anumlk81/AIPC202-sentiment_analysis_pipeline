import ply.lex as lex

tokens = (
    'POSITIVE',
    'NEGATIVE',
    'NEUTRAL',
    'LOAD',
    'SAVE',
    'VECTOR',
    'MODEL',
    'ANALYSE',
    'DATASET',
    'RESULTS'
)

# Use functions for keyword tokens so PLY prioritises them correctly
def t_LOAD(t):
    r'\bload\b'
    return t

def t_SAVE(t):
    r'\bsave\b'
    return t

def t_VECTOR(t):
    r'\bvector\b'
    return t

def t_MODEL(t):
    r'\bmodel\b'
    return t

def t_POSITIVE(t):
    r'\b(positive|good|great|excellent|amazing|fantastic|happy|love)\b'
    return t

def t_NEGATIVE(t):
    r'\b(negative|bad|terrible|awful|horrible|sad|hate)\b'
    return t

def t_NEUTRAL(t):
    r'\b(neutral|okay|fine|average|mediocre)\b'
    return t

def t_ANALYSE(t):
    r'\banalyse\b'
    return t

def t_DATASET(t):
    r'\bdataset\b'
    return t

def t_RESULTS(t):
    r'\bresults\b'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()