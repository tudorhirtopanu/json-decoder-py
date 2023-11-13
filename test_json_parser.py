from json_parser import parse_value
from json_lexer import lexer

# Example JSON input
json_input = '''
[{
    "name": "John",
    "age": 30,
    "isMarried": true,
    "cars":[1, "A", "3"],
    "salary":1000,
    "object":{
    "test":true
    }
},
{
    "name": "Sam",
    "age": 40,
    "isMarried": true,
    "cars":[1, "A", "3"],
    "salary":1000,
    "object":{
    "test":false
    }
}]
'''

# Create a generator of tokens using the lexer (json_lexer.tokens)

lexer.input(json_input)
tokens = list(lexer)

# Call the parsing functions to parse the JSON
parsed_json = parse_value(tokens[0], iter(tokens[1:]))  # Assuming you have a parse_object function

# Now 'parsed_json' contains a Python data structure representing the JSON input
print(parsed_json)