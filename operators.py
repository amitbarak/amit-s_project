"""
in this file we define all the operators classes that we want to use in our calculator:
addition, subtraction, multiplication, division, mod, power, average, min, max, factorial, negation
DoubleMinus, Minus, DoubleSub

additionally we define:
Operator - the base class for all the
OperatorTypes - an enum-like class that defines the types of operators: BEFORE, AFTER, BEFORE_AND_AFTER
get_priorities_dicts() - a function that returns a list of dictionaries, ordered by
priority, that contains all the operators classes and their chars
get_all_operators() - a function that returns a list of all the childClasses of Operator
get_general_priority() - a function that returns the priority of the operator_class
"""
import math

from custom_exceptions import InvalidMath
from operands import Number




class OperatorTypes:
    """
    This class is used to store the different types of operators
    Attributes:
    ------------
    AFTER: int
        The operator is after the operand
    BEFORE: int
        The operator is before the operand
    BETWEEN: int
        The operator is between two operands
    """
    AFTER = 0
    BEFORE = 1
    BEFORE_AND_AFTER = 2


class Operator:
    """
    This class is the base class for all operators.
    Attributes
    ----------
        CHAR: the char that represents the operator
        TYPE: the type of the operator
    Methods
    -------
    get_priority() -> int:
        returns the priority of the operator
    operation() -> Number:
        returns the result of the operation

    """
    CHAR = ""
    TYPE = ""

    @staticmethod
    def get_priority():
        raise Warning("get_priority() is not implemented")

    @staticmethod
    def operation(*args, **kwargs):
        raise Warning("operation() is not implemented")


class Add(Operator):
    """
    a static class to represent the Addition operation
    Attributes
    ----------
    CHAR : str
        the character that represents the operator
    TYPE : OperatorTypes
        the type of the operator
    METHODS
    -------
    get_priority()  -> int
        returns the priority of the operator
    operation(num1: Number, num2: Number) -> Number
        adds the two numbers
    """
    CHAR = "+"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 1

    @staticmethod
    def operation(num1: Number, num2: Number) -> Number:
        """
        adds the two numbers
        :raises: InvalidMath if the operation is not valid
        :param num1: the first Number in the operation
        :param num2: the second Number in the operation
        :return: the result of the Addition operation on the two numbers
        """

        try:
            return Number(num1.get_value() + num2.get_value())
        except ValueError:
            raise InvalidMath(f"cannot Add {num1.get_value()} + {num2.get_value()} because result is out of range")


class Sub(Operator):
    """
    a static class to represent the Subtraction operation
    Attributes
    ----------
    CHAR : str
        the character that represents the operator
    TYPE : OperatorTypes
        the type of the operator
    METHODS
    -------
    get_priority()  -> int
        returns the priority of the operator
    operation(num1: Number, num2: Number) -> Number
        subs the two numbers
    """
    CHAR = "-"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 1

    @staticmethod
    def operation(num1: Number, num2: Number) -> Number:
        """
        subs the two numbers
        :raises: InvalidMath if the operation is not valid
        :param num1: the first Number in the operation
        :param num2: the second Number in the operation
        :return: a number with the result of the Addition operation on the two numbers
        """
        try:
            return Number(num1.get_value() - num2.get_value())
        except ValueError:
            raise InvalidMath(f"cannot sub {num1.get_value()} - {num2.get_value()} because result is out of range")


class Mul(Operator):
    """a static class to represent the Multiplication operation
    Attributes
    ----------
        CHAR : str
            the character that represents the operator
        TYPE : OperatorTypes
            the type of the operator
        METHODS
        -------
            get_priority()  -> int
                returns the priority of the operator
            operation(num1: Number, num2: Number) -> Number
                multiplies the two numbers
"""
    CHAR = "*"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 2

    @staticmethod
    def operation(num1: Number, num2: Number) -> Number:
        """
        multiplies the two numbers
        :raises: InvalidMath if the operation is not valid
        :param num1: the first Number in the operation
        :param num2: the second Number in the operation
        :return: the result of the mul operation on the two numbers
        """

        try:
            return Number(num1.get_value() * num2.get_value())
        except ValueError:
            raise InvalidMath(f"cannot do: {num1.get_value} * {num2.get_value()} because result is out of range")


