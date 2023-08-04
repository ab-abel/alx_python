#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __dir__(cls) -> None:
        """
        this method check if a class is an instance of the define object
            exam 1 is an instancce of the class int
        """
        attrib = super().__dir__()
        n_attri = []
        for attr in attrib:
            if attr != '__init_subclass__':
                n_attri.append(attr)
        return n_attri
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