import pytest
import main
import os


def test_equations_value():
    equations_with_value = {"2^3": 8, "~--2": -2, "(1 / 2) ^ 2": 0.25, "(123 * 2)#": 12,
                            "~-5!": 120, "---~5 $ 3": 5, "-3--2 @ 1": -1.5, "123# @ 0.1": 3.05, "5!#": 3,
                            "-1/2": -0.5, "-7&1": -7, "1.01 + -~1!": 2.01, "31 % -2": -1,
                            "-1/~--2": 0.5, "1 - - ~-3!": 7, "(2 +-- 0.5 * 3 ^ 2 % 3 @ 41# + -~0.5)!": 5040,
                            "2---3! + 4!-~3 - 09 * 0.001 * 10 ^ 3 * (2-1)": 14,
                            "(2 ---1!) + (4!)# + ((4!#!))": 727,
                            "-~5!# * 3 @ 1 + -1 ^ 4 + ((2)) * ((4 ^ -~-2.00)) ": 7.125}
    for equation, result in equations_with_value.items():
        assert main.calculate(equation).get_value() == result
        print(result)


def test_errors():
    errors = ["2^*2", "*1", "21.1*", "-", "3-!4",
              "(( 1+ 2)", "()", "123#!~", "1.1.", "-3!", ""
              "12s1-=1", "", " ", "\t", "", "~5!"]
    for equation in errors:
        assert main.calculate(equation) == None


def test_6():
    lst_strs_entered = [""]