class Div(Operator):
    """a static class to represent the Division operation
    Attributes
    ----------
        CHAR : str
            the character that represents the operator
        TYPE : OperatorTypes
            the type of the operator
    METHODS
    -------
        get_priority()  -> int
            returns the priority of the operator
        operation(num1: Number, num2: Number) -> Number
            divides the two numbers num1 / num2
    """
    CHAR = "/"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 2

    @staticmethod
    def operation(num1: Number, num2: Number) -> Number:
        """
        divides the two numbers num1 / num2
        :raises: InvalidMath if the operation is not valid
        :param num1: the first Number in the operation
        :param num2: the second Number in the operation
        :return: a number with the result of the div operation on the two numbers
        """

        if num2.get_value() == 0:
            raise InvalidMath(f"cannot divide by zero {num1.get_value()} / 0")
        try:
            return Number(num1.get_value() / num2.get_value())
        except ValueError:
            raise InvalidMath(
                f"cannot divide: {num1.get_value()} by  {num2.get_value()} because result is out of range")


class Power(Operator):
    """a static class to represent the Power operation
    Attributes
    ----------
        CHAR : str
            the character that represents the operator
        TYPE : OperatorTypes
            the type of the operator
    METHODS
    -------
        get_priority()  -> int
            returns the priority of the operator
        operation(num1: Number, num2: Number) -> Number
            powers(num1, num2)
    """
    CHAR = "^"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 3

    @staticmethod
    def operation(num1: Number, num2: Number) -> Number:
        """
        powers(num1, num2)
        :param num1: the first Number in the operation
        :param num2: the second Number in the operation
        :return: a number with the result of the Power operation on the two numbers
        """
        if num2 == 0 and num1.get_value() == 0:
            raise InvalidMath("cannot Power zero by zero")
        if int(num2.get_value()) != num2.get_value() and num1.get_value() < 0:
            raise InvalidMath("cannot do: x ^ y if x is negative and y is not an integer")
        try:
            return Number(math.pow(num1.get_value(), num2.get_value()))
        except OverflowError:
            raise InvalidMath(f"cannot do: {num1.get_value()} to the Power of {num2.get_value()} "
                              f"because result is too large")


class Mode(Operator):
    """a static class to represent the Mode operation
    Attributes
    ----------
        CHAR : str
            the character that represents the operator
        TYPE : OperatorTypes
            the type of the operator
    METHODS
    -------
        get_priority()  -> int
            returns the priority of the operator
        operation(num1: Number, num2: Number) -> Number
            returns the result of the Mode operation on the two numbers
    """
    CHAR = "%"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 4

    @staticmethod
    def operation(num1: Number, num2: Number) -> Number:
        """
        takes two Numbers and returns num1 % num2 raises
        :param num1: a Number that the first number of a mode operation
        :param num2: a Number that the second number of a mode operation
        :raise: InvalidMath if the operation is not valid
        :return: a number with the value of the mode operation on num1, num2
        """
        if num2.get_value() == 0:
            raise InvalidMath(f"cannot mode by zero {num1.get_value()} % 0")
        try:
            return Number(num1.get_value() % num2.get_value())
        except ValueError as e:
            raise InvalidMath(f"cannot mode: {num1.get_value()} by  {num2.get_value()} because result is out of range")


class Max(Operator):
    """a static class to represent the Max operation
    Attributes
    ----------
        CHAR : str
            the character that represents the operator
        TYPE : OperatorTypes
            the type of the operator
    METHODS
    -------
        get_priority()  -> int
            returns the priority of the operator
        operation(num1: Number, num2: Number) -> Number
            takes two Numbers and returns the max of them
    """
    CHAR = "$"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 5

    @staticmethod
    def operation(num1: Number, num2: Number):
        """
        takes two Numbers and returns the max of them
        :param num1: the first Number in the operation
        :param num2: the second Number in the operation
        :return: a number with the value of the max operation on the two numbers
        """
        if num1.get_value() > num2.get_value():
            return Number(num1.get_value())
        else:
            return Number(num2.get_value())


