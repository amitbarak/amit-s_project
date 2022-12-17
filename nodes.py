from Operands import Number, Operand
class Node(Operand):
    def __init__(self, operand: Operand):
        super().__init__()
        self.operand = operand

    def get_value(self):
        if type(self.operand) is Number:
            return self.operand
        elif isinstance(self.operand, Node):
            return self.operand.get_value()

    def __repr__(self):
        return f"Node {self.operand}"

class Node2Childs(Node):
    def __init__(self, left_operand, right_operand, operator):
        super().__init__(left_operand)
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.operator = operator

    def get_value(self):
        return self.operator.operation(self.left_operand.get_value(), self.right_operand.get_value())

    def __repr__(self):
        return f"( {self.left_operand} {self.operator.char} {self.right_operand})"



class Node1Child(Node):
    def __init__(self, child_node, operator):
        super().__init__(operator)
        self.child_node = child_node
        self.operator = operator

    def get_value(self):
        return self.operator.operation(self.child_node.get_value())

    def __repr__(self):
        return f"({self.child_node}{self.operator.char})"