from flask import Flask
app = Flask(__name__)
# /welcome
@app.route('/welcome')
def welcome():
    return "welcome"
# Returns “welcome”

# /welcome/home
@app.route('/welcome/home')
def welcome():
    return "welcome home"
# Returns “welcome home”
# /welcome/back
@app.route('/welcome/back')
def welcome():
    return "welcome back"
# Return “welcome back”