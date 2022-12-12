from Operand import Operand
import config



def print_is_operand(operand_str):
    point_count = 0
    if point_count > 1:
        print("a number can't have more than one decimal point")
        return False
    if operand_str.startswith('.'):
        print("a number can't start with an '.'")
        return False
    if operand_str.endswith('.'):
        print("a number can't start with an '.'")
        return False
    if len(operand_str) > 99:
        print(f"number : {operand_str} is too big")
        return False
    return True

def is_valid(str_entered: str):
    if str_entered == "":
        print("input cant be empty")
        return False
    i = 0
    check_brackets = 0
    for c in str_entered:
        i += 1
        if c not in config.ok_chars and c not in config.chars_to_ignore:
            print("'{0}' is not allowed in the expression and was fount at index: {1}".format(c, i))
            return False
        elif c == "(":
            check_brackets += 1
        elif c == ")":
            check_brackets -= 1
        if check_brackets < 0:
            print("there are more closing brackets than opening brackets from the start until index: {0}")
            return False
    return True

"""
def check_str_lst(lst_strings: list):
    for item in lst_strings:
        if item not in config.not_digits and not Operand. (item):
            return False
    return True

"""