#!/bin/bash
user=$(echo $SUDO_USER)
rm -rf /home/sapp
rm -rf /home/stext
rm -rf /home/sweb
rm -rf /home/smail
rm -rf /home/$user/.config/autostart
echo "You should set a new password"
