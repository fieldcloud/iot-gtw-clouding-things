#!/usr/bin/bash

# Required packages installation script
# Version: 1.0.0
# Date: 10/04/2018
# Author: Jean Poma
# Company: fieldcloud

# Install pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

# Update & upgrade
sudo apt-get update
sudo apt-get upgrade

# Install paho mqtt module
sudo pip install paho

# Install GPIO module
sudo pip install RPi.GPIO

#Install serial communication
sudo apt-get install python-serial



# Install grovepi modules
## Get sources
cd /home/pi/
git clone https://github.com/DexterInd/GrovePi.git

## Install programs
cd GrovePi/Script
sudo bash install.sh


