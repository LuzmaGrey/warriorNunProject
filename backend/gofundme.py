from flask import jsonify
import datetime
import requests
import os
from bs4 import BeautifulSoup
import json
import utils.file_format as ff

def fetch_gofundme():
	res = make_gofundme_request()
	target_info = get_target_info_from_response(res)
	current_amount = get_current_amount(target_info)
	goal_amount = get_goal_amount(target_info)
	content = {"current_amount" : current_amount, "goal_amount": goal_amount}
	content = jsonify(content)
	return content


def make_gofundme_request():
	x = requests.get('https://www.gofundme.com/f/get-warrior-nun-the-attention-it-deserves')
	return x.content


def get_target_info_from_response(res):
	soup = BeautifulSoup(res, 'html.parser')
	target_info = json.loads(soup.find('script', id="__NEXT_DATA__").text)
	nested_target_info = json.loads(target_info['props']['initialState'])
	nested_target_info = nested_target_info["feed"]["campaign"]
	return nested_target_info

def get_current_amount(target_info):
	return target_info["current_amount"]
	
def get_goal_amount(target_info):
	return target_info["goal_amount"]
