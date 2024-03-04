from collections import Counter

with open('DATA/breakfast.txt') as breakfast_in:
    all_food = breakfast_in.read()
    items = all_food.splitlines()
    # print(items[:10])

food_count = Counter(items)
food_count['pizza'] += 1

print(food_count)

print(food_count['dosas'])