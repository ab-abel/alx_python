#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).
    """
    def __init__(self, width, height):
        """
        initialaizatio function for base geometry
        """
      
        width = BaseGeometry.integer_validator(self, "width", width)
        height = BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height



print(dir(Rectangle))