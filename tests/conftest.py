import pytest
from modules.stub import MQTT_PAYLOAD, RESPONSE_PAYLOAD

@pytest.fixture
def raw_payload():
    return MQTT_PAYLOAD

@pytest.fixture
def response_payload():
    return RESPONSE_PAYLOAD
