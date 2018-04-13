#!/usr/bin/env python

'''

    CloudingThingsGroveSensor Module
    ==============================

    Usage:
        Create grove actuator for IoT Gateway connected to Clouding Things
        use case prototyping platform
    License: MIT
    Contributors:
        Jean Poma - Initial development

    ==============================

    Example:
        import CloudingThings4Pi.CloudingThingsPiGateway as ctpg
        from CloudingThings4Pi.CloudingThingsGroveActuator import *
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
        ct_gtw.add_actuator(CloudingThingsGroveLedbar('ledbar', 7))
        ct_gtw.run()
'''

#import grovepi
import CloudingThings4Pi.AsynchGrovePi as grovepi
import logging
from datetime import datetime
import time,sys
from twisted.internet.defer import Deferred, inlineCallbacks, returnValue
from twisted.internet import reactor
from twisted.internet import task
import grove_128_64_oled as oled

def sleep(secs):
  d = Deferred()
  reactor.callLater(secs, d.callback, None)
  return d


class CloudingThingsGroveActuator(object):

    '''
        Abstract class managing actuator initialization, link to gateway and
        data publishment
    '''

    _serial='Generic'
    _pin=0


    def __init__(self, serial, pin):
        '''
            Initialize actuator parameters:
                serial -- Clouding Things sensor serial number
                pin -- pin attached to sensor
        '''
        self._serial = serial
        self._pin = pin
        self._init_actuator()
        logging.info('{} Actuator {} started'.format(datetime.now(),
                                                   self._serial))


    def _init_actuator(self):
        '''
            Override if actuator needs initialization
        '''
        pass


    def get_serial(self):
        ''' Return sensor Clouding Things serial number '''
        return self._serial


    def do(self, action):
        '''
            Action done by actuator
        '''
        yield returnValue('0')


class CloudingThingsGroveLedbar(CloudingThingsGroveActuator):

    '''Ledbar actuator'''

    def _init_actuator(self):
        grovepi.ledBar_init(self._pin, 0)
        sleep(0.5)
        grovepi.ledBar_setLevel(self._pin, 5)


    def do(self, action):
        if action is not None:
            for k, v in action.iteritems():
                if k == 'level':
                    grovepi.ledBar_setLevel(self._pin, v)


class CloudingThingsGroveLed(CloudingThingsGroveActuator):

    '''Led actuator'''

    _blinking_period=1.0
    _blinking=False
    _blinking_loop=None
    _led_status=0

    def _init_actuator(self):
        grovepi.pinMode(self._pin, 'OUTPUT')
        self._blinking_loop=task.LoopingCall(self._blink)
        self._blinking_loop.start(0.5)


    def do(self, action):
        print self._blinking_loop
        if self._blinking_loop is not None:
            try:
                self._blinking_loop.stop()
            except:
                pass
        if action is not None:
            for k, v in action.iteritems():
                if k == 'state':
                    grovepi.digitalWrite(self._pin, v)
                elif k == 'blink':
                    self._blinking_period=float(v)
                    self._blinking_loop=task.LoopingCall(self._blink)
                    self._blinking_loop.start(self._blinking_period)
        print 'action done'


    def _blink(self):
        grovepi.digitalWrite(self._pin, self._led_status)
        if self._led_status==0:
            self._led_status=1
        else:
            self._led_status=0


class CloudingThingsGroveRelay(CloudingThingsGroveActuator):

    '''Relay actuator'''

    def _init_actuator(self):
        grovepi.pinMode(self._pin, 'OUTPUT')


    def do(self, action):
        if action is not None:
            for k, v in action.iteritems():
                if k == 'state':
                    grovepi.digitalWrite(self._pin, v)


class CloudingThingsGroveBuzzer(CloudingThingsGroveActuator):

    '''Buzzer actuator'''

    def _init_actuator(self):
        grovepi.pinMode(self._pin, 'OUTPUT')


    def do(self, action):
        if action is not None:
            for k, v in action.iteritems():
                if k == 'state':
                    grovepi.digitalWrite(self._pin, v)


class CloudingThingsGroveOled(CloudingThingsGroveActuator):

    '''Oled actuator'''

    def _init_actuator(self):
        oled.init()
        oled.clearDisplay()
        oled.setNormalDisplay()
        oled.setPageMode()
        for i in range(4, 5):
            oled.setTextXY(0,i)
            oled.putString('Waiting...')


    def do(self, action):
        if action is not None:
            for k, v in action.iteritems():
                if k == 'msg':
                    oled.clearDisplay()
                    for i in range(4, 5):
                        oled.setTextXY(i,i)
                        oled.putString(v)


class CloudingThingsGroveLcd(CloudingThingsGroveActuator):

    '''Lcd actuator'''

    # this device has two I2C addresses
    DISPLAY_RGB_ADDR = 0x62
    DISPLAY_TEXT_ADDR = 0x3e
    _bus=None


    def _init_actuator(self):
        '''
            Override if actuator needs initialization
        '''
        if sys.platform == 'uwp':
            import winrt_smbus as smbus
            self._bus = smbus.SMBus(1)
        else:
            import smbus
            import RPi.GPIO as GPIO
            rev = GPIO.RPI_REVISION
            if rev == 2 or rev == 3:
                self._bus = smbus.SMBus(1)
            else:
                self._bus = smbus.SMBus(0)
        self.set_RGB(0, 128, 64)
        self.set_text('Started, waiting for message...')


    def do(self, action):
        if action is not None:
            for k, v in action.iteritems():
                if k == 'msg':
                    self.set_text(v)
                elif k == 'rgb':
                    pass


    def set_RGB(self, r,g,b):
        self._bus.write_byte_data(self.DISPLAY_RGB_ADDR,0,0)
        self._bus.write_byte_data(self.DISPLAY_RGB_ADDR,1,0)
        self._bus.write_byte_data(self.DISPLAY_RGB_ADDR,0x08,0xaa)
        self._bus.write_byte_data(self.DISPLAY_RGB_ADDR,4,r)
        self._bus.write_byte_data(self.DISPLAY_RGB_ADDR,3,g)
        self._bus.write_byte_data(self.DISPLAY_RGB_ADDR,2,b)


    def _text_command(self, cmd):
        self._bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x80,cmd)


    def set_text(self, text):
        self._text_command(0x01) # clear display
        sleep(.05)
        self._text_command(0x08 | 0x04) # display on, no cursor
        sleep(.05)
        self._text_command(0x28) # 2 lines
        count = 0
        row = 0
        for c in text:
            if c == '\n' or count == 16:
                count = 0
                row += 1
                if row == 2:
                    break
                self._text_command(0xc0)
                if c == '\n':
                    continue
            count += 1
            self._bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x40,ord(c))


    def set_text_norefresh(text):
        self._text_command(0x02) # return home
        sleep(.05)
        self._text_command(0x08 | 0x04) # display on, no cursor
        sleep(.05)
        self._text_command(0x28) # 2 lines
        sleep(.05)
        count = 0
        row = 0
        while len(text) < 32: #clears the rest of the screen
            text += ' '
        for c in text:
            if c == '\n' or count == 16:
                count = 0
                row += 1
                if row == 2:
                    break
                self._text_command(0xc0)
                if c == '\n':
                    continue
            count += 1
            self._bus.write_byte_data(self.DISPLAY_TEXT_ADDR,0x40,ord(c))
