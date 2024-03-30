#!/usr/bin/python3
def find_peak(list_of_integers):
    """Function that finds the peak if integers in the list
    """
    highest = 0
    if list_of_integers == []:
        return None
    for i in list_of_integers:
        if (highest < i):
            highest = i
    if highest == 0:
        return None
    else:
        return highest
