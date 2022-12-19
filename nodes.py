from operands import Number, Operand

"""
this file contains all of the Nodes classes:
Node: the base class for all of the Nodes
Node1Child: a Node that has one child
Node2Child: a Node that has two children
"""


class Node(Operand):
    """
        this is the base class that represents a node in a tree
        Attributes:
        ----------
        operand: Operand - the operand that the node holds
        Methods:
        -------
        get_value() - returns a number with the value of the operand that the node holds

    """
    def __init__(self, operand: Operand):
        super().__init__()
        self.operand = operand

    def get_value(self) -> Number:
        """
        :return: the value of the operand that the node holds as a Number
        """
        if type(self.operand) is Number:
            return self.operand
        elif isinstance(self.operand, Node):
            return self.operand.get_value()

    def __repr__(self):
        return f"Node {self.operand}"


class Node2Child(Node):
    """
    represents a node with 2 childs
    Attributes:
    ----------
    left_operand: Node - the left operand
    right_operand: Node - the right operand
    operator: Operator - the operator class that the node holds
    """
    def __init__(self, left_operand: Operand, right_operand: Operand, operator):
        super().__init__(left_operand)
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.operator = operator

    def get_value(self):
        """
        a recursive function that returns the value of the node according to it's subNodes
        and the operator that the node holds
        :raise: InvalidMath if the calculation is not valid for example: 1/0
        :return: the value of the operand that the node holds as a Number
        """
        return self.operator.operation(self.left_operand.get_value(), self.right_operand.get_value())

    def __repr__(self):
        return f"( {self.left_operand} {self.operator.CHAR} {self.right_operand})"


class Node1Child(Node):
    """
    represents a node with 1 child
    Attributes:
    ----------
    child_node: Node - the child node
    operator: Operator - the operator class that the node holds
    """
    def __init__(self, child_node: Operand, operator):
        super().__init__(operator)
        self.child_node = child_node
        self.operator = operator

    def get_value(self) -> Number:
        """
        a recursive function that returns the value of the node according to it's subNodes
        and the operator that the node holds
        :raise: InvalidMath if the calculation is not valid for example: 1/0
        :return: the value of the operand that the node holds as a Number
        """
        return self.operator.operation(self.child_node.get_value())

    def __repr__(self) -> str:
        return f"({self.child_node}{self.operator.CHAR})"
