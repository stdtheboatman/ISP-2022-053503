import re


def get_sentences(lines):
    sentences = []
    for line in lines:
        sentences += re.split(r'[.?!]', line)

    return sentences


def get_words(sentences):
    words = []
    for sentence in sentences:
        words += sentence.split()

    words = [word.lower() for word in words]
    return list(filter(lambda word: word != '' and word != '\n', words))


def print_words_count(words):
    dict = {}
    for word in words:
        count = dict.get(word, 0)
        dict.update({word: count + 1})

    print("---Word counter---")
    for word in dict:
        print(word, ":", dict[word])


def get_word_counters(sentences):
    counters = []
    for sentence in sentences:
        words = sentence.split()
        words = list(filter(lambda word: word != '' and word != '\n', words))

        counter = len(words)
        if counter > 0:
            counters.append(len(words))

    return counters


def get_average_words_count(counters):
    return round(sum(counters) / len(counters), 3)


def get_median_words_count(counters):
    counters.sort()
    mid = len(counters) // 2
    return counters[mid]


def print_top_ngram(n, topSize, words):
    dict = {}
    for word in words:
        for i in range(len(word) - n + 1):
            subword = word[i:i + n]

            counter = dict.get(subword, 0)
            dict.update({subword: counter + 1})

    top = []
    for ngram in dict:
        top.append([dict[ngram], ngram])

    top.sort(reverse=True)

    top = top[:topSize]
    for ngram in top:
        print(ngram)


# code starts here
lines = []
with open("big_input.txt") as file:
    lines = file.readlines()


sentences = get_sentences(lines)
words = get_words(sentences)

print_words_count(words)

counters = get_word_counters(sentences)

print("---Words counter in sentences---")
print(counters)
print("Average word count in sentence", get_average_words_count(counters))
print("Median word count in sentence", get_median_words_count(counters))

n = 4
k = 10

print(f"---Top: {k} {n}-gram---")
print_top_ngram(n, k, words)
