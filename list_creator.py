"""this file only contains:
List_creator class: Transfers the input received into a list that contains Numbers and operators chars
remove_tabs function: removes all tabs from the input
"""

from custom_exceptions import Illegal_Operand
from operands import Number
import config


def remove_tabs(text):
    """removes all tabs and spaces from the input"""
    text = text.split()
    text = ''.join(text)
    return text


class List_creator:
    """
    a lexer-like class that creates a list of numbers and operators chars from a string

    Attributes
    ----------
    char_current : str
        the current char in the string
    text : iter
        an iterator of the string
    Methods
    -------
    next_char()
        moves the iterator to the next char, ignores chars in config.CHARS_TO_IGNORE
    create_lst_expression()
        creates a list of numbers and operators chars from the string accepted upon class's creation
    create_Number()
        creates a Number from a string, raises Illegal_Operand if the string is not a valid number
    """
    def __init__(self, str_expression):
        """initializes the class with the string of the expression"""
        str_expression = remove_tabs(str_expression)
        self.char_current = None
        self.text = iter(str_expression)
        self.next_char()

    def next_char(self):
        """
        moves the iterator to the next char that is not in config.CHARS_TO_IGNORE
        """
        try:
            self.char_current = next(self.text)
            if self.char_current in config.CHARS_TO_IGNORE:
                self.next_char()
        except StopIteration:
            self.char_current = None

    def create_lst_expression(self):
        """
        creates a list of Numbers and operators chars from the string accepted upon class's creation,
        advances the iterator to the end of the string
        :return: a list of Numbers and operators chars
        """
        lst_expression = []
        while self.char_current is not None:
            if self.char_current in (config.DIGITS + [config.DOT_CHAR]):
                try:
                    lst_expression.append(self.create_Number())
                except Illegal_Operand as e:
                    print(e)
                    return None
            elif self.char_current in config.VALID_CHARS:
                lst_expression.append(self.char_current)
                self.next_char()
            else:
                return None
        return lst_expression

    def create_Number(self):
        """
        creates a Number from a string, raises Illegal_Operand if the string is not a valid number,
        advances the iterator to the end of the number,
        :raises: Illegal_Operand if the string is not a valid number
        :return: the Number Object that was created
        """
        point_count = 0
        operand_str = self.char_current
        self.next_char()

        while self.char_current in ([config.DOT_CHAR] + config.DIGITS)\
                and self.char_current is not None:
            if self.char_current == config.DOT_CHAR:
                point_count += 1
            operand_str += self.char_current
            self.next_char()

        if point_count > 1:
            raise Illegal_Operand("a number can't have more than one decimal point")
        if operand_str.startswith('.'):
            raise Illegal_Operand("a number can't start with an '.'")
        if operand_str.endswith('.'):
            raise Illegal_Operand("a number can't end with an '.'")
        if len(operand_str) > 100:
            raise Illegal_Operand(f"number : {operand_str} is too big")

        return Number(operand_str)
