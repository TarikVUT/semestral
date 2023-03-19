import tkinter as tk
import json
import os


pwd_json = os.getcwd()
pw = pwd_json +'/mainConstants.json'

def toggle_json_value():
    # Read the JSON data from the file
    with open(pw) as f:
        data = json.load(f)

    # Toggle the value of the "toggle_value" key
    data['SOUND'] = not data['SOUND']

    # Write the modified data back to the file
    with open(pw, 'w') as f:
        json.dump(data, f)

    # Update the label to display the new value
    if data['SOUND']:
        label.config(text='SOUND')
    else:
        label.config(text='SOUND')

# Create the Tkinter window and widgets
window = tk.Tk()
window.geometry("300x300")
button = tk.Button(window, text='Toggle', command=toggle_json_value)
label = tk.Label(window, text='Toggle is OFF')
button.pack()
label.pack()

# Run the Tkinter event loop
window.mainloop()