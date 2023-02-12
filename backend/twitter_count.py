import datetime
import os
import requests
import utils.file_format as ff
import json
from flask import jsonify

def fetch_twitter_count():
    res = make_request()
    count = get_count(res)
    content = {"last_7_days_count" : count }
    content = jsonify(content)
    return content

def make_request():
    token = os.getenv('TWT_TOKEN')
    headers = {"Authorization": "Bearer {}".format(token)}

    # For this endpoint we need Academic Research or Enterprise access.
    #endpoint = "https://api.twitter.com/2/tweets/counts/all"
    #params = {'query': '#SaveWarriorNun','granularity': 'day', 'start_time': '2022-12-13T00:00:00Z'}
    
    # Free access endpoint, gives count for the last 7 days only.
    endpoint = "https://api.twitter.com/2/tweets/counts/recent"
    params = {'query': '#SaveWarriorNun','granularity': 'day'}

    x = requests.request("GET", endpoint, headers = headers, params = params)
    return x.json()

def get_count(content):
    return sum([day_data['tweet_count'] for day_data in content['data']])