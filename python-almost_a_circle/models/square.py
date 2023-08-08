'''
This class implement the square method based and also inherit from the 
Rectanngle class we previously built
'''

# from rectangle import Rectangle
from models.rectangle import Rectangle
# 

class Square(Rectangle):
    '''
    this is a class that inherit from the rectangle class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        instantation of the square class
        '''
        super().__init__(width=size,height=size, x=x,y=y, id=id)
        
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
