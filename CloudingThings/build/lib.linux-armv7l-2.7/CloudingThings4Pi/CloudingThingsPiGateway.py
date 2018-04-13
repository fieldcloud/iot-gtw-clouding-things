#!/usr/bin/env python

from datetime import datetime
import calendar
import sys
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import ssl
import time
from twisted.internet import reactor
from twisted.internet import defer
import json
from CloudingThings4Pi.CloudingThingsMqttClient import *

'''
    CloudingThingsPiGateway Module
    ==============================

    Usage: 
        Create sensor/actuator IoT Gateway connected to Clouding Things
        use case prototyping platform
    License: MIT
    Contributors: 
        Jean Poma - Initial development

    ==============================

    Example:
        import CloudingThings4Pi.CloudingThingsPiGateway as ctpg
        gtw_config={
           'client': 'demo',
           'serial': 'demo',
           'credential_file': 'path_to_crt.crt',
           'broker': '5.135.83.28',
           'transport': 'ssl',
           'port': 8883,
           'auto_reconnect': True
        }
        ct_gtw=ctpg.CloudingThingsPiGateway(gtw_config)
        ct_gtw.run()
'''

__version__='0.1.0'


class CloudingThingsPiGateway(CloudingThingsMqttClient):


    _sensors={}
    _actuators={}


    def add_sensor(self, sensor):
        '''
            Allow developpers to add compatible sensors to the gateway.
        '''
        if sensor is not None:
            self._sensors[sensor.get_serial()]=sensor
            sensor.link_to_gateway(self)


    def add_actuator(self, actuator):
        '''
            Allow developpers to add compatible actuators to the gateway.
        '''
        if actuator is not None:
            self._actuators[actuator.get_serial()]=actuator


    @defer.inlineCallbacks
    def on_message(self, cl, userdata, msg):
        '''
            The callback for when a PUBLISH message is received from the server.
            Call do method of related actuator
        '''
        print msg.payload
        if msg is not None:
            sp=msg.payload
            if sp is not None:
                pl=json.loads(sp)
                if pl.get('type') == "TH_setActuator":
                    if pl.get('gatewayId') == self._params.get('serial'):
                        actions=pl.get('payload')
                        for action in actions:
                            yield self._execute(action)
        yield defer.returnValue('0')


    @defer.inlineCallbacks
    def _execute(self, action):
        ids=action.get('deviceId').split('-')
        if len(ids) == 2:
            id=ids[1]
            actuator=self._actuators.get(id)
            if actuator is not None:
                a={}
                a[action.get('outputName')]=action.get('value')
                yield actuator.do(a)
        yield defer.returnValue('0')


    def run(self):
        '''
            Start twisted reactor used by sensors
            Called at end of main program to start the gateway
        '''
        reactor.callWhenRunning(self.start_mqtt_client)
        reactor.run()
