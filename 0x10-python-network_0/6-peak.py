#!/usr/bin/python3
"""Finds the max in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds max in list_of_integers list"""

    if list_of_integers is None or list_of_integers == []:
        return None
    low_index = 0
    high_index = len(list_of_integers)
    mid_index = ((high_index - low_index) // 2) + low_index
    mid_index = int(mid_index)
    if high_index == 1:
        return list_of_integers[0]
    if high_index == 2:
        return max(list_of_integers)
    if list_of_integers[mid_index] >= list_of_integers[mid_index - 1] and\
            list_of_integers[mid_index] >= list_of_integers[mid_index + 1]:
        return list_of_integers[mid_index]
    if mid_index > 0 and list_of_integers[mid_index] < list_of_integers[mid_index + 1]:
        return find_peak(list_of_integers[mid_index:])
    if mid_index > 0 and list_of_integers[mid_index] < list_of_integers[mid_index - 1]:
        return find_peak(list_of_integers[:mid_index])
