#!/usr/bin/env python

import CloudingThings4Pi.CloudingThingsPiGateway as ctpg
from CloudingThings4Pi.CloudingThingsGroveSensor import *
from CloudingThings4Pi.CloudingThingsGroveActuator import *


gtw_config={
        'client': 'FieldCloud',
        'serial': 'PiDemoFlcl_1',
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
    ct_gtw.add_actuator(CloudingThingsGroveLcd('lcd', 0))
    ct_gtw.add_actuator(CloudingThingsGroveLedbar('ledbar', 7))
    ct_gtw.add_actuator(CloudingThingsGroveOled('oled', 0))
    ct_gtw.add_actuator(CloudingThingsGroveLed('led', 8))
    #Sensors
    ct_gtw.add_sensor(CloudingThingsGroveUltrasonic(1.0, 'ultrasonic',4))
    ct_gtw.add_sensor(CloudingThingsGroveGas(10.0, 'gas',1))
    ct_gtw.add_sensor(CloudingThingsGroveLight(9.0, 'light',2))
    ct_gtw.add_sensor(CloudingThingsGrovePotentiometer(6.0, 'potentiometer',0))
    ct_gtw.add_sensor(CloudingThingsGroveMoisture(5.0, 'moisture',2))
    ct_gtw.add_sensor(CloudingThingsGroveDht(1.0, 'dht',5))
    ct_gtw.add_sensor(CloudingThingsGroveDhtPro(1.5, 'dht pro', 6))
    #Start gateway
    ct_gtw.run()
