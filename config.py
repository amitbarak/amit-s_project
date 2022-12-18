import operators
VALID_CHARS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "-", "+", "/",
               "*", "^", "%", "$", "&", "@", "~", "!", "#", "(", ")"]
NUMBER_COMPONENTS = VALID_CHARS[:12]
ROUNDING_COUNT = 10
DOT_CHAR = "."
DIGITS = VALID_CHARS[:10]
OPERATORS_DICT = {operators_class.CHAR: operators_class for operators_class in operators.get_all_operators()}
CHARS_TO_IGNORE = [" ", "\t"]
END_OF_EXPRESSION_CHARS = ["#", "!", ")"] + DIGITS
L_BRACKETS = ["("]
R_BRACKETS = [")"]
ROUNDING_COUNT = 4

