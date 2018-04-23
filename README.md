# Gateway GrovePi/Clouding Things

## Usage

This python module allows any Clouding Things user to create a sensord/actuators gateway using GrovePi extension board for RaspBerry Pi.

## Installation

### Required packages

This module requires:
* twisted
* grovepi
* paho-mqtt 


### Module installation

In CloudingThings folder:

sudo python setup.py install

## Usage

### Gateway


### Sensors

Available sensors:
* Ultrasonic ranger: 
    * https://www.seeedstudio.com/Grove-Ultrasonic-Ranger-p-960.html
    * name: CloudingThingsGroveUltrasonic

* Accelerometer 16G: 
    * https://www.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer%28%C2%B116g%29-p-1156.html
    * name: CloudingThingsGroveAccelerometer16G

* Barometer BMP085:
    * https://www.seeedstudio.com/Grove-Barometer-Sensor-p-1199.html
    * name: CloudingThingsGroveBarometerBmp085

* Gas:
    * https://www.seeedstudio.com/Grove-Gas-Sensor(MQ2)-p-937.html
    * name: CloudingThingsGroveGas

* Potentiometer:
    * https://www.seeedstudio.com/Grove-Rotary-Angle-Sensor-p-770.html
    * name: CloudingThingsGrovePotentiometer

* Electricity
    * https://www.seeedstudio.com/Grove-Electricity-Sensor-p-777.html
    * name: CloudingThingsGroveElectricity

### Actuators

