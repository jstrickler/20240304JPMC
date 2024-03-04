from copy import deepcopy

x = 5
y = x
print(x, y)
x = 10
print(x, y)
y = 15
print(x, y)

mylist = ['a', 'b', 'c']
m1 = mylist
m1.append('d')
print(mylist, m1)

m2 = list(mylist)   # or m2 = mylist[:]
m2.append('e')
print(mylist, m1, m2)
print(id(mylist), id(m1), id(m2))
print(mylist is m1)  # id(mylist) == id(m1)
print(mylist is m2)

# x = None
# ...
# if x is None:

my_nested_list = [[1, 2], [3, 4], [5, 6]]
mn1 = list(my_nested_list)
mn1.append([7,8])
print(my_nested_list)
print(mn1, '\n')
print(my_nested_list is mn1)
mn1[0].append('what the heck?')
print(my_nested_list)
print(mn1)

mn2 = deepcopy(my_nested_list)
mn2[0].append('only the deep copy')
print(mn1)
print(mn2)

x = 5
# y = deepcopy(x)
y = x
print(x)
print(y)

# immutable: str int float tuple bool   (no deepcopy needed)
# mutable: list dict set (deepcopy needed)

x = 6
print(x, y)

name = "John"
n2 = deepcopy(name)
print(name is n2)

a = "abc"
b = "abc"
print(a is b)
