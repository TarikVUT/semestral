# semestral
semestral
#For Debian
echo "user ALL=(ALL:ALL) ALL" >> /etc/sudoers

#For Fedora
1- install gnome-shell-extension
sudo dnf install gnome-shell-extension* -y

2- reload gnome
killall -u user

3-command to disable the automatic Screen Lock in Fedora Workstation
dconf write /org/gnome/desktop/screensaver/lock-enabled false