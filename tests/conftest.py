import pytest
from modules.ca_cert_downloader import download_ca_cert
from modules.stub import MQTT_PAYLOAD, RESPONSE_PAYLOAD

@pytest.fixture
def raw_payload():
    return MQTT_PAYLOAD

@pytest.fixture
def response_payload():
    return RESPONSE_PAYLOAD

@pytest.fixture
def mock_cert():
    return download_ca_cert()

@pytest.fixture
def config():
    return {
        'broker': 'test.mosquitto.org',
        'port': 1883,
        'username': 'user',
        'password': 'pass',
        'topic': 'test/topic',
        'ca_cert_file': 'ca-stage.crt'
    }
