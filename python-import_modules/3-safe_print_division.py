#!/usr/bin/python3
# Using exception to check division properties

def safe_print_division(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        result = "None"
    finally:
        print("Inside result: {}".format(result))
    return result
