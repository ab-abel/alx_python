#!/usr/bin/python3
"""
a finction that return true if the object is an instance of a class other
wise return false
"""


def is_kind_of_class(obj, a_class):
    """
    check if an object is subclass  other class, return true if true 
    AND FALSE OTHERWISE 
    """
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
