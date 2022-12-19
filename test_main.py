import pytest
import calculate

"""
this file tests calculations from calculate.py file
which is the main file of the project
"""


def test_equations_value():
    """
    this function tests the value of the equations
    that has values
    """
    equations_with_value = {"2^3    ": 8, "~--2": -2, "(1 / 2) ^ 2": 0.25, "(123 * 2)#": 12,
                            "~-5!": 120, "---~5 $ 3": 5, "-3--2 @ 1": -1.5, "123# @ 0.1": 3.05, "5!#": 3,
                            "-1/2": -0.5, "-7&1": -7, "1.01 + -~1!": 2.01, "31 % -2": -1,
                            "-1/~--2": 0.5, "1 - - ~-3!": 7,
                            "(2 +-- 0.5 * 3 ^ 2 % 3 @ 41# + -~0.5)! * 2": 10080,
                            "(2---3! - 4.5 * 0.0001 * 10 ^ 4 * (3-1) + 1 + 4!-~3)  $ 10.4 ": 15,
                            "(4 ---1!)  + (5!#!) + (3!)# + ~12 @ (3 $ -1 $ 2.99)": 10.5,
                            "(3*-~--3!) * 3 / (--3!-~-3) ^ 2    - 10 * 0 @ 1.10# $ 1": -4,
                            "(4! + 2 * 3 $ (1 / (0.1) / (1 / 3) * 1000 % 2) & 10000)": 30,
                            "(4! + 2 * 3 $ (1 / (0.1) / (1 / 3) * 1000 % 3) & 10000)": 84,
                            "(1/3 & 2 * (1 / 3 $ 2) / 4 & 4.1 / 5 / 6 /7 * (7!)) @ 3": 2,
                            "\t(1   1 * 2 ^ -(-~(-2))  - 1234.56789# * (1/-5))#! / 8 / 7 / 6\t": 120,
                            "(-1 / -2 / -3 % -2 --3! + 3 % (3 * 2)   \t $ 2) ^ 1.5": 24.7815,
                            "(((1.000 * (-~4!# ^ 6) % 36) $ 0.25) % 0.2) @ 0": 0.025,
                            "12345678#$(--3035.10#) * 10": 360,
                            "\t 2 ^ 2 ^ 2 % 15 + (23.5 ^ 4)  \t": 304996.0625,
                            "(~-3! + 0) @ -2  - (75.435 % 5)#": -15,
                            "(190915# * 5 / 5 ^ 2 @ 2 ^ 1) @ ~-2!!!!! ": 3.5,
                            "((9999999.6633# / 3 ^ 4) * 404 \t)": 404,
                            "7 & 6 & 5 & 4 - (3 $ 2 $ 4 $ ---1.1)": 0,
                            "61# $ 6 $ 5 $ 4 - (3 & 2 & 4 & ----5.1)": 5,
                            "((((((--2!!!! ^ ~-2!!!!# -- 3!!#))))))": (9 + 4),
                            "((1 / 2 / 3 / 4 / 5 / 6 ) * 6!) ^ 2": 1,
                            "       (3!#!#!#        \t!#!#) - 92 @ 92 @ -92 @ 92 ": 49

                            }
    for equation, result in equations_with_value.items():
        assert calculate.calculate(equation).get_value() == result
        print(result)


def test_errors():
    """
    this function tests that certain errors are dedicated correctly in the calculate() function
    """
    errors = ["2^*2", "*1", "21.1*", "-", "3-!4"]
    for equation in errors:
        assert calculate.calculate(equation) is None

