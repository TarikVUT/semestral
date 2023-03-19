'''
Author : Tarik Alkanan

'''
import os
'''
The line below is to hide {pygame 2.1.2 (SDL 2.0.16, Python 3.10.7)
Hello from the pygame community. https://www.pygame.org/contribute.html
}
'''
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"       

from tkinter import *
from Constants import *
from setConstant import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import pygame 
from tkinter import ttk
from pygame import mixer

import importlib
import hashlib
import string

def main():
    ACTIVEBACKGROUND = "#4b4c4b"
    COLOR_BG = "#D3D3D3"
    pwd = os.getcwd()   #get work dir
    #Create the window
    window = Tk()
    screen_width = window.winfo_screenwidth()          ##get screen width
    screen_height= window.winfo_screenheight()         ##get screen height
    button_width = int(screen_width/2 - 10)
    button_height = int(screen_height/2 - 10)

    pygame.mixer.init()

    window.geometry("%dx%d" % (screen_width,screen_height))   
    window.attributes('-fullscreen',True)
    window.resizable(0,0)
    window.title("Senior OS")

    #Resize image 
    def resizeImage(image,width,height):
        resizedImage=image.resize((int(screen_width/2 - 10),int(screen_height/2 - 10)))
        newImage=ImageTk.PhotoImage(resizedImage)
        return newImage
    
    #try to open images for icons
    #In case get error
    try:
        img_smail=(Image.open(SMAIL_IMG))       ##smail image

        img_shutdown=(Image.open(SHUTDOWN_IMG))    ##shutdown image

        img_sweb=(Image.open(SWEB_IMG))   ##sweb image

        img_stext=(Image.open(STEXT_IMG)) ##stext image
    
        img_cancel=(Image.open(CANCEL_IMG)) ##cancel image

    except :##### Set defualt desktop in case can't upload images

        img_smail=Image.new('RGB',(button_width,button_height),color = (180,124,243))       ##smail
        text_smail=ImageDraw.Draw(img_smail)
        text_smail.text((button_width/2,button_height/2),"Email", fill = (255,255,255))
        
        img_shutdown=Image.new('RGB',(button_width,button_height),color = (215,48,48))   #shutdown
        text_shutdown=ImageDraw.Draw(img_shutdown)
        text_shutdown.text((button_width/2,button_height/2),"Shutdown", fill = (255,255,255))
        
        img_sweb=Image.new('RGB',(button_width,button_height),color = (0,242,113))  #sweb
        text_sweb=ImageDraw.Draw(img_sweb)
        text_sweb.text((button_width/2,button_height/2),"Browser", fill = (255,255,255))
        
        img_stext=Image.new('RGB',(button_width,button_height),color = (235,212,5)) #stext
        text_stext=ImageDraw.Draw(img_stext)
        text_stext.text((button_width/2,button_height/2),"Editor", fill = (255,255,255))
        
        img_cancel=Image.new('RGB',(button_width,button_height),color = (25,215,150)) #cancel
        text_cancel=ImageDraw.Draw(img_cancel)
        text_cancel.text((button_width/2,button_height/2),"Cancel", fill = (255,255,255))
    
        messagebox.showerror('Error','Can not open images for icons. The App will start without icons')

    '''
    Resize the imported images to set it in the buttons 
    '''
    img_shutdown_resized=resizeImage(img_shutdown,screen_width,screen_height)
    img_smail_resized=resizeImage(img_smail,screen_width,screen_height)
    img_sweb_resized=resizeImage(img_sweb,screen_width,screen_height)
    img_stext_resized=resizeImage(img_stext,screen_width,screen_height)
    image_cancel_resized=resizeImage(img_cancel,screen_width,screen_height)



    # shutdown function
    def shutdown_system():  
        os.system("shutdown now -h")
        
    #function to reboot the system
    def reboot_sys():
        os.system('reboot')
        
    #Function to hash passwd   
    def hash_fun(string):
        hashed_string = hashlib.sha256(string.encode('utf-8')).hexdigest()
        return hashed_string
        
    '''
    Sound functions
    '''
    def play_shutdown(event):
        if SOUND:
            pygame.mixer.music.load(SHUTDOWN_WAV)
            pygame.mixer.music.play()
        
    def play_sweb(event):
        if SOUND:
            pygame.mixer.music.load(SWEB_WAV)
            pygame.mixer.music.play()
        
    def play_smail(event):
        if SOUND:
            pygame.mixer.music.load(SMAIL_WAV)
            pygame.mixer.music.play()
        
    def play_stext(event):
        if SOUND:
            pygame.mixer.music.load(STEXT_WAV)
            pygame.mixer.music.play()
            
    def play_cancel(event):
        if SOUND:
            pygame.mixer.music.load(CANCEL_WAV)
            pygame.mixer.music.play()

    #turn on/off sound

    
    #open stext app
    def stext_window():
    
        os.system('/home/stext/stextenv/bin/python /home/stext/v.py')
        '''
        try:
            if os.system('home/stext/stextenv/bin/python3 /home/stext/main.py') != 0 :
                raise Exception()
        except (Exception) :
            messagebox.showerror('Error','Can not open texteditor app')
        '''    
    #open smail app     
    def smail_window():
        try:
            if os.system('/home/smail/smailenv/bin/python /home/smail/smail.py') != 0 :
                raise Exception()
        except (Exception) :
            messagebox.showerror('Error','Can not open texteditor app')

    #open sweb app
    def sweb_window():
        try:
            if os.system('python /home/smail/main.py') != 0 :
                raise Exception()
        except (Exception) :
            messagebox.showerror('Error','Can not open texteditor app')
            
    #open smail  
    #def email_window():

    #New window to change passwd

    #def personlize():
        


    def change_password():
        def clear_entry_password():
            pw_box.delete(0,'end')
            pw_confirm_box.delete(0,'end')
        def click():
            username = username_box.get()
            password = pw_box.get()
            confirmed_pw = pw_confirm_box.get()
            file_user= open("/home/sapp/users.txt", "r+")
            user_from_file=file_user.read()
            caps = string.ascii_uppercase
            numbers = []
            for i in range(10):
                numbers.append(str(i))
            special_chars = ['!', '@', '#', '$', '%']
            name_check = False

            def number_found(name):
                found = False
                for number in numbers:
                    if name.find(number) > -1:
                        found = True
                return found
            
            #Capital letter
            def caps_found(pw):
                found = False
                for letter in caps:
                    if pw.find(letter) > -1:
                        found = True
                return found

            def special_found(pw):
                found = False
                for char in special_chars:
                    if pw.find(char) > -1:
                        found = True
                return found

        
            if username != user_from_file[:-1]:
                output_info.configure(text="Invalid user",font="green 15 bold")
                username_box.delete(0,'end')
                return
            if password != confirmed_pw and len(password) > 7:
                output_info.configure(text="Passwords do not match")
                clear_entry_password()
                return
            if not number_found(password):
                output_info.configure(text="Password must contain a number")
                clear_entry_password()
                return
            if not special_found(password):
                output_info.configure(text="Password must contain a special character (!, @, #, $, %)")
                clear_entry_password()
                return
            if not caps_found(password):
                output_info.configure(text="Password must contain a capital letter")
                clear_entry_password()
                return
            if len(password) < 8:
                output_info.configure(text="Password must be at least 8 characters long")
                clear_entry_password()
                return

            file_pass = open("/home/sapp/test.txt", "w")
            file_pass.writelines(hash_fun(password))
            file_pass.close()  
            change_password_win.destroy()
            messagebox.showinfo("info", "Password change was successful")

        change_password_win = Toplevel(window)
        change_password_win.title("Set new password")

        change_password_win.configure(bg=COLOR_BG)
        change_password_win.resizable(0,0)

        user_lbl = Label(change_password_win, text="Enter your username:", bg=COLOR_BG, font="none 12 bold")
        user_lbl.grid(row=1, column=0, sticky=EW, pady=8)
        pass_lbl = Label(change_password_win, text="Enter your password:", bg=COLOR_BG, font="none 12 bold")

        pass_lbl.grid(row=3, column=0, sticky=EW, pady=8)
        cpass_lbl = Label(change_password_win, text="Confirm password:", bg=COLOR_BG, font="none 12 bold")
        cpass_lbl.grid(row=5, column=0, sticky=EW, pady=8)

        username_box = Entry(change_password_win, width=40, bg="white")
        username_box.grid(row=2, column=0)

        pw_box = Entry(change_password_win, width=40, bg="white",show='*')
        pw_box.grid(row=4, column=0)

        pw_confirm_box = Entry(change_password_win, width=40, bg="white",show='*')
        pw_confirm_box.grid(row=6, column=0)

        sub_btn=Button(change_password_win, text="Change", width=6, command=click) 
        sub_btn.grid(row=7, column=0, pady=10)

        output_info = Label(change_password_win, text="Welcome", bg=COLOR_BG, font="none 15", width=60)
        output_info.grid(row=8, column=0, sticky=EW, pady=10)

    #### Administrator window ####
    def administrator_window():
        #start up the gdm (gdm)
        def run_gdm():
            os.system('sudo systemctl start gdm')
        
        def change_pass():
            os.system('python /home/sapp/pass.py')
        

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
                language_btn.config(image=cz_img)
            else:
                 language_btn.config(image=en_img)
                 


        off_img = PhotoImage(file = r'/home/sapp/Images/off-button.png')
        on_img = PhotoImage(file = r'/home/sapp/Images/on-button.png')
        cz_img = PhotoImage(file = r'/home/sapp/Images/cz-button.png')
        en_img = PhotoImage(file = r'/home/sapp/Images/en-button.png')
        start_img = PhotoImage(file = r'/home/sapp/Images/start.png')
        close_img = PhotoImage(file = r'/home/sapp/Images/close.png')
        change_img = PhotoImage(file = r'/home/sapp/Images/change.png')
        reboot_img = PhotoImage(file = r'/home/sapp/Images/reboot.png')

        ############ Check data from mainConstants.JSON ########
        if COLORFUL :
            color_toggle_img = on_img
        else:
            color_toggle_img = off_img

        if LANGUAGE :
             language_toggle_img = cz_img
        else:
             language_toggle_img = en_img

        if SOUND :
             sound_toggle_img = on_img
        else:
             sound_toggle_img = off_img



        root_win = Toplevel(window)
        root_win.title('Administrator window')
        root_win_width = 430
        root_win_height = 500
        x_point_root_win = (screen_width/2)-(root_win_width/2)
        y_point_root_win = (screen_height/2)-(root_win_height/2)
        root_win.geometry("%dx%d+%d+%d"%(root_win_width,
                                root_win_height,x_point_root_win,
                                y_point_root_win))
        #root_win.configure(bg=COLOR_BG)
        root_win.resizable(0,0)

        ###### LABEL ######
        sound_lbl = Label(root_win, text="- Sound:", font="none 12 bold")
        sound_lbl.grid(row=1, column=0, sticky=W, pady=8, padx = 10)

        color_lbl = Label(root_win, text="- Color style:", font="none 12 bold")
        color_lbl.grid(row=3, column=0, sticky=W, pady=8, padx = 10)

        language_lbl = Label(root_win, text="- Language:", font="none 12 bold")
        language_lbl.grid(row=5, column=0, sticky=W, pady=8, padx = 10)

        GDM_lbl = Label(root_win, text="- Run GDM:", font="none 12 bold")
        GDM_lbl.grid(row=7, column=0, sticky=W, pady=8, padx = 10)

        close_lbl = Label(root_win, text="- Close desktop:",  font="none 12 bold")
        close_lbl.grid(row=9, column=0, sticky=W, pady=8, padx = 10)

        change_lbl = Label(root_win, text="- Change user's password",  font="none 12 bold")
        change_lbl.grid(row=11, column=0, sticky=W, pady=8, padx = 10)

        reboot_lbl = Label(root_win, text="- Reboot the OS",  font="none 12 bold")
        reboot_lbl.grid(row=13, column=0, sticky=W, pady=8, padx = 10)
        
        ######## BUTTONS ########

        sound_btn = Button(root_win,image= sound_toggle_img,borderwidth=0,command= toggle_json_sound)
        sound_btn.grid(row=1, column=2,sticky = E,padx = 10, pady=8)
        sound_btn.image= sound_toggle_img

        color_btn = Button(root_win,image= color_toggle_img,borderwidth=0,command = toggle_json_color)
        color_btn.grid(row=3, column=2,sticky = E,padx = 10, pady=8)
        color_btn.image= color_toggle_img

        language_btn = Button(root_win,image= language_toggle_img,borderwidth=0,command=toggle_json_language)
        language_btn.grid(row=5, column=2,sticky = E,padx = 10, pady=8)
        language_btn.image= language_toggle_img

        GDM_btn=Button(root_win,overrelief = SUNKEN,image = start_img,borderwidth=0,                  
                    command=lambda:[root_win.destroy(),run_gdm()])            
        GDM_btn.grid(row=7, column=2,sticky = E,padx = 10, pady=8)
        GDM_btn.image= start_img
        
        close_btn=Button(root_win,image = close_img,borderwidth= 0,
                    command = window.destroy)                
        close_btn.grid(row=9, column=2,sticky = E,padx = 10, pady=8)
        close_btn.image=close_img

        change_btn=Button(root_win,image = change_img,borderwidth= 0,
                    command=lambda:[root_win.destroy(),change_password()]) 
        change_btn.grid(row=11, column=2,sticky = E,padx = 10, pady=8)
        change_btn.image = change_img
        
        reboot_btn=Button(root_win,image=reboot_img,borderwidth=0,
                    command=lambda:[root_win.destroy(),reboot_sys()]) 
        reboot_btn.grid(row=13, column=2,sticky = E,padx = 10, pady=8)
        reboot_btn.image= reboot_img
    #### check root password ####
    def check_administrator_window():
        global count
        count = 0
        #Function to clean entry            
        def clear_entry():
            username_entry.delete(0,'end')
            password_entry.delete(0,'end')
        def get_data(): 
            global count
            count =count + 1
            file_users= open("/home/sapp/users.txt", "r")
            file_passwords= open("/home/sapp/passwords.txt", "r")
            #get values from files
            users_from_file = file_users.read()
            passwords_from_file=file_passwords.read()
            file_passwords.close()
            file_users.close()
        
            #Get values from entry
            username= check_username.get()
            password=check_password.get() 
            if users_from_file[:-1] == username and passwords_from_file[:-1] == hash_fun(password):
                check_root_win.destroy()
                administrator_window()
                return
                
            if count >= 3 :
                info_label.config( text = 'Oops', fg = 'red',font=("Helvetica",12))
                check_root_win.destroy()
                messagebox.showwarning("Warning", "Entering 3-times incorrect password")
                return 
                
            if username == '' or password =='':
                info_label.config( text = 'All fields requried !', fg = 'red',font=("Helvetica",12))
                clear_entry()
            else:
                info_label.config(text = 'Incorrect inputs',fg = 'red',font=("Helvetica",12))
                clear_entry()

        check_username = StringVar()
        check_password = StringVar()
        
        check_root_win = Toplevel(window)
        check_root_win.title('Permission only for Administrator')
        check_root_win_width = 350
        check_root_win_height = 200
        
        x_point=(screen_width/2)-(check_root_win_width/2)
        y_point=(screen_height/2)-(check_root_win_height/2)
        check_root_win.geometry("%dx%d+%d+%d"%(check_root_win_width,
        check_root_win_height,x_point,y_point))
        check_root_win.resizable(0,0)
        
        
        #Labels
        username_label = Label(check_root_win, text="User Name",font=("None 10 bold"))
        username_label.grid(row=0, column=0, pady = 10)
        password_label = Label(check_root_win,text="Password",font=("None 10 bold"))
        password_label.grid(row=1, column=0, pady = 8)
        info_label = Label(check_root_win)
        info_label.grid(row = 2 ,column = 1, pady =10)
        
        #Entry
        username_entry = Entry(check_root_win, textvariable=check_username)
        username_entry.grid(row=0, column=1, pady = 10)
        password_entry = Entry(check_root_win, textvariable=check_password, show='*')
        password_entry.grid(row=1,column=1, pady = 8)
        
        #Button
        login_button = Button(check_root_win, text="Login",bd = 2,font=("None 10 bold"),
                                            overrelief = SUNKEN, 
                                            command=get_data)
        login_button.grid(row=3, column=0, sticky = W ,padx = 20)
        
        close_button = Button(check_root_win, text="Close",bd = 2,font=("None 10 bold"),
                                            overrelief = SUNKEN,
                                            command=check_root_win.destroy)
        close_button.grid(row=3, column=3, sticky = W )

    ##### Shut down window ######  
    def shutdown_window():
        confirm_win = Toplevel(window)
        confirm_win.title('Shut down window')
        confirm_win.geometry("%dx%d" % (screen_width,screen_height))
        confirm_win.attributes('-fullscreen',True)
        confirm_win.resizable(0,0)
        #confirm_win.configure(bg=COLOR_BG)
        confirm_win.resizable(0,0)  
        #Buttons
        #ok button
        ok_btn =Button(confirm_win,  bd=5,overrelief = SUNKEN,
                    image=img_shutdown_resized,background=SHUTDOWN_BACKGROUND,
                    activebackground=SHUTDOWN_ACTIVEBACKGROUND,
                    
                    command=shutdown_system)
        ok_btn.image=img_shutdown_resized

        #cancel button
        cancel_btn =Button(confirm_win, fg="#7d2811",bd=5,overrelief = SUNKEN,
                        image=image_cancel_resized,background=CANCEL_BACKGROUND,
                        activebackground=CANCEL_ACTIVEBACKGROUND,
                        command=confirm_win.destroy)
        cancel_btn.image=image_cancel_resized
    
        #root button 
        root_btn=Button(confirm_win, text='Settings',
                        font=('Times', 20),
                        fg="#7d2811",bd=0,bg = COLOR_BG,
                        activebackground=COLOR_BG,
                        command=lambda:[confirm_win.destroy(),check_administrator_window()])   #run two functions
        
    

        
        root_btn.grid(row = 0, column = 0,sticky = W)
        ok_btn.place(x=0,y=screen_height/4)
        cancel_btn.place(x= screen_width/2,y=screen_height/4)    
        ok_btn.bind('<Enter>',play_shutdown)
        cancel_btn.bind('<Enter>',play_cancel)


    '''
    Import images for desktop
    '''




    #Button on desktop

    swebButton=Button(window,image = img_sweb_resized,
                        activebackground=SWEB_ACTIVEBACKGROUND,background=SWEB_BACKGROUND,
                        bd=5,overrelief = SUNKEN,
                        command=window.destroy) #browser_window


    smailButton=Button(window,image =img_smail_resized,
                    activebackground=SMAIL_ACTIVEBACKGROUND,background=SMAIL_BACKGROUND,
                    overrelief = SUNKEN,
                    bd=5, command = smail_window)


    stextButton=Button(window,image = img_stext_resized,
                        activebackground=STEXT_ACTIVEBACKGROUND,background=STEXT_BACKGROUND,
                        bd=5,overrelief = SUNKEN,
                        command=stext_window)
    shutdownButton =Button(window,image =img_shutdown_resized,
                    activebackground=SHUTDOWN_ACTIVEBACKGROUND,background=SHUTDOWN_BACKGROUND,
                    overrelief = SUNKEN,
                    bd=5,command=shutdown_window)
                    
    shutdownButton.place(x=screen_width/2,y=screen_height/2)                  
    smailButton.place(x=screen_width/2,y=0)
    stextButton.place(x=0,y=screen_height/2)                  
    swebButton.place(x=0,y=0)
    #Sound event

    smailButton.bind('<Enter>',play_smail)
    stextButton.bind('<Enter>',play_stext)
    swebButton.bind('<Enter>',play_sweb)
    shutdownButton.bind('<Enter>',play_shutdown)

    window.mainloop()
if __name__ == "__main__":
   main()
