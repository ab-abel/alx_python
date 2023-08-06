'''
    This is the first Rectangle that 
    inherits from Base Module
'''
from models.base import Base


class Rectangle(Base):
    '''
    Definition:
        A class defition for Rectangle that takes private param,
        and initiialize using a constructior
    Inheritance:
        inherit from Base class.
    '''


    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Class construtuctor for the clas rectangle

        Parameters:
            width:
            height:
            x:  default = 0
            y:  default = 0
            id: default = None, inherited from Base class
        Return:
            The return param will be 

        '''
        self.__width    = self.width(width)
        self.__height   = self.height(height)
        self.__x        = self.x(x)
        self.__y        = self.y(y)
        self.id = super().id
    
    #   @property decorator. This method allows us to 
    #   access the private attribute as if it 
    #   were a regular attribute, using obj.private_attribute
    @property
    def width(self):
        '''
        Return:
            return the width param from the private property
        '''
        return self.__width
    
    #    This method allows us to set the private attribute's 
    #    value with validation or additional logi
    @width.setter
    def width(self, width):
        '''
        Return:
           Set the width private property attributes field.
        '''
        self.__width = width

    @property
    def height(self):
        '''
        Return:
            return the height param from the private property
        '''
        return self.__height
    
    @height.setter
    def height(self, height):
        '''
        Return:
           Set the height private property attributes field.
        '''
        self.__height = height


    @property
    def x(self):
        '''
        Return:
            return the x param from the private property
        '''
        return self.__x
    
    @x.setter
    def x(self, x):
        '''
        Return:
           Set the x private property attributes field.
        '''
        self.__x = x

    @property
    def y(self):
        '''
        Return:
            return the x param from the private property
        '''
        return self.__y
    
    @y.setter
    def y(self, y):
        '''
        Return:
           Set the y private property attributes field.
        '''
        self.__y = y
