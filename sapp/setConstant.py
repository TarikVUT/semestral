import json

import os
pwd_json = os.getcwd()
json_file = open(pwd_json+'/mainConstants.json')
load_file = json.load(json_file)

LANGUAGE = load_file["LANGUAGE"]
COLORFUL = load_file["COLORFUL"]
SOUND = load_file["SOUND"]

def switch_color_style():
    with open(pwd_json+'/mainConstants.json','r') as file:
        data1 = json.load(file)
        if COLORFUL == True:
            data1['COLORFUL']= False
        else:
            data1['COLORFUL']= True

    with open(pwd_json+'/mainConstants.json','w') as file:
        json.dump(data1,file)

def switch_language():
    with open(pwd_json+'/mainConstants.json','r') as file:
        data2 = json.load(file)
        if LANGUAGE == 'CZ':
            data2['LANGUAGE']= 'EN'
        else:
            data2['LANGUAGE']= 'CZ'

    with open(pwd_json+'/mainConstants.json','w') as file:
        json.dump(data2,file)

def switch_sound():
    with open(pwd_json+'/mainConstants.json','r') as file:
        data3 = json.load(file)
        if SOUND == True:
            data3['SOUND']= False
        else:
            data3['SOUND']= True

    with open(pwd_json+'/mainConstants.json','w') as file:
        json.dump(data3,file)
