ok_chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "-", "+", "/",
            "*", "^", "%", "$", "&", "@", "~", "!", "#", "(", ")"]
number_components = ok_chars[:11]
digits = ok_chars[:10]
error_message = ""
end_of_expression_operators = ["!", ")"]
l_brackets = ["("]
r_brackets = [")"]
