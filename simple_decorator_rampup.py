from functools import wraps
from datetime import datetime

def print_timestamp(original_function):

    @wraps(original_function)
    def replacement(*args, **kwargs):
        print(datetime.now().ctime())
        return_value = original_function(*args, **kwargs)
        return return_value
    
    return replacement

def ham(x):
    print("ham!")

r = print_timestamp(ham)  # same as @spam....
print(f"{r = }")

ham = print_timestamp(ham)
print(f"{ham = }")

ham("mango")

@print_timestamp
def soup(a, b):
    print("Soupy Soup")

# soup = spam(soup)

soup("foo", "bar")

def add_squeak(original_class):
    setattr(original_class, 'squeak', lambda self: print("SQUEAK! SQUEAK!"))
    return original_class

class Animal:
    pass

class SwimMixin:
    def swim(self):
        print("Look Mom, I'm swimming!")

@add_squeak
class Penguin(SwimMixin, Animal):
    pass

#  Penguin = add_squeak(Penguin)


p = Penguin()
p.squeak()
p.swim()


# @deco(1, 2, 3)
# def bosh():
#     pass

# bosh = deco(1, 2, 3)(bosh)