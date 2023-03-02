import flask

# API Endpoint Imports
import petition_count as pc
import gofundme as gfm
import twitter_count as twt

app = flask.Flask(__name__)

@app.route("/")
def home():
	return "There is a test page to check your server is running.\
	The endpoints are: /petition_count, /gofundme, and /twitter_count"

@app.route("/petition_count")
def petition_count():
	return pc.fetch_petition_count()

@app.route("/gofundme")
def gofundme():
	return gfm.fetch_gofundme()

@app.route("/twitter_count")
def twitter_count():
	return twt.fetch_twitter_count()

#app.run()
