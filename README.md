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

```
sudo python setup.py install
```

## Usage

Functionnal examples in example folder

### Gateway

Configuration values:

'''
gtw_config={
        'client': 'your_client_name',
        'serial': 'your_gateway_name',
        'credential_file': 'your_crt_file_path',
        'broker': '5.135.83.28',
        'transport': 'ssl',
        'port': 8883,
        'auto_reconnect': True
}
'''

Where:
- client: your client name in Clouding Things platform
- serial: your gateway serial number in Clouding Things platform
- credential_file: path to the crt file created during gateway provisionning

Gateway creation:

'''
import CloudingThings4Pi.CloudingThingsPiGateway as ctpg

ct_gtw=ctpg.CloudingThingsPiGateway(gtw_config)
'''

To start gateway:

'''
ct_gtw.run()
'''
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

* Electricity:
    * https://www.seeedstudio.com/Grove-Electricity-Sensor-p-777.html
    * name: CloudingThingsGroveElectricity

* Light sensor:
    * https://www.seeedstudio.com/Grove-Light-Sensor-v1.2-p-2727.html
    * name: CloudingThingsGroveLight

* Moisture:
    * https://www.seeedstudio.com/Grove-Moisture-Sensor-p-955.html
    * name: CloudingThingsGroveMoisture

* RFID:
    * https://www.seeedstudio.com/Grove-125KHz-RFID-Reader-p-1008.html
    * name: CloudingThingsGroveRfid

* Piezo:
    * https://www.seeedstudio.com/Grove-Piezo-Vibration-Sensor-p-1411.html
    * name: CloudingThingsGrovePiezo

* Motion:
    * https://www.seeedstudio.com/Grove-PIR-Motion-Sensor-p-802.html
    * name: CloudingThingsGrovePirMotion

* Temperature & Humidity DHT:
    * https://www.seeedstudio.com/Grove-Temperature-%26-Humidity-Sensor-%EF%BC%88DHT11%EF%BC%89-p-745.html
    * name: CloudingThingsGroveDht

* Temperature & Humidity DHT pro:
    * https://www.seeedstudio.com/Grove-Temperature%26Humidity-Sensor-Pro%EF%BC%88AM2302%EF%BC%89-p-838.html
    * name: CloudingThingsGroveDhtPro


### Actuators

Available actuators:

* LedBar:
    * https://www.seeedstudio.com/Grove-LED-Bar-v2.0-p-2474.html
    * name: CloudingThingsGroveLedbar

* Led:
    * https://www.seeedstudio.com/Grove-Blue-LED-p-1139.html
    * name: CloudingThingsGroveLed

* Relay:
    * https://www.seeedstudio.com/Grove-Relay-p-769.html
    * name: CloudingThingsGroveRelay

* WaterAtomizer:
    * https://www.seeedstudio.com/Grove-Water-Atomization-v1.0-p-2542.html
    * name: CloudingThingsGroveWaterAtomization

* Buzzer:
    * https://www.seeedstudio.com/Grove-Buzzer-p-768.html
    * name:  CloudingThingsGroveBuzzer

* Oled:
    * https://www.seeedstudio.com/Grove-OLED-Display-0.96%22-p-781.html
    * name: CloudingThingsGroveOled

* LCD: 
    * https://www.seeedstudio.com/Grove-LCD-RGB-Backlight-p-1643.html
    * name: CloudingThingsGroveLcd
