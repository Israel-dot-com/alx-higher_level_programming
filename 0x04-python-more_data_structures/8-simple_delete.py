#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    delcommand = del a_dictionary[key]
    if a_dictionary.get(key) is not None:
        delcommand
    return (a_dictionary)
