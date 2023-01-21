from flask import jsonify
import datetime
import requests
import os
from bs4 import BeautifulSoup
import json


# Check if there is a recent count (within the last minute) file saved.  If so, use that. Otherwise, fetch more current data.
def fetch_petition_count():
	cur_date_time = datetime.datetime.now()
	cur_hour_minute = cur_date_time.strftime("%Y-%m-%d %H-%M")
	filename = format_filename(cur_hour_minute)
	path = format_path(filename)
	if os.path.isfile(path): 
		# There is a current enough file.  Use it.
		with open(path, "r") as f:
			# print("Using file that already exists")
			content = jsonify(json.load(f))
	else:
		res = make_petition_request()
		target_info = get_target_info_from_response(res)
		weekly_count = get_weekly_count(target_info)
		total_count = get_total_count(target_info)
		content = {"weekly_count" : weekly_count, "total_count": total_count}
		with open(path, "w") as f:
			# print("Creating new file")
			json.dump(content, f)
		content = jsonify(content)
	return content



def format_filename(cur_hour_minute):
	t = cur_hour_minute.replace(" ", "_")
	return t + ".json"

def format_path(filename):
	dir_path = os.path.dirname(os.path.realpath(__file__))
	return dir_path + "/petition_files/" + filename

def make_petition_request():
	x = requests.get('https://www.change.org/p/renew-warrior-nun-for-season-3')
	return x.content

def get_target_info_from_response(res):
	soup = BeautifulSoup(res, 'html.parser')
	target_info = soup.head.script.string
	target_info = target_info.replace("changeTargetingData={", "{")
	target_info = target_info.replace("undefined", "null")
	return json.loads(target_info)

def get_weekly_count(target_info):
	return target_info["petition"]["weeklySignatureCount"]
	
def get_total_count(target_info):
	return target_info["petition"]["signatureCount"]["total"]
