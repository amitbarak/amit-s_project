import config
from Operand import Operand
from solve_without_brackets import solve_expression_without_brackets


def solve(lst_expression):
    op_temp = Operand(1)
    lst_temp2 = [0]
    lst_replace = []
    while (len(lst_expression)) != 1:
        lst_replace = get_lst_to_replace(lst_expression)
        lst_temp2 = get_expression_without_brackets(lst_expression)
        lst_expression = replace(lst_expression, lst_replace, solve_expression_without_brackets(lst_temp2))
    return Operand(lst_expression)


def get_lst_to_replace(lst_expression):
    lst_replace = []
    if lst_expression.count(")") != 0:
        lst_replace.append("(")
        lst_replace += get_expression_without_brackets(lst_expression)
        lst_replace.append(")")
    else:
        lst_replace = get_expression_without_brackets(lst_expression)
    return lst_replace


def replace(lst: list, lst_replace: list, op1: Operand):
    lst.reverse()
    lst_replace_size = len(lst_replace)
    lst_new = []
    lst_inside = []
    i = 0
    just_finished_removing = False
    while (lst):
        item = lst.pop()
        if item == lst_replace[i] and not just_finished_removing:
            i += 1
            lst_inside.append(item)
            if i == lst_replace_size:
                just_finished_removing = True
                lst_inside = []
                i = 0
        elif item == lst_replace[0] and not just_finished_removing:
            lst_inside = []
            i = 1
            lst_inside.append(item)
            if i == lst_replace_size:
                just_finished_removing = True
                lst_inside = []
                i = 0
        else:
            if not just_finished_removing:
                lst_new += lst_inside
                lst_inside = []
            else:
                just_finished_removing = False
                lst_new.append(op1)
            lst_new.append(item)
    if not just_finished_removing:
        lst_new += lst_inside
    else:
        lst_new.append(op1)
    return lst_new


def get_expression_without_brackets(lst_expression):
    last_start = 0
    for i in range(len(lst_expression)):
        item = lst_expression[i]
        if item in config.l_brackets:
            last_start = i + 1
        elif item in config.r_brackets:
            #solve_expression_without_brackets(lst_expression[last_start: i].copy())
            return lst_expression[last_start: i].copy()
    return lst_expression.copy()

