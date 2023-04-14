# semestral
semestral
#For Debian
```bash
echo "user ALL=(ALL:ALL) ALL" >> /etc/sudoers
```
enable shutdown without sudo
```bash
<username> ALL=(ALL) NOPASSWD: /sbin/shutdown -h now
```
enable reboot without sudo
```bash
<username> ALL=(ALL) NOPASSWD: /sbin/reboot
```
#For Fedora
1. install gnome-shell-extension
```bash
sudo dnf install gnome-shell-extension* -y
```
2. command to disable the automatic Screen Lock in Fedora Workstation
```bash
dconf write /org/gnome/desktop/screensaver/lock-enabled false
```
3. reload gnome
```bash
killall -u user
```