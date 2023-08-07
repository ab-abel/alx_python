'''
    This is the first Rectangle that 
    inherits from Base Module
'''
from models.base import Base
# from base import Base

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
            width: supplied at instatiation
            height: supplied at instatiation
            x:  default = 0
            y:  default = 0
            id: default = None, inherited from Base class
        Return:
            The return param will be

        '''
        # validate each param
        self.validation('width', width)
        self.validation('height',height)
        self.validation('x',x)
        self.validation('y',y)

        # set each param after validation
        self._Rectangle__width = width
        self._Rectangle__height = height
        self._Rectangle__x = x
        self._Rectangle__y = y
        super().__init__(id)

    #   @property decorator. This method allows us to
    #   access the private attribute as if it
    #   were a regular attribute, using obj.private_attribute
    @property
    def Rectangle__width(self):
        '''
        Return:
            return the width param from the private property
        '''
        return self._Rectangle__width

    #    This method allows us to set the private attribute's
    #    value with validation or additional logic
    @Rectangle__width.setter
    def Rectangle__width(self, width):
        '''
        Return:
           Set the width private property attributes field.
        '''
        self._Rectangle__width = self.validation('width', width)

    @property
    def width(self):
        '''
        Return:
            return the width param from the private property
        '''
        return self._Rectangle__width
    
    @width.setter
    def width(self, width):
        '''
        Return:
           Set the width private property attributes field.
        '''
        self._Rectangle__width = self.validation('width', width)


    @property
    def Rectangle__height(self):
        '''
        Return:
            return the height param from the private property
        '''
        return self._Rectangle__height

    @Rectangle__height.setter
    def Rectangle__height(self, height):
        '''
        Return:
           Set the height private property attributes field.
        '''
        self._Rectangle__height = self.validation('height', height)

    @property
    def height(self):
        '''
        Return:
            return the height param from the private property
        '''
        return self._Rectangle__height
    
    @height.setter
    def height(self, height):
        '''
        Return:
           Set the height private property attributes field.
        '''
        self._Rectangle__height = self.validation('height', height)

    @property
    def Rectangle__x(self):
        '''
        Return:
            return the x param from the private property
        '''
        return self._Rectangle__x

    @Rectangle__x.setter
    def Rectangle__x(self, x):
        '''
        Return:
           Set the x private property attributes field.
        '''
        self._Rectangle__x = self.validation('x', x)

    @property
    def x(self):
        '''
        Return:
            return the x param from the private property
        '''
        return self._Rectangle__x
    
    @x.setter
    def x(self, x):
        '''
        Return:
           Set the x private property attributes field.
        '''
        self._Rectangle__x = self.validation('x', x)

    @property
    def Rectangle__y(self):
        '''
        Return:
            return the x param from the private property
        '''
        return self.__y

    @Rectangle__y.setter
    def Rectangle__y(self, y):
        '''
        Return:
           Set the y private property attributes field.
        '''
        self._Rectangle__y = self.validation('y', y)

    @property
    def y(self):
        '''
        Return:
            return the y param from the private property
        '''
        return self._Rectangle__y
    
    @y.setter
    def y(self, y):
        '''
        Return:
           Set the y private property attributes field.
        '''
        self._Rectangle__y = self.validation('y', y)

    def validation(self, name:str, param:int):
        '''
        Validation method 

        Parameters:
            Name: str name of param to be vailidated. example x
            Param: int, the value to be valitade must be int at
            all time
        Return:
            exception: Typeerror, ValueError or Pass if test is 
            successful
        '''
        if(type(param) != int):
            raise TypeError("{} must be an integer".format(name))
        elif(type(name) != str):
            raise ValueError("{} name must be a str".format(name))
        elif(name not in ['x','y']):
            if(param <= 0):
                raise ValueError("{} must be > 0".format(name))
        elif(name == 'x' or name == 'y'):
            if(param < 0):
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        '''
        THis method return the area of the the rectangle
        PArameters:
            self
        Return:
            the prpduct of height and width
        '''
        return self._Rectangle__height * self._Rectangle__width

    def display(self):
        '''
        This function return a square matrix of # for anyinput of x and y

        Paramter:
            self:
        Return:
            square matrix of #
        '''
        x = self._Rectangle__width
        y = self._Rectangle__height

        # print a square matrix from x and y
        for i in range(0, y):
            for j in range(0, x-1):
                print("#", end="")
            print("#")
