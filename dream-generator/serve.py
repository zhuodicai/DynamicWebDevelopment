import json

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

def get_poem():
    location = ['on the battlefield', 'in the countryside', 'in the room', 'in the tavern', 'in the alley', 'in the corner', 'in a parallel world', 'in shootout game', 'in the stairwell', 'at the nuclear research base', 'in the cave', 'in the street', 'in the house', 'in the classroom', 'by the pool', 'in the backyard', 'in the bathroom', 'on the road', 'in the valley', 'on the bridge', 'in hospital', 'in ruins', 'in the village', 'in the lotus pond', 'in cement pipeline', 'in the elevator', 'in stone city', 'on the hillside', 'in the attic', 'in the garden', 'on the roof', 'in the trap', 'in the channel', 'on theatrical stage', 'at the end of the road', 'deep in the heart', 'at the hair salon', 'in the virtual world of VR', 'in the air']
    environment = ['boundless', 'dark', 'damp', 'empty', 'uninhabited', 'narrow', 'absurd', 'twisted', 'bright', 'dreamy', 'overgrown', 'icy', 'dusted', 'burnt', 'red', 'yellow' , 'flickering', 'bright', 'black', 'gold', 'abandoned', 'brightly lit', 'shattered', 'cracked', 'transparent', 'nested', 'unsafe' , 'breezy', 'spooky', 'looming', 'invisible', 'barren', 'rotting', 'crowded']
    behavior = ['stands on', 'goes upstairs in', 'hides in', 'talks to', 'hangs on the' , 'is drown in' , 'passes through the', 'becomes' , 'is radiated by', 'grows in', 'pulls away from', 'sees', 'is trapped in', 'lies on', 'climbs up', 'is dried by', 'beats', 'touches', 'revives', 'floats in', 'jumps from', 'stares at', 'kisses', 'blows up', 'asks', 'whispers with', 'mirrors', 'is locked in', 'chases']
    myBehavior = ['running', 'vanishing', 'fleeing', 'burning', 'seeking', 'hiding', 'melting', 'flying', 'crying', 'exploding', 'escaping']
    adverb = ['incessantly', 'repeatedly', 'forever', 'silently', 'alone', 'helplessly', 'slowly']
    character = ['marionette', 'patient', 'soldier', 'lover', 'friend', 'snake', 'mutant', 'stranger', 'burnt man', 'green creature', 'woman with red hair', 'witch', 'classmate', 'godfather', 'invisible man', 'robot', 'man with implanted metal parts', 'ghost', 'victim', 'kitten','queen','faceless squire']
    thing = ['light without a light source', 'drizzle', 'severed head', 'stretched navel', 'cracked tooth', 'luminous eye', 'blue face', 'train coming from far away', 'liquid', 'mirror', 'chestnut', 'leaf', 'window', 'hanging rope', 'sunbeam', 'space', 'stair', 'red dead rabbit', 'weapon', 'mashed potato flood', 'minced meat', 'blood', 'fire', 'bath towel', 'bullet', 'cup', 'brick', 'mechanical game machine', 'paint', 'metal pipe', 'telephone', 'floor', 'hospital bed']

    import random

    line = [0 for i in range(11)]

    hour = str(random.randint(0,23))
    # hourStart = str(hour)
    # hourEnd = str(hour + 2)
    minute = str(random.randint(0,59))
    second = str(random.randint(0,59))

    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    if len(second) == 1:
        second = '0' + second

    # time
    line[0]= str(hour + ':' + minute + ':' + second) + ',' + ' ' + random.choice(environment)
    # dream content
    line[1] = '  '*1 + 'As it is'+ ' ' + random.choice(location) 
    for i in range(2,5):
        line[i] = '  '*i + random.choice(character).capitalize() + ' ' + random.choice(behavior)  + ' ' + random.choice(thing) 
    line[5] = '  '*5 + 'I, am' + ' ' + random.choice(myBehavior) + ' ' + random.choice(adverb)
    line[6] = '  '*4 + 'Until'
    for j in range(7,10):
        line[j] = '  '*(10 - j) + random.choice(thing).capitalize() + ' '  + random.choice(behavior) + ' '  + random.choice(character) 
    line[10] = str(hour + ':' + minute + ':' + second) + ',' + ' ' + random.choice(environment)


    print('\033[1mSymbolized Bad Dream\n\033[0m')
    poetry = "</br>".join(line)
    print(poetry)
    return poetry

@app.route("/dream")
def dream():
    return render_template("dream.html", poetry=get_poem())

@app.route("/api", methods=['POST'])
def hello_world():
    print("req", request.json)
    word = request.json.get("word", "")
    print(word)
    ret = {"word": word + " " + word}
    return json.dumps(ret)
