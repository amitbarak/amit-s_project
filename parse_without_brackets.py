import operator

import config
import operators
from Exceptions import MissingItem
from Operands import Number, Operand
from nodes import Node2Childs, Node, Node, Node1Child


end_of_expression_and_not_num = ["!", ")"]  # this needs to change


def solve_expression_without_brackets(lst_expression):
    """
    :param lst_expression: an expression without brackets in it
    :return: an operator with the result
    """
    if len(lst_expression) == 0:
        raise MissingItem("there has to be an item inside each two corresponding brackets")

    lst_expression = parse_priority_minuses(lst_expression)
    #lst_expression = insert_minuses_to_all_nums(lst_expression)
    """
    priority8_dict = {"__": operators.DoubleMinus, "_": operators.Minus}
    priority7_dict = {"#": operators.DigitSum}
    priority6_dict = {"!": operators.Factorial, "~": operators.Negation}
    priority5_dict = {"@": operators.Avg, "&": operators.Min, "$": operators.Max}
    priority4_dict = {"%": operators.Mode}
    priority3_dict = {"^": operators.Power}
    priority2_dict = {"*": operators.Mul, "/": operators.Div}
    priority1_dict = {"+": operators.Add, "-": operators.Sub, "--": operators.DoubleSub}
    """
    priorities_dicts = operators.get_priorities_dicts()
    for dictionary in priorities_dicts:
        lst_expression = parse_regular_priority(lst_expression, dictionary)
    if len(lst_expression) != 1:
        raise MissingItem("there has to be an item between each two expressions") # for example (4)(4) generates this
    return lst_expression[0]


def parse_priority_minuses(lst_expression):
    if len(lst_expression) == 1:
        return lst_expression
    lst_expression.reverse()
    lst_new = []
    item_before = lst_expression.pop()
    item_current = lst_expression.pop()
    while lst_expression:
        if item_before == "-" and item_current == "-":
            item_before = "--"
            item_current = lst_expression.pop()
        elif item_before == "--" and item_current == "-":
            item_before = "-"
            item_current = lst_expression.pop()
        else:
            lst_new.append(item_before)
            item_before = item_current
            item_current = lst_expression.pop()
    lst_new.append(item_before)
    lst_new.append(item_current)
    return insert_minuses_to_all_nums(lst_new)


def insert_minuses_to_all_nums(lst_expression):
    if len(lst_expression) == 1:
        return lst_expression
    SUB = operators.Sub.CHAR
    DOUBLE_SUB = operators.DoubleSub.CHAR
    MINUS = operators.Minus.CHAR
    DOUBLE_MINUS = operators.DoubleMinus.CHAR

    lst_expression.reverse()
    lst_new = []
    item_before = lst_expression.pop()
    item_current = lst_expression.pop()
    if item_before == DOUBLE_SUB:
        item_before = DOUBLE_MINUS
    elif item_before == SUB:
        item_before = MINUS
    while lst_expression:
        if item_before in config.OPERATORS_DICT and item_before != SUB and item_current == SUB:
            operator_before = config.OPERATORS_DICT[item_before]
            if operator_before.TYPE != operators.OperatorTypes.AFTER:
                item_current = MINUS
            else:
                lst_new.append(item_before)
                item_before = item_current
                item_current = lst_expression.pop()
        elif item_before in config.OPERATORS_DICT and item_before != DOUBLE_SUB and item_current == DOUBLE_SUB:
            operator_before = config.OPERATORS_DICT[item_before]
            if operator_before.TYPE != operators.OperatorTypes.AFTER:
                item_current = DOUBLE_MINUS
            else:
                lst_new.append(item_before)
                item_before = item_current
                item_current = lst_expression.pop()
        else:
            lst_new.append(item_before)
            item_before = item_current
            item_current = lst_expression.pop()

    lst_new.append(item_before)
    lst_new.append(item_current)
    return lst_new





def parse_basic_expression(lst_former, lst_next, operator):
    """
    :param lst_former:
    :param lst_next:
    :param operator:
    :return:
    """
    raise_MissingItem(lst_former, lst_next, operator)
    if operator.TYPE == operators.OperatorTypes.BEFORE_AND_AFTER:
        lst_former, lst_next, operand_next = get_next_operand(lst_former, lst_next, operator)
        lst_former, lst_next, operand_former = get_former_operand(lst_former, lst_next, operator)
        result = Node2Childs(Node(operand_former), Node(operand_next), operator)
        return lst_former, lst_next, result
    elif operator.TYPE == operators.OperatorTypes.BEFORE:
        lst_former, lst_next, operand_next = get_next_operand(lst_former, lst_next, operator)
        result = Node1Child(Node(operand_next), operator)
        return lst_former, lst_next, result
    elif operator.TYPE == operators.OperatorTypes.AFTER:
        lst_former, lst_next, operand_former = get_former_operand(lst_former, lst_next, operator)
        result = Node1Child(Node(operand_former), operator)
        return lst_former, lst_next, result


def get_former_operand(lst_former, lst_next, operator):
    item = lst_former.pop()

    if isinstance(item, Operand) or isinstance(item, Node):
        return lst_former, lst_next, item
    operator1 = config.OPERATORS_DICT[item]
    if operator1.TYPE == operators.OperatorTypes.BEFORE or \
            operator1.TYPE == operators.OperatorTypes.BEFORE_AND_AFTER:
        raise MissingItem(f"{operator.CHAR} can't come after {operator1.CHAR}")
    return parse_basic_expression(lst_former, lst_next, operator1)


def get_next_operand(lst_former, lst_next, operator):
    item = lst_next.pop()
    if isinstance(item, Number) or isinstance(item, Node):
        return lst_former, lst_next, item
    operator1 = config.OPERATORS_DICT[item]
    if operator1.TYPE == operators.OperatorTypes.AFTER or \
            operator1.TYPE == operators.OperatorTypes.BEFORE_AND_AFTER:
        raise MissingItem(f"{operator.CHAR} can't come before {operator1.CHAR}")
    return parse_basic_expression(lst_former, lst_next, operator1)


def raise_MissingItem(lst_former, lst_next, operator):
    operator_type = operator.TYPE
    if operator_type == operators.OperatorTypes.BEFORE and not lst_next:
        raise MissingItem(f"there has to be a value after an {operator.CHAR}")
    if operator_type == operators.OperatorTypes.AFTER and not lst_former:
        raise MissingItem(f"there has to be a value before an {operator.CHAR}")
    if operator_type == operators.OperatorTypes.BEFORE_AND_AFTER and (not lst_next or not lst_former):
        raise MissingItem(f"there has to be a value before and after {operator.CHAR}")


def parse_regular_priority(lst_expression, sign_function: dict):
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
            lst_new, lst_expression, temp = parse_basic_expression(lst_new, lst_expression,
                                                                   operator1)  # lst_new.pop() is the former item, lst_expression.pop() is the next
            lst_new.append(temp)
        else:
            lst_new.append(item)
    return lst_new
