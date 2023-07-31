# PYTHON Class
    Understanding python "class everything is a class"
# ALL TASK

## Task 0
###  square with size
    Write a class Square that defines a square by:
    -   Private instance attribute: size
    -   Instantiation with size (no type/value verification)
    -   You are not allowed to import any module

## Task 1
### Size validation
Write a class Square that defines a square by: (based on 0-square.py)

    -   Private instance attribute: size
    -   Instantiation with optional size: def __init__(self, size=0):
        -   size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
        -   if size is less than 0, raise a ValueError exception with the message size must be >= 0
    -   You are not allowed to import any module
## Task 2
###  Area of a square
    Write a class Square that defines a square by: (based on 1-square.py)

    -   Private instance attribute: size
    -   Instantiation with optional size: def __init__(self, size=0):
        -   size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
        -   if size is less than 0, raise a ValueError exception with the message size must be >= 0
    -   Public instance method: def area(self): that returns the current square area
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
### Multiply by using map
    - Prototype: def multiply_list_map(my_list=[], number=0):
    - Returns a new list:
        - Same length as my_list
        - Each value should be multiplied by number
    - Initial list should not be modified
    - You are not allowed to import any module
    - You have to use map
    - Your file should be max 3 lines
