# TOKENS
from token import TOKENTYPE_INT, TOKENTYPE_FLOAT, TOKENTYPE_PLUS, TOKENTYPE_MINUS, TOKENTYPE_MUL, TOKENTYPE_DIV, TOKENTYPE_LEFTPARENTESIS, TOKENTYPE_RIGHTPARENTESIS, TOKENTYPE_EOF, Token
# ERROR
from error import Error, IllegalCharError, InvalidSyntaxError
# PARSE RESULT
from parse_result import ParseResult
# NODES
from node import NumberNode, BinaryOperationNode, UnaryOperationNode

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
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        return self.current_token

    def parse(self):
        response = self.expression()
        if not response.error and self.current_token.type != TOKENTYPE_EOF:
            return response.failure(InvalidSyntaxError(
                self.current_token.position_start, self.current_token.position_end,
                "Expected '+', '-', '*', or '/'"
            ))
        return response



    def factor(self):
        response = ParseResult()
        num_node_token = self.current_token

        if num_node_token.type in (TOKENTYPE_PLUS, TOKENTYPE_MINUS):
            response.register(self.advance())
            factor = response.register(self.factor())
            if response.error: return response
            return response.success(UnaryOperationNode(num_node_token, factor))

        elif num_node_token.type in (TOKENTYPE_INT, TOKENTYPE_FLOAT):
            response.register(self.advance())
            return response.success(NumberNode(num_node_token))

        elif num_node_token.type == TOKENTYPE_LEFTPARENTESIS:
            response.register(self.advance())
            expression = response.register(self.expression())
            if response.error: return response
            if self.current_token.type == TOKENTYPE_RIGHTPARENTESIS:
                response.register(self.advance())
                return response.success(expression)
            else:
                return response.failure(InvalidSyntaxError(
                    self.current_token.position_start, self.current_token.position_end,
                    "Expected ')'"
                ))

        return response.failure(InvalidSyntaxError(
            num_node_token.position_start, num_node_token.position_end,
            "Expected int or float"
        ))

    def term(self):
        return self.binary_operation(self.factor, (TOKENTYPE_MUL, TOKENTYPE_DIV))

    def expression(self):
        return self.binary_operation(self.term, (TOKENTYPE_PLUS, TOKENTYPE_MINUS))



    def binary_operation(self, fun, operations):
        response = ParseResult()
        left = response.register(fun())
        if response.error: return response

        while self.current_token.type in operations:
            binary_operation_token = self.current_token
            response.register(self.advance())
            right = response.register(fun())
            if response.error: return response
            left = BinaryOperationNode(left, binary_operation_token, right)
        
        return response.success(left)