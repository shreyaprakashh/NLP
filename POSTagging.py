#POS TAGGING
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk import pos_tag
sentence = "The quick brown fox jumps over the lazy dog."
words = word_tokenize(sentence)
pos_tags = pos_tag(words)
print(pos_tags)
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")
