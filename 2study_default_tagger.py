import nltk
from nltk.tag import DefaultTagger

exptagger = DefaultTagger('NN')

from nltk.corpus import treebank
testsentences = treebank.tagged_sents()[1000:]

# Calculate accuracy using the accuracy() function
print(exptagger.evaluate(testsentences))

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Tagging a list of sentences
import nltk
from nltk.tag import DefaultTagger

exptagger = DefaultTagger('NN')
print(exptagger.tag_sents([['Hi', ','], ['How', 'are', 'you', '?']]))
