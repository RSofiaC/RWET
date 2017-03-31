import random

#need to review this code and undestand perfectly what the final part is doing
biome_lines = list()
for line in open('biome.txt'):
    line = line.strip()
    if len(line) > 0:
        biome_lines.append(line)

tropical_lines = list()
for line in open('paisTropical.txt'): #before paisTropical.txt
    line = line.strip()
    if len(line) > 0:
        tropical_lines.append(line)

for i in range(10):
    random_biome = random.choice(biome_lines)
    random_tropical = random.choice(tropical_lines)
    print random_biome[:len(random_biome)/2]+ random_tropical[len(random_tropical)/2:]
