#!/bin/bash 

# установка необходимых пакетов в ubuntu
sudo apt-get -y install libldap2-dev libsasl2-dev libssl-dev

sudo apt-get -y install python3-pip
sudo pip3 install --upgrade pip
sudo pip3 install virtualenv

# создание папки для программы
sudo mkdir /opt/afii/
sudo chmod 777 /opt/afii/

# копирование проекта
git clone https://github.com/kovalewvladimir/afii.git /opt/afii
cd /opt/afii/
git checkout deploy
virtualenv --no-site-packages -p python3 /opt/afii/
source ./bin/activate
pip install -r ./requirements.txt
deactivate