from models.error_model import emission_prob
class SpellChecker:
    def __init__(self, language_model):
        self.lm = language_model
        self.vocab = list(language_model.unigrams.keys())

    def candidates(self, typo):
        return [word for word in self.vocab
            if abs(len(word) - len(typo)) <= 2]

    def correct(self, typo):
        best_word = typo
        best_prob = 0
        for word in self.candidates(typo):
            p_error = emission_prob(typo, word)
            p_lang = self.lm.unigram_prob(word)
            score = p_error * p_lang
            if score > best_prob:
                best_prob = score
                best_word = word
        return best_word
