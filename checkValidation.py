import operators
import config

"""
a module for validating the string expression
contains the function is_valid which checks the validation of the string expression
"""


def is_valid(str_expression: str):
    """
    this function receives a string that represents a mathematical expression and
    checks the validation of it's chars, it's brackets and it's ~ operators
    prints the problem if there is one and returns False or True according the result

    :param str_expression: a mathematical expression which is represented by a string
    :return: True if the expression is valid, False otherwise
    """
    if str_expression is None:
        return False
    if str_expression == "":
        print("input cant be empty")
        return False
    i = 0
    check_brackets = 0
    negation_to_digits = []
    was_negation = False
    is_empty = True
    for c in str_expression:
        if c in config.CHARS_TO_IGNORE: continue
        i += 1
        # check if the char is valid
        if c not in config.VALID_CHARS and c not in config.CHARS_TO_IGNORE:
            print("'{0}' is not allowed in the expression and was fount at index: {1}".format(c, i))
            return False

        # check if brackets are valid
        if c == config.R_BRACKETS[0]:
            check_brackets += 1
        if c == config.R_BRACKETS[0]:
            check_brackets -= 1
        if check_brackets < 0:
            print("there are more closing brackets than opening brackets from the start until index: {0}".format(i))
            return False

        # check negation
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

        # check if the expression is empty
        if c not in config.CHARS_TO_IGNORE:
            is_empty = False

    if is_empty:
        print("input only contains empty chars")
        return False

    return True
