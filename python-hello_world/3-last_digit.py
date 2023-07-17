#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

if(number > 0):
    number_to_str = str(number)
    last_digit = int(number_to_str[-1])
elif(number < 0):
    number_to_str = str(number)
    last_digit = int('-'+number_to_str[-1])

# print(last_digit)
msg = str("Last digit of {} is {}".format(number, last_digit))
if last_digit > 5:
    print(msg, "and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(msg, "and is less than 6 and not 0")
elif last_digit == 0:
    print(msg, "and is 0")
