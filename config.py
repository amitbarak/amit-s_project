import operators

ok_chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "-", "+", "/",
            "*", "^", "%", "$", "&", "@", "~", "!", "#", "(", ")"]
number_components = ok_chars[:12]
DOT_CHAR = "."
digits = ok_chars[:10]
not_digits = ok_chars[10:]
operators_dict = {"-": operators.sub, "+" : operators.add, "/": operators.div, "*" : operators.mul,
                  "^": operators.pow, "%": operators.mod, "$": operators.max, "@": operators.avg,
                  "&": operators.min, "~": operators.negation, "!": operators.factorial,
                  "#": operators.DigitSum, "--": operators.DoubleSub, "_": operators.Minus,
                  "__" : operators.DoubleMinus}
chars_to_ignore = [" ", "\t"]
end_of_expression_chars = ["#", "!", ")"] + digits
l_brackets = ["("]
r_brackets = [")"]

