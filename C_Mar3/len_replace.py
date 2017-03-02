import sys

# part one: create the length-to-words dictionary
contents = open("sonnets.txt").read()
words = contents.split()

by_length = {}

for item in words:
	if len(item) not in by_length:
		by_length[len(item)] = []
	by_length[len(item)].append(item)



print by_length