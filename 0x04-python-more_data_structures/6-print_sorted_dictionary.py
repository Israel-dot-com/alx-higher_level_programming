#!/usr/bin/python3
    listofkeys = list(a_dictionary.keys())
    listofkeys.sort()
    for i in listofkeys:
        print("{}: {}".format(i, a_dictionary.get(i)))
