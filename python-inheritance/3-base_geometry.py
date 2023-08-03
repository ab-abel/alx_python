#!/usr/bin/python3
"""
a function that return true if class instance of or a subclass is the same
"""


class BaseGeometry:
    """
    this method check if a class is an instance of the define object
    exam 1 is an instancce of the class int
    """
    def __dir__(self):

        attrib = super().__dir__()
        n_attri = []
        for attr in attrib:
            if attr != '__init_subclass__':
                n_attri.append(attr)
        return n_attri
