# README.md file

<h1>This project is make integrated chart from mellon,genie,bugs top100 chart.</h1>

<h2>1. installing for python file</h2>
<br/>
- install python3 

<pre>
sudo apt-get install python3
sudo apt-get update
sudo apt-get upgrade python3
</pre>
- check python version
<pre>
python3 --version(python version: 3.6.9)
</pre>
- install pip
<pre>
apt install python3-pip
</pre>
- install beautifulsoup4 & requests
<pre>
pip3 install requests beautifulsoup4
</pre>
- intstall pandas
<pre>
pip3 install pandas
</pre>

<br/>

<h2>
2.installing for php,apache</h2>
<br/>

- base setting
<pre>
apt update
apt upgrade
apt install vim
</pre>

- install xampp(assume not installed mysql in your computer)
<pre>
sudo apt install net-tools
sudo wget  https://www.apachefriends.org/xampp-files/7.3.11/xampp-linux-x64-7.3.11-0-installer.run
sudo chmod +x xampp-linux-x64-7.3.11-0-installer.run
sudo chmod +x xampp-linux-x64-7.3.11-0-installer.run
</pre>

- operate xampp
<pre>
start xampp :sudo /opt/lampp/lampp start
stop xampp  :sudo /opt/lampp/lampp stop
</pre>

<i>
*if you want to modify configure move to '/opt/lampp/etc/extra/httpd-xampp.conf'</i>
<br/><br/>

- git clone
<pre>
1)move to '/opt/lampp/hdotcs'
2)make directory 
3)move to new directory that you make
4)clone our git project
</pre>
- configure mysql
<pre>
you have to make table 'song(title,singer,albumName,score,lyrics,youtube)'</pre>
