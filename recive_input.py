def get_input():
    try:
        str_entered = input("TYPE expression")
    except KeyboardInterrupt:
        print("keyboard was Interrupted")
        exit(1)
        return None
    except EOFError:
        print("EOF when reading a line")
        exit(1)
        return None
    return str_entered