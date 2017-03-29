import sys

for line in sys.stdin:
	line = line.strip()
	snumber = line[3:]
	print snumber

#trying to get rid of the lines that remain with a point in the begining after first strip
if line.find(' '):
		line = line.strip()
		cline = line[2:]
		print cline


