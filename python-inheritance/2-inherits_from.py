#!/usr/bin/python3
"""
a finction that return true if the object is an instance of a class other
wise return false
"""


def is_kind_of_class(obj, a_class):
    """
    this method check if a class is a issubclass of the define object exam 1 is a subclass of the class int this method check 
    if a class is a issubclass of the define object
    exam 1 is a issubclass of the class int 
    """
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
