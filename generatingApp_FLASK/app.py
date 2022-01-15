from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("What do you want the name of your song to be?")
	flash("How long do you want your song?")
	return render_template("index.html")

@app.route("/generating", methods=['POST', 'GET'])
def greeter():
	flash(str(request.form['name_input']) + ", is generating now for you! " + str(request.form['min_input']))
	#fun(request.form['name_input'],request.form['min_input'])
	return render_template("request.html")
