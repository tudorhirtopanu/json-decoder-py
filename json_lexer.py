from ply import lex

tokens = (
    'STRING',
    'NUMBER',
    'TRUE',
    'FALSE',
    'NULL',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COLON',
    'COMMA',
)

# Define regular expressions for tokens
t_STRING = r'"[^"]*"'
t_NUMBER = r'-?\d+(\.\d+)?([eE][-+]?\d+)?'
t_TRUE = r'true'
t_FALSE = r'false'
t_NULL = r'null'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COLON = r':'
t_COMMA = r','

# Handle whitespace (ignored)
t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Sample input for testing
sample_input = '''
{
    "name": "John",
    "age": 30,
    "isMarried":true
}
'''

# Test the lexer with the sample input
#lexer.input(sample_input)
#for token in lexer:
   # print(f"Token: {token.type}, Value: {token.value}")
