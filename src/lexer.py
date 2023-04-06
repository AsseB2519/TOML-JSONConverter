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
    'REAL',
    'NEWLINE'
)

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

t_STRING = r'(?<=")[^"\n]*(?=")'

t_BOOL = r'(?i)\b(?:true|false)\b'

t_NEWLINE = r'\n'

def t_REAL(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'-?\d+(?!\d|T|-|:)'
    t.value = int(t.value)
    return t

t_ignore = " \""

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

inp2 = """
# This is a TOML document

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[database]
enabled = true
"""

lexer.input(inp2)

while tok := lexer.token():
  print(tok)

def p_toml(p):
    '''
    toml : toml keyvalue_list
         | toml table
         | keyvalue_list
         | table
    '''
    if len(p) == 3:
        if isinstance(p[1], dict) and isinstance(p[2], tuple):
            p[1].update([p[2]])
        elif isinstance(p[1], dict) and isinstance(p[2], list):
            p[1].update(p[2])
        p[0] = p[1]
    else:
        if isinstance(p[1], tuple):
            p[0] = {p[1][0]: p[1][1]}
        elif isinstance(p[1], list):
            p[0] = dict(p[1])

def p_keyvalue_list(p):
    '''
    keyvalue_list : keyvalue_list keyvalue
                  | keyvalue_list NEWLINE
                  | keyvalue
                  | NEWLINE
    '''
    if len(p) == 3:
        if p[1] is None:
            p[1] = []
        if isinstance(p[2], tuple):
            p[1].append(p[2])
        p[0] = p[1]
    else:
        if isinstance(p[1], tuple):
            p[0] = [p[1]]
        else:
            p[0] = []

def p_keyvalue(p):
    '''
    keyvalue : KEY EQUALS value NEWLINE
    '''
    p[0] = (p[1], p[3])

def p_table(p):
    '''
    table : OBRACKET TABLENAME CBRACKET NEWLINE keyvalue_list
    '''
    p[0] = [(p[2], dict(p[5]))]

def p_value(p):
    '''
    value : INT
          | REAL
          | STRING
          | BOOL
          | FIRSTCLASSDATE
    '''
    p[0] = p[1]

def p_error(p):
    print(f"Syntax error at line {p.lineno}, column {p.lexpos}")

parser = yacc.yacc()
parsed_dict = parser.parse(inp2, lexer=lexer, debug=True)
json_str = json.dumps(parsed_dict)

print(json_str)

