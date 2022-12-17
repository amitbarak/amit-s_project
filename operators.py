import math

import config
from Exceptions import InvalidMath
from Operands import Number


class OperatorTypes:
    AFTER = 0
    BEFORE = 1
    BEFORE_AND_AFTER = 2


class Operator:

    @staticmethod
    def operation(num1, *args, **kwargs):
        return num1



class add(Operator):
    char = "+"
    type = OperatorTypes.BEFORE_AND_AFTER
    priority = 1

    @staticmethod
    def operation(num1: Number, num2):
        try:
            return Number(num1.get_value() + num2.get_value())
        except ValueError:
            raise InvalidMath(f"cannot add {num1.get_value()} + {num2.get_value()} because result is out of range")


class sub(Operator):
    char = "-"
    type = OperatorTypes.BEFORE_AND_AFTER
    priority = 1

    @staticmethod
    def operation(num1, num2):
        if num2 == sub.char:
            return num1
        try:
            return Number(num1.get_value() - num2.get_value())
        except ValueError:
            raise InvalidMath(f"cannot sub {num1.get_value()} - {num2.get_value()} because result is out of range")


class mul(Operator):
    char = "*"
    type = OperatorTypes.BEFORE_AND_AFTER
    priority = 2

    @staticmethod
    def operation(num1: Number, num2: Number):
        try:
            return Number(num1.get_value() * num2.get_value())
        except ValueError:
            raise InvalidMath(f"cannot do: {num1.get_value} * {num2.get_value()} because result is out of range")


class div(Operator):
    char = "/"
    type = OperatorTypes.BEFORE_AND_AFTER
    priority = 2

    @staticmethod
    def operation(num1, num2):
        if type(num2) != Number:
            print(f"got {num2} where an operator should be")
            return Number(1)
        if num2 == 0:
            raise InvalidMath(f"cannot divide by zero {num1.get_value()} / 0")
        try:
            return Number(num1.get_value() / num2.get_value())
        except ValueError as e:
            raise InvalidMath(f"cannot divide: {num1.get_value} by  {num2.get_value()} because result is out of range")


class pow(Operator):
    char = "^"
    type = OperatorTypes.BEFORE_AND_AFTER
    priority = 3

    @staticmethod
    def operation(num1, num2):
        if num2 == 0 and num1.get_value() == 0:
            raise InvalidMath("cannot pow zero by zero")
        try:
            return Number(math.pow(num1.get_value(), num2.get_value()))
        except ValueError:
            raise InvalidMath(f"cannot do: {num1.get_value} to the power of {num2.get_value()}")
        except OverflowError:
            raise InvalidMath(f"cannot do: {num1.get_value} to the power of {num2.get_value()} "
                              f"because result is too large")


class mod(Operator):
    char = "%"
    type = OperatorTypes.BEFORE_AND_AFTER
    priority = 4

    @staticmethod
    def operation(num1, num2):
        return Number(num1.get_value() % num2.get_value())


class max(Operator):
    char = "$"
    type = OperatorTypes.BEFORE_AND_AFTER
    priority = 5

    @staticmethod
    def operation(num1, num2):
        if (num1.get_value() > num2.get_value()):
            return Number(num1.get_value())
        else:
            return Number(num2.get_value())


class min(Operator):
    char = "&"
    type = OperatorTypes.BEFORE_AND_AFTER
    priority = 5

    @staticmethod
    def operation(num1, num2):
        if num1.get_value() < num2.get_value():
            return Number(num1.get_value())
        else:
            return Number(num2.get_value())


class avg(Operator):
    char = "@"
    type = OperatorTypes.BEFORE_AND_AFTER
    priority = 5

    @staticmethod
    def operation(num1, num2):
        op2 = add.operation(num1, num2)
        return Number(div.operation(op2, Number(2)))


class negation(Operator):
    char = "~"
    type = OperatorTypes.BEFORE
    priority = 6

    @staticmethod
    def operation(num1):
        return Number(mul.operation(num1, Number(-1)))


class factorial(Operator):
    char = "!"
    type = OperatorTypes.AFTER
    priority = 6

    @staticmethod
    def operation(num1):
        if int(num1.get_value()) != num1.get_value():
            raise InvalidMath("cannot factorial a number that's not an integer")
        if num1.get_value() <= 0:
            raise InvalidMath("cannot factorial a number that's not above zero")
        if num1.get_value() == 1:
            return Number(1)
        return Number(mul.operation(factorial.operation(Number(num1.get_value() - 1)), num1))


class DigitSum(Operator):
    char = "#"
    type = OperatorTypes.AFTER
    priority = 10

    @staticmethod
    def operation(num1):
        if num1.get_value() < 0:
            raise InvalidMath("cannot count the digit sum of a number below zero")
        chars = str(num1.get_value())
        num = 0
        for c in chars:
            if c in config.digits:
                num += int(c)
        return Number(num)


class DoubleSub(Operator):
    char = "--"
    type = OperatorTypes.BEFORE_AND_AFTER
    priority = 1

    @staticmethod
    def operation(num1, num2):
        return add.operation(num1, num2)


class Minus(Operator):
    char = "_"
    type = OperatorTypes.BEFORE
    priority = 10

    @staticmethod
    def operation(num1):
        return negation.operation(num1)


class DoubleMinus(Operator):
    char = "__"
    type = OperatorTypes.BEFORE
    priority = 10

    @staticmethod
    def operation(num1):
        return num1
