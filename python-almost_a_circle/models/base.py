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
    # create a class attribute to hold the count
    __nb_objects = 0

    def __init__(self, id:int = None):
        '''
        Funtion instantiation for base clss

            Parameters:
                id: integer, default value = None

            Returns:
                increment self.id if id is none otherwise self id = id
        '''

        # increament count anytime the instance is created
        Base.__nb_objects += 1

        if id != None:
            self.id = id
        else:
           self.id = Base.__nb_objects
