#!/usr/bin/env python

# 

'''

    CloudingThingsGroveSensor Module
    ==============================

    Usage:
        Create grove sensor for IoT Gateway connected to Clouding Things
        use case prototyping platform
    License: MIT
    Contributors:
        Jean Poma - Initial development

    ==============================

    Example:
        import CloudingThings4Pi.CloudingThingsPiGateway as ctpg
        from CloudingThings4Pi.CloudingThingsGroveSensor import *
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
        ct_gtw.add_sensor(CloudingThingsGroveGas(10.0, 'gas',1))
        ct_gtw.run()
'''

#import grovepi
import CloudingThings4Pi.AsynchGrovePi as grovepi
import CloudingThingsPiGateway
from twisted.internet import reactor
from twisted.internet import defer
from twisted.internet import task
import logging
from datetime import datetime
from serial import Serial


def sleep(secs):
    d = defer.Deferred()
    reactor.callLater(secs, d.callback, None)
    return d


class CloudingThingsGroveSensor(object):

    '''
        Abstract class managing sensor initialization, link to gateway and 
        data publishment
    '''

    _clouding_things_gtw=None
    _period = 5.0
    _serial='Generic'
    _pin=0


    def __init__(self, serial, period=1.0, pin=0):
        '''
            Initialize sensor parameters:
                period -- time between 2 data readings
                serial -- Clouding Things sensor serial number
                pin -- pin attached to sensor
        '''
        self._period=period
        self._serial=serial
        self._pin=pin
        self._init_sensor()
        reactor.callWhenRunning(self._start)
        logging.info('{} Sensor {} started'.format(datetime.now(),
                                                   self._serial))


    def get_serial(self):
        ''' Return sensor Clouding Things serial number '''
        return self._serial


    def link_to_gateway(self, gateway):
        ''' Add sensor to the gateway '''
        self._clouding_things_gtw=gateway


    def _init_sensor(self):
        '''
            Method managing sensor specific initialization
            Has to be override
        '''
        pass


    def _start(self):
        l = task.LoopingCall(self._run)
        l.start(self._period)


    @defer.inlineCallbacks
    def _run(self):
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


    def _read(self):
        '''
            Method managing data acquisition
            Has to be override for every sensor
        '''
        return {}


class CloudingThingsGroveUltrasonic(CloudingThingsGroveSensor):

    '''Ultrasonic ranger sensor'''

    def _read(self):
        data={}
        data['distance'] = grovepi.ultrasonicRead(self._pin)
        presence = data.get('distance') < 50
        if presence == True:
            data['presence'] = 1
        else:
            data['presence'] = 0
        return data


class CloudingThingsGroveAccelerometer16G(CloudingThingsGroveSensor):

    '''Accelerometer 16g sensor'''

    _adxl1345=None

    def _init_sensor(self):
        from adxl345 import ADXL345
        self._adxl345 = ADXL345()


    def _read(self):
        data={}
        axes = self._adxl345.getAxes(True)
        data['x']=axes['x']
        data['y']=axes['y']
        data['z']=axes['z']
        return data


class CloudingThingsGroveBarometerBmp085(CloudingThingsGroveSensor):

    '''Barometer Bmp085 sensor'''

    _barometer=None

    def _init_sensor(self):
        import grove_barometer_lib
        self._barometer=grove_barometer_lib.barometer()


    def _read(self):
        data={}
        self._barometer.update
        data['temperature']=self._barometer.temperature
        data['pressure']=self._barometer.pressure
        data['altitude']=self._barometer.altitude
        return data


class CloudingThingsGroveGas(CloudingThingsGroveSensor):

    '''Gas sensor'''

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


class CloudingThingsGroveSound(CloudingThingsGroveSensor):

    '''Sound sensor'''

    def _init_sensor(self):
        try:
            grovepi.pinMode(self._pin,"INPUT")
        except:
            pass


    def _read(self):
        data={}
        sensor_value=grovepi.analogRead(self._pin)
        data['sound_measurement']=sensor_value
        return data


