#!/usr/bin/python3
"""
a function that return true if class instance of or a subclass is the same
"""


def is_kind_of_class(obj, a_class):
    """
    Return the boolean True or False between the check 'obj' and 'a_class'.
    The issubclass methotd takes the obj type vairable, and a_class method.
    The if compirison operator is use to check if the return value is 'true or not'
    exampel:
    >>> class ClassName(obj):
    ...    pass
    >>> ClassName()
    ...
    >>>     pass
    >>>     if issubclass(type(obj), a_class):
    ...        return True
    >>>     else:
    ...         return False
    
    >>> obj = ClassName()
    >>> is 
    """
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
