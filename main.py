import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.preprocessing import load_corpus
from models.language_model import LanguageModel
from models.noisy_channel import SpellChecker

tokens = load_corpus("data/corpus.txt")

lm = LanguageModel(tokens)
checker = SpellChecker(lm)

while True:
    word = input("Enter word: ")
    print("Correction:", checker.correct(word))
    
