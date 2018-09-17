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

The Generic gateway allow you to create the gateway you want using the sensors & actuators available in "Clouding Things Pi Gateway" product type.

Available sensors:
* Ultrasonic ranger: 
    * https://www.seeedstudio.com/Grove-Ultrasonic-Ranger-p-960.html
    * name: CloudingThingsGroveUltrasonic
    * available:
        * distance: measured distance in cm
        * presence: return 1 when distance is less than 50cm

* Accelerometer 16G: 
    * https://www.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer%28%C2%B116g%29-p-1156.html
    * name: CloudingThingsGroveAccelerometer16G
    * available:
        * x: x axe value
        * y: y axe value
        * z: z axe value

* Barometer BMP085:
    * https://www.seeedstudio.com/Grove-Barometer-Sensor-p-1199.html
    * name: CloudingThingsGroveBarometerBmp085
    * available:
        * temperature: measured temperature in °C
        * pressure: measured atmospheric pressure in hpa
        * altitude: calculated altitude in meters

* Gas:
    * https://www.seeedstudio.com/Grove-Gas-Sensor(MQ2)-p-937.html
    * name: CloudingThingsGroveGas
    * available:
        * gas_measurement: analog value
        * gas_density: calculated gas density

* Sound:
    * http://wiki.seeedstudio.com/Grove-Sound_Sensor/
    * name: CloudingThingsGroveSound
    * available:
        * sound_measurement: analog value

* Potentiometer:
    * https://www.seeedstudio.com/Grove-Rotary-Angle-Sensor-p-770.html
    * name: CloudingThingsGrovePotentiometer
    * available:
        * potentiometer: analog value

* Electricity:
    * https://www.seeedstudio.com/Grove-Electricity-Sensor-p-777.html
    * name: CloudingThingsGroveElectricity
    * available:
        * measurement: 
        * amplitude: 
        * effective: 

* Light sensor:
    * https://www.seeedstudio.com/Grove-Light-Sensor-v1.2-p-2727.html
    * name: CloudingThingsGroveLight
    * available:
        * light: analog value

* Moisture:
    * https://www.seeedstudio.com/Grove-Moisture-Sensor-p-955.html
    * name: CloudingThingsGroveMoisture
    * available:
        * moisture: analog value

* RFID:
    * https://www.seeedstudio.com/Grove-125KHz-RFID-Reader-p-1008.html
    * name: CloudingThingsGroveRfid
    * available:
        * tag: tag id

* Piezo:
    * https://www.seeedstudio.com/Grove-Piezo-Vibration-Sensor-p-1411.html
    * name: CloudingThingsGrovePiezo
    * available:
        * vibrating: return 1 if is vibrating

* Motion:
    * https://www.seeedstudio.com/Grove-PIR-Motion-Sensor-p-802.html
    * name: CloudingThingsGrovePirMotion
    * available:
        * motion: return 1 if movement detected

* Temperature & Humidity DHT:
    * https://www.seeedstudio.com/Grove-Temperature-%26-Humidity-Sensor-%EF%BC%88DHT11%EF%BC%89-p-745.html
    * name: CloudingThingsGroveDht
    * available:
        * temperature: measured temperature in °C
        * humidity: measured relative humidity in %

* Temperature & Humidity DHT pro:
    * https://www.seeedstudio.com/Grove-Temperature%26Humidity-Sensor-Pro%EF%BC%88AM2302%EF%BC%89-p-838.html
    * name: CloudingThingsGroveDhtPro
    * available:
        * temperature: measured temperature in °C
        * humidity: measured relative humidity in %

Available actuators:

* LedBar:
    * https://www.seeedstudio.com/Grove-LED-Bar-v2.0-p-2474.html
    * name: CloudingThingsGroveLedbar
    * available:
        * level: led level from 0 to 10

* Led:
    * https://www.seeedstudio.com/Grove-Blue-LED-p-1139.html
    * name: CloudingThingsGroveLed
    * available:
        * state: led state (0 or 1)
        * blink: blink at defined period

* Relay:
    * https://www.seeedstudio.com/Grove-Relay-p-769.html
    * name: CloudingThingsGroveRelay
    * available:
        * state: relay state (0 or 1)

* WaterAtomizer:
    * https://www.seeedstudio.com/Grove-Water-Atomization-v1.0-p-2542.html
    * name: CloudingThingsGroveWaterAtomization
    * available:
        * state: atomizer state (0 or 1)

* Buzzer:
    * https://www.seeedstudio.com/Grove-Buzzer-p-768.html
    * name:  CloudingThingsGroveBuzzer
    * available:
        * state: buzzer state (0 or 1)

* Oled:
    * https://www.seeedstudio.com/Grove-OLED-Display-0.96%22-p-781.html
    * name: CloudingThingsGroveOled
    * available:
        * msg: msg showed by oled screen

* LCD: 
    * https://www.seeedstudio.com/Grove-LCD-RGB-Backlight-p-1643.html
    * name: CloudingThingsGroveLcd
    * available:
        * msg: msg showed by lcd screen
        * rgb: backlight color (not implemented yet)

## Setup

Open gtw_test.py program.

In gtw_config, update your client name and your product serial:

```
gtw_config={
        'client': '{your client name}',
        'serial': '{your product serial}',
        'credential_file': '/home/pi/.ct/gtw_crt_file.crt',
        'broker': '5.135.83.28',
        'transport': 'ssl',
        'port': 8883,
        'auto_reconnect': True
}
```

## Sensors

Plug the sensor on grovepi board and note connector pin id.

In the main program, you can add the sensor to the gateway:
```
ct_gtw.add_sensor({Sensor name}('{sensor id}', period={period interval}, pin={pin number}))
```

Where:
* Sensor name: CloudingThingsGroveSensor sensor name
* Sensor id: your sensor id in Clouding Things platform
* period: interval between 2 communication to Clouding Things platform
* pin: pin number the sensor is connected to

## Actuators

Plug the actuator on grovepi board and note connector pin id.

In the main program, you can add the actuator to the gateway:
```
ct_gtw.add_actuator({Actuator name}('{actuator id}', period={period interval}, pin={pin number}))
```

Where:
* Actuator name: CloudingThingsGroveActuator actuator name
* Actuator id: your actuator id in Clouding Things platform
* period: interval between 2 communication to Clouding Things platform
* pin: pin number the actuator is connected to

## Gateway

Launch gateway using the following command:

```python gtw_test.py```

# Smoke detector

You can create a simple smoke detector using smoke_detector.py example.

Create your product using "Grove Pi Smoke Detector" product type.

Plug sensors & actuators using same pin as used int the program.

Launch the program.
