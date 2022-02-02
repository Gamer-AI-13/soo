from flask import Flask
from flask import render_template, request, redirect, url_for, jsonify, json
import os
from encription import aencode, decode
from datetime import datetime
from database import Sessions
import random
import string
import requests
import json
BOT_USERNAME = "bottoken"
db = Sessions("mongodb+srv://gamerai:sree123456789@cluster0.7xpnm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", BOT_USERNAME)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def homepage():
    print(request.json)
    return render_template('index.html')

@app.route('/web', methods=['GET', 'POST'])
def botpage():
    token = request.args['token']
    things = request.json
    idofp = things['message']['from']['id']
    print(token)
    #newthings = json.loads(things)
    try:
        somet = things['message']['text']
        if "/start" not in somet:
            return render_template('index.html')
        print(somet)
    except Exception as e:
        print (token)
        details = db.get_bot(token)
        username = details['username']
        if details['id'] != idofp:
            return
        print(e)
        try:
            somevideo = things['message']['video']
            idofp = things['message']['from']['id']
            videoid = things['message']['message_id']
            toencriptstr = str(idofp) + "/" + str(videoid)
            encriptedstr = aencode("afuckingpasswordkunji", toencriptstr)
            strr = encriptedstr.decode("ascii")
            print(strr)
            q = f"https://api.telegram.org/bot{token}/sendmessage?chat_id={idofp}&text=https://t.me/{username}?start={strr}"
            #q1 = f"https://api.telegram.org/bot{token}/forwardMessage?chat_id={idofp}&from_chat_id={idofp}&message_id={videoid}"
            req1 = requests.get(q)
            print (req1)
        except Exception as e:
            print(e)
            pass
        try:
            somefile = things['message']['photo']
            idofp = things['message']['from']['id']
            videoid = things['message']['message_id']
            toencriptstr = str(idofp) + "/" + str(videoid)
            encriptedstr = aencode("afuckingpasswordkunji", toencriptstr)
            strr = encriptedstr.decode("ascii")
            print(strr)
            q = f"https://api.telegram.org/bot{token}/sendmessage?chat_id={idofp}&text=https://t.me/{username}?start={strr}"
            #q2 = f"https://api.telegram.org/bot{token}/forwardMessage?chat_id={idofp}&from_chat_id={idofp}&message_id={videoid}"
            req2 = requests.get(q)
            print (req2)
        except Exception as e:
            print(e)
            pass
        try:
            somefile = things['message']['document']
            idofp = things['message']['from']['id']
            videoid = things['message']['message_id']
            toencriptstr = str(idofp) + "/" + str(videoid)
            encriptedstr = aencode("afuckingpasswordkunji", toencriptstr)
            strr = encriptedstr.decode("ascii")
            print(strr)
            q = f"https://api.telegram.org/bot{token}/sendmessage?chat_id={idofp}&text=https://t.me/{username}?start={strr}"
            #q2 = f"https://api.telegram.org/bot{token}/forwardMessage?chat_id={idofp}&from_chat_id={idofp}&message_id={videoid}"
            req2 = requests.get(q)
            print (req2)
        except Exception as e:
            print(e)
            pass
        try:
            somefile = things['message']['audio']
            idofp = things['message']['from']['id']
            videoid = things['message']['message_id']
            toencriptstr = str(idofp) + "/" + str(videoid)
            encriptedstr = aencode("afuckingpasswordkunji", toencriptstr)
            strr = encriptedstr.decode("ascii")
            print(strr)
            q = f"https://api.telegram.org/bot{token}/sendmessage?chat_id={idofp}&text=https://t.me/{username}?start={strr}"
            #q3 = f"https://api.telegram.org/bot{token}/forwardMessage?chat_id={idofp}&from_chat_id={idofp}&message_id={videoid}"
            req3 = requests.get(q)
            print (req3)
        except Exception as e:
            print(e)
            return render_template('index.html')   
        return render_template('index.html')
    try:
        recivedstring = somet.split(" ")[1]
    except Exception as e:
        print(e)
        q = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={idofp}&text=Create your own version of this bot at @I_sharebot"
        req = requests.get(q)
        print (req.content)
        return render_template('index.html') 
    print(recivedstring)
    bytestr = recivedstring.encode("ascii")
    print(bytestr)
    decodedstr = decode("afuckingpasswordkunji", bytestr)
    print(decodedstr)
    newstr = decodedstr.split("/")
    userid = newstr[0]
    files = newstr[1]
    q = f"https://api.telegram.org/bot{token}/copyMessage?chat_id={idofp}&from_chat_id={userid}&message_id={files}"
    req = requests.get(q)
    print (req.content)
    return render_template('index.html')

@app.route('/404')
def not_found():
    return render_template('404.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)


