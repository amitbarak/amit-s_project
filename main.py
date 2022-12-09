import config
from Operand import Operand
from solve_without_brackets import solve_expression_without_brackets
num_components = config.number_components
lst_allowed = config.ok_chars

end_of_expression_and_not_num = ["!", ")"]  # this needs to change


def main():
    print("hi")
    str_entered = input("type expression")
    str_entered = str_entered.replace(" ", "")  # removes all spaces
    print(str_entered)
    for c in str_entered:
        if c not in lst_allowed:
            print("'{0}' is not allowed in the expression".format(c))
            return
    print(num_components)
    # puts into a sufficient list

    lst_expression = convert_to_list(str_entered)
    for item in lst_expression:
        print(item.__str__(), end=",")
    print()
    op1 = solve_expression_without_brackets(lst_expression)
    print(op1)
    for item in lst_expression:
        print(item.__str__(), end=",")





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
                except:
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


if __name__ == "__main__":
    main()
