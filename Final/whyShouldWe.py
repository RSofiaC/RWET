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
        lineOne = 'Because '.join(random.choice(offense))
        lineTwo = ', '.join(random.choice(question))
        lineThree = random.choice(request)
    return  start + " " + lineOne + " " + lineTwo + " " + lineThree
