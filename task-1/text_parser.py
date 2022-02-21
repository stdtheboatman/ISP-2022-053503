import re


class TextParser:
    def __init__(self, n, k, input):
        self._n = n
        self._k = k
        self._input = input

    def print_statistics(self):
        lines = []
        with open("data/" + self._input) as file:
            lines = file.readlines()

        sentences = self.get_sentences(lines)
        words = self.get_words(sentences)

        self.print_words_count(words)

        counters = self.get_word_counters(sentences)

        print("---Words counter in sentences---")
        print(counters)
        print("Average word count in sentence",
              self.get_average_words_count(counters))
        print("Median word count in sentence",
              self.get_median_words_count(counters))

        print(f"---Top: {self._k} {self._n}-gram---")
        self.print_top_ngram(self._n, self._k, words)

    def get_sentences(self, lines):
        sentences = []
        for line in lines:
            sentences += re.split(r'[.?!]', line)

        return sentences

    def get_words(self, sentences):
        words = []
        for sentence in sentences:
            words += re.split(r'[ ,\n]', sentence)

        words = [word.lower() for word in words]
        return list(filter(lambda word: word != '', words))

    def print_words_count(self, words):
        dict = {}
        for word in words:
            count = dict.get(word, 0)
            dict.update({word: count + 1})

        print("---Word counter---")
        for word in dict:
            print(word, ":", dict[word])

    def get_word_counters(self, sentences):
        counters = []
        for sentence in sentences:
            words = self.get_words(sentence)

            counter = len(words)
            if counter > 0:
                counters.append(len(words))

        return counters

    def get_average_words_count(self, counters):
        return round(sum(counters) / len(counters), 3)

    def get_median_words_count(self, counters):
        counters.sort()
        mid = len(counters) // 2
        return counters[mid]

    def print_top_ngram(self, n, top_size, words):
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

        top = top[:top_size]
        for ngram in top:
            print(ngram)
