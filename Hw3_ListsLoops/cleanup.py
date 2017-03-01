import sys
import random

for line in sys.stdin:
  line = line.strip()
  if len(line) > 20:
      print line
