'''
This is a module that implement the base required 
for other class in python.
'''

class Base:
    '''
    A bass class for python just a circle.
    the goal of the base class will be to manage
    your id in all your projects.
    '''
    def __init__(self, id:int = None):
        '''
        Funtion instantiation for base clss

            Parameters:
                id: integer, default value = None

            Returns:
                increment self.id if id is none otherwise self id = id
        '''
        self.__nb_objects = 0
        self.id = id if id != None else self.__nb_objects + 1