
def parse_object(tokens):

    # Initialize empty dictionary to represent json object
    obj = {}
    
    # Get the first token from input
    token = next(tokens, None)

    # Check if the input starts with an opening curly brace '{'
    if token is None or token.type != 'LBRACE':
        raise ValueError("Expected an object to start with '{'")
    
    # Iterate through the tokens to parse key-value pairs in the object
    for token in tokens:

        # Check if the current token is the closing curly brace '}'
        if token.type == 'RBRACE':
            return obj
        
        # Check if the current token is a 'STRING' (indicating a key)
        if token.type == 'STRING':

            # Extract the key and remove surrounding double quotes
            key = token.value.strip('"')

            # Get the next token (expecting a colon ':')
            token = next(tokens, None)

            # Check if the next token is a colon ':'
            if token is None or token.type != 'COLON':
                raise ValueError("Expected a ':' after a key")
            
            # Check if the next token is an array or a regular JSON value
            if token.type == 'LBRACKET':
                value = parse_array(tokens)
            else:
                value = parse_value(tokens)

            # Add the key-value pair to the dictionary
            obj[key] = value

            # Get the next token (expecting either '}' or ',')
            token = next(tokens, None)

            # Check if the next token is '}' (indicating the end of the object)
            
            # If next token is '}' then return object
            if token.type == 'RBRACE':
                return obj
            
            # Token isn't '}' ...
            if token is None:
                raise ValueError("Expected '}' or ',' in object")

            if token.type != 'COMMA':
                raise ValueError("Expected a ',' after a value in object")
            
def parse_array(tokens):
    # Initialize an empty list to represent the JSON array
    arr = []
    
    # Get the first token from input
    token = next(tokens, None)

    print("array entered "+token.type)
    
    print("stop 1 " + token.type)

    # TODO Error if no comma
    # TODO Incorporate rest of function

    if token.type == 'RBRACKET':
        return arr  # Return an empty array if the array is empty

    while token:
        if token.type != None :
            # Pass the current token to parse_value for parsing

            if token.type == 'COMMA':
                token = next(tokens, None)
                if token.type == 'RBRACKET':
                    raise ValueError("Object expected to follow after ','")

            value = parse_value(iter([token]))  # Pass the token in an iterator

            # Append the parsed value to the array
            arr.append(value)

        token = next(tokens, None)

        if token is None:
            raise ValueError("Expected ']' in array")

        if token.type == 'RBRACKET':
            print("Array End")
            return arr  # Return the array when ']' is encountered
        
        

     # Check if the input starts with an opening square bracket '['
    
     # Iterate through the tokens to parse elements in the array
    for token in tokens:
        print("stop 2 "+token.type)
        # Check if the current token is the closing square bracket ']'
        if token.type == 'RBRACKET':
            print("stop 3 "+token.type)
            return arr
        
        # Parse the value associated with the key (as in JSON arrays, there are no keys)
        value = parse_value(tokens)

        # Add the parsed value to the array
        arr.append(value)

        # Get the next token (expecting either ']' or ',')
        token = next(tokens, None)

        # Token isn't ']' ...
        if token is None:
            raise ValueError("Expected ']' or ',' in array")
        
        # Check if the next token is ']' (indicating the end of the array)
        if token.type == 'RBRACKET':
            return arr
        
        #  Check if the next token is a comma ',' to separate elements in the array
        if token.type != 'COMMA':
            raise ValueError("Expected a ',' after a value in array")

def parse_value(tokens):

    # Get the next token from the input
    token = next(tokens, None)

    print("value "+ token.value)

     # Check if the token is None, indicating an unexpected end of input
    if token is None:
        raise ValueError("Unexpected end of input")
    
    # If the token is a STRING, return its value with surrounding double quotes removed
    if token.type == 'STRING':
        return token.value.strip('"') 
    
    if token.type == 'NUMBER':
        # If the token is a NUMBER, parse it as a float if it contains a decimal point or scientific notation,
        # otherwise, parse it as an integer
        return float(token.value) if '.' in token.value or 'e' in token.value.lower() else int(token.value)
    
    # If the token is 'TRUE', return the boolean value True
    if token.type == 'TRUE':
        return True
    
    # If the token is 'FALSE', return the boolean value False
    if token.type == 'FALSE':
        return False
    
    # If the token is 'NULL', return None
    if token.type == 'NULL':
        return None
    
    # If the token is a left curly brace '{', parse an object
    if token.type == 'LBRACE':
        return parse_object(tokens)
    
    # If the token is a left square bracket '[', parse an array
    if token.type == 'LBRACKET':
        print("Array found")
        return parse_array(tokens)
    
    # If none of the expected token types are found, raise an error
    raise ValueError(f"Unexpected token: {token.type}")
