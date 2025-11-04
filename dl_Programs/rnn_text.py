"""
rnn_text.py
Tiny RNN/LSTM skeleton for character-level modelling. Falls back to a no-deps demo.
"""
try:
    import torch
    import torch.nn as nn
    has_torch = True
except Exception:
    has_torch = False

if has_torch:
    class TinyRNN(nn.Module):
        def __init__(self, input_size=16, hidden=32, out=16):
            super().__init__()
            self.rnn = nn.LSTM(input_size, hidden, batch_first=True)
            self.fc = nn.Linear(hidden, out)
        def forward(self,x):
            o,_ = self.rnn(x)
            return self.fc(o[:, -1])

    if __name__ == '__main__':
        print('Running TinyRNN forward with PyTorch')
        m = TinyRNN()
        x = torch.randn(4, 10, 16)
        print('out shape', m(x).shape)
else:
    if __name__ == '__main__':
        print('PyTorch not installed — RNN demo requires torch. Showing a simple sequence summary using numpy')
        import numpy as np
        seq = np.random.randn(5, 10, 8)
        print('Sequence mean over time axis', seq.mean(axis=1).shape)
