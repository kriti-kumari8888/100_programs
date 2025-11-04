"""
topic_modeling.py
Topic modeling demo: tries gensim LDA if available, otherwise a very small sklearn NMF example or fallback.
"""
try:
    import gensim
    from gensim.corpora.dictionary import Dictionary
    from gensim.models.ldamodel import LdaModel
    has_gensim = True
except Exception:
    has_gensim = False

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import NMF
    has_sklearn = True
except Exception:
    has_sklearn = False

if __name__ == '__main__':
    docs = [
        'cats dogs pets',
        'dogs bark and run',
        'cats purr and sleep',
        'cars drive on road',
        'trucks and cars transport goods'
    ]
    if has_gensim:
        toks = [d.split() for d in docs]
        dic = Dictionary(toks)
        corp = [dic.doc2bow(t) for t in toks]
        lda = LdaModel(corp, num_topics=2, id2word=dic, random_state=0)
        for i, t in lda.print_topics():
            print(i, t)
    elif has_sklearn:
        tf = TfidfVectorizer(max_features=50)
        X = tf.fit_transform(docs)
        nmf = NMF(n_components=2, random_state=0)
        W = nmf.fit_transform(X)
        H = nmf.components_
        print('Top words per topic:')
        terms = tf.get_feature_names_out()
        for topic_idx, comp in enumerate(H):
            top = comp.argsort()[-5:][::-1]
            print([terms[i] for i in top])
    else:
        print('No topic-modeling libraries found. Install gensim or scikit-learn to run examples.')
