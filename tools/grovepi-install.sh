#!/bin/bash

# Grovepi extension board installation script
# Based on tutorial: https://github.com/DexterInd/GrovePi
# Version: 1.0.0
# Date: 10/04/2018
# Author: Jean Poma
# Company: fieldcloud


# Get sources
cd /home/pi/
git clone https://github.com/DexterInd/GrovePi.git

# Install programs
cd GrovePi/Script
sudo bash install.sh

