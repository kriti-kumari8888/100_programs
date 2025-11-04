"""
augmentations.py
Simple image augmentation utilities. Uses PIL if available; otherwise shows numpy-based flips.
"""
try:
    from PIL import Image, ImageOps
    has_pil = True
except Exception:
    has_pil = False

import numpy as np

def flip_horizontal_np(img: np.ndarray) -> np.ndarray:
    return img[:, ::-1, ...]

if __name__ == '__main__':
    if has_pil:
        print('PIL found — demonstrating a horizontal flip on a generated image')
        img = Image.new('RGB', (64,64), color='purple')
        img2 = ImageOps.mirror(img)
        print('PIL image flipped (mode, size)=', img2.mode, img2.size)
    else:
        print('PIL not installed — running numpy flip demo')
        arr = np.zeros((32,32,3), dtype=np.uint8)
        arr2 = flip_horizontal_np(arr)
        print('Numpy array flipped shape=', arr2.shape)
