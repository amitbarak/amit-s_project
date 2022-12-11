import config
import operators
from Operand import Operand

num_components = config.number_components
lst_allowed = config.ok_chars

end_of_expression_and_not_num = ["!", ")"]  # this needs to change


def solve_expression_without_brackets(lst_expression):
    """
    :param lst_expression: an expression without brackets in it
    :return: an operand with the result
    """

    lst_expression = solve_priority_minuses(lst_expression)
    lst_expression = solve_priority6(lst_expression)
    priority5_dict = {"@": operators.avg, "&": operators.min, "$": operators.max}
    priority4_dict = {"%": operators.mod}
    priority3_dict = {"^": operators.pow}
    priority2_dict = {"*": operators.mul, "/": operators.div}
    priority1_dict = {"+": operators.add, "-": operators.sub}
    lst_expression = solve_regular_priority(lst_expression, priority5_dict)
    lst_expression = solve_regular_priority(lst_expression, priority4_dict)
    lst_expression = solve_regular_priority(lst_expression, priority3_dict)
    lst_expression = solve_regular_priority(lst_expression, priority2_dict)
    lst_expression = solve_regular_priority(lst_expression, priority1_dict)
    return Operand(lst_expression[0])


def count_minueses_until_next_operand(lst_partial_expression):
    """
    :param lst_partial_expression: an expression starting with
    :return: the number of minuses until next operand
    """


def solve_priority_minuses(lst_expression):
    """
    :param lst_expression: an expression without Brackets and after inserting '-' into the operands
    :return: the expression after replacing the priority 6 operators with their result
    """
    lst_expression.reverse()
    lst_new = []
    copy = lst_expression.copy()
    factor = 1
    count = 0

    if lst_expression[-1] == "-":
        item_before_minuses = None
    else:
        item_before_minuses = lst_expression[-1]

    while lst_expression:
        item = lst_expression.pop()
        copy.pop()
        does_contain_regular_minus = item_before_minuses in end_of_expression_and_not_num \
                                     or type(item_before_minuses) is Operand
        if item == "-":
            factor *= -1
            count += 1
        elif count >= 2 and does_contain_regular_minus:
            lst_new.append("-")
            if count % 2 == 0:
                lst_new.append(item.negation())
            else:
                lst_new.append(item)
        elif count >= 1 and not does_contain_regular_minus:
            if count % 2 == 0:
                lst_new.append(item)
            else:
                lst_new.append(item.negation())
        elif count == 1:
            lst_new.append("-")
            lst_new.append(item)
        else:
            lst_new.append(item)
            count = 0
            item_before_minuses = item
    return lst_new


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
            operator1 = sign_function.get(item)
            print(operator1.operation)
            temp = operator1.operation(lst_new.pop(), lst_expression.pop()) # lst_new.pop() is the former item, lst_expression.pop() is the next

            lst_new.append(temp)
        else:
            lst_new.append(item)
    return lst_new
