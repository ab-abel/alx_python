#!/usr/bin/python3
#  a function that raises a type exception.


def raise_exception():
    try:
        raise TypeError 
    except TypeError as te:
        print("Exception has been raised")
