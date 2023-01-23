import flask

# API Endpoint Imports
import petition_count as pc
import gofundme as gfm

app = flask.Flask(__name__)

@app.route("/")
def home():
	return "There is a test page to check your server is running."

@app.route("/petition_count")
def petition_count():
	return pc.fetch_petition_count()

@app.route("/gofundme")
def gofundme():
	return gfm.fetch_gofundme()

app.run()