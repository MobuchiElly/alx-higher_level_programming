#!/usr/bin/python3
for i in range(0, 100):
    sep = ', ' if i < 99 else '\n'
    if i < 10:
        print(f"0{i}", end=sep)
    else:
        print(f"{i}", end=sep)