class Min(Operator):
    """a static class to represent the Min operation
    Attributes
    ----------
        CHAR : str
            the character that represents the operator
        TYPE : OperatorTypes
            the type of the operator
    METHODS
    -------
        get_priority()  -> int
            returns the priority of the operator
        operation(num1: Number, num2: Number) -> Number
            takes two Numbers and returns the min of them
    """
    CHAR = "&"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 5

    @staticmethod
    def operation(num1: Number, num2: Number):
        """
        takes two Numbers and returns the min of them
        :param num1: the first Number in the operation
        :param num2: the second Number in the operation
        :raise: InvalidMath if the operation is not valid
        :return: a number with the value of the min operation on the two numbers
        """
        if num1.get_value() < num2.get_value():
            return Number(num1.get_value())
        else:
            return Number(num2.get_value())


class Avg(Operator):
    """a static class to represent the Avg operation
        Attributes
        ----------
            CHAR : str
                the character that represents the operator
            TYPE : OperatorTypes
                the type of the operator
        METHODS
        -------
            get_priority()  -> int
                returns the priority of the operator
            operation(num1: Number, num2: Number) -> Number
                takes two Numbers and returns the average of them
                        """
    CHAR = "@"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 5

    @staticmethod
    def operation(num1: Number, num2: Number):
        """
        takes two Numbers and returns the average of them
        :param num1: the first Number in the operation
        :param num2: the second Number in the operation
        :raise: InvalidMath if the result is out of range
        :return: the average of the two numbers
        """
        op2 = Add.operation(num1, num2)
        return Number(Div.operation(op2, Number(2)))


class Negation(Operator):
    """
    a static class to represent the Negation operation
    Attributes
    ----------
        CHAR : str
            the character that represents the operator
        TYPE : OperatorTypes
            the type of the operator
    METHODS
    -------
        get_priority()  -> int
            returns the priority of the operator
        operation(num1: Number, num2: Number) -> Number
            returns the result of the Negation operation on the two numbers
    """
    CHAR = "~"
    TYPE = OperatorTypes.BEFORE

    @staticmethod
    def get_priority():
        return 6

    @staticmethod
    def operation(num1: Number):
        """
        takes a Number and returns the negation of it
        :param num1: a Number that the negation operation will be done on
        :raise: InvalidMath if the operation is not valid
        :return: a number with the value of the negation operation on num1
        """
        return Number(-num1.get_value())


class Factorial(Operator):
    """
    a static class to represent the Factorial operation
    Attributes
    ----------
        CHAR : str
            the character that represents the operator
        TYPE : OperatorTypes
            the type of the operator
    METHODS
    -------
        get_priority()  -> int
            returns the priority of the operator
        operation(num1: Number, num2: Number) -> Number
            returns the result of the Factorial operation on the number
    """
    CHAR = "!"
    TYPE = OperatorTypes.AFTER

    @staticmethod
    def get_priority():
        return 6

    @staticmethod
    def operation(num1: Number):
        """
        takes a Number and returns the factorial of it
        :param num1: a number that the factorial operation is performed on
        :raises InvalidMath: if the number is not a natural number, or if the result is too large
        :return: the result of the factorial operation on num1
        """
        initial_value = num1.get_value()
        try:
            return Factorial.factorial(num1)
        except RecursionError:
            raise InvalidMath(f"cannot do: {initial_value}! because result is too large")

    @staticmethod
    def factorial(num1: Number):
        """a helper function to the operation of the factorial class
        :param num1: a number that the factorial operation is performed on
        :raises InvalidMath: if the number is not a natural number or result is too large"""

        if int(num1.get_value()) != num1.get_value():
            raise InvalidMath("cannot Factorial a number that's not an integer")
        if num1.get_value() <= 0:
            raise InvalidMath("cannot Factorial a number that's not above zero")
        if num1.get_value() == 1:
            return Number(1)
        result_before = Factorial.factorial(Number(num1.get_value() - 1)).get_value()
        if str(result_before) == "inf":
            raise InvalidMath("cannot factorial because result is too large")
        return Number(result_before * num1.get_value())


