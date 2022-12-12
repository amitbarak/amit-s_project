import checkValidation
import operators
from Operand import Operand
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
            elif self.char_current in config.number_components:
                lst_expression.append(self.handle_operand_creation())
            elif self.char_current in config.ok_chars:
                lst_expression.append(self.char_current)
                self.next_char()
            else:
                return None
        return lst_expression

    def handle_operand_creation(self):
        point_count = 0
        operand_str = self.char_current
        self.next_char()

        while self.char_current in config.number_components and self.char_current is not None:
            if self.char_current == '.':
                point_count += 1
            operand_str += self.char_current
            self.next_char()

        return Operand(operand_str)

    def numbers_create(self, lst_strings: list):
        lst_expression = []
        for item in lst_strings:
            if item not in config.not_digits and not checkValidation.print_is_operand(item):
                return None
            elif item not in config.not_digits:
                lst_expression.append(Operand(item))
            else:
                lst_expression.append(item)
            return lst_expression
