#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    print("{0}".format(
        chr(i - 32) if (ord('z') - i) % 2 != 0 else chr(i)
        ), end="")
