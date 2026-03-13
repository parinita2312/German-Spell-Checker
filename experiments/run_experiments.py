from utils.preprocessing import load_corpus
from models.language_model import LanguageModel
from models.noisy_channel import SpellChecker
import time
tokens = load_corpus("data/corpus.txt")
lm = LanguageModel(tokens)
checker = SpellChecker(lm)

test = [("hause","haus"),("arbei","arbeit"),("technolgie","technologie"),("schuel","schule")]
tp = 0
fp = 0
fn = 0

start = time.time()
for typo,correct in test:
    pred = checker.correct(typo)
    if pred == correct:
        tp += 1
    else:
        fp += 1
        fn += 1
end = time.time()

print("Precision:",tp/(tp+fp))
print("Recall:",tp/(tp+fn))
print("F1:",2*(tp/(tp+fp))*(tp/(tp+fn))/((tp/(tp+fp))+(tp/(tp+fn))))
print("Time:",end-start)
