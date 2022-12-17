import checkValidation
import operators
from Exceptions import Illegal_Operand
from Operands import Number
import config


class List_creator:

    def __init__(self, text):
        self.char_current = None
        self.text = iter(text)
        self.next_char()

    def next_char(self):
        try:
            self.char_current = next(self.text)
        except StopIteration:
            self.char_current = None

    def create_lst_expression(self):
        lst_expression = []
        while self.char_current is not None:
            if self.char_current in config.chars_to_ignore:
                self.next_char()
            elif self.char_current in (config.digits + [config.DOT_CHAR]):
                try:
                    lst_expression.append(self.create_Number())
                except Illegal_Operand as e:
                    print(e)
                    return None
            elif self.char_current in config.ok_chars:
                lst_expression.append(self.char_current)
                self.next_char()
            else:
                return None
        return lst_expression

    def create_Number(self):
        point_count = 0
        operand_str = self.char_current
        self.next_char()

        while self.char_current in ([config.DOT_CHAR] + config.digits + config.chars_to_ignore)\
                and self.char_current is not None:
            if self.char_current == config.DOT_CHAR:
                point_count += 1
                operand_str += self.char_current
            elif self.char_current not in config.chars_to_ignore:
                operand_str += self.char_current
            self.next_char()

        if point_count > 1:
            raise Illegal_Operand("a number can't have more than one decimal point")
        if operand_str.startswith('.'):
            raise Illegal_Operand("a number can't start with an '.'")
        if operand_str.endswith('.'):
            raise Illegal_Operand("a number can't end with an '.'")
        if len(operand_str) > 99:
            raise Illegal_Operand(f"number : {operand_str} is too big")

        return Number(operand_str, True)
