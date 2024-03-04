from collections import namedtuple

person = ("Frank", "Smith", 'OH')

print(person[2], person[-1])

Person = namedtuple('Person', "first_name last_name state")

p1 = Person("Frank", "Smith", "OH")
print(p1)
print(p1.first_name, p1.last_name)
print(p1[0], p1[1])

print(type(p1))

pd = {'first_name': 'Frank', 'last_name': 'Smith', 'state': 'OH'}
print(pd['first_name'])

pd['stat'] = 'TX'


list_a = [1, 2, 3, 4]
list_b = [1, (2, 3), 4]

#  immutable: str tuple 



print(p1, type(p1), id(p1))
p2 = p1

p3 = Person(*p1)
print(p1 is p2)
print(p1 is p3)
