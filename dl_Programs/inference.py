"""
inference.py
Small inference helper showing how to load a model checkpoint (PyTorch) and run a forward pass.
If PyTorch missing, prints guidance.
"""
try:
    import torch
    has_torch = True
except Exception:
    has_torch = False

if __name__ == '__main__':
    if not has_torch:
        print('PyTorch not installed. To run inference install torch. Example:')
        print('  model = torch.load("model.pt")\n  model.eval()\n  out = model(torch.randn(1,3,224,224))')
    else:
        print('PyTorch available — demo forward pass on random data')
        class Dummy(torch.nn.Module):
            def forward(self,x):
                return x.sum(dim=[1,2,3])
        m = Dummy()
        out = m(torch.randn(2,3,32,32))
        print('Output:', out)
