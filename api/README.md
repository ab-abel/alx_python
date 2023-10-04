# API
## General
    Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

    One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

    This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

# ALL TASK

## Task 0
###  Gather data from an API
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

    NB: The endpoint for access specific TODO items for an employee with ID = 1 will be https://jsonplaceholder.typicode.com/users/1/todos and the endpoint to get specific employee details will be https://jsonplaceholder.typicode.com/users/1

    Requirements:

    - You must use urllib or requests module
    - The script must accept an integer as a parameter, which is the employee ID
    - The script must display on the standard output the employee TODO list progress in this exact format:
        - First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            - where:
            - EMPLOYEE_NAME: name of the employee
            - NUMBER_OF_DONE_TASKS: number of completed tasks
            - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
        - Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

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

