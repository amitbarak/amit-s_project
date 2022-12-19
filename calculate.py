from checkValidation import is_valid
from parse_with_brackets import create_root_node
from list_creator import List_creator
from interpreter import interpret
from recive_input import get_input

"""
the exercise was made in way 2 for minuses handling
here lies the main functions of the program:

METHODS:
    calculate:
        this function receives a string that represents a mathematical expression 
        and returns the result of the calculation
    main:
        receives input from the user and prints the result
"""


def calculate(str_expression: str):
    """
    this function receives a string that represents a mathematical expression
     and returns the result of the calculation
    :param str_expression: the string that represents a mathematical expression
    :return: the result of the expression, if the expression is not valid, return None
    """
    if not is_valid(str_expression): return None
    list_creator = List_creator(str_expression)
    lst_expression = list_creator.create_lst_expression()
    if lst_expression is None: return None
    head = create_root_node(lst_expression)
    if head is None: return None
    result = interpret(head)
    return result


def main():
    """
    this function is the main function of the program
    it accepts input from the user and prints the result
    :return None
    """
    while True:
        str_entered = get_input()
        result = calculate(str_entered)
        if result is not None:
            print("the result is: " ,result.get_value())


if __name__ == "__main__":
    main()
