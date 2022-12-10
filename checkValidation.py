import config


def isValid(str_entered: str):
    if str_entered == "":
        print("input cant be empty")
        return False
    i = 0
    check_brackets = 0
    for c in str_entered:
        i += 1
        if c not in config.ok_chars:
            print("'{0}' is not allowed in the expression and was fount at index: {1}".format(c, i))
            return False
        elif c == "(":
            check_brackets += 1
        elif c == ")":
            check_brackets -= 1
        if check_brackets < 0:
            print("there are more closing brackets than opening brackets from the start until index: {0}")
            return False
    return True
