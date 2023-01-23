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
    return render_template('waitTimes.html', data = data['lands'])

@app.route("/californiaWaitTimes")
def get_cal_times():
    req = requests.get("https://queue-times.com/en-US/parks/17/queue_times.json")
    data = json.loads(req.content)
    return render_template('californiaWaitTimes.html', data = data['lands'])

@app.route("/hollywoodStudiosWaitTimes")
def get_hollywood_times():
    req = requests.get("https://queue-times.com/en-US/parks/7/queue_times.json")
    data = json.loads(req.content)
    return render_template('hollywoodStudiosWaitTimes.html', data = data['lands'])

@app.route("/magicKingdomWaitTimes")
def get_MK_times():
    req = requests.get("https://queue-times.com/en-US/parks/6/queue_times.json")
    data = json.loads(req.content)
    return render_template('magicKingdomWaitTimes.html', data = data['lands'])

@app.route("/epcotWaitTimes")
def get_epcot_times():
    req = requests.get("https://queue-times.com/en-US/parks/5/queue_times.json")
    data = json.loads(req.content)
    return render_template('epcotWaitTimes.html', data = data['lands'])

@app.route("/animalKingdomWaitTimes")
def get_AK_times():
    req = requests.get("https://queue-times.com/en-US/parks/8/queue_times.json")
    data = json.loads(req.content)
    return render_template('animalKingdomWaitTimes.html', data = data['lands'])

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