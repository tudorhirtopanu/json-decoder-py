from json_lexer import tokens

def parse_object(tokens):
    obj = {}
    
    token = next(tokens, None)
    if token is None or token.type != 'LBRACE':
        raise ValueError("Expected an object to start with '{'")
    
    for token in tokens:
        if token.type == 'RBRACE':
            return obj
        if token.type == 'STRING':
            key = token.value.strip('"')
            token = next(tokens, None)
            if token is None or token.type != 'COLON':
                raise ValueError("Expected a ':' after a key")
            value = parse_value(tokens)
            obj[key] = value
            token = next(tokens, None)
            if token is None:
                raise ValueError("Expected '}' or ',' in object")
            if token.type == 'RBRACE':
                return obj
            if token.type != 'COMMA':
                raise ValueError("Expected a ',' after a value in object")
            
def parse_array(tokens):
    arr = []
    
    token = next(tokens, None)
    if token is None or token.type != 'LBRACKET':
        raise ValueError("Expected an array to start with '['")
    
    for token in tokens:
        if token.type == 'RBRACKET':
            return arr
        value = parse_value(tokens)
        arr.append(value)
        token = next(tokens, None)
        if token is None:
            raise ValueError("Expected ']' or ',' in array")
        if token.type == 'RBRACKET':
            return arr
        if token.type != 'COMMA':
            raise ValueError("Expected a ',' after a value in array")

def parse_value(tokens):
    token = next(tokens, None)
    if token is None:
        raise ValueError("Unexpected end of input")
    if token.type == 'STRING':
        return token.value.strip('"') ######
    if token.type == 'NUMBER':
        return float(token.value) if '.' in token.value or 'e' in token.value.lower() else int(token.value)
    if token.type == 'TRUE':
        return True
    if token.type == 'FALSE':
        return False
    if token.type == 'NULL':
        return None
    if token.type == 'LBRACE':
        return parse_object(tokens)
    if token.type == 'LBRACKET':
        return parse_array(tokens)
    raise ValueError(f"Unexpected token: {token.type}")
