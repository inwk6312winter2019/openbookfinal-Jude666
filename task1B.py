#This is the code 

from collections import Counter


def top20_common():
    d = dict()
    f = open('book1.txt','book2.txt','book3.txt')
    c = Counter()
    for line in f:
        words = line.split()
        c += Counter(words)
    for words in c.most_common(20):
        if words not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d
