import json
from lexer import lexer
from parser import parser

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

def main():
    lexer.input(inp)
    parsed_dict = parser.parse(inp, lexer=lexer)
    json_str = json.dumps(parsed_dict, indent=2)
    print(json_str)

if __name__ == '__main__':
    main()
