#!/usr/bin/env python

import CloudingThings4Pi.CloudingThingsPiGateway as ctpg
from CloudingThings4Pi.CloudingThingsGroveSensor import *
from CloudingThings4Pi.CloudingThingsGroveActuator import *


gtw_config={
        'client': 'FieldCloud',
        'serial': 'Smoke_detector_example',
        'credential_file': '/home/pi/.ct/gtw_crt_file.crt',
        'broker': '5.135.83.28',
        'transport': 'ssl',
        'port': 8883,
        'auto_reconnect': True
}

if __name__ == "__main__":
    #Gateway
    ct_gtw=ctpg.CloudingThingsPiGateway(gtw_config)
    #Add buzzer
    ct_gtw.add_actuator(CloudingThingsGroveBuzzer('buzzer'))
    #Add gas and smoke sensor
    ct_gtw.add_sensor(CloudingThingsGroveGas('gas', period=0.2, pin=8))
    ct_gtw.add_sensor(CloudingThingsGroveFlame('flame', period=0.1, pin=7))
    #Start gateway
    ct_gtw.run()
