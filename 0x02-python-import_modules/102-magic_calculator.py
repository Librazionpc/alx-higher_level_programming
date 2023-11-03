#!/usr/bin/python3


def magic_calculation(a, b):
    add, sub = __import__('magic_calculation_102', globals(), locals(),
            ['add', 'sub'], 0)
    c = add(a, b)
    for i in range(4, 6):
        c = add(c, i)
    return c


if __name__ == "__magic_calculation__":
    magic_calculation()
