from itertools import product, combinations, permutations

a = 1, 2, 3
b = 'red', 'blue', 'green'

print(f"{list(product(a, b)) = }\n")

print(f"{list(combinations(b, 2)) = }\n")

print(f"{list(permutations(b)) = }\n")
