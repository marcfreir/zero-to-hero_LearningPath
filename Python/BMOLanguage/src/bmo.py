###############
### IMPORTS ###
###############

# ERROR
from error import Error, IllegalCharError, InvalidSyntaxError
# POSITION
from position import Position
# TOKENS
from token import TOKENTYPE_INT, TOKENTYPE_FLOAT, TOKENTYPE_PLUS, TOKENTYPE_MINUS, TOKENTYPE_MUL, TOKENTYPE_DIV, TOKENTYPE_LEFTPARENTESIS, TOKENTYPE_RIGHTPARENTESIS, TOKENTYPE_EOF, Token
# LEXER
from lexer import Lexer
# NODES
from node import NumberNode, BinaryOperationNode, UnaryOperationNode
# PARSER
from parser import Parser


def run(file_name, text):
    #Generate Tokens
    lexer = Lexer(file_name, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    #Generate Abstract Syntax Tree
    parser = Parser(tokens)
    abstract_syntax_tree = parser.parse()

    return abstract_syntax_tree.node, abstract_syntax_tree.error