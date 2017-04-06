from __future__ import unicode_literals
import spacy
import sys
import random

nlp = spacy.load("en")
text = sys.stdin.read().decode('utf8', 'replace')
doc = nlp(text)

plural_nouns = []
ing_words = []

for word in doc:
  if word.tag_ == "NNS":
    plural_nouns.append(word.text)
  elif word.tag_ == "VBG":
    ing_words.append(word.text)

print "Spring came and then it all started to happen"
for i in range(10):
  print random.choice(plural_nouns) + " were " + random.choice(ing_words)
