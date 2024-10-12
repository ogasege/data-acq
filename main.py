import os
import logging
from dotenv import load_dotenv
from modules.mqtt_handler import MQTTClient 
from modules.ca_cert_downloader import download_ca_cert  # Correct import statement

# Load environment variables from .env file
load_dotenv()

# Logging setup
logging.basicConfig(level=logging.INFO)

# MQTT Broker configurations
MQTT_CONFIG = {
    'broker': os.getenv('MQTT_BROKER'),
    'port': int(os.getenv('MQTT_PORT')),
    'username': os.getenv('MQTT_USERNAME'),
    'password': os.getenv('MQTT_PASSWORD'),
    'topic': os.getenv('MQTT_TOPIC'),
    'ca_cert_file': 'ca-stage.crt'  
}

# Main function to start the MQTT client
def main():
    # Download the CA certificate
    download_ca_cert()

    # Create and start the MQTT client
    mqtt_client = MQTTClient(MQTT_CONFIG)
    mqtt_client.start()

if __name__ == '__main__':
    main()