import flask
from flask import request, jsonify
import json
import os
import sys


app = flask.Flask(__name__)
gps = {"lat": None,"long":None}
values = {'battery':100,'compass':-180,'location':gps}
science = {'atmospheric_pressure':None,
'air_temperature':None,
'air_humidity':None,
'soil_temperature':None,
'soil_humidity':None,
'gases':None,
'phosphor':None,
'potassium':None,
'nitrogen':None}
retrieval = {'CFL':None,'CFR':None,'CML':None,'CMR':None,'CBL':None,'CBR':None}

@app.route("/")
def admin_control():
	return flask.render_template("admin_control.html")

@app.route("/retrieval")
def retrieval_task():
	return flask.render_template("retrieval.html")

@app.route("/autonomous")
def autonomous():
	return flask.render_template("autonomous.html")

@app.route("/science")
def science_task():
	return flask.render_template("science_task.html")		
	
@app.route("/ping")
def ping():
	response = os.system("ping -c 1 localhost");
	if(response==0):
		return "Connected"
	else:
		return "Not connected"	

@app.route("/science/set_science")
def set_science():
	global science		
	data_string = request.args.get('json')
	data = json.loads(data_string)
	for key in science:
		science[key] = data[key]
	return science	
	
@app.route("/science/get_science")
def get_science():
    global science
    return jsonify(science)

@app.route("/retrieval/set_retrieval")
def set_retrieval():
    global retrieval
    data_string = request.args.get('json')
    data = json.loads(data_string)
    for key in retrieval:
        retrieval[key] = data[key]
    return retrieval

@app.route("/retrieval/get_retrieval")    
def get_retrieval():
    global retrieval
    return jsonify(retrieval)
            	
@app.route("/set_values")
def set_values():
    global values
    data_string = request.args.get('json')
    data = json.loads(data_string)
    for key in values:
        values[key] = data[key]
    return values

@app.route("/get_values")
def get_values():
    global values
    return jsonify(values)
	

if __name__ == "__main__":
    app.run(host = 'localhost', debug=True)
