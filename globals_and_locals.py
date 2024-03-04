from pprint import pprint

print(f"{__name__ = }")
print(f"{__file__ = }")


x = 5
print(x)

if x > 3:
    r = "rutabaga"

def bark():
    m = "mango"   # local name 'm'
    print('woof! woof!')
    print(f"{locals() = }")
    

class Person:
    pass


g = globals()

pprint(g)
print('-' * 60)

print(f"{g['r'] = }")
print(f"{r = }")

g['color'] = 'blue'

print(f"{color = }")

g['bark']()
print('-' * 60)

print(g.keys())

print(locals().keys())



