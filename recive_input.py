"""
this file exists to receive
input from the user and handle errors it might directly
cause
"""


def get_input():
    """
    this function receives input from the user
    exits the program if encounters EOF or KeyboardInterrupt
    :return: the input from the user
    """
    try:
        str_entered = input("TYPE expression")
    except KeyboardInterrupt:
        print("\nkeyboard was Interrupted")
        exit(1)
        return None
    except EOFError:
        print("\nEOF when reading a line")
        exit(1)
        return None
    return str_entered
