import markov

lines = list()

for line in open("problems.txt"):
  line = line.strip()
  lines.append(line)

markov.word_level_generate(lines, 3, count=4)
print '\n'.join(markov.char_level_generate(lines, 9, count=4))

#model = markov.build_model(text,3)
#markov.generate(model,3)

#rint ''.join(markov.generate(model,3))
