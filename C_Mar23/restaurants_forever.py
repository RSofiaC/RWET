import sys
import random

def restaurant ( building = "House", foodstuff = "Pancakes"):
	return " International " + building + " of " + foodstuff

def human_join(parts, conjunction):
	if len(parts) == 1:
		return parts[0]
	return ', '.join(parts[:-1]) + " " + conjunction + " " + parts[-1] 

def ucfirst(s):
	return s[0].upper() + s[1:]

if __name__== "__main__":

	nouns = json.loads(open("nouns.json").read())
	noun_list = [ucfirst(item) for item in nouns ["nouns"]]

	for i in range (10):
		noun_count = random.randrange(1,5)
		things = random.sample(noun_list, noun_count)
		print restaurant(building=random.choice(noun_list),
			foodstuff=human_join(things))