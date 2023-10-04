#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
    print("Last digit of {} is {} and is ".format(number, digit), end="")
if digit > 5:
    digit = digit
    print("greater than 5")
elif digit == 0:
    digit = digit
    print("0")
else:
    print("less than 6 and not 0")
