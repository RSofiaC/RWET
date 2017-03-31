import sys
import random

def ucfirst(s):
  return s[0].upper() + s[1:]

#the main function puts the three parts together
def ridiculeces(one, two, three):
    #I would like to make the If I only could or If only you to me also randomly
    #selected (time)
  return "If I only could " + one + " and " + two + three

#I took the human_join function and just added moreParts to it and a second join
def human_join(parts, conjunction, moreParts):
  if len(parts) == 1:
    return parts[0]
  first_join = ', '.join(parts[:-1])
  second_join = ', '.join(moreParts[:-1])
#So this is the start of the angsty bit
  return first_join + " " + conjunction + " " + second_join + " " + ","

#This just prepares the file of synonyms and antonyms for Quit
words = list()
for line in open('sinonimos.txt'):
  line = line.strip()
  words.append(ucfirst(line))

#This just prepares the file of synonyms to learn
palabras = list()
for line in open('aAntonym.txt'):
  line = line.strip()
  palabras.append(ucfirst(line))

#This prepares the file of angsty phrases
monts = list()
for line in open('angst.txt'):
  line = line.strip()
  monts.append(line)

#And the we go into making the paragraph
for i in range(8):
  number_to_sample = random.randrange(1, 3)
  things = random.sample(words, number_to_sample)
  morethings = random.sample(palabras, number_to_sample)
  andmore = random.sample(monts, 1)
  print ridiculeces(random.choice(words), human_join(things, "and", morethings), random.choice(monts))
#If I could only print 4 lines and then other 4 lines so it looks like an angsty
#teenage poem
