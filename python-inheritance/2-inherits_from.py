'''
#!/usr/bin/python3
Ths Module is issubclass method takes the obj type vairable,
and a_class method.
'''


def inherits_from(obj, a_class):
    '''
    Function to check if a data is a subclass of the other.
    This function takes two numbers, 'obj' and 'a_class',
    and returns a bool if it was inherited from it class.

        Parameters:
            obj (field): The first number.
            a_class (object): The second number.

        Returns:
            bool (True and False): from the the comparison of
            obj and a_class

    '''
    if isinstance(type(obj),  a_class):
        return True
    else:
        return False

# a = 1
# print(inherits_from(a, int)) #False
# a = [1, 2, 3]
# print(inherits_from(a, list)) #False