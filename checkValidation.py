import operators
from Operands import Number
import config


def is_valid(str_entered: str):
    if str_entered is None:
        return False
    if str_entered == "":
        print("input cant be empty")
        return False
    i = 0
    check_brackets = 0
    negation_to_digits = []
    was_negation = False
    is_empty = True
    for c in str_entered:
        if c in config.CHARS_TO_IGNORE: continue
        i += 1
        if c not in config.VALID_CHARS and c not in config.CHARS_TO_IGNORE:
            print("'{0}' is not allowed in the expression and was fount at index: {1}".format(c, i))
            return False
        elif c == config.R_BRACKETS[0]:
            check_brackets += 1
        elif c == config.R_BRACKETS[0]:
            check_brackets -= 1
        if check_brackets < 0:
            print("there are more closing brackets than opening brackets from the start until index: {0}".format(i))
            return False

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

        if c not in config.CHARS_TO_IGNORE:
            is_empty = False

    if is_empty:
        print("input only contains empty chars")
        return False

    return True




"""
def check_str_lst(lst_strings: list):
    for item in lst_strings:
        if item not in config.not_digits and not Number. (item):
            return False
    return True

"""
