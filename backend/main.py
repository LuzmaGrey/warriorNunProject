from flask import Flask, render_template
import tweepy
import schedule
import time 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
# Define the hashtag you want to count
hashtag = '#SaveWarriorNun'

# Authenticate with Twitter API
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_secret = 'your_access_secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Define a global variable to store the tweet count
tweet_count = 0

# Define a function to count tweets and update the global variable
def count_tweets():
    global tweet_count
    tweet_count = len(tweepy.Cursor(api.search_tweets, hashtag).items())

# Schedule the count_tweets function to run every day at 9:00 AM
schedule.every().day.at('00:00').do(count_tweets)

# Define a function to run the scheduler in the background
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the scheduler in a separate thread
import threading
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()
if __name__ == '__main__':
    app.run(debug=True)
