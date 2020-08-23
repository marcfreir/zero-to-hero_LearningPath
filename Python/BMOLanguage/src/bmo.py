#######################
### DIGIT CONSTANTS ###
#######################

#Digits
DIGITS = '0123456789'

##############
### ERRORS ###
##############

class Error:
    def __init__(self, position_start, position_end, error_name, error_details):
        self.position_start = position_start
        self.position_end = position_end
        self.error_name = error_name
        self.error_details = error_details

    def as_string(self):
        result = f'{self.error_name}: {self.error_details}\n'
        result += f'File {self.position_start.file_name}, line {self.position_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, position_start, position_end, error_details):
        super().__init__(position_start, position_end, 'Illegal Character', error_details)


################
### POSITION ###
################

class Position:
    def __init__(self, index, ln, col, file_name, file_txt):
        self.index = index
        self.ln = ln
        self.col = col
        self.file_name = file_name
        self.file_txt = file_txt

    def advance(self, current_char):
        self.index += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.index, self.ln, self.col, self.file_name, self.file_txt)

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
                position_start = self.position.copy()
                char = self.current_char
                self.advance()
                return[], IllegalCharError(position_start, self.position, ">>" + char + "<<")
        
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


#############
### NODES ###
#############

class NumberNode:
    def __init__(self, num_node_token):
        self.num_node_token = num_node_token
    
    def __repr__(self):
        return f'{self.num_node_token}'


class BinaryOperationNode:
    def __init__(self, left_node, binary_operation_token, right_node):
        self.left_node = left_node
        self.binary_operation_token = binary_operation_token
        self.right_node = right_node
    
    def __repr__(self):
        return f'({self.left_node}, {self.binary_operation_token}, {self.right_node})'


##############
### PARSER ###
##############

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = -1
        self.advance('')

    def advance(self, chunk):
        self.token_index += 1
        self.chunk = chunk

        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        return self.current_token

    def parse(self):
        result = self.expression()
        return result

    def factor(self):
        num_node_token = self.current_token

        if num_node_token.type in (TOKENTYPE_INT, TOKENTYPE_FLOAT):
            self.advance('')
            return NumberNode(num_node_token)


    def term(self):
        return self.binary_operation(self.factor, (TOKENTYPE_MUL, TOKENTYPE_DIV))


    def expression(self):
        return self.binary_operation(self.term, (TOKENTYPE_PLUS, TOKENTYPE_MINUS))

    def binary_operation(self, fun, operations):
        left = fun()

        while self.current_token.type in operations:
            binary_operation_token = self.current_token
            self.advance('')
            right = fun()
            left = BinaryOperationNode(left, binary_operation_token, right)

        return left


###########
### RUN ###
###########

def run(file_name, text):
    #Generate Tokens
    lexer = Lexer(file_name, text)
    tokens, error = lexer.make_tokens()

    if error:
        return None, error

    #Generate Abstract Syntax Tree
    parser = Parser(tokens)
    abs_sy_tree = parser.parse()

    return abs_sy_tree, None