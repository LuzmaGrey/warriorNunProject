from flask import jsonify
import datetime
import requests
import os
from bs4 import BeautifulSoup
import json
import utils.file_format as ff

def fetch_petition_count():
	res = make_petition_request()
	target_info = get_target_info_from_response(res)
	weekly_count = get_weekly_count(target_info)
	total_count = get_total_count(target_info)
	content = {"weekly_count" : weekly_count, "total_count": total_count}
	content = jsonify(content)
	return content


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
