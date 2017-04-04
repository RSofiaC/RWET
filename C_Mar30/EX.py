import sys
import EXngramcount

n = int(sys.argv[1])
counts = list()

for line in sys.stdin:
    line = line.strip()
    counts.append(count_ngrams(list(line), n))
combined_counts = merge_counts(counts)
sorted_counts = sorted(combined_counts.items(), key=lambda x:x[1], reverse=True)
for key, val in sorted_counts:
    print ''.join(key) + ": "+str(val)
