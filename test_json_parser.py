from json_parser import parse_object, parse_value, parse_array
from json_lexer import lexer

# Example JSON input
json_input = '''
{
    "name": "John",
    "age": 30,
    "isMarried": true,
    "cars":[1, "A", "3"],
    "salary":1000
}
'''

# Create a generator of tokens using the lexer (json_lexer.tokens)

lexer.input(json_input)
tokens = list(lexer)

# Call the parsing functions to parse the JSON
parsed_json = parse_object(iter(tokens))  # Assuming you have a parse_object function

# Now 'parsed_json' contains a Python data structure representing the JSON input
print(parsed_json)
print(parsed_json["name"])
print(parsed_json["age"])

carArray = parsed_json["cars"]
print(carArray[0])