from flask import Flask, render_template, request


app = Flask(__name__, template_folder = 'templates')

@app.route("/")
def index():    
    return render_template("jax.html")


@app.route("/greet")
def greet():
    return render_template("greet.html", name = request.args.get("name"))