class CloudingThingsGrovePotentiometer(CloudingThingsGroveSensor):

    '''Potentiometer sensor'''

    def _init_sensor(self):
        try:
            grovepi.pinMode(self._pin,"INPUT")
        except:
            pass


    def _read(self):
        data={}
        sensor_value=grovepi.analogRead(self._pin)
        data['potentiometer']=sensor_value
        return data


class CloudingThingsGroveElectricity(CloudingThingsGroveSensor):

    '''Electricity sensor'''

    _vcc=5.0


    def _init_sensor(self):
        try:
            grovepi.pinMode(self._pin,"INPUT")
        except:
            pass


    def _read(self):
        data={}
        sensor_value=grovepi.analogRead(self._pin)
        amplitude = float(sensor_value) / 1024.0 * _vcc / 800.0 * 2000000.0
        effective = amplitude_current / 1.414
        data['measurement']=sensor_value
        data['amplitude']=amplitude
        data['effective']=effective
        return data


class CloudingThingsGroveLight(CloudingThingsGroveSensor):

    '''Light sensor'''

    def _init_sensor(self):
        try:
            grovepi.pinMode(self._pin,"INPUT")
        except:
            pass


    def _read(self):
        data={}
        sensor_value=grovepi.analogRead(self._pin)
        data['light']=sensor_value
        return data


class CloudingThingsGroveMoisture(CloudingThingsGroveSensor):

    '''Moisture sensor'''

    def _init_sensor(self):
        try:
            grovepi.pinMode(self._pin,"INPUT")
        except:
            pass


    def _read(self):
        data={}
        data['moisture']=grovepi.analogRead(self._pin)
        return data


class CloudingThingsGroveRfid(CloudingThingsGroveSensor):

    '''Rfid tag reader sensor'''

    _ser=None
    _last_tag=None


    @defer.inlineCallbacks
    def _read(self):
        self._last_tag = None
        data={}
        self._ser=Serial('/dev/ttyS0', baudrate=9600, timeout=0)
        self._ser.close()
        self._ser.open()
        if self._ser is not None:
            tag=''
            while self._last_tag is None:
                try:
                    if self._ser.inWaiting():
                        tag = tag +  self._ser.read()
                    if len(tag) == 14:
                        t2 = '0x{}'.format(tag[3:11])
                        i_tag = int(t2,0)
                        tag = str(i_tag)
                        while len(tag) < 10:
                            tag = '0{}'.format(tag)
                        break
                except Exception as e:
                    print e.args
                yield sleep(0.01)
            self._ser.close()
            if len(tag) == 10:
                data['tag']=tag
            else:
                data['tag']=''
            self._last_tag=tag
        self._ser=None
        yield defer.returnValue(data)


class CloudingThingsGrovePiezo(CloudingThingsGroveSensor):

    '''Piezo sensor'''

    def _init_sensor(self):
        try:
            grovepi.pinMode(self._pin,"INPUT")
        except:
            pass


    def _read(self):
        data={}
        data['vibrating']=grovepi.analogRead(self._pin)
        return data


class CloudingThingsGrovePirMotion(CloudingThingsGroveSensor):

    '''Pir motion sensor'''

    def _init_sensor(self):
        try:
            grovepi.pinMode(self._pin,"INPUT")
        except:
            pass


    def _read(self):
        data={}
        data['motion']=grovepi.digitalRead(self._pin)
        return data


class CloudingThingsGroveFlame(CloudingThingsGroveSensor):

    '''Flame sensor'''

    def _init_sensor(self):
        try:
            grovepi.pinMode(self._pin,"INPUT")
        except:
            pass


    def _read(self):
        data={}
        data['flame']=grovepi.digitalRead(self._pin)
        return data


class CloudingThingsGroveDht(CloudingThingsGroveSensor):

    '''Dht Temperature & Humidity sensor'''

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

    '''Dht Pro Temperature & Humidity sensor'''

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
