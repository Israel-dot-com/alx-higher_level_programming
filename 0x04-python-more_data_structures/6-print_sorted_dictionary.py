#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listofkeys = list(a_dictionary.keys())
    listofkeys.sort()
    for i in listofkeys:
        print("{}: {}".format(i, a_dictionary.get(i)))
