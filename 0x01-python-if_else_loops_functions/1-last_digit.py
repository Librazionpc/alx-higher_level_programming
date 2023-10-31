#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    number *= -1
    num = number % 10
    number *= -1
else:
    num = number % 10
answer = f"Last digit of {number} is {num}"
if (num > 5):
    answer = answer + " " + "and is greater than 5"
elif (num < 6 and not 0):
    answer = answer + " " + "and is less than 6 and not 0"
elif (num == 0):
    answer = answer + " " + "and is 0"
print(answer)
