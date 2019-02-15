#This is Task1A-1

def break_into_words():

    book = open('book1.txt', 'book2.txt','book3.txt')
    words_list = []
    for line in book:
        for item in line.split():
            item = del_punctuation(item)
            item = item.lower()
            # print(item)
            words_list.append(item)
    return words_list

def create_dict():

    words_list = break_into_words()
    d = {}
    for word in words_list:
        if word not in :
            d[word] = 1
        else:
            d[word] += 1

    return d

def unique_words():
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[vall].append[key]
    return inv

d = create_dict()
print(unique_words(d))


#This is Task1A-2

def break_into_words():

    book = open('book1.txt', 'book2.txt', 'book3.txt')
    words_list = []
    for line in book:
        for item in line.split():
            item = del_punctuation(item)
            item = item.lower()
            # print(item)
            words_list.append(item)
    return words_list


def count_the_article():
   
    words_list = break_into_words()
    dictionary = {}
    for word in words_list:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    count = len(dictionary)
    return count

print(count_the_article())

