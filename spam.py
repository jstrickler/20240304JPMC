
class Groot:
    def __str__(self):  # human-friendly
        return "I am Groot!"
    
    def __repr__(self):  # how to create object
        return "Groot()"

    def __len__(self):
        return 42
    
    def __add__(self, other):
        # check to see if 'other' is a Groot
        return [self, other]
    
    def __getitem__(self, item):
        if isinstance(item, str):
            return item.upper()
        else:
            raise ValueError("item must be a string!")
        
g = Groot()
print(f"{type(g) = }")
print(f"{g = }")  # calls repr() not str()

print(f"{g['apple'] = }")
# print(f"{g[4.9] = }")


print(g)

print(f"{len(g) = }")

result = g + g
print(result)

print(f"{g['apple'] = }")
