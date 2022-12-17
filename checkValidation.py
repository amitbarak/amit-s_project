from Operands import Number
import config


def print_is_operand(operand_str):
    point_count = 0


def is_valid(str_entered: str):
    if str_entered == "":
        print("input cant be empty")
        return False
    i = 0
    check_brackets = 0
    char_before = ""
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
        if char_before == "~":
            if c not in config.number_components and c != "-":
                print("~ must be followed by a number")  # Tilda must be close to a number
                return False
        char_before = c
    return True


"""
def check_str_lst(lst_strings: list):
    for item in lst_strings:
        if item not in config.not_digits and not Number. (item):
            return False
    return True

"""
