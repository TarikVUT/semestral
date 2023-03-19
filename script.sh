#!/bin/bash

user=$(echo $SUDO_USER)
dir_to_install="/home/"$user
echo The user is $user
echo Installation direction $dir_to_install
check_command_success(){

command_run="$1"
message_to_user="$2"

$command_run

if [ $? -eq 0 ]	
then
	echo "---> Installation $message_to_user was successful<---"
else
	echo "*** Installation $message_to_user failed ***"
	return 0
fi
}

if [ -f /etc/fedora-release ]
then	
        echo "Your system is Fedora, install virtuallenv"
        #install virtualenv for python
        check_command_success "sudo dnf install virtualenv -y" "virtualenv"

	#Download source from Githut
	check_command_success "git clone https://github.com/TarikVUT/semestral.git $dir_to_install/OS" "sapp"
	#check_command_success "git clone -b sapp https://github.com/forsenior/os.git $dir_to_install/OS" "sapp"
	
	#Change OS owner
	check_command_success "sudo chown -R $user /home/$user/OS" "OS"
	
	#Move sapp,stext to /home/
	check_command_success "sudo mv $dir_to_install/OS/sapp /home/root" "trans sapp"
	check_command_success "sudo mv $dir_to_install/OS/stext /home/root" "trans stext"
	
	#Create virtual env inside sapp,stext,sweb,smail.
	check_command_success "virtualenv /home/root/sapp/env" "create sapp env"
	check_command_success "virtualenv /home/root/stext/env" "create sapp env"
	#check_command_success "sudo chown -R $user /home/root/sapp" "sapp"
	source /home/root/sapp/env/bin/activate && pip install pillow pygame 
	
	source /home/root/stext/env/bin/activate && pip install pyqt5 xhtml2pdf  bs4 markdown
	#pip install pillow pygame ,pyqt5 xhtml2pdf  bs4 markdown
	
	#Create autostart file to run sapp
	
	
	# disable window button

else
        echo "ERROR"
fi

