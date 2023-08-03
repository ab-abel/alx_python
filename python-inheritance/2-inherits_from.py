#!/usr/bin/python3
"""
a function that return true if class instance of or a subclass is the same
"""



def is_kind_of_class(obj, a_class):
    """
    this method check if a class is an instance of the define object exam 1 is an instancce of the class int
    #the function is 
    """
    if issubclass(type(obj), a_class): #check two class
        return True #return a bolean
    else:#alternative
        return False #return bolean
