'''
Author : Tarik Alkanan 
'''
import json
from test import *
import os
pwd_json = os.getcwd()
json_file = open(pwd_json+'/mainConstants.json')
load_file = json.load(json_file)

LANGUAGE = load_file["LANGUAGE"]
COLORFUL = load_file["COLORFUL"]
SOUND = load_file["SOUND"]
