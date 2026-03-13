import sys
import os

sys.path.append(os.getcwd())

from utils.preprocessing import load_corpus
from models.language_model import LanguageModel
from models.noisy_channel import SpellChecker

tokens = load_corpus("data/corpus.txt")

lm = LanguageModel(tokens)
checker = SpellChecker(lm)

while True:
    word = input("Enter word: ")
    print("Correction:", checker.correct(word))
