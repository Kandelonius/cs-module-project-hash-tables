
filter = {}
new = []

def no_dups(s):
    string = s.split(" ")
    for l in string:
        if l not in filter:
            filter[l] = 1
            new.append(l)
        else:
            continue
    new_string = " ".join(new)
    return new_string.strip()

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))