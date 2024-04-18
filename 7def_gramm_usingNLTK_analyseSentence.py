import nltk
from nltk import tokenize

grammar1 = nltk.CFG.fromstring("""
    S -> VP
    VP -> VP NP
    NP -> Det NP
    Det -> 'that'
    NP -> 'flight'
    VP -> 'Book'
""")

sentence = "Book that flight"
all_tokens = tokenize.word_tokenize(sentence)

print(all_tokens)

parser = nltk.ChartParser(grammar1)
for tree in parser.parse(all_tokens):
    print(tree)
    tree.draw()
