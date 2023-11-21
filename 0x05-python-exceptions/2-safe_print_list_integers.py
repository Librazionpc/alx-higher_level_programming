#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    int_printed = 0

    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                int_printed += 1
    except (TypeError, ValueError):
        pass
    finally:
        print()
    return (int_printed)
