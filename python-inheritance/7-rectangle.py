#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).
    """
    def __dir__(cls)->None:
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def __init__(self, width, height):
        """
        initialaizatio function for base geometry
        """
      
        width = BaseGeometry.integer_validator(self, "width", width)
        height = BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
        

    def area(self):
        return self.__width/self.__height

print(dir(Rectangle))
