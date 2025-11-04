"""
train_mlp.py
Tiny MLP training skeleton. Attempts to import PyTorch; if unavailable, prints instructions and runs a tiny numpy demo.
"""
from __future__ import annotations

try:
    import torch
    import torch.nn as nn
    import torch.optim as optim
    has_torch = True
except Exception:
    has_torch = False

if has_torch:
    class MLP(nn.Module):
        def __init__(self, input_dim=10, hidden=32, out=2):
            super().__init__()
            self.net = nn.Sequential(nn.Linear(input_dim, hidden), nn.ReLU(), nn.Linear(hidden, out))
        def forward(self, x):
            return self.net(x)

    def train_one_epoch():
        model = MLP()
        opt = optim.SGD(model.parameters(), lr=0.01)
        for i in range(5):
            x = torch.randn(8, 10)
            y = torch.randint(0, 2, (8,))
            logits = model(x)
            loss = nn.functional.cross_entropy(logits, y)
            loss.backward(); opt.step(); opt.zero_grad()
            print(f"step {i} loss={loss.item():.4f}")

    if __name__ == '__main__':
        print("PyTorch found — running tiny MLP training loop...")
        train_one_epoch()
else:
    if __name__ == '__main__':
        print("PyTorch not found. To run this example install torch.\nFalling back to a small numpy demo.")
        import numpy as np
        X = np.random.randn(8,10)
        W = np.random.randn(10,2)
        logits = X.dot(W)
        print("Computed logits shape:", logits.shape)
