from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("Do you Love techno music?, I already Know your answer , So What do you want the name of your song to be?")
	return render_template("index.html")

@app.route("/generating", methods=['POST', 'GET'])
def greeter():
	flash(str(request.form['name_input']) + ", is generating now for you!")
	return render_template("index.html")
