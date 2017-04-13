from flask import Flask
import pronouncing
import random

app = Flask(__name__)

@app.route('/rhyme')
def define():
    word_str = rquest.args['word']
    rhymes = pronouncing.rhymes(word_str.lower())
    if len(rhymes) > 0:
        
