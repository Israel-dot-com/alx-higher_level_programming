#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    maxindex = len(my_list) - 1
    new_list = my_list.copy()
    if idx < 0 or idx > maxindex:
        return my_list.copy( )
    else:
        new_list[idx] = element
        return new_list
