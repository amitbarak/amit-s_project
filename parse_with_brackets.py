import Exceptions
import config
from Operands import Number
from parse_without_brackets import solve_expression_without_brackets


def create_root_node(lst_expression):
    while (len(lst_expression)) != 1:
        opening_index, closing_index = get_inner_expression(lst_expression)
        lst_inner = lst_expression[opening_index: closing_index]
        result = solve_expression_without_brackets(lst_inner)
        if opening_index == 0 and closing_index == len(lst_expression):
            lst_expression = replace(lst_expression, opening_index, closing_index, result)
        else:
            lst_expression = replace(lst_expression, opening_index - 1, closing_index + 1, result)
    return lst_expression[0]


def replace(lst, start_index, end_index, inserted):
    return lst[:start_index] + [inserted] + lst[end_index:]


def get_inner_expression(lst_expression):
    last_start = 0
    for i in range(len(lst_expression)):
        item = lst_expression[i]
        if item in config.l_brackets:
            last_start = i + 1
        elif item in config.r_brackets:
            return last_start, i
    if last_start != 0:
        raise Exceptions.MissingItem("there has to be closing brackets after opening brackets")
    return 0, len(lst_expression)
