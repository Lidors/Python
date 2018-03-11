def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    count = len(word) - 3
    check = False
    for i in range(0, count):
        if count >= 0:
            if word[i] == word[i + 1] == word[i + 2]:
                check = True
    return check


word = 'aa'
word1 = trifeca(word)
print(word1)

word = 'aaabbcc'
word2 = trifeca(word)
print(word2)
