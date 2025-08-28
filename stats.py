def get_number_of_words(text):
    words = text.split()
    return len(words)


def get_number_of_characters(text):
    dic = {}

    for char in text:
        ch = char.lower()
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1

    return dic


def sort_on(items):
    return items["num"]


def sort_chars(items):
    list = []
    for item in items:
        ch = {
            "char": item,
            "num": items[item]
        }
        list.append(ch)

    list.sort(key=sort_on, reverse=True)

    return list
