"""
word_embeddings.py
Demonstrates loading word2vec via gensim if available, otherwise creates random embeddings with numpy.
"""
try:
    import gensim
    has_gensim = True
except Exception:
    has_gensim = False

import numpy as np

if __name__ == '__main__':
    words = ['dog','cat','king','queen']
    if has_gensim:
        print('Gensim available — you can load a keyed vectors file like GoogleNews-vectors-negative300.bin')
    else:
        print('Gensim not installed; using random embeddings for demo')
        vecs = {w: np.random.randn(50) for w in words}
        print('dog vec sample:', vecs['dog'][:5])
