import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
text = "Tokenization is an important task. It splits text into tokens "
nltk.download('punkt')
token1 = word_tokenize(text)
print(token1)
token2 = sent_tokenize(text)
print(token2)
