#!/usr/bin/python3
def no_c(my_string):
    listitem = list(my_string)
    countitem = listitem.count('c') - 1
    i = 0
    while i < countitem:
        if 'c' in listitem:
            listitem.remove('c')
        else:
            break
        i += 1
return listitem
