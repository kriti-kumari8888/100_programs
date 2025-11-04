"""
seq2seq_demo.py
Tiny seq2seq skeleton using PyTorch if available; otherwise prints guidance.
"""
try:
    import torch
    import torch.nn as nn
    has_torch = True
except Exception:
    has_torch = False

if has_torch:
    class TinySeq2Seq(nn.Module):
        def __init__(self, vocab=50, emb=16, hid=32):
            super().__init__()
            self.emb = nn.Embedding(vocab, emb)
            self.enc = nn.LSTM(emb, hid, batch_first=True)
            self.dec = nn.LSTM(emb, hid, batch_first=True)
            self.out = nn.Linear(hid, vocab)
        def forward(self, src, tgt):
            _, (h,c) = self.enc(self.emb(src))
            o, _ = self.dec(self.emb(tgt), (h,c))
            return self.out(o)
    if __name__ == '__main__':
        m = TinySeq2Seq()
        src = torch.randint(0,50,(2,6))
        tgt = torch.randint(0,50,(2,6))
        print('out shape', m(src,tgt).shape)
else:
    if __name__ == '__main__':
        print('PyTorch not installed. To run seq2seq example: pip install torch')
