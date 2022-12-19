"""
this file is dedicated to the parsing of an expression without brackets
contains the following methods:
    solve_expression_without_brackets:
        this function receives a list that represents an expression without brackets and parses it into a tree
        and returns the result of the expression
    parse_minuses:
        this function parses the minuses in the expression into: double_minus, minus, double_sub and returns the changed list
    parse_priority_minuses:
        this function replaces sub chars that follow one another with DoubleSub or Sub accordingly
    insert_minuses_to_all_nums:
        this function replaces all the subs and DoubleSub chars ot that are not operators with
         regular_minus or double_minus

"""

import config
import operators
from custom_exceptions import MissingItem
from operands import Number, Operand
from nodes import Node2Childs, Node, Node1Child


def solve_expression_without_brackets(lst_expression):
    """
    this function solves an expression without brackets and returns the result
    :raises: MissingItem if there is a missing item in the expression (like 2+ or !3 or 1 ** 2)
    :param lst_expression: an expression without brackets in it
    :return: a number with the result of the expression
    """
    if len(lst_expression) == 0:
        raise MissingItem("there has to be an item inside each two corresponding brackets")

    lst_expression = parse_minuses(lst_expression)
    priorities_dicts = operators.get_priorities_dicts()
    for dictionary in priorities_dicts:
        lst_expression = parse_regular_priority(lst_expression, dictionary)
    if len(lst_expression) != 1:
        raise MissingItem("there has to be an item between each two expressions")  # for example (4)(4) generates this
    return lst_expression[0]


def parse_basic_expression(lst_former, lst_next, operator):
    """
    this function receives the list of items before and after and the operator's class
    and returns a tree or a node of the operation
    with the list before and after the expression after removing the items that were parsed into the node
    :param lst_former: the former part of the expression (which is before the operator)
    :param lst_next: the next part of the expression (which is after the operator)
    :param operator: the class of the operator that is between the two parts of the expression
    :return: a tuple containing:
    (list of the former parts of the expression after removing the parts that had to be
    parsed in order to preform the operation, a List of the next parts of the expression after
    removing the parts that had to be parsed in order to preform the operation,
    Node of the result of the operation
    """
    check_MissingItems(lst_former, lst_next, operator)
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


def get_former_operand(lst_former: list, lst_next: list, operator):
    """
    this function receives the two lists of items before and after an operator, and the operator's class
    it parses all the former items until reaching an Operand
    :raises: MissingItem Error if it encounters an operator that is not allowed after an Operand on the way
    :param lst_former:this is the list of items before the operator
    :param lst_next: this is the list of items after the operator
    :param operator: this is the operator's class
    :return: a tuple containing:
    (list of the former parts of the expression after removing the parts that had to be
    parsed in order to preform the operation, a List of the next parts of the expression after
    parsing if was needed, an Operand of the items that were parsed)
    """
    item = lst_former.pop()

    if isinstance(item, Operand):
        return lst_former, lst_next, item
    operator1 = config.OPERATORS_DICT[item]
    if operator1.TYPE == operators.OperatorTypes.BEFORE or \
            operator1.TYPE == operators.OperatorTypes.BEFORE_AND_AFTER:
        raise MissingItem(f"{operator.CHAR} can't come after {operator1.CHAR}")
    return parse_basic_expression(lst_former, lst_next, operator1)


def get_next_operand(lst_former, lst_next, operator):
    """
    this function receives the two lists of items before and after an operator, and the operator's class
    it parses all the next items until reaching an Operand
    :raises: MissingItem Error if it encounters an operator that is not allowed before an Operand on the way
    :param lst_former:this is the list of items before the operator
    :param lst_next: this is the list of items after the operator
    :param operator: this is the operator's class
    :return: a tuple containing:
    (list of the former parts of the expression after removing the parts that had to be
    parsed in order to preform the operation, a List of the next parts of the expression after
    parsing if was needed, an Operand of the items that were parsed)
    """
    item = lst_next.pop()
    if isinstance(item, Number) or isinstance(item, Node):
        return lst_former, lst_next, item
    operator1 = config.OPERATORS_DICT[item]
    if operator1.TYPE == operators.OperatorTypes.AFTER or \
            operator1.TYPE == operators.OperatorTypes.BEFORE_AND_AFTER:
        raise MissingItem(f"{operator.CHAR} can't come before {operator1.CHAR}")
    return parse_basic_expression(lst_former, lst_next, operator1)


