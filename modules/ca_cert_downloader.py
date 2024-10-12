import os
import requests
import logging

# URL to the CA certificate
CA_CERT_URL = 'https://github.com/ammpio/ammp-edge/raw/main/resources/certs/ca-stage.crt'
CA_CERT_FILE = 'ca-stage.crt'

def download_ca_cert():
    """Check if the CA cert file exists; if not, download it."""
    if os.path.exists(CA_CERT_FILE):
        logging.info(f"CA certificate already exists: {CA_CERT_FILE}")
    else:
        logging.info(f"CA certificate not found, downloading from {CA_CERT_URL}")
        try:
            response = requests.get(CA_CERT_URL)
            response.raise_for_status()  # Raise an error for bad status codes
            with open(CA_CERT_FILE, 'wb') as file:
                file.write(response.content)
            logging.info(f"Downloaded CA certificate successfully: {CA_CERT_FILE}")
        except requests.RequestException as e:
            logging.error(f"Failed to download CA certificate: {e}")
            raise  # Re-raise the exception to handle it upstream if needed