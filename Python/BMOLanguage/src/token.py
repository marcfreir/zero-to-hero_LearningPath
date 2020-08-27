##############
### TOKENS ###
##############

TOKENTYPE_INT             = 'INT'
TOKENTYPE_FLOAT           = 'FLOAT'
TOKENTYPE_PLUS            = 'PLUS'
TOKENTYPE_MINUS           = 'MINUS'
TOKENTYPE_MUL             = 'MUL'
TOKENTYPE_DIV             = 'DIV'
TOKENTYPE_LEFTPARENTESIS  = 'LPAREN'
TOKENTYPE_RIGHTPARENTESIS = 'RPAREN'
TOKENTYPE_EOF             = 'EOF'

class Token:
    def __init__(self, type_, value=None, position_start=None, position_end=None):
        self.type = type_
        self.value = value

        if position_start:
            self.position_start = position_start.copy()
            self.position_end = position_start.copy()
            self.position_end.advance()
        
        if position_end:
            self.position_end = position_end

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'