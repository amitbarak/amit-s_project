import config
from Operand import Operand
from checkValidation import is_valid
from solve_with_brackets import solve
from List_creator import List_creator

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
        return None
    return str_entered


def main():
    while True:
        str_entered = get_input()
        if not str_entered: continue
        if not is_valid(str_entered): continue
        print(str_entered)
        # puts into a sufficient list
        list_creator = List_creator(str_entered)
        lst_expression = list_creator.create_lst_expression()
        if lst_expression is None: continue

        print(lst_expression)
        op_res = solve(lst_expression)
        print(op_res)
        print()
        print()



if __name__ == "__main__":
    main()
