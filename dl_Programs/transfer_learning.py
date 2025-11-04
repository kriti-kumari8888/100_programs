"""
transfer_learning.py
Sketch of transfer learning flow (uses torchvision if present). Falls back to explanatory printout.
"""
try:
    import torch
    import torch.nn as nn
    has_torch = True
except Exception:
    has_torch = False

if has_torch:
    try:
        import torchvision.models as models
        has_torchvision = True
    except Exception:
        has_torchvision = False

if __name__ == '__main__':
    if not has_torch:
        print('PyTorch not installed. To run transfer learning install torch and torchvision.')
    elif not has_torchvision:
        print('torchvision not available. You can still load a model checkpoint manually.')
    else:
        print('Building a pretrained resnet18 and replacing the head...')
        model = models.resnet18(pretrained=True)
        model.fc = nn.Linear(model.fc.in_features, 5)  # e.g. 5 classes
        print('Model ready. Summary:')
        print(model)
