import Exceptions
import config
from Operands import Number
from nodes import Node2Childs, Node, Node1Child


def interpret(node_head: Node):
    try:
        return Number(round(node_head.get_value().get_value(), config.ROUNDING_COUNT))
    except Exceptions.InvalidMath as e:
        print(e)
        return None
