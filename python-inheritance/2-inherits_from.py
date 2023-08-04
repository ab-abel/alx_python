'''
#!/usr/bin/python3
Ths Module is issubclass methotd takes the obj type vairable, and a_class method.
'''


def is_kind_of_class(obj, a_class):
    '''
    Function to check if a data is a subclass of the other.
    This function takes two numbers, 'obj' and 'a_class', and returns their sum.

        Parameters:
            obj (field): The first number.
            a_class (object): The second number.

        Returns:
            bool (True and False): from the the comparison of obj and  a_class

    '''
    if issubclass(type(obj), a_class): 
        return True
    else:
        return False

print(__doc__)