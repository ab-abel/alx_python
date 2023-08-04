"""
#!/usr/bin/python3
Ths Module is issubclass methotd takes the obj type vairable, and a_class method.
"""


def is_kind_of_class(obj, a_class):
    """
    Function to check if a data is a subclass of the other.
    This function takes two numbers, 'a' and 'b', and returns their sum.

    Parameters:
    obj (int, float, boolean, string, list): The first number.
    a_class (could be any class or object): The second number.

    Returns:
    True or false: The output is a boolean of the comparison of the 
    the two input variable.
    """
    #class conditional statment
    if issubclass(type(obj), a_class): 
        #return param
        return True
        #coditional state][ment
    else:
        #conditional statement
        return False
