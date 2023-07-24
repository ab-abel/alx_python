#!/usr/bin/env python3
# A prime number function
# Example of prime numebr is 2 ,3, 5, 7, 11..abs

def is_prime(num):
    a = []
    for i in range(2, num):
        if(num%i ==0):
            a.append('False')
            break
        else:
            a.append('True')
    if ('False' in a or num<=1): 
        is_valid = False
    else:
        is_valid = True
    return is_valid
