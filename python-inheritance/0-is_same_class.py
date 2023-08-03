#!/usr/bin/python3
"""
a function that return true if class instance is the same
"""


def is_same_class(obj, a_class):
    """
    this method check if a class is an instance of the define object
    exam 1 is an instancce of the class int
    """
    if type(obj) is a_class:
        return True
    else:
        return False
