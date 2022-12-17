def get_input():
    try:
        str_entered = input("type expression")
    except KeyboardInterrupt:
        print("keyboard was Interrupted")
        return None
    except EOFError:
        print("EOF when reading a line")
        exit(1)
        return None
    return str_entered