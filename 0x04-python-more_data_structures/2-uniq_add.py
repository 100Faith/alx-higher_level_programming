#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    function to get sum of unique numbers
    """
    new_list = set(my_list)
    sum = 0
    for i in set(my_list):
    sum += i
    return sum