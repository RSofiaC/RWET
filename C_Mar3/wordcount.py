import sys

count = {}

for line in sys.stdin:
	line = line.strip()
	words = line.split()
	# how do I acutually count here?
	for item in words:
		if item in count:
			count[item] += 1 #evaluate the value and store it into the key of the dictionary
		else:
			count[item] = 1


#how do I make the output pretty?
# you: 3
# sort it by count descending? <- hard
for key, val in count.iteritems():
	if val > 1:
		print key + ":" + str(val)


