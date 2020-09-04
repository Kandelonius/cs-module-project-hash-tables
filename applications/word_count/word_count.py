punc = '''!()-[]{};:"\, <>./?@#$%^&*_~'''

def word_count(s):
    words = {}
    if s == "":
        return words
    if s == '":;,.-+=/\\|[]{}()*^&':
        return words
    text = s.lower().strip().split(" ")
    for word in text:
        word = word.strip('":;,.-+=/\\|[]{}()*^&')
        # for l in word:
        #     if l in punc:
        #         word = word.replace(l, "")
        if word == "":
            continue
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    return words


if __name__ == "__main__":
    print(word_count("Hello    hello"))
    print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))