import paho.mqtt.client as mqtt
import logging
from time import sleep

# Get a logger
logging.getLogger("awm-logger")


class client(object):
    '''
    MQTT client class
    '''

    def __init__(self, host, port, topic):
        self.address = host
        self.port = port
        self.topic = topic
        
        try:
            # A client for the sensorData
            self.mqtt = mqtt.Client()
            # Assigning the Callback functions
            self.mqtt.on_connect = self.on_connect
            self.mqtt.on_message = self.on_message
            self.mqtt.on_disconnect = self.on_disconnect
        except Exception as e:
            logging.error("MQTT:Exception:Connection Issue" + str(e))

    def on_connect(self, client, userdata, flags, rc):
        logging.info("Connected MQTT")

    def on_message(self, client, userdata, message):
        logging.info("New MQTT message" + str(message.payload.decode()))

    def on_disconnect(self, client, userdata, rc):
        logging.info("Disconnected MQTT")

    def connectMqtt(self) -> bool:
        '''
        Function to connect to an address and port
        '''
        self.mqtt.connect(self.address, self.port)
        sleep(0.2)
        return True
    
    def disconnect(self):
        '''
        Function to disconnect
        '''
        self.mqtt.disconnect()

    def publishData(self, data) -> bool:
        '''
        Function to publish an MQTT message
        '''
        logging.info("Publishing a MQTT message")
        self.mqtt.publish(self.topic, data)
        return True