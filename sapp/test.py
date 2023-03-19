from tkinter import *
from Constants import *
from setConstant import *
import json
import os

test = True

pwd_json = os.getcwd()

window = Tk()
window.geometry("800x800")
pw = pwd_json +'/mainConstants.json'
json_file = open(pwd_json+'/mainConstants.json')
load_file = json.load(json_file)
SOUND = load_file["SOUND"]

off_img = PhotoImage(file = r'/home/sapp/Images/off-button.png')
on_img = PhotoImage(file = r'/home/sapp/Images/on-button.png')

if COLORFUL == True:
            color_toggle_img = on_img
else:
            color_toggle_img = off_img

if LANGUAGE == 'CZ':
             language_toggle_img = on_img
else:
             language_toggle_img = off_img

if SOUND == True:
             sound_toggle_img = on_img
else:
             sound_toggle_img = off_img

def toggle_json_sound():
            # Read the JSON data from the file
            with open(pwd_json+'/mainConstants.json') as f:
                data = json.load(f)

            # Toggle the value of the "toggle_value" key
            data['SOUND'] = not data['SOUND']

            # Write the modified data back to the file
            with open(pwd_json+'/mainConstants.json', 'w') as f:
                json.dump(data, f)

            # Update the label to display the new value
            if data['SOUND']:
                sound_btn.config(image=on_img)
            else:
                sound_btn.config(image=off_img)

def toggle_json_color():
                # Read the JSON data from the file
    with open(pwd_json+'/mainConstants.json') as f:
                    data = json.load(f)

                # Toggle the value of the "toggle_value" key
    data['COLORFUL'] = not data['COLORFUL']

                # Write the modified data back to the file
    with open(pwd_json+'/mainConstants.json', 'w') as f:
                    json.dump(data, f)

                # Update the label to display the new value
    if data['COLORFUL']:
                color_btn.config(image=on_img)
    else:
                 color_btn.config(image=off_img)



def toggle_json_language():
                # Read the JSON data from the file
    with open(pwd_json+'/mainConstants.json') as f:
                    data = json.load(f)

                # Toggle the value of the "toggle_value" key
    data['LANGUAGE'] = not data['LANGUAGE']

                # Write the modified data back to the file
    with open(pwd_json+'/mainConstants.json', 'w') as f:
                    json.dump(data, f)

                # Update the label to display the new value
    if data['LANGUAGE']:
                language_btn.config(image=on_img)
    else:
                 language_btn.config(image=off_img)
                 

if SOUND == True:
    sound_toggle_img=on_img
else:
        sound_toggle_img=off_img

sound_lbl = Label(window, text="- Sound:", font="none 12 bold")
sound_lbl.grid(row=1, column=0, sticky=W, pady=8, padx = 10)

sound_btn = Button(window,image= sound_toggle_img,borderwidth=0, command= toggle_json_sound)
sound_btn.grid(row=1, column=2,sticky = E,padx = 10, pady=8)
sound_btn.image= sound_toggle_img

color_lbl = Label(window, text="- Color:", font="none 12 bold")
color_lbl.grid(row=3, column=0, sticky=W, pady=8, padx = 10)

color_btn = Button(window,image= color_toggle_img,borderwidth=0, command= toggle_json_color)
color_btn.grid(row=3, column=2,sticky = E,padx = 10, pady=8)
color_btn.image= sound_toggle_img

language_lbl = Label(window, text="- Language:", font="none 12 bold")
language_lbl.grid(row=5, column=0, sticky=W, pady=8, padx = 10)

language_btn = Button(window,image= language_toggle_img,borderwidth=0, command= toggle_json_language)
language_btn.grid(row=5, column=2,sticky = E,padx = 10, pady=8)
language_btn.image= sound_toggle_img
window.mainloop()