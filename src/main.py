import ply.lex as lex
import ply.yacc as yacc
import json

tokens = (
    'COMMENT',
    'EQUALS',
    'COMMA',
    'OBRACKET',
    'CBRACKET',
    'OBRACE',
    'CBRACE',
    'KEY',
    'TABLENAME',
    'SUBTABLENAME',
    'STRING',
    'BOOL',
    'FIRSTCLASSDATE',
    'INT',
    'REAL'
)

# ignore comments
def t_COMMENT(t):
    r'\#[^\n]*'
    pass

t_FIRSTCLASSDATE = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}-\d{2}:\d{2}'

t_EQUALS = r'\='

t_COMMA = r','

t_OBRACKET = r'\['

t_CBRACKET = r']'

t_OBRACE = r'{'

t_CBRACE = r'}'

t_KEY = r'\S+(?=\s=)'

t_TABLENAME = r'(?<=\[)[^\[\]""]+(?=\])'

t_SUBTABLENAME = r'\[[^\[\]""]+\.[^\[\]""]+\]'

t_STRING = r'\"[^\"]*\"'

t_BOOL = r'(?i)\b(?:true|false)\b'

def t_REAL(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'-?\d+(?!\d|T|-|:)'
    t.value = int(t.value)
    return t

t_ignore = " \n"

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

inp = """
# This is a TOML document

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[database]
enabled = true
ports = [ 8000, 8001, 8002 ]
data = [ ["delta", "phi"], [3.14] ]
temp_targets = { cpu = 79.5, case = 72.0 }

[servers]

[servers.alpha]
ip = "10.0.0.1"
role = "frontend"

[servers.beta]
ip = "10.0.0.2"
role = "backend"
"""

lexer.input(inp)

while tok := lexer.token():
    print(tok)












