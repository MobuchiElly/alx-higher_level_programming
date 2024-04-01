#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if 97 <= ord(str[i]) <= 122:
            print("{0}".format(chr(ord(str[i])-32)), end="")
        else:
            print("{0}".format(str[i]), end="")
