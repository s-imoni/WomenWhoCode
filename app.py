import re

from flask import Flask, url_for, render_template, request

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
    streetName = request.form["sn"].title()
    print(streetName)
    city = request.form["city"]
    print(city)
    address = request.form["state"]
    print(address)
    zipcode = request.form["zip"]
    print(zipcode)
    
    return "here are your results"


@app.route('/<varC>/login', methods=['POST'])
def login(varC):
    time = request.form.get('time')  # AM PM BOTH
    print(time)
    dOrp = request.form.get('dp')  # DRIVER / PASSENGER
    error = None
    if dOrp == 'driver':
        print("driver");
        return render_template('driver.html', varC=varC)
    else:
        return render_template('passenger.html', varC=varC)


app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
