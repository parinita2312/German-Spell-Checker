import re
def load_corpus(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().lower()
    text = re.sub(r"[^a-zäöüß\s]", "", text)
    tokens = text.split()
    return tokens
