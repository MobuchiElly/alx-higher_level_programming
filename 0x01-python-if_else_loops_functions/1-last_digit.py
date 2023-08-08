#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digt = abs(number) % 10
if l_digt > 5:
    print(f'Last digit of {number} is {l_digt} and is greater than 5')
elif l_digt == 0:
    print(f'Last digit of {number} is {l_digt} and is 0')
else l_digt < 6 and not l_digt == 0:
    print(f'Last digit of {number} is -{l_digt} and is less than 6 and not 0')
