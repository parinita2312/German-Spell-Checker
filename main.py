import sys
import os

sys.path.append(os.getcwd())

from preprocessing import load_corpus
from language_model import LanguageModel
from noisy_channel import SpellChecker

tokens = load_corpus("corpus.txt")

lm = LanguageModel(tokens)
checker = SpellChecker(lm)

while True:
    word = input("Enter word: ")
    print("Correction:", checker.correct(word))
