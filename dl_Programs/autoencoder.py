"""
autoencoder.py
Autoencoder training skeleton. Falls back to numpy demonstration if torch missing.
"""
try:
    import torch
    import torch.nn as nn
    has_torch = True
except Exception:
    has_torch = False

if has_torch:
    class AE(nn.Module):
        def __init__(self):
            super().__init__(); self.enc = nn.Sequential(nn.Flatten(), nn.Linear(28*28,32), nn.ReLU())
            self.dec = nn.Sequential(nn.Linear(32,28*28), nn.Unflatten(1,(1,28,28)))
        def forward(self,x): z = self.enc(x); return self.dec(z)
    if __name__ == '__main__':
        print('PyTorch autoencoder demo — forward pass')
        m = AE(); x = torch.randn(2,1,28,28); print('out', m(x).shape)
else:
    if __name__ == '__main__':
        print('PyTorch not installed — autoencoder demo fallback. Use numpy to simulate encoding/decoding shapes.')
        import numpy as np
        x = np.random.randn(2,1,28,28)
        print('input shape', x.shape)
