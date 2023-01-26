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
    print(data)
    return render_template('disneyland.html', data = data['lands'])

@app.route('/lands/<id>')
def spec_land(id):
    req = requests.get('https://queue-times.com/en-US/parks/16/queue_times.json')
    data = json.loads(req.content)
    return render_template('lands.html', data= data['lands'])
@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/users')
def users():
    return render_template('users.html')


if __name__ == '__main__':
    app.run(debug=True)