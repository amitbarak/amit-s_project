import operators
import config

"""
a module for validating the string expression
contains the function is_valid which checks the validation of the string expression:
METHODS:
    is_valid(str_expression: str) -> bool
        receives a string that represents a mathematical expression and returns True if it
        passed it's validation, False otherwise
    it's composed from the following functions:
        check_negation(str_expression: str) -> bool
            checks if there are ~ operators that follow one another
        check_brackets(str_expression: str) -> bool
            checks if the brackets are balanced
        check_all_valid_chars(str_expression: str) -> bool
            checks if the expression contains only valid chars
        check_not_empty(str_expression) -> bool
            checks if the expression is empty
"""


def is_valid(str_expression: str) -> bool:
    """
    this function receives a string that represents a mathematical expression and
    checks the validation of it's chars, it's brackets and it's ~ operators
    prints the problem if there is one and returns False or True according the result

    :param str_expression: a mathematical expression which is represented by a string
    :return: True if the expression is valid, False otherwise
    """

    valid = True
    valid &= check_negation(str_expression)
    valid &= check_brackets(str_expression)
    valid &= check_all_valid_chars(str_expression)
    valid &= check_not_empty(str_expression)

    return valid


def check_negation(str_expression: str) -> bool:
    """
    this function checks if all there aren't ~ operators that follow one another for example: ~-~3: false
    prints a proper message if there is a problem and returns False or True according the result
    :param str_expression: a mathematical expression which is represented by a string
    :return: whether the expression contains ~ operators that follow one another
    """
    was_negation = False
    i = 0
    negation_to_digits = ""
    for c in str_expression:
        i += 1
        error_message = f"negation must be close to a number or a sequence of numbers," \
                        f" index of wrong charcter after negation: {i}"
        if c in config.CHARS_TO_IGNORE: continue
        # checks negation
        if c == operators.Negation.CHAR:
            if was_negation == True:
                print(f"negation must be close to a number or a sequence of numbers,"
                      f" index of wrong charcter after negation: {i}")
                return False
            was_negation = True
            negation_to_digits += c
        elif was_negation:
            if c not in (config.NUMBER_COMPONENTS + config.L_BRACKETS):
                print(f"negation must be close to a number or a sequence of numbers,"
                      f" index of wrong charcter after negation: {i}")
                return False
            elif c in config.DIGITS:
                was_negation = False
            else:
                negation_to_digits += c
    return True


def check_brackets(str_expression: str) -> bool:
    """
    this function checks if the brackets are balanced returns True or False according to it
    and prints a proper message if they're not balanced
    balnced example : ((2 ) + 3), unbalanced example: ((2 + 3)
    :param str_expression: a mathematical expression which is represented by a string
    :return: whether the brackets are balanced
    """
    check_brackets = 0
    i = 0
    for c in str_expression:
        i += 1
        if c in config.CHARS_TO_IGNORE: continue
        if c == config.L_BRACKETS[0]:
            check_brackets += 1
        elif c == config.R_BRACKETS[0]:
            check_brackets -= 1
        if check_brackets < 0:
            print(f"there is a closing bracket without an opening bracket until index: {i}")
            return False
    if check_brackets != 0:
        print("there is a difference between the number of opening brackets and the number of closing brackets")
        return False
    return True


def check_all_valid_chars(str_expression: str) -> bool:
    """
    this function checks if the expression contains only valid chars
    prints a proper message if there is a problem and returns False or True according the result
     of the check
    :param str_expression: a mathematical expression which is represented by a string
    :return:
    """
    for c in str_expression:
        if c in config.CHARS_TO_IGNORE: continue
        if c not in config.VALID_CHARS:
            print(f"invalid character: {c}")
            return False
    return True



def check_not_empty(str_expression) -> bool:
    """
    this function checks if the expression is empty and prints a message if it's empty
    :param str_expression: a mathematical expression which is represented by a string
    :return: True if not empty, False otherwise
    """
    is_empty = True
    for c in str_expression:
        if c in config.CHARS_TO_IGNORE: continue

        # check if the expression is empty
        if c not in config.CHARS_TO_IGNORE:
            is_empty = False

    if is_empty or str_expression is None:
        print("input is empty")
        return False
    return True