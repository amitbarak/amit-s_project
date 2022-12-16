import operator

import config
import operators
from Exceptions import MissingItem
from Operands import Number, Operand
from nodes import Node2Childs, Node, Node, Node1Child

num_components = config.number_components
lst_allowed = config.ok_chars

end_of_expression_and_not_num = ["!", ")"]  # this needs to change


def solve_expression_without_brackets(lst_expression):
    """
    :param lst_expression: an expression without brackets in it
    :return: an operator with the result
    """
    if len(lst_expression) == 0:
        raise MissingItem("there has to be an item inside each two corresponding brackets")
    # lst_expression = solve_priority_minuses(lst_expression)

    priority7_dict = {"#": operators.DigitSum}
    priority6_dict = {"!": operators.factorial, "~": operators.negation}
    priority5_dict = {"@": operators.avg, "&": operators.min, "$": operators.max}
    priority4_dict = {"%": operators.mod}
    priority3_dict = {"^": operators.pow}
    priority2_dict = {"*": operators.mul, "/": operators.div}
    priority1_dict = {"+": operators.add, "-": operators.sub}
    lst_expression = solve_regular_priority(lst_expression, priority7_dict)
    lst_expression = solve_regular_priority(lst_expression, priority6_dict)
    lst_expression = solve_regular_priority(lst_expression, priority5_dict)
    lst_expression = solve_regular_priority(lst_expression, priority4_dict)
    lst_expression = solve_regular_priority(lst_expression, priority3_dict)
    lst_expression = solve_regular_priority(lst_expression, priority2_dict)
    lst_expression = solve_regular_priority(lst_expression, priority1_dict)
    return lst_expression[0]

"""
def count_minueses_until_next_operand(lst_partial_expression):
    
     :param lst_partial_expression: an expression starting with
     :return: the number of minuses until next operator
    
def solve_priority_minuses2(lst_expression):
    if len(lst_expression) <= 2:
        return lst_expression
    lst_expression.reverse()
    operand1 = lst_expression.pop()
    if operand1 == "-":
        operator1 = operators.negation
        result = Node1Child(solve_priority_minuses2(lst_expression), operator1)
        return [result] + lst_expression
    else:
        return solve_priority_minuses1(lst_expression)

def solve_priority_minuses1(lst_expression):
    pass

def solve_priority_minuses(lst_expression):
    
    :param lst_expression: an expression without Brackets and after inserting '-' into the operands
    :return: the expression after replacing the priority 6 operators with their result
    
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
                                     or type(item_before_minuses) is Number
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

"""

def parse_basic_expression(lst_former, lst_next, operator):
    """
    :param lst_former:
    :param lst_next:
    :param operator:
    :return:
    """
    raise_MissingItem(lst_former, lst_next, operator)
    if operator.type == operators.OperatorTypes.BEFORE_AND_AFTER:
        lst_former, lst_next, operand_next = get_next_operand(lst_former, lst_next, operator)
        lst_former, lst_next, operand_former = get_former_operand(lst_former, lst_next, operator)
        result = Node2Childs(Node(operand_former), Node(operand_next), operator)
        return lst_former, lst_next, result
    elif operator.type == operators.OperatorTypes.BEFORE:
        lst_former, lst_next, operand_next = get_next_operand(lst_former, lst_next, operator)
        result = Node1Child(Node(operand_next), operator)
        return lst_former, lst_next, result
    elif operator.type == operators.OperatorTypes.AFTER:
        lst_former, lst_next, operand_former = get_former_operand(lst_former, lst_next, operator)
        result = Node1Child(Node(operand_former), operator)
        return lst_former, lst_next, result


def get_former_operand(lst_former, lst_next, operator):
    item = lst_former.pop()

    if isinstance(item, Operand) or isinstance(item, Node):
        return lst_former, lst_next, item
    operator1 = config.operators_dict[item]
    return parse_basic_expression(lst_former, lst_next, operator1)


def get_next_operand(lst_former, lst_next, operator):
    item = lst_next.pop()
    if isinstance(item, Number) or isinstance(item, Node):
        return lst_former, lst_next, item
    operator1 = config.operators_dict[item]
    return parse_basic_expression(lst_former, lst_next, operator1)


def raise_MissingItem(lst_former, lst_next, operator):
    operator_type = operator.type
    if operator_type == operators.OperatorTypes.BEFORE and not lst_next:
        raise MissingItem(f"there has to be a value before an {operator.char}")
    if operator_type == operators.OperatorTypes.AFTER and not lst_former:
        raise MissingItem(f"there has to be a value before an {operator.char}")
    if operator_type == operators.OperatorTypes.BEFORE_AND_AFTER and (not lst_next or not lst_former):
        raise MissingItem(f"there has to be a value before and after {operator.char}")



def solve_regular_priority(lst_expression, sign_function: dict):
    """
    :param lst_expression: an expression without Brackets and after inserting '-' into the operands
    :return: the expression after replacing the priority's operators with their result
    """
    lst_expression.reverse()
    lst_new = []
    while lst_expression:
        item = lst_expression.pop()
        if item in sign_function.keys():
            operator1 = sign_function.get(item)
            print(operator1.operation)
            lst_new, lst_expression, temp = parse_basic_expression(lst_new, lst_expression,
                                                                   operator1)  # lst_new.pop() is the former item, lst_expression.pop() is the next
            lst_new.append(temp)
        else:
            lst_new.append(item)
    return lst_new
