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


@app.route('/<varC>/final')
def final(varC):
    return "here are your results"


@app.route('/<varC>/login', methods=['POST', 'GET'])
def login(varC):
    error = None
    if request.args.get('driver') == "I'd like to drive.":
        return render_template('driver.html', varC=varC)
    else:
        return render_template('passenger.html', varC=varC)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
