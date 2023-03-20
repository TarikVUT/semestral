#!/bin/bash

user=$(echo $SUDO_USER)
dir_to_install="/home/"$user
echo The user is $user
echo Installation direction $dir_to_install
dnf update
check_command_success(){

command_run="$1"
message_to_user="$2"

$command_run

if [ $? -eq 0 ]	
then
	echo "---> Installation $message_to_user was successful<---"
else
	echo "*** Installation $message_to_user failed ***"
	exit 0
fi
}

if [ -f /etc/fedora-release ]
then	
        echo "Your system is Fedora, install virtuallenv"
        #install virtualenv for python
        check_command_success "sudo dnf install virtualenv -y" "virtualenv"

	#Download source from Githut
	check_command_success "git clone https://github.com/TarikVUT/semestral.git /tmp/OS" "sapp"
	#check_command_success "git clone -b sapp https://github.com/forsenior/os.git $dir_to_install/OS" "sapp"
	
	#Change OS owner
	check_command_success "sudo chown -R $user /tmp/OS" "OS"
	
	#Move sapp,stext to /home/
	check_command_success "sudo mv /tmp/OS/sapp /home" "move sapp to /home"
	check_command_success "sudo mv /tmp/OS/stext /home" "move stext to /home"
	check_command_success "sudo mv /tmp/OS/sweb /home" "move sweb to /home"
	check_command_success "sudo mv /tmp/OS/smail /home" "move smail to /home"
	
	#Create virtual env inside sapp,stext,sweb,smail.
	check_command_success "virtualenv /home/sapp/env" "create sapp env"
	check_command_success "virtualenv /home/stext/env" "create stext env"
	check_command_success "virtualenv /home/sweb/env" "create sweb env"
	check_command_success "virtualenv /home/smail/env" "create smail env"
	
	check_command_success "sudo chown -R $user /home/sapp /home/stext /home/sweb /home/smail" "Change owner"

	source /home/stext/env/bin/activate && pip install pyqt5 xhtml2pdf  bs4 markdown && deactivate
	source /home/sapp/env/bin/activate && pip install pillow pygame && dnf install python3-tkinter && deactivate
	source /home/sapp/env/bin/activate && dnf install python3-tkinter && deactivate
	source /home/sapp/env/bin/activate && dnf install python3-tkinter && deactivate
	
	
	#Create autostart file to run sapp
	mkdir /home/tarik/.config/autostart && echo -e "[Desktop Entry]\nType=Application\nName=Pyapp\nExec=/home/sapp/env/bin/python /home/sapp/main.py\nTerminal=false" >/home/tarik/.config/autostart/autostart.desktop && chmod +x /home/tarik/.config/autostart/autostart.desktop
	
	passwd -d $user
	
	init 6
	
	#/home/sapp/env/bin/python /home/sapp/main.py

	#pip install pillow pygame ,pyqt5 xhtml2pdf  bs4 markdown
	
	
	
	
	# disable window button

else
        echo "ERROR"
fi

