#CHUNKING
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
#Sample text
text = "The quick brown fox jumps over the lazy dog. John Smith wrote a book."
#Tokenize the text
tokens = word_tokenize(text)
#Perform POS Tagging
pos_tags = nltk.pos_tag(tokens)
chunk_grammar = r"""NP:{<DT>?<JJ>*<NN>}"""
chunk_parser = RegexpParser(chunk_grammar)
tree = chunk_parser.parse(pos_tags)
for subtree in tree.subtrees():
  if subtree.label() == 'NP':
    print(subtree)
