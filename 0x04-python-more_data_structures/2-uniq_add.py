#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = set(my_list)
    num = 0
    for i in newlist:
        num += i
    return (num)
