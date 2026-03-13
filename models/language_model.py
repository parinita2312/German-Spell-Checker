from collections import Counter, defaultdict
class LanguageModel:
    def __init__(self, tokens):

        self.unigrams = Counter(tokens)

        self.bigrams = Counter(zip(tokens[:-1], tokens[1:]))

        self.trigrams = Counter(zip(tokens[:-2], tokens[1:-1], tokens[2:]))

        self.total = sum(self.unigrams.values())

    def unigram_prob(self, word):
        return self.unigrams[word] / self.total

    def bigram_prob(self, w1, w2):
        return (self.bigrams[(w1, w2)] + 1) / (self.unigrams[w1] + len(self.unigrams))

    def trigram_prob(self, w1, w2, w3):
        return (self.trigrams[(w1, w2, w3)] + 1) / (self.bigrams[(w1, w2)] + len(self.unigrams))
