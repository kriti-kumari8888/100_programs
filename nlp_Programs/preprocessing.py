"""
preprocessing.py
Common text preprocessing helpers: lowercasing, remove punctuation, optional stopword removal with NLTK.
"""
import re

try:
    import nltk
    from nltk.corpus import stopwords
    nltk.data.find('corpora/stopwords')
    has_nltk_sw = True
except Exception:
    has_nltk_sw = False

def simple_normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def remove_stopwords(tokens: list[str]) -> list[str]:
    if has_nltk_sw:
        sw = set(stopwords.words('english'))
        return [t for t in tokens if t not in sw]
    else:
        # tiny fallback
        common = {'the','is','a','an','and','of','in'}
        return [t for t in tokens if t not in common]

if __name__ == '__main__':
    s = "This is an example, showing preprocessing of text!"
    norm = simple_normalize(s)
    toks = norm.split()
    print('Normalized:', norm)
    print('After stopword removal:', remove_stopwords(toks))
