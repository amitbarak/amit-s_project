import config
from Operand import Operand

num_components = config.number_components
lst_allowed = config.ok_chars

end_of_expression_and_not_num = ["!", ")"]  # this needs to change


def solve_expression_without_brackets(lst_expression):
    """
    :param lst_expression: an expression without brackets in it
    :return: an operand with the result
    """

    lst_expression = solve_priority6(lst_expression)
    priority5_dict = {"@": Operand.avg, "&": Operand.min, "$": Operand.max}
    priority4_dict = {"%": Operand.mod}
    priority3_dict = {"^": Operand.pow}
    priority2_dict = {"*": Operand.mul, "/": Operand.div}
    priority1_dict = {"+": Operand.add, "-": Operand.sub}
    lst_expression = solve_regular_priority(lst_expression, priority5_dict)
    lst_expression = solve_regular_priority(lst_expression, priority4_dict)
    lst_expression = solve_regular_priority(lst_expression, priority3_dict)
    lst_expression = solve_regular_priority(lst_expression, priority2_dict)
    lst_expression = solve_regular_priority(lst_expression, priority1_dict)
    return Operand(lst_expression[0])


def solve_priority6(lst_expression):
    """
    :param lst_expression: an expression without Brackets and after inserting '-' into the operands
    :return: the expression after replacing the priority 6 operators with their result
    """
    lst_expression.reverse()
    lst_new = []
    temp = 0
    while lst_expression:
        item = lst_expression.pop()
        if item == "~":
            temp = lst_expression.pop().negation()
            lst_new.append(temp)
        elif item == "!":
            temp = lst_new.pop().factorial()
            lst_new.append(temp)
        else:
            lst_new.append(item)
    return lst_new


def solve_regular_priority(lst_expression, sign_function: dict):
    """
    :param lst_expression: an expression without Brackets and after inserting '-' into the operands
    :return: the expression after replacing the priority's operators with their result
    """
    lst_expression.reverse()
    lst_new = []
    temp = 0
    while lst_expression:
        item = lst_expression.pop()
        if item in sign_function.keys():
            operation = sign_function.get(item)
            temp = operation(lst_new.pop(), lst_expression.pop())
            lst_new.append(temp)
        else:
            lst_new.append(item)
    return lst_new
