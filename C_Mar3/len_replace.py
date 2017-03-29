import sys

# part one: create the length-to-words dictionary
contents = open("sonnets.txt").read()
words = contents.split()

by_length = {}

for item in words:
	if len(item) not in by_length:
		by_length[len(item)] = []
	by_length[len(item)].append(item)

#part two: read in standard input and perform the replacements
for line in sys.stdin:
	line = line.strip()
	words = line.split()
	print ' '.join([random.choice(by_length[len(w)]) for w in words])

print by_length