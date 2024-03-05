def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            # respond to next()
            yield line.rstrip('\n\r')  # 'yield' causes this function to return a generator object

mary_in = trimmed('../DATA/mary.txt')
print(f"{type(mary_in) = }")

first_line = next(mary_in)

for trimmed_line in mary_in:
    print(trimmed_line)
print('-' * 60)

mary_in = trimmed('../DATA/mary.txt')
next(mary_in)
next(mary_in)
next(mary_in)
line = next(mary_in)
print(line)
next(mary_in)



