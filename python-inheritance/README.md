# PYTHON Inheritance 
    Understanding python classes and subclass
# ALL TASK

## Task 0
###  Exact same object
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

    - Prototype: def is_same_class(obj, a_class):
    - You are not allowed to import any module

## Task 1
### Same class or inherit from
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

    - Prototype: def is_kind_of_class(obj, a_class):
    - You are not allowed to import any module
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

