from json_parser import parse_value
from json_lexer import lexer
from dummy_json import json_input
import requests

api_url = 'https://jsonplaceholder.typicode.com/posts/1/comments'
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Access the content of the response as a string
    data_as_string = response.text
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

# Create a generator of tokens using the lexer (json_lexer.tokens)
lexer.input(data_as_string)
tokens = list(lexer)

# Call the parsing functions to parse the JSON
parsed_json = parse_value(tokens[0], iter(tokens[1:]))  # Assuming you have a parse_object function

# Now 'parsed_json' contains a Python data structure representing the JSON input
print(parsed_json)

object = parsed_json[1]
object_email = object["email"]

print(object_email)
