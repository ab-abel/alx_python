class Animal:
    pass

class Goat:
    pass

class Dog(Animal):
    pass

class Fish(Dog):
    pass


print(issubclass(Fish, Goat))