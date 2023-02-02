from flask import Flask, render_template, redirect, flash, request, session, url_for
from jinja2 import StrictUndefined
import json

import requests
import os 

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/waitTimes", )
def get_times():
    req = requests.get("https://queue-times.com/en-US/parks/16/queue_times.json")
    data = json.loads(req.content)
    park = "Disneyland"
    return render_template('waitTimes.html', data = data['lands'], park = park)

@app.route("/californiaWaitTimes")
def get_cal_times():
    req = requests.get("https://queue-times.com/en-US/parks/17/queue_times.json")
    data = json.loads(req.content)
    park = "California Adventure"
    return render_template('waitTimes.html', data = data['lands'], park = park)

@app.route("/hollywoodStudiosWaitTimes")
def get_hollywood_times():
    req = requests.get("https://queue-times.com/en-US/parks/7/queue_times.json")
    data = json.loads(req.content)
    park = "Hollywood Studios"
    return render_template('waitTimes.html', data = data['lands'], park = park)

@app.route("/magicKingdomWaitTimes")
def get_MK_times():
    req = requests.get("https://queue-times.com/en-US/parks/6/queue_times.json")
    data = json.loads(req.content)
    park = "Magic Kingdom"
    return render_template('waitTimes.html', data = data['lands'], park = park)

@app.route("/epcotWaitTimes")
def get_epcot_times():
    req = requests.get("https://queue-times.com/en-US/parks/5/queue_times.json")
    data = json.loads(req.content)
    park = 'Epcot Center'
    return render_template('waitTimes.html', data = data['lands'], park = park)

@app.route("/animalKingdomWaitTimes")
def get_AK_times():
    req = requests.get("https://queue-times.com/en-US/parks/8/queue_times.json")
    data = json.loads(req.content)
    park = "Animal Kingdom"
    return render_template('waitTimes.html', data = data['lands'], park = park)

@app.route('/parks')
def parks():
    return render_template('parks.html')

@app.route('/californiaAdventure')
def dca():
    req = requests.get("https://queue-times.com/en-US/parks/17/queue_times.json")
    data = json.loads(req.content)
    return render_template('californiaAdventure.html', data = data['lands'])

@app.route('/disneyland')
def disneyland():
    req = requests.get('https://queue-times.com/en-US/parks/16/queue_times.json')
    data = json.loads(req.content) 
    return render_template('disneyland.html', data = data['lands'])

@app.route('/lands/<id>')
def spec_land(id):
    req = requests.get('https://queue-times.com/en-US/parks/16/queue_times.json')
    data = json.loads(req.content)
    return render_template('lands.html', data= data['lands'])


@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/epcot')
def epcot():
    return render_template('epcot.html')

@app.route('/magicKingdom')
def magic():
    return render_template('magicKingdom.html')

@app.route('/animalKingdom')
def animal():
    return render_template('animal.html')

@app.route('/hollywoodStudios')
def hollywood():
    return render_template('hollywood.html')


@app.route('/disneyrides')
def disneyRide():
    req = requests.get('http://touringplans.com/disneyland/attractions.json')
    data = json.loads(req.content)
    return render_template('disneyRides.html', data = data, landName = "Disneyland")

@app.route('/californiaRides')
def californiaRide():
    req = requests.get('http://touringplans.com/disney-california-adventure/attractions.json')
    data = json.loads(req.content)
    return render_template('disneyRides.html', data = data, landName = "California Adventure")

@app.route('/epcotRides')
def epcotRide():
    req = requests.get('http://touringplans.com/epcot/attractions.json')
    data = json.loads(req.content)
    return render_template('disneyRides.html', data = data, landName = "Epcot")

@app.route('/animalRides')
def animalRide():
    req = requests.get('http://touringplans.com/animal-kingdom/attractions.json')
    data = json.loads(req.content)
    return render_template('disneyRides.html', data = data, landName = "Animal Kingdom")

@app.route('/magicRides')
def magicRide():
    req = requests.get('http://touringplans.com/magic-kingdom/attractions.json')
    data = json.loads(req.content)
    return render_template('disneyRides.html', data = data, landName = "Magic Kingdom")

@app.route('/hollywoodRides')
def hollywoodRide():
    req = requests.get('http://touringplans.com/hollywood-studios/attractions.json')
    data = json.loads(req.content)
    return render_template('disneyRides.html', data = data, landName = "Hollywood Studios")

@app.route('/disneyfood')
def disneyFood():
    req = requests.get('http://touringplans.com/disneyland/dining.json')
    data = json.loads(req.content)
    return render_template('disneyFood.html', data = data[0], data2 = data[1], landName = "Disneyland")

@app.route('/californiaFood')
def californiaFood():
    req = requests.get('http://touringplans.com/disney-california-adventure/dining.json')
    data = json.loads(req.content)
    print(data)
    return render_template('disneyFood.html', data = data[0], data2 = data[1], landName = "California Adventure")

@app.route('/epcotFood')
def epcotFood():
    req = requests.get('http://touringplans.com/epcot/dining.json')
    data = json.loads(req.content)
    return render_template('disneyFood.html', data = data[0], data2 = data[1], landName = "Epcot")

@app.route('/animalFood')
def animalFood():
    req = requests.get('http://touringplans.com/animal-kingdom/dining.json')
    data = json.loads(req.content)
    return render_template('disneyFood.html', data = data[0], data2 = data[1], landName = "Animal Kingdom")

@app.route('/magicFood')
def magicFood():
    req = requests.get('http://touringplans.com/magic-kingdom/dining.json')
    data = json.loads(req.content)
    return render_template('disneyFood.html', data = data[0], data2 = data[1], landName = "Magic Kingdom")

@app.route('/hollywoodFood')
def hollywoodFood():
    req = requests.get('http://touringplans.com/hollywood-studios/dining.json')
    data = json.loads(req.content)
    return render_template('disneyFood.html', data = data[0], data2 = data[1], landName = "Hollywood Studios")

@app.route('/disneyentertainment')
def disneyEntertainment():
    return render_template('disneyEntertainment.html')


if __name__ == '__main__':
    app.run(debug=True)