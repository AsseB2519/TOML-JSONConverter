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
    'INLINETABLE',
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

# t_KEY = r'\S+(?=\s=)'
#t_KEY = r'[A-Za-z\d_-]+(?=\s=)'
t_KEY = r'[A-Za-z\d_-]+(\.[A-Za-z\d_-]+)*(?=\s=)'

t_INLINETABLE = r'\{[^{}]*\}'

t_TABLENAME = r'(?<=\[)[^\[\]""]+(?=\])'

t_SUBTABLENAME = r'\[[^\[\]""]+\.[^\[\]""]+\]'

#t_STRING = r'(?<=")[^"\n]*(?=")'
#t_STRING = r'"(?:[^"\n]|\\.)*"'

t_BOOL = r'(?i)\b(?:true|false)\b'

t_NEWLINE = r'\n'

def t_STRING(t):
    r'(\"([^\n\\\"]|\\.|\\\n)*\")|(\'([^\n\\\']|\\.|\\\n)*\')'
    t.value = t.value[1:-1]
    return t

def t_REAL(t):
    #r'-?\d+\.\d+'
    r'(?<![\'"])-?\d+\.\d+(?![\'"])'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'(?<![\'"])((?<!\d)-)?\d+(?![\'"]|\d|T|-|:|(?<=\d)\s=)'
    t.value = int(t.value)
    return t

# t_ignore = " \""
t_ignore = " "
# t_ignore_COMMENT = r'\#[^\n]*'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

inp2 = """
name = "Orange"
physical.color = "orange"
physical.shape = "round"
"""

lexer.input(inp2)

while tok := lexer.token():
  print(tok)

def merge_dicts(d1, d2):
    for key, value in d2.items():
        if key in d1 and isinstance(d1[key], dict) and isinstance(value, dict):
            merge_dicts(d1[key], value)
        else:
            if isinstance(value, dict) and len(value) == 1:
                print(d1)
                print(key)
                print(value)
                k, v = next(iter(value.items()))
                print(k)
                print(v)
                #if key not in d1:
                #    print("cheguei")
                #    d1[key] = {}
                d1[k] = v
            else:
                d1[key] = value

def p_toml(p):
    '''
    toml : toml inline_table
         | toml keyvalue_list
         | toml table
         | inline_table
         | keyvalue_list
         | table
    '''
    if len(p) == 3:
        if isinstance(p[1], dict) and isinstance(p[2], tuple):
            merge_dicts(p[1], {p[2][0]: p[2][1]})
        elif isinstance(p[1], dict) and isinstance(p[2], list):
            for item in p[2]:
                merge_dicts(p[1], {item[0]: item[1]})
        p[0] = p[1]
    else:
        if isinstance(p[1], tuple):
            p[0] = {p[1][0]: p[1][1]}
        elif isinstance(p[1], list):
            p[0] = dict(p[1])

def p_inline_table(p):
    '''
    inline_table : KEY EQUALS INLINETABLE NEWLINE
                 | NEWLINE
    '''
    if len(p) == 5:
        p[0] = [(p[1], p[3])]
    else:
        p[0] = []

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
    keyvalue : KEY EQUALS value
    '''
    key_parts = p[1].split('.')
    if len(key_parts) > 1:
        nested_dict = {key_parts[-1]: p[3]}
        for part in reversed(key_parts[:-1]):
            nested_dict = {part: nested_dict}
        p[0] = (key_parts[0], nested_dict)
    else:
        if isinstance(p[3], list):
            value = dict(value=p[3])
            if len(value) == 1 and 'value' in value:
                p[0] = (p[1], value['value'])
            else:
                p[0] = (p[1], value)
        else:
            p[0] = (p[1], p[3])

def p_table(p):
    '''
    table : OBRACKET TABLENAME CBRACKET NEWLINE
          | OBRACKET TABLENAME CBRACKET NEWLINE keyvalue_list
    '''
    if len(p) == 5:
        p[0] = [(p[2], {})]
    else:
        p[0] = [(p[2], dict(p[5]))]


def p_value(p):
    '''
    value : INT
          | REAL
          | STRING
          | BOOL
          | FIRSTCLASSDATE
          | list
    '''
    if isinstance(p[1], str) and p[1].lower() == 'true':
        p[0] = True
    elif isinstance(p[1], str) and p[1].lower() == 'false':
        p[0] = False
    else:
        p[0] = p[1]

def p_list(p):
    '''
    list : OBRACKET nested_values CBRACKET
    '''
    p[0] = p[2]

def p_values(p):
    '''
    values : value
           | values COMMA value
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_nested_values(p):
    '''
    nested_values : nested_values COMMA value
                  | nested_values COMMA list
                  | value
                  | list
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_error(p):
    print(f"Syntax error at line {p.lineno}, column {p.lexpos}")

parser = yacc.yacc()
parsed_dict = parser.parse(inp2, lexer=lexer) #, debug=True)
json_str = json.dumps(parsed_dict)
print(json_str)

# try:
#     parsed_dict = parser.parse(inp2, lexer=lexer)
#     json_str = json.dumps(parsed_dict)
# except ValueError as e:
#     print(f"Error: {e}")
#     json_str = "{}"