def check_MissingItems(lst_former, lst_next, operator):
    """
    this function checks accepts lists of the items before and after an operator
    if there aren't any items before or after the operator
    that should have items before or after it. if there are, it raises a MissingItem Error
    :raise: MissingItem Error if there is an operator that should have items before or after it
    and doesn't have any
    :param lst_former: the former part of the expression (which is before the operator)
    :param lst_next: the next part of the expression (which is after the operator)
    :param operator: the class of the operator that is between the two parts of the expression
    """
    operator_type = operator.TYPE
    if operator_type == operators.OperatorTypes.BEFORE and not lst_next:
        raise MissingItem(f"there has to be a value after an {operator.CHAR}")
    if operator_type == operators.OperatorTypes.AFTER and not lst_former:
        raise MissingItem(f"there has to be a value before an {operator.CHAR}")
    if operator_type == operators.OperatorTypes.BEFORE_AND_AFTER and (not lst_next or not lst_former):
        raise MissingItem(f"there has to be a value before and after {operator.CHAR}")


def parse_regular_priority(lst_expression, operators_dict: dict):
    """
     this function receives a list of items and a dictionary of operators that
     are on same priority and inserts the operators and the operands they are
     working on into nodes, inserts the nodes into the lst_expression instead of the
     operators and their corresponding operands and returns the lst_expression
    :param operators_dict : a dictionary of the operators chars in the expression as keys and their
    corresponding classes as items in the dictionary {char: operator_class}
    :param lst_expression: an expression without Brackets that only contains Operands, and chars of
    their correct corresponding operators
    :return: the expression after replacing the priority's operators with their result
    """
    lst_expression.reverse()
    lst_new = []
    while lst_expression:
        item = lst_expression.pop()
        if item in operators_dict.keys():
            operator1 = operators_dict.get(item)
            lst_new, lst_expression, temp = parse_basic_expression(lst_new, lst_expression,
                                                                   operator1)
            lst_new.append(temp)
        else:
            lst_new.append(item)
    return lst_new


def parse_minuses(lst_expression):
    """
    this function parses the minuses in the expression into: double_minus, minus, double_sub
     and returns the changed list
    :param lst_expression:
    :return:
    """
    lst_expression = parse_priority_minuses(lst_expression)
    lst_expression = insert_minuses_to_all_nums(lst_expression)
    return lst_expression


def parse_priority_minuses(lst_expression):
    """
    this function parses the minuses in the expression into: double_minus, minus, double_sub and returns the result
    :param lst_expression: an expression containing a list of the items in the mathematical expression
    :return:
    """
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
    return lst_new


def insert_minuses_to_all_nums(lst_expression):
    """
    this function replaces all the subs and DoubleSub chars that are not operators with
    regular_minus or double_minus
    :param lst_expression: an expression containing a list of the items in the mathematical expression
    after replacing the sub chars with double_sub where needed
    :return: the expression after replacing the sub chars with double_sub where needed
    """
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
        if item_before in config.OPERATORS_DICT and item_current == SUB:
            operator_before = config.OPERATORS_DICT[item_before]
            if operator_before.TYPE != operators.OperatorTypes.AFTER:
                item_current = MINUS
            else:
                lst_new.append(item_before)
                item_before = item_current
                item_current = lst_expression.pop()
        elif item_before in config.OPERATORS_DICT and item_current == DOUBLE_SUB:
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
