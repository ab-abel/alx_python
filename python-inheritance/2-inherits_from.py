#!/usr/bin/python3
"""
a function that return true if class instance of or a subclass is the same
"""


def is_kind_of_class(obj, a_class):
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
