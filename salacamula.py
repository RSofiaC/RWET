import sys
import random

all_lines = list()

for line in sys.stdin:
	line = line.strip()
	words = line.split(" ")
	random.shuffle(words)
	output = " ".join(words)
	print output

for line in output:
	line = line.strip()
	all_lines.append(line)

random.shuffle(all_lines)

for line in all_lines:
  line = line.strip()
  if len(line) >= 40:
      print line


