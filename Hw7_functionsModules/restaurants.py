import sys
import random

def ucfirst(s):
  return s[0].upper() + s[1:]

def restaurant (synon="run", antonym="stay"):
  return "If I could " + synon + " and " + antonym

def human_join (parts, conjunction) :
  if len(parts) == 1:
    return parts [0]
  first_join = ', '.join(parts[:-1])
  return first_join + " " + conjunction + " " + parts[-1]

synonyms = list()
for line in open('aSynonym.txt'):
  line = line.strip()
  synonyms.append(ucfirst(line))

antonyms = list()
for line in open('aAntonym.txt'):
   line = line.strip()
   antonyms.append(ucfirst(line))

for i in range(10):
  number_to_sample = random.randrange(1, 5)
  things = random.sample(synonyms, number_to_sample)
  print restaurant (random.choice(synonyms), human_join(things, "and"))
