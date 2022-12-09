#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary
    with all values multiplied by 2
    """
    copy = a_dictionary.copy()
    list_d = list(copy.keys())
    list_d.sort()
    for val in list_d:
        copy[val] *= 2
        return copy
