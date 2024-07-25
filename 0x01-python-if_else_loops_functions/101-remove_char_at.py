#!/usr/bin/python3
def remove_char_at(str, n):
    copystr = ''
    for i in range(0, len(str)):
        if (i != n):
            copystr += str[i]
    return copystr
