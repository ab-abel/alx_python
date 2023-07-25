#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        result = a/b
        break
    except ZeroDivisionError:
        print("None")
    else:
        print("Inside result: {}".format(result))
    finally:
        print("{:d} / {:d} = {}".format(a, b, result))
