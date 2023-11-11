#!/usr/bin/python3

def search_replace(my_list, search, replace):

    if my_list is not None and search >= 0:
        new_list = []
        for i in range(0, len(my_list)):
            if (i == (search - 1)):
                new_list.append(replace)
                continue
            new_list.append(my_list[i])
    return (new_list)
