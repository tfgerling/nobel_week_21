#!/usr/bin/env python

# pip install flask
from flask import Flask, json, render_template, request
import os

# create instance of Flask app
app = Flask(__name__)

# decorator


@app.route("/")
def echo_hello():
    return app.send_static_file('instruct.html')
    # return "Initial page reached!"


@app.route("/all")
def all():
    json_url = os.path.join(app.static_folder, "", "nobel.json")
    data_json = json.load(open(json_url))

    return render_template('index.html', data=data_json)


# this will be my post method
# @app.route('/add', )
if __name__ == "__main__":
    app.run(debug=True)
