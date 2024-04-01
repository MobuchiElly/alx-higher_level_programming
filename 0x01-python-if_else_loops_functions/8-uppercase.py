#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if 'a' <= str[i] <= 'z':
            print("{0}".format(chr(ord(str[i])-32)), end="")
        else:
            print("{0}".format(str[i]), end="")
