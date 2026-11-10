def parse_transicion():
    if token.tipo == 'TOKEN_ID':
        get_token() 
    else:
        error("Error sintactico: Se esperaba un identificador de origen")
        
    if token.tipo == 'TOKEN_ARROW':
        get_token()
    else:
        error("Error sintactico: Se esperaba el operador de transición '->'")
        
    if token.tipo == 'TOKEN_ID':
        get_token() 
    else:
        error("Error sintactico: Se esperaba un identificador de destino")
        
    if token.tipo == 'TOKEN_LBRACKET':
        parse_opcional_atributos()
        
    if token.tipo == 'TOKEN_SEMICOLON':
        get_token() 
    else:
        error("Error sintactico: Falta punto y coma ';' al final de la transición")