"""
in this file custom exceptions are defined:
Illegal_Operand: raised when an illegal operand is received
InvalidMath: raised when an invalid math operation is received
MissingItem: raised when an item is missing
"""


class Illegal_Operand(Exception):
    """
    this class represents an Exception that is raised when an illegal operand is encountered
    """
    pass


class InvalidMath(Exception):
    """ this class represents an Exception that is raised when an invalid math operation is encountered"""
    pass


class MissingItem(Exception):
    """ this class represents an Exception that is raised when a missing item is encountered"""
    pass
