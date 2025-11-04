"""
data_loader.py
Small utilities for synthetic data generation and a simple Dataset-like iterator.
This script has no heavy dependencies and can run as-is.
"""
from typing import Iterator, Tuple
import numpy as np

def synthetic_classification(n_samples=100, n_features=8, n_classes=2):
    X = np.random.randn(n_samples, n_features)
    y = np.random.randint(0, n_classes, size=(n_samples,))
    return X, y

class SimpleLoader:
    def __init__(self, X, y, batch_size=16):
        self.X = X; self.y = y; self.bs = batch_size
        self.i = 0
    def __iter__(self) -> Iterator[Tuple]:
        self.i = 0
        return self
    def __next__(self):
        if self.i >= len(self.X):
            raise StopIteration
        b = slice(self.i, min(self.i+self.bs, len(self.X)))
        self.i += self.bs
        return self.X[b], self.y[b]

if __name__ == '__main__':
    X,y = synthetic_classification(50, 6, 3)
    loader = SimpleLoader(X,y, batch_size=10)
    for xb, yb in loader:
        print('batch', xb.shape, yb.shape)
