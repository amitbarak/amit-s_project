import math

import config
from Operand import Operand


class Operator:
    @staticmethod
    def operation(num1, num2: Operand):
        raise RuntimeError("this is an empty operand")


class add(Operator):
    char = "+"

    @staticmethod
    def operation(num1: Operand, num2):
        try:
            return Operand(num1.getValue() + num2.getValue())
        except ValueError:
            print(f"cannot add {num1.getValue()} - {num2.getValue()} because result is out of range")
            raise RuntimeError()


class sub(Operator):
    char = "-"

    @staticmethod
    def operation(num1, num2):
        try:
            return Operand(num1.getValue() - num2.getValue())
        except ValueError:
            print(f"cannot sub {num1.getValue()} - {num2.getValue()} because result is out of range")
            raise RuntimeError()


class mul(Operator):
    char = "*"

    @staticmethod
    def operation(num1: Operand, num2: Operand):
        return Operand(num1.getValue() * num2.getValue())


class div(Operator):
    char = "/"

    @staticmethod
    def operation(num1, num2):
        if type(num2) != Operand:
            print(f"got {num2} where an operand should be")
            return Operand(1)
        if num2 == 0:
            print(f"cannot divide by zero {num1.getValue()} / 0")
        return Operand(num1.getValue() / num2.getValue())


class pow(Operator):
    char = "^"

    @staticmethod
    def operation(num1, num2):
        if num2 == 0 and num1.getValue() == 0:
            config.error_message = "cannot pow zero by zero"
            return Operand(1)
        return Operand(math.pow(num1.getValue(), num2.getValue()))


class mod(Operator):
    char = "%"

    @staticmethod
    def operation(num1, num2):
        return Operand(num1.getValue() % num2.getValue())


class max(Operator):
    char = "^"

    @staticmethod
    def operation(num1, num2):
        if (num1.getValue() > num2.getValue()):
            return Operand(num1.getValue())
        else:
            return Operand(num2.getValue())


class min(Operator):
    char = "&"

    @staticmethod
    def min(num1, num2):
        if (num1.getValue() > num2.getValue()):
            return Operand(num1.getValue())
        else:
            return Operand(num2.getValue())


class avg(Operator):
    char = "@"

    @staticmethod
    def avg(num1, num2):
        op2 = num1.add(num2)
        return Operand(op2.div(Operand(2)))


class negation(Operator):
    char = "~"

    @staticmethod
    def negation(num1):
        return Operand(num1.mul(Operand(-1)))


class factorial(Operator):
    char = "!"

    @staticmethod
    def factorial(num1: Operand, num2=None):
        if num2 is not None:
            print("")
        if int(num1.getValue()) != num1.getValue():
            print("cannot factorial a number that's not an integer")
            raise RuntimeError()
        if num1.getValue() < 0:
            print("cannot factorial a number that's bellow zero")
            raise RuntimeError()
        if num1.getValue() == 1:
            return Operand(1)
        return Operand(Operand(num1.getValue() - 1).factorial())


class digit_sum(Operator):
    char = "!"

    @staticmethod
    def digit_sum(self):
        if self.__value__ <= 0:
            print("cannot count the digit sum of a number below zero")
        chars = str(self.__value__)
        num = 0
        for c in chars:
            num += int(c)
        return Operand(num)
