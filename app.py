from flask import Flask
from flask import render_template, request, redirect, url_for, jsonify, json
import os
from datetime import datetime
from database import urlall
import random
import string
import json
DATABASENAME = "urls"
ConfigDATABASE_URL = os.environ.get("DATABASE_URL", "12345")
db = urlall(ConfigDATABASE_URL, DATABASENAME)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def homepage():
    print(request.json)
    return render_template('index.html')

@app.route('/web', methods=['GET', 'POST'])
def botpage():
    #token = request.args['token']
    things = request.json
    print(things)
    newthings = json.loads(things)
    try:
        print(newthings['update_id'])
    except Exception as e:
        print (e)
    return #render_template('index.html')

@app.route('/404')
def not_found():
    return render_template('404.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)


