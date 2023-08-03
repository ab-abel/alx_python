#!/usr/bin/python3
"""
a function that return true if class instance of or a subclass is the same

Return the boolean True or False between the check 'obj' and 'a_class'.
The issubclass methotd takes the obj type vairable, and a_class method.
The if compirison operator is use to check if the return value is 'true or not'
exampel:

Parameters:
obj : any
    THe object to be checked for its class mambership
a_class : class
    the class that the object membeship is to be tested against
Returns:
bool
which mean its True if the obj is an instance of the class and
false if the objet is not an instance of the class

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


def is_kind_of_class(obj, a_class):

    if issubclass(type(obj), a_class):
        return True
    else:
        return False
