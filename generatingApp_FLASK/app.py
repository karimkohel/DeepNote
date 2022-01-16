from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/generating", methods=['POST', 'GET'])
def greeter():
	name = str(request.form['name_input'])
	# take seconds and name to pass it to model
	return render_template("request.html", name=name)

@app.route("/main-hall", methods=['POST', 'GET'])
def fame():
	wavs = []
	wavPaths = [item for item in os.listdir("static") if ".wav" in item]
	for path in wavPaths:
		wavs.append({"name": path.replace(".wav", ''), "path":path})
	return render_template("hall.html", wavs=wavs)