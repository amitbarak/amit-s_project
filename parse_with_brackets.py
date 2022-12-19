import custom_exceptions
import operands
import config
from nodes import Node
from parse_without_brackets import solve_expression_without_brackets


"""
this file is dedicated to parsing a list of the expression
and creating a tree that represents the expression
if there is an Operator or bracket that is not in the right place
MissingItem exception will be raised and handled at create_root_node
"""

def create_root_node(lst_expression):
    """create a tree that represents the expression from a list that represents the expression
    :param lst_expression: a list that represents the expression
    :return: the root of the tree"""
    while not isinstance(lst_expression[0], operands.Operand) or len(lst_expression) != 1:
        try:
            # creating a list that represents the first inner expression: (9-0) + (1*2) -> 9-0
            opening_index, closing_index = get_inner_expression(lst_expression)
            lst_inner = lst_expression[opening_index: closing_index]

            # solving the inner expression: 9 - 0 = 9
            result = solve_expression_without_brackets(lst_inner)

            # replacing the inner expression with the result
            if opening_index == 0 and closing_index == len(lst_expression):
                lst_expression = replace(lst_expression, opening_index, closing_index, result)
            else:
                lst_expression = replace(lst_expression, opening_index - 1, closing_index + 1, result)
        except custom_exceptions.MissingItem as e:
            print(e)
            return None
    return Node(lst_expression[0])


def replace(lst, start_index, end_index, inserted):
    """
    this function receives a list and replaces the items from start_index to end_index with the inserted list
    :param lst: a list that will be replaced
    :param start_index: the index of the start of the replacement
    :param end_index: the index of the end of the replacement
    :param inserted: the item that will be inserted
    :return: list with all items from start_index to end_index replaced with the inserted object
    """
    return lst[:start_index] + [inserted] + lst[end_index:]


def get_inner_expression(lst_expression):
    """
    this function receives a list that represents an expression and returns the
    indexes of the first inner expression in the list for example: (9-0) + (1*2) -> 9-0
    :param lst_expression: a list that represents a mathematical expression
    :return: the start and end indexes of the first and last item in the first inner expression in the list
    """
    last_start = 0
    for i in range(len(lst_expression)):
        item = lst_expression[i]
        if item in config.L_BRACKETS:
            last_start = i + 1
        elif item in config.R_BRACKETS:
            return last_start, i
    return 0, len(lst_expression)
