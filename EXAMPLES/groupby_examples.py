
from itertools import groupby

with open('../DATA/words.txt') as words_in:  # open file for reading
    # create generator of all words, stripped of the trailing '
    all_words = (w.rstrip() for w in words_in)  

    # create a groupby() object where the key is the first character in the word
    g = groupby(all_words, key=lambda e: e[0])  
    for letter, words in g:
        num_words = len(list(words))
        print(letter, num_words)

    # make a dictionary where the key is the first character, and the value 
    # is the number of words that start with that character; groupby groups 
    # all the words, then len() counts the number of words for that character
#    counts = {letter: len(list(wlist)) for letter, wlist in g}  

# sort the counts dictionary by value (i.e., number of words, not the letter
#  itself) into a list of tuples
# sorted_letters = sorted(counts.items(), key=lambda e: e[1], reverse=True)

# loop over the list of tuples and print the letter and its count
# sum all the individual counts and print the result
# print("Total words counted:", sum(counts.values()))

presidents = []
with open('../DATA/presidents.txt') as pres_in:
    for line in pres_in:
        fields = line.rstrip().split(':')
        presidents.append(fields)

presidents_sorted = sorted(presidents, key=lambda p: p[-1])

print(presidents_sorted[:3])
print()

group_pres = groupby(presidents_sorted, key=lambda p: p[-1])

for party, entries in group_pres:
    print(party, len(list(entries)))
print('-' * 60)

group_pres = groupby(presidents_sorted, key=lambda p: p[-1])
for party, entries in group_pres:
    names = [entry[1] for entry in entries]
    print(party, names)

