# ERROR
from error import Error, IllegalCharError, InvalidSyntaxError
# POSITION
from position import Position
# DIGITS
from digits import DIGITS
# TOKENS
from token import TOKENTYPE_INT, TOKENTYPE_FLOAT, TOKENTYPE_PLUS, TOKENTYPE_MINUS, TOKENTYPE_MUL, TOKENTYPE_DIV, TOKENTYPE_LEFTPARENTESIS, TOKENTYPE_RIGHTPARENTESIS, TOKENTYPE_EOF, Token

#############
### LEXER ###
#############

class Lexer:
    def __init__(self, file_name, text):
        self.file_name = file_name
        self.text = text
        self.position = Position(-1, 0, -1, file_name, text)
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.position.advance(self.current_char)
        self.current_char = self.text[self.position.index] if self.position.index < len(self.text) else None
    
    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TOKENTYPE_PLUS, position_start=self.position))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TOKENTYPE_MINUS, position_start=self.position))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TOKENTYPE_MUL, position_start=self.position))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TOKENTYPE_DIV, position_start=self.position))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TOKENTYPE_LEFTPARENTESIS, position_start=self.position))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TOKENTYPE_RIGHTPARENTESIS, position_start=self.position))
                self.advance()
            else:
                position_start = self.position.copy()
                char = self.current_char
                self.advance()
                return[], IllegalCharError(position_start, self.position, ">>" + char + "<<")
        
        tokens.append(Token(TOKENTYPE_EOF, position_start=self.position))
        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0
        position_start = self.position.copy()

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TOKENTYPE_INT, int(num_str), position_start, self.position)
        else:
            return Token(TOKENTYPE_FLOAT, float(num_str), position_start, self.position)
