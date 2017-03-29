import random

newBelt_string = open("newBelt.txt").read()
newBelt_words = newBelt_string.split()

for line in open("paisTropical.txt"):
    line = line.strip()
    if len(line) == 0:
        print line
    else:
        line_words = line.split()
        random_newBelt_word = random.choice(newBelt_words)
        random_tropical_word = random.choice(line_words)
        line = line.replace(random_tropical_word, random_newBelt_word)
        print line