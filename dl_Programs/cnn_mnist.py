"""
cnn_mnist.py
Small CNN skeleton for MNIST. If torchvision/PyTorch are missing, prints instructions and demonstrates shape ops.
"""
try:
    import torch
    import torch.nn as nn
    has_torch = True
except Exception:
    has_torch = False

if has_torch:
    class TinyCNN(nn.Module):
        def __init__(self):
            super().__init__()
            self.conv = nn.Sequential(nn.Conv2d(1,8,3), nn.ReLU(), nn.AdaptiveAvgPool2d(1))
            self.fc = nn.Linear(8,10)
        def forward(self,x):
            x = self.conv(x)
            x = x.view(x.size(0), -1)
            return self.fc(x)

    if __name__ == '__main__':
        print("PyTorch available — creating a TinyCNN and running a dummy forward pass.")
        model = TinyCNN()
        x = torch.randn(4,1,28,28)
        y = model(x)
        print('Output shape:', y.shape)
else:
    if __name__ == '__main__':
        print('PyTorch not installed. To run with real MNIST install torch and torchvision.')
        print('Demo: simulate shapes using numpy')
        import numpy as np
        x = np.random.randn(4,1,28,28)
        print('Simulated input shape:', x.shape)
