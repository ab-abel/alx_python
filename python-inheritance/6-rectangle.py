#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        width = BaseGeometry.integer_validator(self, "width", width)
        height = BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
    
