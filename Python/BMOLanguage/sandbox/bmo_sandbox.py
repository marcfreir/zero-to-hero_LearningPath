###############
### IMPORTS ###
###############

from strings_with_circumflex import string_with_circumflex


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
        result += '\n\n' + string_with_circumflex(self.position_start.file_txt, self.position_start, self.position_end)
        return result

class IllegalCharError(Error):
    def __init__(self, position_start, position_end, error_details):
        super().__init__(position_start, position_end, 'Illegal Character', error_details)

class InvalidSyntaxError(Error):
    def __init__(self, position_start, position_end, error_details = ''):
        super().__init__(position_start, position_end, 'Invalid Syntax', error_details)


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

    def advance(self, current_char=None):
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
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TOKENTYPE_INT, int(num_str), position_start, self.position)
        else:
            return Token(TOKENTYPE_FLOAT, float(num_str), position_start, self.position)


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


class UnaryOperationNode:
    def __init__(self, unary_operation_token, node):
        self.unary_operation_token = unary_operation_token
        self.node = node
    
    def __repr__(self):
        return f'({self.unary_operation_token}, {self.node})'

#####################
### PARSER RESULT ###
#####################

class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None

    def register(self, result):
        if isinstance(result, ParseResult):
            if result.error:
                self.error = result.error
            return result.error

        return result

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        self.error = error
        return self


##############
### PARSER ###
##############

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = -1
        self.advance()

    def advance(self, ):
        self.token_index += 1
        #self.chunk = chunk

        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        return self.current_token

    def parse(self):
        result = self.expression()
        if not result.error and self.current_token.type != TOKENTYPE_EOF:
            return result.failure(InvalidSyntaxError(self.current_token.position_start, self.current_token.position_end, "Expected '+', '-', '*' or '/'"))
        return result

    def factor(self):
        result = ParseResult()
        num_node_token = self.current_token

        if num_node_token.type in (TOKENTYPE_PLUS, TOKENTYPE_MINUS):
            result.register(self.advance())
            factor = result.register(self.factor())
            if result.error:
                return result
            return result.success(UnaryOperationNode(num_node_token, factor))

        elif num_node_token.type in (TOKENTYPE_INT, TOKENTYPE_FLOAT):
            result.register(self.advance())
            return result.success(NumberNode(num_node_token))
        
        elif num_node_token.type == TOKENTYPE_LEFTPARENTESIS:
            result.register(self.advance())
            expression = result.register(self.expression())
            if result.error:
                return result
            if self.current_token.type == TOKENTYPE_RIGHTPARENTESIS:
                result.register(self.advance())
                return result.success(expression)
            else:
                return result.failure(InvalidSyntaxError(self.current_token.position_start, self.current_token.position_end, "Expected ')'"))
            #return result.success(NumberNode(num_node_token))
        
        return result.failure(InvalidSyntaxError(num_node_token.position_start, num_node_token.position_end, "Expected int or float"))


    def term(self):
        return self.binary_operation(self.factor, (TOKENTYPE_MUL, TOKENTYPE_DIV))


    def expression(self):
        return self.binary_operation(self.term, (TOKENTYPE_PLUS, TOKENTYPE_MINUS))

    def binary_operation(self, fun, operations):
        result = ParseResult()
        left = result.register(fun())
        if result.error:
            return result

        while self.current_token.type in operations:
            binary_operation_token = self.current_token
            result.register(self.advance())
            right = result.register(fun())
            if result.error:
                return result
            left = BinaryOperationNode(left, binary_operation_token, right)

        return result.success(left)


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

    return abs_sy_tree.node, abs_sy_tree.error