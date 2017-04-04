import sys
import EXngramcount

#pairs here is a dictionary not a list
pairs = dict()

#We are operating on the lines of the file
for line in sys.stdin:
#take the blank space out and then make a dic with blank space
#in between
  line = line.strip()
  words = line.split(" ")

#si el tama;o del archivo es menor que 2 igual continua
  if len(words) < 2:
    continue
#iterate through the dictionary until the last item (-1)
  for i in range(len(words) - 1):
#each pair becomes a tuple from the lsit
    pair = tuple(words[i:i+2])
    #here it starts checking for the repetition
    if pair in pairs:
      pairs[pair] += 1 #if the pair is already in there add another count
    else:
      pairs[pair] = 1 #if it is not in yet start of one

#IT IS NOT COMPLETLY CLEAR AT WHICH POINT THE KEYS WERE ASSIGNED
for pair in pairs.keys(): #we said it was a dictionary so we are iterating
#through its keys so we know which ones are repeated
  count = pairs[pair]
#take only those keys that appear more than once
  if count > 1:
      #print them and show their count
    print ' '.join(pair) + ": " + str(count)
