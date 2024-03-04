import operator as OP

def bark(bark_type):
    print(f"{bark_type}! {bark_type}!")

def doit(f, arg):
    f(arg)

doit(bark, 'woof')
doit(bark, "yip")

doit(lambda x: print(x.upper()), 'abc')



fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f1  = sorted(fruits, key=len)
print(f"{f1 = }")

print(f"{min(fruits) = }")
print(f"{min(fruits, key=len) = }")

f2 = sorted(fruits, key=lambda f: f[-1])
print(f"{f2 = }")

def calc(op, v1, v2):
    if op == '+':
        return OP.add(v1, v2)

print(f"{calc('+', 3, 4) = }")

#  str.upper(s)   str.lower(s)   etc etc 

f3 = map(str.title, fruits)
print(f"{list(f3) = }\n")

f3 = [f.upper() for f in fruits]  # get a list
print(f"{f3 = }\n")

f3gen = (f.upper() for f in fruits)  # get a generator
print(f"{f3gen = }")
print(f"{list(f3gen) = }\n")

print(f"{fruits = }\n")

from itertools import islice, chain

ftitle = (f.title() for f in fruits)
print(f"{ftitle = }\n")

# print(f"{ftitle[:4] = }")

sliced = islice(ftitle, 0, 4)
print(f"{list(sliced) = }")

a = ['alpha', 'beta', 'gamma']
b = 'delta', 'epsilon', 'eta'
c = {'mu', 'nu', 'rho'}

for value in chain(a, b, c):
    print(value)












