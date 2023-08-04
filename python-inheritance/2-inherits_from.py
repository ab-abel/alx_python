"""
#!/usr/bin/python3
Ths Module is issubclass methotd takes the obj type vairable, and a_class method.
"""


def is_kind_of_class(obj, a_class):
    """
    Function to check if a data is a subclass of the other.
    This function takes two numbers, 'obj' and 'a_class', and returns their sum.

    Parameters:
    obj (int, float, boolean, string, list): The first number.
    a_class (could be any class or object): The second number.

    Returns:
    True: The output if the result of the subclass check is  true
    False: If the result of the subclass is false
    """
    #   class conditional statment
    if issubclass(type(obj), a_class): 
        """
        Conditional statements
        """
        return True
        """
        Conditional statements
        """
    else:
        """
        Conditional statements
        """
        return False
