"""
pos_tagging.py
POS tagging: tries spaCy, then NLTK, otherwise a tiny rule-based tagger.
"""
try:
    import spacy
    nlp = spacy.load('en_core_web_sm')
    has_spacy = True
except Exception:
    has_spacy = False

try:
    import nltk
    from nltk import pos_tag, word_tokenize
    nltk.data.find('tokenizers/punkt')
    has_nltk = True
except Exception:
    has_nltk = False

def rule_based_tag(tokens):
    out = []
    for t in tokens:
        if t.lower() in ('a','the','an'):
            out.append((t,'DET'))
        elif t.endswith('ing'):
            out.append((t,'VBG'))
        elif t[0].isupper():
            out.append((t,'NNP'))
        else:
            out.append((t,'NN'))
    return out

if __name__ == '__main__':
    text = "The quick brown fox is jumping over the lazy dog"
    if has_spacy:
        doc = nlp(text)
        print([(t.text, t.pos_) for t in doc])
    elif has_nltk:
        toks = word_tokenize(text)
        print(pos_tag(toks))
    else:
        toks = text.split()
        print(rule_based_tag(toks))
