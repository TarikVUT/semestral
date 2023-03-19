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
fi
}

if [ -f /etc/fedora-release ]
then	
        echo "Your system is Fedora, install virtuallenv"
        #install virtualenv for python
        check_command_success "sudo dnf install virtualenv -y" "virtualenv"

	#Download source from Githut
	check_command_success "git clone -b sapp https://github.com/forsenior/os.git $dir_to_install/OS" "sapp"
	
	#Change OS owner
	check_command_success "sudo chown -R $user /home/$user/OS" "OS"
	
	#Move sapp to /home/
	check_command_success "sudo mv $dir_to_install/OS/sapp /home/root" "trans"

else
        echo "ERROR"
fi

