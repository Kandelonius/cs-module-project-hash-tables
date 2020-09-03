"""
Items: .items() method on a dictionary might be useful.
Sorting: it's possible for .sort() to sort on multiple keys at once.
Sorting: negatives might help where reverse won't.
Printing: you can print a variable field width in an f-string with nested braces, like so {x:{y}}
"""

f = open('robin.txt')
# print(f.read())
text = f.read().split(' ')
f.close()

histo = {}
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

# for word in text:
#     # print(word)
#     for l in word:
#         if l in punc:
#             print(f"letter is {l} word is {word}")
#             word = word.replace(l, "")
#             print(f"word is {word}")

for word in text:
    # print(word[0])
    if (word[0] >= 'a' and word[0] <= 'z'):
        for l in word:
            if l in punc:
                # print(f"letter is {l} word is {word}")
                word = word.replace(l, "")
                # print(f"word is {word}")
        if word not in histo:
            histo[word] = ''
        histo[word] += '#'

# histo.sort()
h = list(histo.items())
h.sort(key=lambda w: w[1])
print(h)
