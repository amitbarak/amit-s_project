import math

import config


class Operand:
    def __init__(self, num):
        if type(num) is Operand:
            self.__value__ = num.getValue()
        else:
            self.__value__ = float(num)


    def getValue(self) ->float:
        return self.__value__


    def add(self, num2):
        return Operand(self.__value__ + num2.getValue())


    def sub(self, num2):
        return Operand(self.__value__ - num2.getValue())

    def mul(self, num2):
        return Operand(self.__value__ * num2.getValue())

    def div(self, num2):
        return Operand(self.__value__ / num2.getValue())

    def pow(self, num2):
        return Operand(math.pow(self.__value__, num2.getValue()))

    def mod(self, num2):
        return Operand(self.__value__ % num2.getValue())

    def max(self, num2):
        if(self.__value__ > num2.getValue()):
            return Operand(self.__value__)
        else:
            return Operand(num2.getValue())

    def min(self, num2):
        if(self.__value__ > num2.getValue()):
            return Operand(self.__value__)
        else:
            return Operand(num2.getValue())

    def avg(self, num2):
        return Operand(self.mul(self.div(num2), Operand(2)))

    def negation(self, num2):
        return Operand(self.mul(Operand(-1)))

    def factorial(self):
        if self.__value__ == 1:
            return Operand(1)
        return Operand(self.mul(Operand(self.__value__ - 1).factorial()))

    def digit_sum(self):
        if self.__value__ <= 0:
            raise RuntimeError("cannot count the digit sum of a number below zero")
        chars = str(self.__value__)
        num = 0
        for c in chars:
            if c in config.digits:
                num += int(c)
        return Operand(num)


    def __str__(self):
        return str(self.__value__)