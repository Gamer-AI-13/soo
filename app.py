from flask import Flask
from flask import render_template, request, redirect, url_for, jsonify, json
import os
from datetime import datetime
from database import urlall
import random
import string
import urllib.request
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
    token = request.args['token']
    things = request.json
    print(things)
    #newthings = json.loads(things)
    try:
        somet = things['message']['text']
        if "/start" not in somet:
            return render_template('index.html')
        idofp = things['message']['from']['id']
        print(somet)
    except Exception as e:
        print(e)
        try:
            somevideo = things['message']['video']
            idofp = things['message']['from']['id']
            videoid = things['message']['message_id']
            q1 = f"https://api.telegram.org/bot{token}/forwardMessage?chat_id={idofp}&from_chat_id={idofp}&message_id={videoid}"
            req1 = urllib.request.urlopen(q1)
            print (req1.content)
        except Exception as e:
            print(e)
            return render_template('index.html')
        try:
            somefile = things['message']['document']
            idofp = things['message']['from']['id']
            videoid = things['message']['message_id']
            q2 = f"https://api.telegram.org/bot{token}/forwardMessage?chat_id={idofp}&from_chat_id={idofp}&message_id={videoid}"
            req2 = urllib.request.urlopen(q1)
            print (req2.content)
        except Exception as e:
            print(e)
            return render_template('index.html')
        try:
            somefile = things['message']['audio']
            idofp = things['message']['from']['id']
            videoid = things['message']['message_id']
            q3 = f"https://api.telegram.org/bot{token}/forwardMessage?chat_id={idofp}&from_chat_id={idofp}&message_id={videoid}"
            req3 = urllib.request.urlopen(q1)
            print (req3.content)
        except Exception as e:
            print(e)
            return render_template('index.html')   
        return render_template('index.html')
    q = f"https://api.telegram.org/bot{token}/sendmessage?chat_id={idofp}&text=hello"
    req = urllib.request.urlopen(q)
    print (req.content)
    return render_template('index.html')

@app.route('/404')
def not_found():
    return render_template('404.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)


