#!/usr/bin/python3
for i in range(0, 100):
    sep = ', ' if i < 99 else '\n'
    if i < 10:
        print("0{0}".format(i), end=sep)
    else:
        print("{0}".format(i), end=sep)
