"""this class defines the Operands base class
and the numbers class
note: that Nodes are also Operands however
they are defined in nodes.py"""


class Operand:
    """this abstract class represents an operand
    __init__:
        initializes the class
    get_value:
        returns the value of the operand
    """

    def __init__(self):
        """initializes the class"""
        pass

    def get_value(self):
        """returns the value of the operand"""
        pass


class Number(Operand):
    """
    this class represents a number


    __init__:
        initializes the class with a number
    get_value:
        returns the value of the number
    """

    def __init__(self, num):
        """
        initializes the class with a number
        :param num: list / string / number / float / int
        """
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
        """
        returns the value of the number
        """
        return self.__value

    def __str__(self):
        """
        returns the string representation of the number"""
        return "number: " + str(self.__value)

    def __repr__(self):
        """
        returns the string representation of the number
        """
        return "number: " + str(self.__value)
