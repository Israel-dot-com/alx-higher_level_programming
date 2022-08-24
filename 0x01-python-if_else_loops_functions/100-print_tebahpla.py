#!/usr/bin/python3
for i in range(-122, -96):
    if i % 2 == 0:
        print("{0}".format(chr(i*(-1))).lower(), end="")
    else:
        print("{0}".format(chr(i*(-1))).upper(), end="")
