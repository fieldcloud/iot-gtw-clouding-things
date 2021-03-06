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

'''
    CloudingThingsMqttClient Module
    ===============================

    Usage: 
        Create mqtt client connected to Clouding Things use case prototyping
         platform
    License: MIT
    Contributors: 
        Jean Poma - Initial development

    ===============================

    Example:
        import CloudingThings4Pi.CloudingThingsMqttClient as ctmc
        gtw_config={
           'client': 'demo',
           'serial': 'demo',
           'credential_file': 'path_to_crt.crt',
           'broker': '5.135.83.28',
           'transport': 'ssl',
           'port': 8883,
           'auto_reconnect': True
        }
        ct_gtw.run()
'''

__version__='0.1.0'


class CloudingThingsMqttClient(object):
    '''
        MQTT client for Clouding Things use case prototyping cloud platform
    '''

    _params={
        'client': 'public_demo',
        'serial': 'demo',
        'credential_file': 'gtw_crt_file.crt',
        'broker': '5.135.83.28',
        'transport': 'ssl',
        'port': 8883,
        'auto_reconnect': True
    }
    _mqtt_client=None
    _topic='{client}/{serial}/FromDevice'
    _subscription='{client}/{serial}/ToDevice'


    def __init__(self, config):
        '''
            Initialize gateway with configuration informations
        '''
        if config is not None and self._check_config(config) == True:
            self._params=config
            self._topic=self._topic.format(**self._params)
            self._subscription=self._subscription.format(**self._params)
            print self._topic
        else:
            logging.warning('{} Error loading configuration'.format(
                                                               datetime.now()))


    def _check_config(self, config):
        if config is None:
            return False
        elif config.get('client') is None:
            return False
        elif config.get('serial') is None:
            return False
        elif config.get('credential_file') is None:
            return False
        elif config.get('broker') is None:
            return False
        elif config.get('transport') is None:
            return False
        elif config.get('port') is None:
            return False
        elif config.get('auto_reconnect') is None:
            return False
        else:
            return True


#------------------------------- MQTT methods ---------------------------------#
    def on_message(self, cl, userdata, msg):
        '''
            Override to add action on message
        '''
        Logging.info('Message received: {}'.format(msg.payload))


    def on_connect(self, cl, userdata, flags, rc):
        '''
            Called on connection to Clouding Things platform. Manage 
            subscriptions to mqtt events.
        '''
        logging.info("Connected with result code {}".format(str(rc)))
        self._mqtt_client.subscribe(self._subscription)


    def on_disconnect(self, cl, userdata, rc):
        '''
            The callback for when a disconnect event is detected.
            If auto reconnect is set True, try to reconnect
        '''
        logging.warning('{} Disconnected with code: {}'.format(datetime.now(),
                                                               rc))
        ar= self._params.get('auto_reconnect')
        if ar is not None and ar == True:
            try:
                self._mqtt_client.reconnect()
            except Exception as e:
                logging.warning('{} - Impossible to reconnect with error: {}'\
                      ''.format(datetime.now(), str(e.args).strip('(),\"')))


    def start_mqtt_client(self):
        '''
           Manage gateway connection to mqtt broker
        '''
        print self._params
        #serial & security parameters
        print 'starting'
        # mqtt client creation
        self._mqtt_client = mqtt.Client(client_id=self._params.get('client'),
                                     transport=self._params.get('transport'))
        #callbacks
        self._mqtt_client.on_connect = self.on_connect
        self._mqtt_client.on_message = self.on_message
        self._mqtt_client.on_disconnect = self.on_disconnect
        #tls config
        self._mqtt_client.tls_set(ca_certs=self._params.get('credential_file'),
                                certfile=None,
                                keyfile=None,
                                cert_reqs=ssl.CERT_REQUIRED,
                                tls_version=ssl.PROTOCOL_TLSv1,
                                ciphers=None)
        self._mqtt_client.tls_insecure_set(True)
        #connection
        res = self._mqtt_client.connect_async(self._params.get('broker'), 
                                              port=self._params.get('port'))
        print res
        self._mqtt_client.loop_start()


    def disconnect(self):
        '''
            Disconnect mqtt client
        '''
        if self._mqtt_client is not None:
            self._mqtt_client.disconnect()


#publish
    @defer.inlineCallbacks
    def publish(self, data):
        '''
            Publish data received from sensor on mqtt topic
        '''
        pl = self._make_ct_payload(data)
        try:
            payload= json.dumps(pl).encode('utf-8')
            print 'payload:'
            print payload
            print self._topic
            if self._mqtt_client is not None:
                r = yield self._mqtt_client.publish(self._topic,
                                                    payload=payload)
                print r
        except Exception as e:
            logging.warning('{} - Impossible to publish message: {}'\
                  ''.format(datetime.now(), str(e.args).strip('(),\"')))
        yield defer.returnValue('0')


    def _make_ct_payload(self, data):
        result = {}
        result['gatewayId'] = self._params.get('serial')
        result['type'] = "TH_monitoring"
        payload = {}
        val = {}
        payload[data.get('serial')] = val
#        tss=datetime.utcnow()
        tss=datetime.now()
        ts = int(time.mktime(tss.timetuple()))*1000+(tss.microsecond/1000)
        for k, v in data.iteritems():
            if k != 'serial':
                p = []
                pv = []
                pv.append(ts)
                pv.append(v)
                p.append(pv)
                val[k] = p
        result['payload'] = payload
        return result

