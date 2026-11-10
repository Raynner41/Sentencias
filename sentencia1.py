# Sentenci: nodo Inicio as circle("Inicio"); 
def parse_nodo():
    
    if token.tipo == 'TOKEN_NODE':
        get_token() 
    else:
        error("Error sintactico: Se esperaba la palabra reservada 'node'")
        
    if token.tipo == 'TOKEN_ID':
        get_token()
    else:
        error("Error sintactico: Se esperaba un identificador para el nodo")
        
    if token.tipo == 'TOKEN_AS':
        get_token()
    else:
        error("Error sintactico: Se esperaba la palabra reservada 'as'")
        
    parse_forma() 
    
    if token.tipo == 'TOKEN_LPAREN':
        get_token()
    else:
        error("Error sintactico: Se esperaba '('")
        
    if token.tipo == 'TOKEN_STRING':
        get_token()
    else:
        error("Error sintactico: Se esperaba una cadena de texto (etiqueta)")
        
    if token.tipo == 'TOKEN_RPAREN':
        get_token()
    else:
        error("Error sintactico: Se esperaba ')'")
        
    if token.tipo == 'TOKEN_LBRACKET': 
        parse_opcional_atributos()
        
    if token.tipo == 'TOKEN_SEMICOLON':
        get_token()
    else:
        error("Error sintactico: Falta punto y coma ';' al final de la declaración")

