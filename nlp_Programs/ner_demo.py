"""
ner_demo.py
NER demo: tries spaCy's NER if available; otherwise prints usage notes.
"""
try:
    import spacy
    nlp = spacy.load('en_core_web_sm')
    has_spacy = True
except Exception:
    has_spacy = False

if __name__ == '__main__':
    text = "Apple is looking at buying U.K. startup for $1 billion"
    if has_spacy:
        doc = nlp(text)
        print([(ent.text, ent.label_) for ent in doc.ents])
    else:
        print('spaCy not available. To run NER: pip install spacy && python -m spacy download en_core_web_sm')
