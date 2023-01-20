import flask

# API Endpoint Imports
import petition_count as pc

app = flask.Flask(__name__)

@app.route("/")
def home():
	return "There is a test page that your server is running."

@app.route("/petition_count")
def petition_count():
	return pc.fetch_petition_count()

app.run()