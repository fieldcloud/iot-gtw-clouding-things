#!/usr/bin/env python

from CloudingThingsPiGateway import CloudingThingsPiGateway
#import CloudingThingsGatewayRunner as gr
from CloudingThingsGroveSensor import CloudingThingsGroveUltrasonic
from CloudingThingsGroveSensor import CloudingThingsGroveGas
from CloudingThingsGroveSensor import CloudingThingsGroveMoisture
from CloudingThingsGroveSensor import CloudingThingsGroveDht
from CloudingThingsGroveSensor import CloudingThingsGroveDhtPro


gtw_config={
        'client': 'FieldCloud',
        'serial': 'PiDemoFlcl_1',
        'subscriptions':[
        ],
        'credential_file': '/home/pi/.ct/gtw_crt_file.crt',
        'broker': '5.135.83.28',
        'transport': 'ssl',
        'port': 8883,
        'auto_reconnect': True
}

if __name__ == "__main__":
    print 'starting'
    ct_gtw=CloudingThingsPiGateway(gtw_config)
    us_sensor = CloudingThingsGroveUltrasonic(ct_gtw, 1.0, 'ultrasonic',4)
    gas_sensor = CloudingThingsGroveGas(ct_gtw, 10.0, 'gas',3)
    moisture_sensor = CloudingThingsGroveMoisture(ct_gtw, 5.0, 'moisture',2)
    dht_sensor = CloudingThingsGroveDht(ct_gtw, 1.0, 'dht',5)
    dht_sensor = CloudingThingsGroveDhtPro(ct_gtw, 1.5, 'dht pro', 6)
    ct_gtw.run()
