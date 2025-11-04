"""
hyperparam_search.py
Tiny grid search example for hyperparameters. No heavy libs required.
"""
import itertools

def train_with(hparams):
    # Dummy objective: pretend lower lr and larger hidden are better
    score = 1.0 / (hparams['lr'] * 1000.0) + hparams['hidden'] * 0.01
    return score

if __name__ == '__main__':
    lrs = [1e-1, 1e-2, 1e-3]
    hiddens = [16, 32, 64]
    best = None
    for lr, h in itertools.product(lrs, hiddens):
        hparams = {'lr': lr, 'hidden': h}
        s = train_with(hparams)
        print(f"lr={lr} hidden={h} -> score={s:.4f}")
        if best is None or s > best[0]:
            best = (s, hparams)
    print('Best:', best)
