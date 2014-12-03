# 服务器命令记录

echo "Create New User"
# create user work
# login as root
adduser work
# add sudo privileges
visudo

echo "Clone Code"
sudo apt-get install git
git clone git@github.com:WhiteWorld/SellTa.git


echo "Env Init"
# login as work
# install pip
sudo apt-get install python-pip
# install virtualenvwrapper
sudo pip install virtualenvwrapper
# Add to .bashrc/.zshrc
# export WORKON_HOME=$HOME/.virtualenvs
# export PROJECT_HOME=$HOME/Devel
# source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv tmpenv
workon tmpenv
pip install -r requirements.txt

echo "Install supervisor"
sudo apt-get install supervisor
# edit /etc/supervisor/supervisord.conf
supervisorctl reread
supervisorctl update

echo "Install Gunicorn/Gevent"
workon tmpenv
pip install gunicorn
sudo apt-get install python-dev
pip install gevent

echo "Install MySQL"
sudo apt-get install mysql-server
sudo mysql_install_db
sudo mysql_secure_installation

# set default character
# http://stackoverflow.com/questions/3513773/change-mysql-default-character-set-to-utf-8-in-my-cnf
[mysqld]
collation-server = utf8_unicode_ci
init-connect='SET NAMES utf8'
character-set-server = utf8

mysql> show variables like "%character%";show variables like "%collation%";

mysql> CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
mysql> GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> CREATE DATABASE sellta;
# events
mysql> SHOW VARIABLES LIKE 'event_scheduler';
mysql> SET GLOBAL event_scheduler = ON;

mysql> SHOW EVENTS;
mysql> DROP EVENTS event_name;

# Install Nginx
sudo apt-get update
sudo apt-get install nginx
sudo update-rc.d nginx defaults