class DigitSum(Operator):
    """
    a static class to represent the DigitSum operation
    Attributes
    ----------
        CHAR : str
            the character that represents the operator
        TYPE : OperatorTypes
            the type of the operator
    METHODS
    -------
        get_priority()  -> int
            returns the priority of the operator
        operation(num1: Number, num2: Number) -> Number
            returns the result of the DigitSum operation on the two numbers
    """
    CHAR = "#"
    TYPE = OperatorTypes.AFTER

    @staticmethod
    def get_priority():
        return 8

    @staticmethod
    def operation(num1: Number):
        """
        takes a Number and returns the DigitSum of it
        :param num1: a Number that the DigitSum operation will be done on
        :return: a Number with the value of the DigitSum operation on num1
        """
        from config import DIGITS
        if num1.get_value() < 0:
            raise InvalidMath("cannot count the digit sum of a number below zero")
        chars = str(num1.get_value())
        num = 0
        for c in chars:
            if c in DIGITS:
                num += int(c)
        return Number(num)


class DoubleSub(Operator):
    """
    a static class to represent the DoubleSub operation
    for example: 5--3 = 5+3
    Attributes
    ----------
        CHAR : str
            the character that represents the operator
        TYPE : OperatorTypes
            the type of the operator
    METHODS
    -------
        get_priority()  -> int
            returns the priority of the operator
        operation(num1: Number, num2: Number) -> Number
            returns the result of the DoubleSub operation on the two numbers

    """
    CHAR = "--"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 1

    @staticmethod
    def operation(num1: Number, num2: Number):
        """
        takes two Numbers and returns the result of the DoubleSub operation on them
        :param num1: the first Number in the operation
        :param num2: the second Number in the operation
        :return: the result of the DoubleSub operation on the two numbers
        """
        return Add.operation(num1, num2)


class Minus(Operator):
    """
    a static class to represent the Minus operation
    for example: 3 + -3 will be 3 + (_3)
    Attributes
    ----------
        CHAR : str
            the character that represents the operator
        TYPE : OperatorTypes
            the type of the operator
    METHODS
    -------
        get_priority()  -> int
            returns the priority of the operator
        operation(num1: Number, num2: Number) -> Number
            returns the result of the Minus operation on the two numbers
    """
    CHAR = "_"
    TYPE = OperatorTypes.BEFORE
    priority = 7

    @staticmethod
    def get_priority():
        return 7

    @staticmethod
    def operation(num1: Number):
        """
        takes a Number and returns the Minus of it
        :param num1: a Number that the Minus operation will be done on
        :return: the result of the Minus operation on num1
        """
        return Number(-num1.get_value())


class DoubleMinus(Operator):
    """
    a static class to represent the DoubleMinus operation
    for example: 3 + --3 will be 3 + (__3)
    Attributes
    ----------
        CHAR : str
            the character that represents the operator
        TYPE : OperatorTypes
            the type of the operator
    METHODS
    -------
        get_priority()  -> int
            returns the priority of the operator
        operation(num1: Number, num2: Number) -> Number
            returns the result of the DoubleMinus operation on the two numbers
    """
    CHAR = "__"
    TYPE = OperatorTypes.BEFORE

    @staticmethod
    def get_priority():
        return 7

    @staticmethod
    def operation(num1: Number):
        return num1


def get_general_priority(operator_class):
    """
    This function returns the priority of the operator_class
    :param operator_class: this is the class of an operator
    :return: the priority of the operator_class
    """
    return operator_class.get_priority()


def get_all_operators():
    """
    This function returns a list of all the childClasses of Operator
    :return: all of the childClasses of Operator
    """
    Operators_list = Operator.__subclasses__()
    for operator_class in Operators_list:
        if len(operator_class.__subclasses__()):
            Operators_list += operator_class.__subclasses__()
    return Operators_list


def get_priorities_dicts():
    """
     This function creates a list of dictionaries,
     ordered by priority, that contains all the operators classes and their CHAR values as keys
     :return: a list of dictornaries, ordered by priority,
      that contains all the operators classes and their CHAR values as keys
    """
    Operators_list = get_all_operators()
    Operators_list.sort(key=get_general_priority, reverse=True)
    lst_priorities_dict = []
    last_priority = -1
    for operator_class in Operators_list:
        if operator_class.get_priority() == last_priority:
            lst_priorities_dict[-1].update({operator_class.CHAR: operator_class})
        else:
            lst_priorities_dict.append({operator_class.CHAR: operator_class})
            last_priority = operator_class.get_priority()
    return lst_priorities_dict