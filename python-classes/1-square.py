#!/usr/bin/python3
"""
This is a module design to explore basic concept of class
"""

class Square:
    """
    This module initilaize a square methond and check if the value is of type int or less than 0 
    """
    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) != int:
            try:
                raise TypeError
            except TypeError as var:
                print("size must be an integer")
        if self.__size<=0:
            try:
                raise ValueError
            except ValueError as var:
                print("size must be >= 0")
    
