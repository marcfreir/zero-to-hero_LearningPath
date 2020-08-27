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