from modules.payload_processor import process_payload

def test_process_payload_structure(raw_payload):
    result = process_payload(raw_payload) 

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

    schneider_controller = result['data']['schneider-controller']
    assert all(key in schneider_controller for key in ['pvinv_P_total', 'pvinv_total_yield'])
    assert all(isinstance(schneider_controller[key], float) for key in schneider_controller)

def test_process_payload_invalid_payload():
    invalid_payload = "Invalid payload format"
    result = process_payload(invalid_payload)
    assert result is None
