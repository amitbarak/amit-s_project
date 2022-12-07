import config
from Operand import Operand


end_of_expression_and_not_num = ["!", ")"]  # this needs to change


def main():
    num_components = config.number_components
    lst_allowed = config.ok_chars
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
    print(lst_expression)

"""
def solve_factorial(lst_expression):
    lst_new = []
    temp = 0
    for item in lst_expression:
        if(item == "!"):
            temp = lst_new.pop() * 2
            lst_new.append(temp)
        lst_new.append(item)

def solve_addition(lst_expression):
    lst_new = []
    temp = 0
    former_item = None
    while(lst_expression != []):
        item = lst_expression.pop()
        if(item == "+"):
            temp = lst_new.pop() + item
            lst_new.append(temp)
        else:
            lst_new.append(item)
"""
def convert_to_list(str_entered : str):
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
    if str_current not in end_of_expression_and_not_num:
        try:
            lst_expression.append(Operand(str_current))
        except:
            print(str_current + " isn't a proper number")
            return
    else:
        lst_expression.append(str_current)

    return lst_expression
if __name__ == "__main__":
    main()