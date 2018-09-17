# Setup

## Install module

To be able to use examples, first install CloudingThingsGrovePi module on your Raspberry Pi: 
https://github.com/fieldcloud/iot-gtw-clouding-things/blob/master/README.md

## Clouding Things product

Add your product to Clouding Things platform using "Clouding Things Pi Gateway":
https://www.clouding-things.fr:8443/spepsiot/#!devices

## Raspberry Pi environment

When your python environment is ready, you have to gather your Clouding Things parameters: 
* Your client name: https://www.clouding-things.fr:8443/spepsiot/#!My%20profile
* Your gateway serial: https://www.clouding-things.fr:8443/spepsiot/#!devices
* Your device product certificate: https://www.clouding-things.fr:8443/spepsiot/#!devices

Copy your credential file on your Raspberry Pi:
* path: ```/home/pi/.ct/```
* file name: ```gtw_crt_file.crt```

# Generic gateway

The Generic gateway allow you to create the gateway you want using the sensors & actuators available in "Clouding Things Pi Gateway" product type: 
* Moisture sensor
* DHT (Temperature and Humidity)
* DHT Pro (Temperature and Humidity)
* Oled display
* Relay
* Piezo
* Led
* LCD display
* RFID reader
* Barometer sensor
* Accelerometer
* Water atomizer
* Electricity
* Gas
* Ultrasonic ranger
* Buzzer
* Light
* Potentiometer
* Flame
* Sound

## Setup

## Sensors

## Actuators

# Smoke detector

You can create a simple smoke detector using smoke_detector.py example.
