from __future__ import unicode_literals
import spacy
nlp = spacy.load('en')
import random

docR = nlp(open("peoplevsOhio.txt").read().decode('utf8'))
docO = nlp(open("unwanted.txt").read().decode('utf8'))
docQ = nlp(open("why.txt").read().decode('utf8'))

questions = list(docQ.sents)
offenses = list(docO.sents)
requests = list(docR.sents)

def understand (start, offense, question, request):
        lineOne = 'Because '.join(str(random.choice(offense)))
        lineTwo = ', '.join(str(random.choice(question)))
        lineThree = str(random.choice(request))
        return  start + " " + lineOne + " " + lineTwo + " " + lineThree

#having trouble here trying to turn the lines from unicode into str so it can
#get printed
    [line.decode('utf-8').strip() for line in title_file.readlines()]
