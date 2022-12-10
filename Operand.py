import math

import config


class Operand:
    def __init__(self, num):
        if type(num) is Operand:
            self.__value__ = num.getValue()
        elif type(num) is int or type(num) is float:
            self.__value__ = float(num)
        elif type(num) is str:  # there is only need to check 'num' of it's a string
            self.__value__ = float(num)
        elif type(num) is list:
            self.__value__ = num[0]
        elif type(num) is Operand:
            self.__value__ = float(num.getValue())
#
    def getValue(self) -> float:
        return self.__value__

    def add(self, num2):
        try:
            return Operand(self.__value__ + num2.getValue())
        except ValueError:
            print(f"cannot add {self.__value__} - {num2.getValue()} because result is out of range")
            raise RuntimeError()

    def sub(self, num2):
        try:
            return Operand(self.__value__ - num2.getValue())
        except ValueError:
            print(f"cannot sub {self.__value__} - {num2.getValue()} because result is out of range")
            raise RuntimeError()

    def mul(self, num2):
        return Operand(self.__value__ * num2.getValue())

    def div(self, num2):
        if type(num2) != Operand:
            print(f"got {num2} where an operand should be")
        if num2 == 0:
            print(f"cannot divide by zero {self.__value__} / 0")
        return Operand(self.__value__ / num2.getValue())

    def pow(self, num2):
        if num2 == 0 and self.__value__ == 0:
            config.error_message = "cannot pow zero by zero"
            return Operand(1)
        return Operand(math.pow(self.__value__, num2.getValue()))

    def mod(self, num2):
        return Operand(self.__value__ % num2.getValue())

    def max(self, num2):
        if (self.__value__ > num2.getValue()):
            return Operand(self.__value__)
        else:
            return Operand(num2.getValue())

    def min(self, num2):
        if (self.__value__ > num2.getValue()):
            return Operand(self.__value__)
        else:
            return Operand(num2.getValue())

    def avg(self, num2):
        op2 = self.add(num2)
        return Operand(op2.div(Operand(2)))

    def negation(self):
        return Operand(self.mul(Operand(-1)))

    def factorial(self):
        if int(self.__value__) != self.__value__:
            print("cannot factorial a number that's not an integer")
            raise RuntimeError()
        if self.__value__ < 0:
            print("cannot factorial a number that's bellow zero")
            raise RuntimeError()
        if self.__value__ == 1:
            return Operand(1)
        return Operand(self.mul(Operand(self.__value__ - 1).factorial()))



    def digit_sum(self):
        if self.__value__ <= 0:
            print("cannot count the digit sum of a number below zero")
        chars = str(self.__value__)
        num = 0
        for c in chars:
            num += int(c)
        return Operand(num)

    def __str__(self):
        return "operand: " + str(self.__value__)
