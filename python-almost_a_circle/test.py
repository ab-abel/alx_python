from models.base import Base

class Rectangle:

    def __init__(self, width, Base):
        self._Rectangle__width = width
    

    @property
    def Rectangle__width(self):
        return self._Rectangle__width
    
    @Rectangle__width.setter
    def Rectangle__width(self, width):
        self._Rectangle__width = width


r = Rectangle(12, 14)
if r is None:
    print("Can't create Rectangle")
    exit(1)

if r._Rectangle__width != 12:
    print("Wrong width: {}".format(r._Rectangle__width))
    exit(1)

print('OK')