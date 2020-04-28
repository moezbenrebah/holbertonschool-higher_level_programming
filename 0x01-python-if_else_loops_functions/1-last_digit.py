#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 10:
    ldigit = number % 10
else:
    ldigit = number % -10
print("last digit of {:d} is {:d} and is".format(number, ldigit), end=' ')
if ldigit == 0:
    print("and is 0")
elif ldigit > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
