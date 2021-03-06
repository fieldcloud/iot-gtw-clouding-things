#!/usr/bin/env python

import CloudingThings4Pi.CloudingThingsPiGateway as ctpg
from CloudingThings4Pi.CloudingThingsGroveSensor import *
from CloudingThings4Pi.CloudingThingsGroveActuator import *


gtw_config={
        'client': 'Put your organization name here',
        'serial': 'Put your serial number here',
        'credential_file': '/home/pi/.ct/gtw_crt_file.crt',
        'broker': '5.135.83.28',
        'transport': 'ssl',
        'port': 8883,
        'auto_reconnect': True
}

if __name__ == "__main__":
    #Gateway
    ct_gtw=ctpg.CloudingThingsPiGateway(gtw_config)
    #Actuators
#    ct_gtw.add_actuator(CloudingThingsGroveLcd('lcd'))
#    ct_gtw.add_actuator(CloudingThingsGroveOled('oled'))
    ct_gtw.add_actuator(CloudingThingsGroveLedbar('ledbar', pin=7))
    ct_gtw.add_actuator(CloudingThingsGroveLed('led', pin=8))

#Sensors
    ct_gtw.add_sensor(CloudingThingsGroveUltrasonic('ultrasonic', pin=4))
#    ct_gtw.add_sensor(CloudingThingsGroveGas('gas', period=5.0, pin=1))
#    ct_gtw.add_sensor(CloudingThingsGroveLight('light', period=2.0, pin=2))
#    ct_gtw.add_sensor(CloudingThingsGrovePotentiometer('potentiometer', pin=0))
#    ct_gtw.add_sensor(CloudingThingsGroveMoisture('moisture', pin=2))
#    ct_gtw.add_sensor(CloudingThingsGroveDht('dht', period=2.0, pin=5))
    ct_gtw.add_sensor(CloudingThingsGroveDhtPro('dht pro', pin=6))
    ct_gtw.add_sensor(CloudingThingsGroveSound('sound', pin=3))
    ct_gtw.add_sensor(CloudingThingsGroveBarometerBmp085('barometer'))
    ct_gtw.add_sensor(CloudingThingsGroveRfid('barometer'))

    #Start gateway
    ct_gtw.run()

