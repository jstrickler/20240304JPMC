

class Animal:
    pass


Dog = type('Dog', (Animal,), {'bark': lambda self: print("woof!")})

d = Dog()
d.bark()

