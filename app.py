import re
import pyrebase

from flask import Flask, url_for, render_template, request
from flask import *

config= {
    "apiKey": "AIzaSyAR2qriqMRofJ0bnvLPWapI3pdI_7gZpAE",
    "authDomain": "rideshare-5860d.firebaseapp.com",
    "databaseURL": "https://rideshare-5860d.firebaseio.com",
    "projectId": "rideshare-5860d",
    "storageBucket": "rideshare-5860d.appspot.com",
    "messagingSenderId": "837425501722",    
}

firebase = pyrebase.initialize_app(config)
db=firebase.database()


app = Flask(__name__)


@app.route('/')
def intro():
    return render_template('enterName.html')


@app.route('/<varC>', methods=['POST', 'GET'])  # change for individual company names
def index(varC):
    error = None
    print(varC)
    if request.method == 'GET':
        print(varC)
        return render_template('index.html', varC=varC)


@app.route('/<varC>/final', methods=['POST'])
def final(varC):
    print(varC)
    phone = re.sub("[-()]","", request.form["phone"])  # Phone Number
    print(phone)
    streetName = request.form.get('sn')
    print(streetName)
    city = request.form.get('city')
    print(city)
    address = request.form.get('state')
    print(address)
    zipcode = request.form.get('zip')
    print(zipcode)
    thisDriver=request.form.get('isDriver')
    thisTime=request.form.get('userTime')
    thisSeats=request.form.get('seats')
    thisCompany= varC
    
    post = {
        "company" : thisCompany,
        "isDriver" : thisDriver,
        "seats": thisSeats,
        "isTime" : thisTime,
        "phone" : phone,
        "city" : city,
        "streetName" : streetName,
        "address" : address,
        "zipcode" : zipcode,
    }

    db.child("Posts").child(id).update(post)

    return render_template('enterName.html')


@app.route('/<varC>/login', methods=['POST'])
def login(varC):
    time = request.form.get('time')  # AM PM BOTH
    print(time)
    dOrp = request.form.get('dp')  # DRIVER / PASSENGER
    error = None
    if dOrp == 'driver':
        print("driver");
        return render_template('driver.html', varC=varC, userTime = time)
    else:
        return render_template('passenger.html', varC=varC, userTime = time)


app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
