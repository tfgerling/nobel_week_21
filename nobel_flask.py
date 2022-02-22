#!/usr/bin/env python

# pip install flask
from flask import Flask, json, render_template, request, send_file
import os

# create instance of Flask app
app = Flask(__name__)

# decorator


@app.route("/")
def echo_hello():
    return app.send_static_file('instruct.html')


@app.route("/all")
def all():
    json_url = os.path.join(app.static_folder, "", "nobel.json")
    data_json = json.load(open(json_url))

    return render_template('index.html', data=data_json)


# @app.route("/add")
# def form():
    #form_url = os.path.join("templates", "form.html")
    # return send_file(form_url)
#    return render_template("form.html")

@app.route("/add", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # return request.method
        year = request.form['year']
        category = request.form['category']
        id = request.form['id']
        firstname = request.form['firstname']
        surname = request.form['surname']
        motivation = request.form['motivation']
        share = request.form['share']
        nobel_prz = {"year": year,
                     "category": category,
                     "laureates": [{"id": id,
                                    "firstname": firstname,
                                    "surname": surname,
                                    "motivation": motivation,
                                    "share": share}]
                     }
        # return nobel_prz
        json_url = os.path.join(app.static_folder, "", "nobel.json")
        with open(json_url, "r+") as file:
            data_json = json.load(file)
            file.seek(0)
            data_json["prizes"].append(nobel_prz)
            json.dump(data_json, file)
        return "Data successfully added: " + str(nobel_prz)
        return render_template('index.html', text_success)
    else:
        form_url = os.path.join("templates", "form.html")
        return send_file(form_url)


@app.route("/<year>", methods=['GET'])
def add_year(year):
    json_url = os.path.join(app.static_folder, "", "nobel.json")
    data_json = json.load(open(json_url))
    # return json.dumps(data_json)
    data = data_json['prizes']
    # return data
    if request.method == 'GET':
        data_json = json.load(open(json_url))
        data = data_json['prizes']
        year = request.view_args['year']
        output_data = [x for x in data if x['year'] == year]
        return render_template('index.html', data=output_data)


if __name__ == "__main__":
    app.run(debug=True)
