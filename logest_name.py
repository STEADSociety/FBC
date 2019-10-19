words = ["hello", "world", "hi", "bye"]


def longest_word(data):

    max_len = len(max(data, key=len))
    return [word for word in data if len(word) == max_len]


print(longest_word(words))