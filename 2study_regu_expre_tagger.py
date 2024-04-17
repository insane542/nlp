from nltk.corpus import brown
from nltk.tag import RegexpTagger

test_sent = brown.sents(categories='news')[0]
regexp_tagger = RegexpTagger([
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers
    (r'(The|the|A|a|An|an)$', 'AT'),   # articles
    (r'.*able$', 'JJ'),                 # adjectives
    (r'.*ness$', 'NN'),                 # nouns formed from adjectives
    (r'.*ly$', 'RB'),                   # adverbs
    (r'.*s$', 'NNS'),                   # plural nouns
    (r'.*ing$', 'VBG'),                 # gerunds
    (r'.*ed$', 'VBD'),                  # past tense verbs
    (r'.*', 'NN')                       # nouns (default)
])

# Tag the test sentence
tagged_sent = regexp_tagger.tag(test_sent)
print(tagged_sent)
