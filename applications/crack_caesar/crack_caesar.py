# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

f = open('ciphertext.txt')
# print(f.read())
text = f.read()
f.close()

total = 0
d = {}
def letter_count(text):
    global total
    # for line in text:
        # print(f"{line} is line")
    for c in text:
        # print(f"{c} is c")
        if (c >= 'A' and c <= 'Z'):
            c = c.upper()

            if c not in d:
                #d[c] = 0
                d[c] = 1
            else:
                d[c] += 1
            total += 1
    # return d
letter_count(text) # calling letter_count to fill dict d
# print(d.get('L'))
cracked = ""
# take the numbers in d and divide them by the total * 100 to 2 significant digits to get their percentages.
for l in text:
    if (l >= 'A' and l <= 'Z'):
        num = int(d.get(l))
        percentage = round((num / total) * 100, 2)
        if percentage == 11.53:
            cracked += "E"
        if percentage == 9.75:
            cracked += "T"
        if percentage == 8.46:
            cracked += "A"
        if percentage == 8.08:
            cracked += "O"
        if percentage == 7.71:
            cracked += "H"
        if percentage == 6.73:
            cracked += "N"
        if percentage == 6.29:
            cracked += "R"
        if percentage == 5.84:
            cracked += "I"
        if percentage == 5.56:
            cracked += "S"
        if percentage == 4.74:
            cracked += "D"
        if percentage == 3.92:
            cracked += "L"
        if percentage == 3.08:
            cracked += "W"
        if percentage == 2.59:
            cracked += "U"
        if percentage == 2.48:
            cracked += "G"
        if percentage == 2.42:
            cracked += "F"
        if percentage == 2.19:
            cracked += "B"
        if percentage == 2.18:
            cracked += "M"
        if percentage == 2.02:
            cracked += "Y"
        if percentage == 1.58:
            cracked += "C"
        if percentage == 1.08:
            cracked += "P"
        if percentage == 0.84:
            cracked += "K"
        if percentage == 0.59:
            cracked += "V"
        if percentage == .17:
            cracked += "Q"
        if percentage == .07:
            if l == "T":
                cracked += "J"
            elif l == "L":
                cracked += "X"
        if percentage == .03:
            cracked += "Z"
    else:
        cracked += l



print(cracked)


