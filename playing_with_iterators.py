
fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

# two different iterables
f_list = [f.upper() for f in fruits] # iterable, container (NOT directly an iterator)
f_gen = (f.upper() for f in fruits)  # iterable, iterator

print(f"{type(f_list) = }")
print(f"{type(f_gen) = }")
print()

print(f"{f_list[5] = }")

print(f"{next(f_gen) = }")
print(f"{next(f_gen) = }")

# print(f"{next(f_list) = }")
f_list_iterator = iter(f_list)  # iter(x) returns the iterator of iterable x
print(f"{type(f_list_iterator) = }")

print(f"{next(f_list_iterator) = }")
print(f"{next(f_list_iterator) = }")

with open('DATA/presidents.txt') as pres_in:
    first_line = next(pres_in)

    for raw_line in pres_in:
        line = raw_line.rstrip() # remove \n
        print(line)
print('-' * 60)





