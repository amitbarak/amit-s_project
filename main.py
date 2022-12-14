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
        """
    except KeyboardInterrupt:
        print("keyboard was Interrupted")
        return None"""
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


"""
def solve_addition(lst_expression):
    lst_new = []
    temp = 0
    former_item = None
    while(lst_expression != []):
        item = lst_expression.pop()
        if(item == "+"):
            temp = lst_new.pop().add(item)
            --lst_new.append(temp)
        else:
            lst_new.append(item)
"""

"""
def solve_expression_with_brackets(lst_expression):
    lst_expression.reverse()
    i = 0
    last_start = 0
    lst_new = []
    while (lst_expression):
        i += 1
        item = lst_expression.pop()
        lst_new.append(item)
        if item == "(":
            last_start = i + 1
        elif item == ")":
            return solve_expression_without_brackets(lst_expression[last_start: i].copy())
    return solve_expression_without_brackets(lst_expression.copy())
    """

if __name__ == "__main__":
    main()
