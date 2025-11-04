"""
bert_demo.py
Shows how to run a tiny inference with Hugging Face transformers if available; otherwise prints install notes.
"""
try:
    from transformers import BertTokenizer, BertModel
    import torch
    has_transformers = True
except Exception:
    has_transformers = False

if __name__ == '__main__':
    if has_transformers:
        tok = BertTokenizer.from_pretrained('bert-base-uncased')
        model = BertModel.from_pretrained('bert-base-uncased')
        inputs = tok('Hello world', return_tensors='pt')
        out = model(**inputs)
        print('Last hidden size:', out.last_hidden_state.shape)
    else:
        print('transformers not installed. To run: pip install transformers torch')
