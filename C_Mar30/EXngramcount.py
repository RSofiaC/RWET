def count_ngrams (tokens, n):
  ngrams = dict()
  if len(tokens) < n:
    return ngrams
  for i in range (len(tokens) - n + 1):
    ngram = tuple(tokens[i:i+n])
    if ngram not in ngrams:
      ngrams[ngram] = 0
    ngrams[ngram] += 1
  return ngrams

def merge_counts(ngrams_list):
  merged = dict()
  for ngrams in ngrams_list:
    for key, val in ngrams.iteritems():
      if key not in merged:
        merged[key] = 0
      merged[key] += val
  return merged

if __name__ == '__main__':
    print "in the if"
    import sys
    n = int(sys.argv[1])
    counts = list()
    with open(sys.argv[2], "r") as myfile:
        for line in myfile:
        	line = line.strip()
        	counts.append(count_ngrams(list(line), n))
        combined_counts = merge_counts(counts)
        sorted_counts = sorted(combined_counts.items(), key=lambda x: x[1],
        		reverse=True)
        for key, val in sorted_counts:
        	print ''.join(key) + ": " + str(val)
