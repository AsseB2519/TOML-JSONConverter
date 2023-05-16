import ply.lex as lex

tokens = (
    'COMMENT',
    'EQUALS',
    'COMMA',
    'OBRACKET',
    'CBRACKET',
    'KEY',
    'INLINETABLE',
    'TABLENAME',
    'SUBTABLENAME',
    'STRING',
    'BOOL',
    'FIRSTCLASSDATE',
    'DATE',
    'TIME',
    'INT',
    'REAL',
    'NEWLINE'
)

def t_COMMENT(t):
    r'\#[^\n]*\n*'
    pass

t_FIRSTCLASSDATE = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}-\d{2}:\d{2}'

t_DATE = r'\d{4}-\d{2}-\d{2}'

t_TIME = r'\d{2}:\d{2}:\d{2}'

t_EQUALS = r'\='

t_COMMA = r','

t_OBRACKET = r'\['

t_CBRACKET = r']'

t_KEY = r'[A-Za-z\d_-]+(\.[A-Za-z\d_-]+)*(?=\s=)'



t_TABLENAME = r'(?<=\[)[^\[\]""]+(?=\])'

t_SUBTABLENAME = r'(?<=\[)[^\[\]"]+\.[^\[\]"]+(?=\])'

t_BOOL = r'\b(?:true|false)\b'

t_NEWLINE = r'\n'

def t_STRING(t):
    r'(\"([^\n\\\"]|\\.|\\\n)*\")|(\'([^\n\\\']|\\.|\\\n)*\')'
    t.value = t.value[1:-1]
    return t

def t_INLINETABLE(t):
    r'\{[^{}]*\}'
    d = {}
    parts = t.value[1:-1].split(',')
    for part in parts:
        key, value = [x.strip() for x in part.split('=')]
        value = value.strip('"')
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                if value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False

        # Handle nested keys
        key_parts = key.split('.')
        if len(key_parts) > 1:
            nested_dict = {key_parts[-1]: value}
            for part in reversed(key_parts[:-1]):
                nested_dict = {part: nested_dict}
            d.update(nested_dict)
        else:
            d[key] = value
    t.value = d
    return t



def t_REAL(t):
    r'(?<![\'"])-?\d+\.\d+(?![\'"])'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'(?<![\'"])((?<!\d)-)?\d+(?![\'"]|\d|T|-|:|(?<=\d)\s=)'
    t.value = int(t.value)
    return t

t_ignore = " "

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
