import ply.yacc as yacc
from lexer import tokens

def merge_dicts(d1, d2):
    for key, value in d2.items():
        if key in d1 and isinstance(d1[key], dict) and isinstance(value, dict):
            merge_dicts(d1[key], value)
        else:
            d1[key] = value

def p_toml(p):
    '''
    toml : toml inline_table
         | toml keyvalue
         | toml keyvalue_list
         | toml table
         | toml subtable_list
         | inline_table
         | keyvalue
         | keyvalue_list
         | table
         | subtable_list
    '''
    if len(p) == 3:
        if isinstance(p[1], dict) and isinstance(p[2], tuple):
            merge_dicts(p[1], {p[2][0]: p[2][1]})
        elif isinstance(p[1], dict) and isinstance(p[2], list) and len(p[2]) == 2:
            for item in p[2]:
                merge_dicts(p[1], {item[0]: item[1]})
        elif isinstance(p[1], dict) and isinstance(p[2], list) and len(p[2]) == 0:  # handle empty list
            pass
        else:
            merge_dicts(p[1], {p[2][0][0]: p[2][0][1]})
        p[0] = p[1]
    else:
        if isinstance(p[1], tuple):
            p[0] = {p[1][0]: p[1][1]}
        elif isinstance(p[1], list):
            p[0] = dict(p[1])

def p_inline_table1(p):
    '''
    inline_table : KEY EQUALS INLINETABLE NEWLINE
    '''
    p[0] = (p[1], p[3])

def p_inline_table2(p):
    '''
    inline_table : NEWLINE
    '''
    p[0] = []

def p_keyvalue_list1(p):
    '''
    keyvalue_list : keyvalue_list keyvalue
    '''
    if p[1] is None:
        p[1] = []
    if isinstance(p[2], tuple):
        p[1].append(p[2])
    p[0] = p[1]

def p_keyvalue_list2(p):
    '''
    keyvalue_list : keyvalue_list NEWLINE
    '''
    p[0] = p[1]

def p_keyvalue_list3(p):
    '''
    keyvalue_list : keyvalue
    '''
    p[0] = [p[1]]

def p_keyvalue_list4(p):
    '''
    keyvalue_list : NEWLINE
    '''
    p[0] = []

def p_keyvalue(p):
    '''
    keyvalue : KEY EQUALS value
             | KEY EQUALS INLINETABLE
    '''
    key_parts = p[1].split('.')
    if len(key_parts) > 1:
        nested_dict = p[3]
        for part in reversed(key_parts):
            nested_dict = {part: nested_dict}
        p[0] = (key_parts[0], nested_dict[key_parts[0]])
    else:
        p[0] = (p[1], p[3])

def p_subtable1(p):
    '''
    subtable : OBRACKET SUBTABLENAME CBRACKET NEWLINE
    '''
    subtable_dict = {}
    names = p[2].split(".")
    sub_dict = subtable_dict
    for name in names[:-1]:
        if name not in sub_dict and  name is not names[0]:
            sub_dict[name] = {}
        if name is not names[0]:
            sub_dict = sub_dict[name]
    sub_dict[names[-1]] = {}
    p[0] = subtable_dict

def p_subtable2(p):
    '''
    subtable : OBRACKET SUBTABLENAME CBRACKET NEWLINE keyvalue_list
    '''
    subtable_dict = {}
    names = p[2].split(".")
    sub_dict = subtable_dict
    for name in names[:-1]:
        if name not in sub_dict and  name is not names[0]:
            sub_dict[name] = {}
        if name is not names[0]:
            sub_dict = sub_dict[name]
    sub_dict[names[-1]] = dict(p[5])
    p[0] = subtable_dict

def p_subtable_list(p):
    '''
    subtable_list : subtable
    '''
    p[0] = p[1]

def p_subtable_list2(p):
    '''
    subtable_list : subtable_list subtable
    '''
    merge_dicts(p[1], p[2])
    p[0] = p[1]

def p_table1(p):
    '''
    table : OBRACKET TABLENAME CBRACKET NEWLINE
    '''
    p[0] = [(p[2], {})]

def p_table2(p):
    '''
    table : OBRACKET TABLENAME CBRACKET NEWLINE keyvalue_list
    '''
    p[0] = [(p[2], dict(p[5]))]

def p_table3(p):
    '''
    table : OBRACKET TABLENAME CBRACKET NEWLINE subtable_list
    '''
    p[0] = [(p[2], p[5])]

def p_table4(p):
    '''
    table : OBRACKET TABLENAME CBRACKET NEWLINE inline_table subtable_list
    '''
    if isinstance(p[5], tuple):
        p[0] = [(p[2], merge_dicts({p[5][0]: p[5][1]}, p[6]))]
    else:
        p[0] = [(p[2], p[6])]

def p_value1(p):
    '''
    value : INT
          | REAL
          | STRING
          | FIRSTCLASSDATE
          | DATE
          | TIME
          | list
    '''
    p[0] = p[1]

def p_value2(p):
    '''
    value : BOOL
    '''
    if p[1].lower() == 'true':
        p[0] = True
    else:
        p[0] = False

def p_list(p):
    '''
    list : OBRACKET nested_values CBRACKET
    '''
    p[0] = p[2]

def p_values1(p):
    '''
    values : value
    '''
    p[0] = [p[1]]

def p_values2(p):
    '''
    values : values COMMA value
    '''
    p[0] = p[1] + [p[3]]

def p_nested_values1(p):
    '''
    nested_values : nested_values COMMA value
    '''
    p[0] = p[1] + [p[3]]

def p_nested_values2(p):
    '''
    nested_values : nested_values COMMA list
    '''
    p[0] = p[1] + [p[3]]

def p_nested_values3(p):
    '''
    nested_values : value
    '''
    p[0] = [p[1]]

def p_nested_values4(p):
    '''
    nested_values : list
    '''
    p[0] = [p[1]]

def p_error(p):
    print(f"Syntax error at line {p.lineno}, column {p.lexpos}, '{p.value}'")

parser = yacc.yacc()
