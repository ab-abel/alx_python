#!/usr/bin/python3
"""
The module of a class name Geometry that has a single function
"""


class BaseGeometry:
    """
    this method check if a class is an instance of the define object
    exam 1 is an instancce of the class int
    """
    def area(self):
        raise NotImplementedError("area() is not implemented")
