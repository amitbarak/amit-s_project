import config
from Operand import Operand
from solve_without_brackets import solve_expression_without_brackets
from checkValidation import isValid
from solve_with_brackets import solve
num_components = config.number_components

end_of_expression_and_not_num = ["!", ")"]  # this needs to change


def main():
    print("hi")
    try:
        str_entered = input("type expression")
    except KeyboardInterrupt:
        print("keyboard was Interrupted")
        return
    str_entered = str_entered.replace(" ", "")  # removes all spaces
    if not isValid(str_entered):
        return
    print(str_entered)
    print(num_components)
    # puts into a sufficient list

    lst_expression = convert_to_list(str_entered)
    op_res_list = solve(lst_expression)
    print()

    for item in lst_expression:
        print(item.__str__(), end=",")
    print()
    for item in op_res_list:
        print(item.__str__())


"""
def solve_addition(lst_expression):
    lst_new = []
    temp = 0
    former_item = None
    while(lst_expression != []):
        item = lst_expression.pop()
        if(item == "+"):
            temp = lst_new.pop().add(item)
            lst_new.append(temp)
        else:
            lst_new.append(item)
"""


def convert_to_list(str_entered: str) -> list:
    """

    :param str_entered: the expression received from the user as String
    :return: a list containing that expression with operands and operator separated
    """
    lst_expression = []
    str_current = ""
    for c in str_entered:
        if c not in num_components:
            if len(str_current) > 0:
                try:
                    lst_expression.append(Operand(str_current))
                except ValueError:
                    print(str_current + " isn't a proper number")
                    return
            lst_expression.append(c)
            str_current = ""
        else:
            str_current += c
    if str_current not in end_of_expression_and_not_num and str_current != "":
        try:
            lst_expression.append(Operand(str_current))
        except:
            print(str_current + " isn't a proper number")
            return
    elif str_current != "":
        lst_expression.append(str_current)
    return lst_expression



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
