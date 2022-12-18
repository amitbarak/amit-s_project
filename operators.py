import math

from Exceptions import InvalidMath
from Operands import Number


class OperatorTypes:
    AFTER = 0
    BEFORE = 1
    BEFORE_AND_AFTER = 2


class Operator:
    CHAR = ""
    TYPE = ""

    @staticmethod
    def get_priority():
        return -1

    @staticmethod
    def operation(num1: Number, *args, **kwargs):
        return num1


def get_general_priority(operator_class):
    return operator_class.get_priority()


def get_all_operators():
    Operators_list = Operator.__subclasses__()
    for operator_class in Operators_list:
        if len(operator_class.__subclasses__()):
            Operators_list += operator_class.__subclasses__()
    return Operators_list


def get_priorities_dicts():
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


class Add(Operator):
    CHAR = "+"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 1

    @staticmethod
    def operation(num1: Number, num2: Number):
        try:
            return Number(num1.get_value() + num2.get_value())
        except ValueError:
            raise InvalidMath(f"cannot Add {num1.get_value()} + {num2.get_value()} because result is out of range")


class Sub(Operator):
    CHAR = "-"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 1

    @staticmethod
    def operation(num1: Number, num2: Number):
        try:
            return Number(num1.get_value() - num2.get_value())
        except ValueError:
            raise InvalidMath(f"cannot sub {num1.get_value()} - {num2.get_value()} because result is out of range")


class Mul(Operator):
    CHAR = "*"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 2

    @staticmethod
    def operation(num1: Number, num2: Number):
        try:
            return Number(num1.get_value() * num2.get_value())
        except ValueError:
            raise InvalidMath(f"cannot do: {num1.get_value} * {num2.get_value()} because result is out of range")


class Div(Operator):
    CHAR = "/"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 2

    @staticmethod
    def operation(num1: Number, num2: Number):
        if num2.get_value() == 0:
            raise InvalidMath(f"cannot divide by zero {num1.get_value()} / 0")
        try:
            return Number(num1.get_value() / num2.get_value())
        except ValueError as e:
            raise InvalidMath(f"cannot divide: {num1.get_value} by  {num2.get_value()} because result is out of range")


class Power(Operator):
    CHAR = "^"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 3

    @staticmethod
    def operation(num1: Number, num2: Number):
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
    CHAR = "%"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 4

    @staticmethod
    def operation(num1: Number, num2: Number):
        return Number(num1.get_value() % num2.get_value())


class Max(Operator):
    CHAR = "$"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 5

    @staticmethod
    def operation(num1: Number, num2: Number):
        if (num1.get_value() > num2.get_value()):
            return Number(num1.get_value())
        else:
            return Number(num2.get_value())


class Min(Operator):
    CHAR = "&"
    TYPE = OperatorTypes.BEFORE_AND_AFTER
    priority = 5

    @staticmethod
    def get_priority():
        return 5

    @staticmethod
    def operation(num1: Number, num2: Number):
        if num1.get_value() < num2.get_value():
            return Number(num1.get_value())
        else:
            return Number(num2.get_value())


class Avg(Operator):
    CHAR = "@"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 5

    @staticmethod
    def operation(num1: Number, num2: Number):
        op2 = Add.operation(num1, num2)
        return Number(Div.operation(op2, Number(2)))


class Negation(Operator):
    CHAR = "~"
    TYPE = OperatorTypes.BEFORE

    @staticmethod
    def get_priority():
        return 6

    @staticmethod
    def operation(num1: Number):
        return Number(-num1.get_value())


class Factorial(Operator):
    CHAR = "!"
    TYPE = OperatorTypes.AFTER

    @staticmethod
    def get_priority():
        return 6

    @staticmethod
    def operation(num1: Number):
        if int(num1.get_value()) != num1.get_value():
            raise InvalidMath("cannot Factorial a number that's not an integer")
        if num1.get_value() <= 0:
            raise InvalidMath("cannot Factorial a number that's not above zero")
        if num1.get_value() == 1:
            return Number(1)
        result_before = Factorial.operation(Number(num1.get_value() - 1)).get_value()
        if str(result_before) == "inf":
            raise InvalidMath("cannot factorial because result is too large")
        return Number(result_before * num1.get_value())


class DigitSum(Operator):
    CHAR = "#"
    TYPE = OperatorTypes.AFTER

    @staticmethod
    def get_priority():
        return 7

    @staticmethod
    def operation(num1: Number):
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
    CHAR = "--"
    TYPE = OperatorTypes.BEFORE_AND_AFTER

    @staticmethod
    def get_priority():
        return 1

    @staticmethod
    def operation(num1: Number, num2: Number):
        return Add.operation(num1, num2)


class Minus(Operator):
    CHAR = "_"
    TYPE = OperatorTypes.BEFORE
    priority = 8

    @staticmethod
    def get_priority():
        return 8

    @staticmethod
    def operation(num1: Number):
        return Number(-num1.get_value())


class DoubleMinus(Operator):
    CHAR = "__"
    TYPE = OperatorTypes.BEFORE

    @staticmethod
    def get_priority():
        return 8

    @staticmethod
    def operation(num1: Number):
        return num1
