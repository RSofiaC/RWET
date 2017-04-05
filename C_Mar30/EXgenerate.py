import sys
import markov

text = sys.stdin.read()
model = markov.build_model(text.split(), 4)
generated = markov.generate(model, 4)
print ' '.join(generated)
