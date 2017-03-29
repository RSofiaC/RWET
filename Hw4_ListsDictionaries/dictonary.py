import sys
import random

letters = {}

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        first_letter = word[0]
        if first_letter not in letters:
            letters[first_letter] = []
        letters[first_letter].append(word)

for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter in letters:
        print random.choice(letters[letter])