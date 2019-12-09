# README.md file

"This project is make integrated chart from mellon,genie,bugs top100 chart."

<installing for python file>

1. install python3 

sudo apt-get install python3
sudo apt-get update
sudo apt-get upgrade python3

2. check python version
python3 --version(python version: 3.6.9)

3. install pip
apt install python3-pip

4. install beautifulsoup4 & requests
pip3 install requests beautifulsoup4

5. intstall pandas
pip3 install pandas

<installing for php,apache>

1. base setting
apt update
apt upgrade
apt install vim

2. install xampp(assume not installed mysql in your computer)
sudo apt install net-tools
sudo wget  https://www.apachefriends.org/xampp-files/7.3.11/xampp-linux-x64-7.3.11-0-installer.run
sudo chmod +x xampp-linux-x64-7.3.11-0-installer.run
sudo chmod +x xampp-linux-x64-7.3.11-0-installer.run

3. operate xampp
start xampp :sudo /opt/lampp/lampp start
stop xampp  :sudo /opt/lampp/lampp stop

*if you want to modify configure move to '/opt/lampp/etc/extra/httpd-xampp.conf'

4. git clone
1)move to '/opt/lampp/hdotcs'
2)make directory 
3)move to new directory that you make
4)clone our git project

5. configure mysql
1) you have to make table 'song(title,singer,albumName,score,lyrics,youtube)'
