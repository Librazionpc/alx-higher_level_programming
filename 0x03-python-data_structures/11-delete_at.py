#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    if (idx < 0 or idx >= len(my_list)):
        return (my_list)

    i = 0
    new_list = []
    while (i < len(my_list)):
        if (i == idx):
            i += 1
            continue
        else:
            new_list.append(my_list[i])
        i += 1
    my_list[:] = new_list
    return (new_list)
