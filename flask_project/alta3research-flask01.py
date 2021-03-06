#!/usr/bin/python3
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for
from flask import jsonify
import json

app = Flask(__name__)

## This is where we want to redirect users to
@app.route("/success/<answer>") # missing a trailing >
def success(answer):
    return f"Correct! The answer is {answer}\n"

# First endpint
# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("index.html") 

# Second endpoint
# This endpoint determines if user input is right or incorrect
# accepts POST requests 
@app.route("/correct", methods = ["POST"])   
def answer():
    if request.method == "POST":
        if request.form.get('nm'): # check if there's a value first
           
            # then check if it's the value you want
            # Alo redirects the user to the success endpoint 
            if request.form.get('nm').lower() == 'jupiter':
                ans = request.form.get("nm")
                return redirect(url_for("success", answer = ans))
        # complete the line below; if we didn't get returned to /success for getting the answer right, return the client back to / or /start to try again
            else:
                # this redirects the user to the starting point wnen if the input is incorrect
                return redirect(url_for('start'))
   

#json object
gotdata = {
        'characters': [{
            'name': 'Game of Thrones',
            'genre': 'fantasy', 
            'country': 'USA', 
            'number of seasons': 8, 
            'language': 'English',
            },
            {
             'name' : 'Tywin',
             'house' : 'House Lannister',
             'age' : 55  
            },
            {
             'name' : 'Tyrion',
             'house' : 'House Lannister',
             'age' : 26  
            },
            {
             'name' : 'Ramsey Bolton',
             'house' : 'House Bolton',
             'age' : 22  
            },
            {
             'name' : 'Ned Stark',
             'house' : 'House Stark',
             'age' : 41  
            },
            ]}


# Third endpoint
# end point that returns json
@app.route("/json", methods = ["GET"])
def showmethejson():
    return jsonify(gotdata)


# Fourth endpoint
# end point to add new character in dictionary
@app.route("/newcharacter", methods = ["POST"])
def addChar():
    # getting the data from the request in json format
    data = request.json

    # converting data into python readable object
    json_dict = json.loads(data)

    # adding the object into the dictionary
    gotdata['characters'].append(json_dict)

    # this redirect helps the json to be rendered with the changes when a new object is appended to the "characters" game of thrones dictionary/object 
    return redirect('/json')



# runs the server
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

    

