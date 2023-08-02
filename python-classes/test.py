class Base():

    __nb_instance = 0

    def __init__(self):
        Base.__nb_instance += 1
        self.id = Base.__nb_instance

class User(Base):
    pass
    def __init__(self):
        super().__init__()
        self.id =89

# for i in range(3):
    # b =Base()
# b = Base()
u = User()

print(u.id)