"""
tokenize_demo.py
Simple tokenization examples: regex-based, and NLTK fallback if available.
"""
import re

try:
    import nltk
    nltk.data.find('tokenizers/punkt')
    from nltk.tokenize import word_tokenize
    has_nltk = True
except Exception:
    has_nltk = False

def regex_tokenize(text):
    return re.findall(r"\w+\'\w+|\w+|[.,!?;]", text)

if __name__ == '__main__':
    s = "Hello, world! I'm testing tokenization." 
    print('Input:', s)
    if has_nltk:
        print('NLTK tokens:', word_tokenize(s))
    else:
        print('Regex tokens:', regex_tokenize(s))
        print('\nTip: install NLTK and run: python -c "import nltk; nltk.download(\'punkt\')"')
