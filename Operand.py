import math



class Operand:
    def __init__(self, num):
        if type(num) is Operand:
            self.__value__ = num.get_value()
        elif type(num) is int or type(num) is float:
            self.__value__ = float(num)
        elif type(num) is str:  # there is only need to check 'num' of it's a string
            self.__value__ = float(num)
        elif type(num) is list:
            self.__value__ = Operand(num[0]).get_value()

    def get_value(self) -> float:
        return self.__value__

    def __str__(self):
        return "operator: " + str(self.__value__)

    def __repr__(self):
        return "operator: " + str(self.__value__)



