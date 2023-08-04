#!/usr/bin/python3
"""
a function that return true if class instance of or a subclass is the same

Return the boolean True or False between the check 'obj' and 'a_class'.
The issubclass methotd takes the obj type vairable, and a_class method.
The if compirison operator is use to check if the return value is 'true or not'
exampel:



"""


def is_kind_of_class(obj, a_class):
    """
    Function to check if a data is a subclass of the other.

    This function takes two numbers, 'a' and 'b', and returns their sum.

    Parameters:
    obj (int, float, boolean, string, list): The first number.
    a_class (could be any class or object): The second number.

    Returns:
    True or false: The output is a boolean of the comparison of the 
    the two input variable.
    
    Example
    >>> class ClassName(obj):
    ...    pass
    >>> ClassName()
    ...
    >>>    pass
    >>> if issubclass(type(obj), a_class):
    ...   return True
    >>> else:
    ...   return False

    >>> obj = ClassName()
    >>> 

    """
    if issubclass(type(obj), a_class): 
        return True
    else:
        return False
