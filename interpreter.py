from custom_exceptions import InvalidMath
from config import ROUNDING_COUNT
from operands import Number
from nodes import Node

"""this file contains the interpretation function:
interpret(node_head: Node) activates the get_value() function of the node_head
and thus for recursively calculates the value of the expression
"""


def interpret(node_head: Node) -> Number:
    """
    this function receives a node that represents the root of a tree
    :param node_head: the root of the tree
    :return: the result of the calculation, None if there is an Illegal Operation in the tree
    """
    try:
        result = node_head.get_value()
        return Number(round(result.get_value(), ROUNDING_COUNT))
    except InvalidMath as e:
        print(e)
        return None
