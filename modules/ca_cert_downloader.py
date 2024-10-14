import os
import requests
import logging

# URL to the CA certificate
ca_cert_url = os.getenv('CA_CERT_URL')
ca_cert_file = 'ca-stage.crt'

def download_ca_cert():
    """Check if the CA cert file exists; if not, download it."""
    print ('CA_CERT_URL=', ca_cert_url)
    if os.path.exists(ca_cert_file):
        logging.info(f"CA certificate already exists: {ca_cert_file}")
    else:
        logging.info(f"CA certificate not found, downloading from {ca_cert_url}")
        try:
            response = requests.get(ca_cert_url)
            response.raise_for_status()  # Raise an error for bad status codes
            with open(ca_cert_file, 'wb') as file:
                file.write(response.content)
            logging.info(f"Downloaded CA certificate successfully: {ca_cert_file}")
        except requests.RequestException as e:
            logging.error(f"Failed to download CA certificate: {e}")
            raise
        