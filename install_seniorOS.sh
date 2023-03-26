#!/bin/bash

user=$(echo $SUDO_USER)
dir_to_install="/home/"$user
echo The user is $user
echo Installation direction $dir_to_install
#dnf update -y

check_command_success(){

command_run="$1"
message_to_user="$2"

$command_run

if [ $? -eq 0 ]	
then
	echo -e "\n--->  $message_to_user was successful <---"
else
	echo -e "\n***  $message_to_user failed :( ***"
	exit 0
fi
}

check_if_os_exists(){

downloaded_file="OS"

if [ -e "/tmp/$downloaded_file" ]
then
	i=1
	while [ -e "/tmp/OS_$i" ]
	do 
		let i++
	done
	
	new_dir="OS_$i"
	#mkdir /tmp/$new_file
	
	else
	new_dir="OS"

fi

}

delete_existing_dir(){
dis_dir="$1"

if [ -e "/home/$1" ]
then 
	rm -rf /home/$1
fi
}
check_if_system_exists(){

if [ -e "/home/sapp" ]
then
	echo -e "One of the diractories (/home/sapp or /home/smail or /home/stext or /home/sweb) exists."
	read -p "Do you want to replace it? [y/N] " confirmation
	if [[ "$confirmation" =~ ^[Yy]$ ]]
		then
			echo "The old folder will be replaced"
		else	
			echo "The installation has stoped"
			exit 0
	fi
else 
	echo "The check was successful"

fi
}

if [ -f /etc/fedora-release ]
then	
        echo "Your system is Fedora"
        #install virtualenv for python
        #check_command_success "sudo dnf install virtualenv -y" "Install virtualenv"
        
        check_if_system_exists
        
	check_if_os_exists
	#Download source from Githut
	check_command_success "git clone https://github.com/TarikVUT/semestral.git /tmp/$new_dir" "Download seniorOS"
	#check_command_success "git clone -b sapp https://github.com/forsenior/os.git $dir_to_install/OS" "sapp"
	#exit 0
	
	#check if sapp, stext, sweb, smail are exist
	
	delete_existing_dir "sapp"
	delete_existing_dir "stext"
	delete_existing_dir "sweb"
	delete_existing_dir "smail"
	
	#Move sapp,stext to /home/
	check_command_success "sudo mv /tmp/$new_dir/sapp /home" "move sapp to /home"
	check_command_success "sudo mv /tmp/$new_dir/stext /home" "move stext to /home"
	check_command_success "sudo mv /tmp/$new_dir/sweb /home" "move sweb to /home"
	check_command_success "sudo mv /tmp/$new_dir/smail /home" "move smail to /home"
	
	#Create virtual env inside sapp,stext,sweb,smail.
	check_command_success "virtualenv /home/sapp/env" "Create sapp env"
	check_command_success "virtualenv /home/stext/env" "Create stext env"
	check_command_success "virtualenv /home/sweb/env" "Create sweb env"
	check_command_success "virtualenv /home/smail/env" "Create smail env"
	
	#Change OS owner
	check_command_success "sudo chown -R $user /home/sapp /home/stext /home/sweb /home/smail" "Change owner to $user"
	
	#install needed packages for stext app
	source /home/stext/env/bin/activate && pip install pyqt5 xhtml2pdf  bs4 markdown && deactivate
	#install needed packages for sapp app
	source /home/sapp/env/bin/activate && pip install pillow pygame && dnf install python3-tkinter -y && deactivate
	#install needed packages for sweb app
	source /home/sweb/env/bin/activate && dnf install python3-tkinter -y && deactivate
	#install needed packages for smail app
	source /home/smail/env/bin/activate && dnf install python3-tkinter -y && deactivate
	
	
	#Create autostart file to run sapp
	mkdir -p /home/$user/.config/autostart && echo -e "[Desktop Entry]\nType=Application\nName=Pyapp\nExec=/home/sapp/env/bin/python /home/sapp/main.py\nTerminal=false" >/home/$user/.config/autostart/autostart.desktop && chmod +x /home/$user/.config/autostart/autostart.desktop
	check_command_success "sudo chown -R $user /home/$user/.config/autostart" "Change autostart owner to $user"
	passwd -d $user
	
	init 6
	
	# disable window button

else
        echo "ERROR"
fi
