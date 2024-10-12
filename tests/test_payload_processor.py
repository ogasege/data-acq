import pytest
import json
import os
from modules.payload_processor import process_payload

# Utility function to load JSON file
def load_json_payload(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r') as file:
        return json.load(file)

@pytest.fixture
def valid_payload():
    return load_json_payload('test_payload.json')

def test_process_payload_structure(valid_payload):
    result = process_payload(json.dumps(valid_payload))  # Pass payload as a string

    # Ensure result is not None
    assert result is not None

    # Ensure top-level keys exist
    assert "time" in result
    assert "data" in result

    # Check each device type
    devices = ['strato-1', 'power-meter', 'pv-inverter-1', 'schneider-controller']
    for device in devices:
        assert device in result['data']

    # Test specific fields for each device
    strato_1 = result['data']['strato-1']
    assert all(key in strato_1 for key in ['cpu_load', 'boot_time', 'memory_usage', 'cpu_temp', 'disk_usage'])
    assert all(isinstance(strato_1[key], (int, float)) for key in strato_1)

    power_meter = result['data']['power-meter']
    assert all(key in power_meter for key in ['grid_status', 'genset_status', 'I_L1', 'P_total', 'E_exported'])
    assert isinstance(power_meter['grid_status'], int)
    assert isinstance(power_meter['genset_status'], int)
    assert isinstance(power_meter['I_L1'], float)
    assert isinstance(power_meter['P_total'], int)
    assert isinstance(power_meter['E_exported'], int)

    pv_inverter = result['data']['pv-inverter-1']
    assert all(key in pv_inverter for key in ['PF', 'P_total', 'total_yield'])
    assert all(isinstance(pv_inverter[key], int) for key in pv_inverter)

    schneider_controller = result['data']['schneider-controller']
    assert all(key in schneider_controller for key in ['pvinv_P_total', 'pvinv_total_yield'])
    assert all(isinstance(schneider_controller[key], float) for key in schneider_controller)

def test_process_payload_missing_field(valid_payload):
    # Create a copy of the payload to avoid modifying the fixture
    modified_payload = valid_payload.copy()
    modified_payload['data'] = modified_payload['data'].copy()
    
    # Remove 'strato-1' to simulate missing field
    del modified_payload['data']['strato-1']
    result = process_payload(json.dumps(modified_payload))  # Ensure it's passed as a string
    
    # Ensure result is not None
    assert result is not None
    
    assert 'strato-1' not in result['data']
    assert all(device in result['data'] for device in ['power-meter', 'pv-inverter-1', 'schneider-controller'])

def test_process_payload_invalid_payload():
    invalid_payload = "Invalid payload format"
    result = process_payload(invalid_payload)
    assert result is None

def test_process_payload_invalid_json():
    invalid_json = '{"time": "2024-10-10T16:03:00+00:00", "data": "Invalid"}'
    result = process_payload(invalid_json)
    assert result is None

def test_process_payload_missing_time():
    missing_time_payload = {'data': {'strato-1': {'cpu_load': 0.1}}}
    result = process_payload(json.dumps(missing_time_payload))  # Ensure it's passed as a string
    assert result is None