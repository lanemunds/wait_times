from flask import Flask, render_template, redirect, flash, request, session, url_for
from jinja2 import StrictUndefined
import json

import requests
import os 

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/", )
def get_times():
    req = requests.get("https://queue-times.com/en-US/parks/16/queue_times.json")
    print(req.content)
    data = json.loads(req.content)
    adventure =  data['rides']

    return render_template('waitTimes.html', data = data['lands'], adventure = adventure)


if __name__ == '__main__':
    app.run(debug=True)