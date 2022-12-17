import Exceptions
from nodes import Node2Childs, Node, Node, Node1Child


def interpret(node_head: Node):
    try:
        return node_head.get_value()
    except Exceptions.InvalidMath as e:
        print(e)
        return None
