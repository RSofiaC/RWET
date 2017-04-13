#library and object
from flask import Flask
#create a new app object b
app = Flask(__name__)
import random

#whenever someone does a request to the root / reply this
@app.route("/")
def hello():
 return "Finally! It took you forever!"

@app.route("/greeting")
def greeting():
 greetings = ["zup", "yo", "hey"]
 places = ["stranger", "handsome", "old chum"]
 return random.choice(greetings) + " " + random.choice(places)

if __name__ == "__main__":
 app.run()
