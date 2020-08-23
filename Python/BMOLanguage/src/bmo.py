#######################
### DIGIT CONSTANTS ###
#######################

#Digits
DIGITS = '0123456789'

##############
### ERRORS ###
##############

class Error:
    def __init__(self, error_name, error_details):
        self.error_name = error_name
        self.error_details = error_details

    def as_string(self):
        result = f'{self.error_name}:{self.error_details}'
        return result

class IllegalCharError(Error):
    def __init__(self, error_details):
        super().__init__('Illegal Character', error_details)


##############
### TOKENS ###
##############

#Tokens
TOKENTYPE_INT             = 'INT'
TOKENTYPE_FLOAT           = 'FLOAT'
TOKENTYPE_PLUS            = 'PLUS'
TOKENTYPE_MINUS           = 'MINUS'
TOKENTYPE_MUL             = 'MUL'
TOKENTYPE_DIV             = 'DIV'
TOKENTYPE_LEFTPARENTESIS  = 'LPAREN'
TOKENTYPE_RIGHTPARENTESIS = 'RPAREN'

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'


#############
### LEXER ###
#############

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
    
    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TOKENTYPE_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TOKENTYPE_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TOKENTYPE_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TOKENTYPE_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TOKENTYPE_LEFTPARENTESIS))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TOKENTYPE_RIGHTPARENTESIS))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return[], IllegalCharError(">>" + char + "<<")
        
        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TOKENTYPE_INT, int(num_str))
        else:
            return Token(TOKENTYPE_FLOAT, float(num_str))

###########
### RUN ###
###########

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error