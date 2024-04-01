#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += "{0}".format(chr(ord(char) - 32))
        else:
            result += "{0}".format(char)
    print(result)
