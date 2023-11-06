#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    i = 0
    c = 0
    for b in my_list:
        for a in my_list:
            if b > a and b > c:
                c = my_list[i]
                index = i
        i += 1
    return (my_list[index])
