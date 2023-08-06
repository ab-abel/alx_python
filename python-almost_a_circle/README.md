# Python - Almost a circle
## General
    -   What is Unit testing and how to implement it in a large project
    -   How to serialize and deserialize a Class
    -   How to write and read a JSON file
    -   What is *args and how to use it
    -   What is **kwargs and how to use it
    -   How to handle named arguments in a function
# ALL TASK

## Task 0
###  Base class
Write the first class Base:

Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

Create a file named models/base.py:

    -   Class Base:
        -   private class attribute __nb_objects = 0
        -   class constructor: def __init__(self, id=None)::
            -   if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
            -   otherwise, increment __nb_objects and assign the new value to the public instance attribute id
This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

## Task 1
### First Rectangle
Write the class Rectangle that inherits from Base:

    -   In the file models/rectangle.py
    -   Class Rectangle inherits from Base
    -   Private instance attributes, each with its own public getter and setter:
        -   __width -> width
        -   __height -> height
        -   __x -> x
        -   __y -> y
    -   Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
        -   Call the super class with id - this super call with use the logic of the __init__ of the Base class
        -   Assign each argument width, height, x and y to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.
## Task 2
###  Only sub class of
    Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

    -   Prototype: def inherits_from(obj, a_class):
    -   You are not allowed to import any module

## Task 3
### Access and update private attribute
Write a class Square that defines a square by: (based on 2-square.py)

    - Private instance attribute: size:
      - property def size(self): to retrieve it
      - property setter def size(self, value): to set it:
        - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
        - if size is less than 0, raise a ValueError exception with the message size must be >= 0
    - Instantiation with optional size: def __init__(self, size=0):
    - Public instance method: def area(self): that returns the current square area
    - You are not allowed to import any module

## Task 4
### Printing a square
Write a class Square that defines a square by: (based on 3-square.py)

    -   Private instance attribute: size:
    -   property def size(self): to retrieve it
        -   property setter def size(self, value): to set it:
            -   size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            -   if size is less than 0, raise a ValueError exception with the message size must be >= 0
    -   Instantiation with optional size: def __init__(self, size=0):
    -   Public instance method: def area(self): that returns the current square area
    -   Public instance method: def my_print(self): that prints in stdout the square with the character #:
        -   if size is equal to 0, print an empty line
    -   You are not allowed to import any module

