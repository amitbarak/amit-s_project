import math


class Operand:
    def __init__(self):
        pass

    def get_value(self):
        pass



class Number(Operand):
    def __init__(self, num: float):
        from config import ROUNDING_COUNT
        super().__init__()
        if type(num) is Number:
            self.__value = num.get_value()
        elif type(num) is int or type(num) is float:
            self.__value = float(num)
        elif type(num) is str:
            self.__value = float(num)
        elif type(num) is list:
            self.__value = Number(num[0]).get_value()

    def get_value(self):
        return self.__value

    def __str__(self):
        return "number: " + str(self.__value)

    def __repr__(self):
        return "number: " + str(self.__value)
