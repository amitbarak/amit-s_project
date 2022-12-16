import config
from Operands import Number
from checkValidation import is_valid
from parse_with_brackets import create_root_node
from List_creator import List_creator
from interpreter import interpret
num_components = config.number_components

end_of_expression_and_not_num = ["!", ")"]  # this needs to change


def get_input():
    try:
        str_entered = input("type expression")
    except KeyboardInterrupt:
        print("keyboard was Interrupted")
        return None
    except EOFError:
        print("EOF when reading a line")
        exit(1)
        return None
    return str_entered


def main():
    while True:
        str_entered = get_input()
        if not is_valid(str_entered): continue
        print(str_entered)
        # puts into a sufficient list
        list_creator = List_creator(str_entered)
        lst_expression = list_creator.create_lst_expression()
        if lst_expression is None: continue
        print(lst_expression)
        head = create_root_node(lst_expression)
        if head is None: continue
        print(head)
        print(interpret(head))
        print()
        print()



if __name__ == "__main__":
    main()
