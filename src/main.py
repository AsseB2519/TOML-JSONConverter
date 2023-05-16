import json
from lexer import lexer
from parser import parser

inp = """
[product]
type = { name = "Nail" }
"""

def main():
    lexer.input(inp)
    parsed_dict = parser.parse(inp, lexer=lexer)
    json_str = json.dumps(parsed_dict, indent=2)
    print(json_str)

if __name__ == '__main__':
    main()
