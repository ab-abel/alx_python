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
        self.size = size
        super().__init__(width=size,height=size, x=x,y=y, id=id)
        
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return Rectangle.width

    @size.setter
    def size(self, size):
        Rectangle.validation(self,'size', size)
        Rectangle.width = size
        Rectangle.height = size

s = Square(12)
if s is None:
    print("Can't create Square")
    exit(1)

for attribute in list(s.__dict__.keys()):
    if "size" in attribute:
        print("You are not allowed to add any new attribute for size: {}".format(attribute))
        exit(1)

if s.size != 12:
    print("Wrong size getter: {}".format(s.size))
    exit(1)

s.size = 5

if s.size != 5:
    print("Wrong size getter: {}".format(s.size))
    exit(1)

print("OK", end="")