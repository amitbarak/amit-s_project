"""
This file contains the CONSTANT values for the calculator
"""
import operators


VALID_CHARS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "-", "+", "/",
               "*", "^", "%", "$", "&", "@", "~", "!", "#", "(", ")"]
NUMBER_COMPONENTS = VALID_CHARS[:12]  # all the chars that can be in a number
ROUNDING_COUNT = 4  # the number of digits after the dot to round to
DOT_CHAR = "."  # the char that represents the dot
DIGITS = VALID_CHARS[:10]  # all the chars that represent digits
# the chars that represent the operators in a dictionary
OPERATORS_DICT = {operators_class.CHAR: operators_class for operators_class in operators.get_all_operators()}
# all blank chars
CHARS_TO_IGNORE = [" ", "\t"]
# the characters that represent the brackets
L_BRACKETS = ["("]
R_BRACKETS = [")"]
