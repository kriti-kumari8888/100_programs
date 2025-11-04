"""
sentiment_analysis.py
Tiny sentiment demo: uses TextBlob if available, otherwise a simple lexicon-based fallback.
"""
try:
    from textblob import TextBlob
    has_tb = True
except Exception:
    has_tb = False

POS = {'good':1, 'great':2, 'happy':1}
NEG = {'bad':-1, 'sad':-1, 'terrible':-2}

def lexicon_sentiment(text):
    s = 0
    for w in text.lower().split():
        s += POS.get(w, 0) + NEG.get(w, 0)
    return s

if __name__ == '__main__':
    txt = "I am very happy with this good product"
    if has_tb:
        tb = TextBlob(txt)
        print('Polarity:', tb.sentiment.polarity)
    else:
        print('Lexicon score:', lexicon_sentiment(txt))
        print('Tip: pip install textblob')
