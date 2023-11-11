#!/usr/bin/python3

def uniq_add(my_list=[]):
    results = 0
    num_is_present = []

    for num in my_list:
        if num not in num_is_present:
            results += num
            num_is_present.append(num)
    return (results)
