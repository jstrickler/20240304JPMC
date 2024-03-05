import sys

class Spam:
    COLOR = "blue"  # class variable

    def __init__(self):
        self.animal = 'penguin'
        self.foo = 1000

    def hello(self):
        x = 5  # local variable
        print("hello from Spam")

    def foo(self):
        print("foo foo foo")

print(Spam.foo)

s = Spam()
print(f"{s.COLOR = }")
print(f"{Spam.COLOR = }")

attr_name = "COLOR"

# print(f"{s.attr_name = }")
print(f"{getattr(s, attr_name) = }")

print(f"{getattr(sys, 'executable') = }")

m = getattr(s, 'hello')
m()

print(f"{hasattr(Spam, 'hello') = }")

class Ham:
    def hello(self):
        print("Hello from Ham")

class Toast:
    def hi(self):
        print("Hi from Toast")

h = Ham()
t = Toast()

things = [s, h, t]

for thing in things:
    if hasattr(thing, 'hello'):
        thing.hello()

f = getattr(s, "hello")
print(dir(f))
print(f.__name__)

def goodbye(self):
    print("see you later")

setattr(Spam, 'bye', goodbye)

s.bye()

setattr(Spam, 'FOO', 'BAR')
print(f"{Spam.FOO = }")

def blech(cls):
    print("Hello from blech()")

setattr(Spam, 'blech', classmethod(blech))

s.blech()
Spam.blech()

delattr(Spam, 'hello')

# s.hello()

print(f"{type(s) = }")

print(s.animal)
print(f"{getattr(s, 'animal') = }")
print('-' * 60)
print(dir(Spam))
print('-' * 60)
print(dir(s))

print(s.foo)