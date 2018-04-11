#!/usr/bin/env python

# 

'''
The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sens$
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import grovepi
import CloudingThingsPiGateway
from twisted.internet import reactor
from twisted.internet import defer
import logging
from datetime import datetime


class CloudingThingsGroveSensor(object):

    _clouding_things_client=None
    _period = 5.0
    _serial='Generic'
    _pin=0


    def __init__(self, gateway, period, serial, pin):
        self._clouding_things_gtw=gateway
        self._period=period
        self._serial=serial
        self._pin=pin
        self._init_sensor()
        gateway.add_sensor(self)
        reactor.callWhenRunning(self._start)
        logging.info('{} Sensor {} started'.format(datetime.now(),
                                                   self._serial))


    def get_serial(self):
        return self._serial


    def _init_sensor(self):
        '''
            Method managing sensor specific initialization
            Has to be override
        '''
        pass


    @defer.inlineCallbacks
    def _start(self):
        '''
            Manage sensor data acquisition and publication
        '''
        result={}
        try:
            data= yield self._read()
            data['serial']=self._serial
            yield self._clouding_things_gtw.publish(data)
        except Exception as e:
            msg='{} Error publishing to Clouding Things client: {}'\
                ''.format(datetime.now(), str(e.args).strip('(),\"'))
            logging.warning(result.get('msg'))
        reactor.callLater(self._period, self._start)


    def _read(self):
        '''
            Method managing data acquisition
            Has to be override for every sensor
        '''
        return {}


class CloudingThingsGroveUltrasonic(CloudingThingsGroveSensor):


    def _read(self):
        data={}
        data['distance'] = grovepi.ultrasonicRead(self._pin)
        presence = data.get('distance') < 50
        if presence == True:
            data['presence'] = 1
        else:
            data['presence'] = 0
        return data


class CloudingThingsGroveGas(CloudingThingsGroveSensor):


    def _init_sensor(self):
        try:
            grovepi.pinMode(self._pin,"INPUT")
        except:
            pass


    def _read(self):
        data={}
        sensor_value=grovepi.analogRead(self._pin)
        data['gas_measurement']=sensor_value
        gas_density = float(sensor_value) / 1024.0
        data['gas_density'] = gas_density
        return data


class CloudingThingsGroveMoisture(CloudingThingsGroveSensor):


    def _init_sensor(self):
        try:
            grovepi.pinMode(self._pin,"INPUT")
        except:
            pass


    def _read(self):
        data={}
        data['moisture']=grovepi.analogRead(self._pin)
        return data


class CloudingThingsGroveDht(CloudingThingsGroveSensor):


    def _init_sensor(self):
        try:
            grovepi.pinMode(self._pin,"INPUT")
        except:
            pass


    def _read(self):
        data={}
        [temp,humidity] = grovepi.dht(self._pin,0)
        data['temperature']=temp
        data['humidity']=humidity
        return data


class CloudingThingsGroveDhtPro(CloudingThingsGroveSensor):


    def _init_sensor(self):
        try:
            grovepi.pinMode(self._pin,"INPUT")
        except:
            pass


    def _read(self):
        data={}
        [temp,humidity] = grovepi.dht(self._pin,1)
        data['temperature']=temp
        data['humidity']=humidity
        return data
