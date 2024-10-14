import logging
import json
import paho.mqtt.client as mqtt
from .payload_processor import process_payload

class MQTTClient:
    def __init__(self, config):
        """Initialize the MQTT client with configuration."""
        self.config = config
        self.client = mqtt.Client(userdata=self.config)

        # Set username and password for authentication
        self.client.username_pw_set(self.config['username'], self.config['password'])

        # Set TLS/SSL configuration
        self.client.tls_set(ca_certs=self.config['ca_cert_file'])

        # Attach callback functions
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

    # Callback for successful connection
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logging.info("Connected successfully to broker")
            self.client.subscribe(self.config['topic'])
        else:
            logging.error(f"Connection failed with code {rc}")
            raise ConnectionError(f"Connection failed with code {rc}")

    # Callback for receiving a message
    def on_message(self, client, userdata, msg):
        logging.info(f"Received message on topic {msg.topic}")
        structured_payload = process_payload(msg.payload.decode())

        if structured_payload:
            print(json.dumps(structured_payload, indent=4))

    # Callback for handling connection loss
    def on_disconnect(self, client, userdata, rc):
        logging.warning(f"Disconnected from broker with code {rc}. Reconnecting...")
        self.client.reconnect()

    def start(self):
        """Start the MQTT client and connect to the broker."""
        try:
            self.client.connect(self.config['broker'], self.config['port'], keepalive=60)
            self.client.loop_forever()
        except Exception as e:
            logging.error(f"Could not connect to broker: {e}")
            