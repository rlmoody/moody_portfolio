from flask import Flask
from flask import redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
	return redirect(url_for("home"))

@app.route("/home")
def home():
	return "Home"

@app.route("/about")
def about():
	return "About Me"

@app.route("/projects")
def projects():
	return "Projects"

@app.route("/hello")
def hello_world():
	return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
