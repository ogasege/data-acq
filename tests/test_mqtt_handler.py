import pytest
from unittest.mock import patch, MagicMock
from modules.mqtt_handler import MQTTClient

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

def test_mqtt_client_init(mock_cert, config):
    client = MQTTClient(config)
    assert client.config['broker'] == 'test.mosquitto.org'
    assert client.config['port'] == 1883

@patch('modules.mqtt_handler.mqtt.Client.connect')
def test_mqtt_client_connection(mock_connect, mock_cert, config):
    mock_connect.return_value = 0
    client = MQTTClient(config)
    client.start()
    mock_connect.assert_called_with('test.mosquitto.org', 1883, keepalive=60)

def test_mqtt_client_subscription(mock_cert, config):
    client = MQTTClient(config)
    mqtt_mock = MagicMock()
    client.client = mqtt_mock
    client.on_connect(client.client, None, None, 0)
    mqtt_mock.subscribe.assert_called_with('test/topic')
    