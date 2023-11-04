import re

def tokenize_json(json_string):

    token_patterns = [
    ('LBRACE', r'{'),
    ('RBRACE', r'}'),
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('COLON', r':'),
    ('COMMA', r','),
    ('STRING', r'"([^"\\]*(\\.[^"\\]*)*)"'),
    ('INTEGER', r'\d+'),
    ('FLOAT', r'-?\d+\.\d+'),
    ('BOOLEAN', r'true|false'),
    ('NULL', r'null'),
]

# Combine the token patterns into a single regular expression
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_patterns ) 

    tokens = []
    for match in re.finditer(token_regex, json_string):
        for name, value in match.groupdict().items():
            if value:
                tokens.append((name, value))
    return tokens

json_input = '{"name": "Josh", "Age": 20}'
tokens = tokenize_json(json_input)
print(tokens)
