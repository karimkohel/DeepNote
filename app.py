from concurrent.futures import thread
from flask import Flask, render_template, request, flash
import os
from generate import main as model_generate
from threading import Thread

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
t = Thread(target=model_generate, )


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/generating", methods=['POST', 'GET'])
def greeter():
	name = str(request.form['name_input'])
	name = 'static/generated/'+name + '.wav'
	time = int(request.form['min_input'])
	if time > 5:
		time = 5
	t = Thread(target=model_generate, args=(name, time))
	t.start()
	return render_template("generating.html", name=name)

@app.route("/main-hall", methods=['POST', 'GET'])
def fame():
	wavs = []
	wavPaths = [item for item in os.listdir("static/generated") if ".wav" in item]
	for path in wavPaths:
		wavs.append({"name": path.replace(".wav", ''), "path":path})
	return render_template("hall.html", wavs=wavs)