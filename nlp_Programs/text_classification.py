"""
text_classification.py
A tiny scikit-learn text classification pipeline (TF-IDF + LogisticRegression) if scikit-learn is present.
Falls back to a simple keyword-rule classifier.
"""
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import make_pipeline
    has_sklearn = True
except Exception:
    has_sklearn = False

if __name__ == '__main__':
    docs = ['I love this product', 'This is terrible', 'Absolutely great', 'Not good']
    labels = [1,0,1,0]
    if has_sklearn:
        model = make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=400))
        model.fit(docs, labels)
        print('Preds:', model.predict(['I love it', 'worst ever']))
    else:
        print('scikit-learn not installed — running a keyword rule classifier')
        def rule(doc):
            if any(w in doc.lower() for w in ('love','great','excellent')): return 1
            return 0
        print([rule(d) for d in ['I love it','Worst ever']])
