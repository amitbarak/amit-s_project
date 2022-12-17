
from checkValidation import is_valid
from parse_with_brackets import create_root_node
from List_creator import List_creator
from interpreter import interpret
from recive_input import get_input


def calculate(str_entered):
    if not is_valid(str_entered): return None
    # puts into a sufficient list
    list_creator = List_creator(str_entered)
    lst_expression = list_creator.create_lst_expression()
    if lst_expression is None: return None
    head = create_root_node(lst_expression)
    if head is None: return None
    result = interpret(head)
    return result


def main():
    while True:
        str_entered = get_input()
        result = calculate(str_entered)
        print(result)


if __name__ == "__main__":
    main()
