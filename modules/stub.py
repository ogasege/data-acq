MQTT_PAYLOAD = {
    "t": 1728734580,
    "r": [
        {
            "_d": "logger",
            "_vid": "strato-1",
            "cpu_load": 0.04296875,
            "boot_time": 1702379385.0,
            "memory_usage": 27.4,
        },
        {
            "_d": "logger_strato",
            "_vid": "strato-1",
            "cpu_temp": 63.376,
            "disk_usage": 63.8,
        },
        {
            "_d": "power_meter",
            "_vid": "power-meter",
            "grid_status": 0,
            "genset_status": 1647,
            "I_L1": 0.0,
            "I_L2": 0.0,
            "I_L3": 0.0,
            "freq": 0.0,
            "P_total": 0,
            "E_exported": 1540509000,
        },
        {
            "_d": "pv_inverter_1",
            "_vid": "pv-inverter-1",
            "PF": 0,
            "I_L1": 217,
            "I_L2": 218,
            "I_L3": 218,
            "V_L1": 0,
            "V_L2": 0,
            "V_L3": 0,
            "freq": 499.0,
            "P_total": 14400,
            "Q_total": 600,
            "S_total": 15000,
            "dc_in_P1": 0,
            "dc_in_V1": 0,
            "total_yield": 51421000,
        },
        {
            "_d": "pv_inverter_2",
            "_vid": "pv-inverter-2",
            "PF": 0,
            "I_L1": 215,
            "I_L2": 216,
            "I_L3": 215,
            "V_L1": 0,
            "V_L2": 0,
            "V_L3": 0,
            "freq": 499.0,
            "P_total": 14900,
            "Q_total": 600,
            "S_total": 14900,
            "dc_in_P1": 0,
            "dc_in_V1": 0,
            "total_yield": 52785000,
        },
        {
            "_d": "pv_inverter_3",
            "_vid": "pv-inverter-3",
            "PF": 0,
            "I_L1": 219,
            "I_L2": 219,
            "I_L3": 219,
            "V_L1": 0,
            "V_L2": 0,
            "V_L3": 0,
            "freq": 499.0,
            "P_total": 15000,
            "Q_total": 600,
            "S_total": 15000,
            "dc_in_P1": 0,
            "dc_in_V1": 0,
            "total_yield": 51102000,
        },
        {
            "_d": "pv_inverter_4",
            "_vid": "pv-inverter-4",
            "PF": 0,
            "I_L1": 207,
            "I_L2": 207,
            "I_L3": 207,
            "V_L1": 0,
            "V_L2": 0,
            "V_L3": 0,
            "freq": 499.0,
            "P_total": 14300,
            "Q_total": 600,
            "S_total": 14300,
            "dc_in_P1": 0,
            "dc_in_V1": 0,
            "total_yield": 54917000,
        },
        {
            "_d": "pv_inverter_5",
            "_vid": "pv-inverter-5",
            "PF": 0,
            "I_L1": 0,
            "I_L2": 0,
            "I_L3": 0,
            "V_L1": 0,
            "V_L2": 0,
            "V_L3": 0,
            "freq": 500.0,
            "P_total": 0,
            "Q_total": 0,
            "S_total": 0,
            "dc_in_P1": 0,
            "dc_in_V1": 0,
            "total_yield": 52953000,
        },
        {
            "_d": "pv_inverter_6",
            "_vid": "pv-inverter-6",
            "PF": 0,
            "I_L1": 213,
            "I_L2": 213,
            "I_L3": 213,
            "V_L1": 0,
            "V_L2": 0,
            "V_L3": 0,
            "freq": 500.0,
            "P_total": 14100,
            "Q_total": 600,
            "S_total": 14600,
            "dc_in_P1": 0,
            "dc_in_V1": 0,
            "total_yield": 52232000,
        },
        {
            "_d": "_calc",
            "_vid": "schneider-controller",
            "pvinv_P_total": 72700.0,
            "pvinv_total_yield": 315410000.0,
        },
    ],
    "m": {"snap_rev": 912, "reading_duration": 35.67856407165527},
}

RESPONSE_PAYLOAD = {
    "time": "2024-10-10T16:03:00+00:00",
    "data": {
        "strato-1": {
            "cpu_load": 0.08740234375,
            "boot_time": 1702379385.0,
            "memory_usage": 27.4,
            "cpu_temp": 64.99,
            "disk_usage": 63.8
        },
        "power-meter": {
            "grid_status": 1,
            "genset_status": 0,
            "I_L1": 205.60000000000002,
            "I_L2": 200.70000000000002,
            "I_L3": 212.10000000000002,
            "freq": 50.29,
            "P_total": 136400,
            "E_exported": 1531708000
        },
        "pv-inverter-1": {
            "PF": 0,
            "I_L1": 245,
            "I_L2": 246,
            "I_L3": 245,
            "V_L1": 0,
            "V_L2": 0,
            "V_L3": 0,
            "freq": 502.0,
            "P_total": 16100,
            "Q_total": 1800,
            "S_total": 16700,
            "dc_in_P1": 0,
            "dc_in_V1": 0,
            "total_yield": 51159000
        },
        "pv-inverter-2": {
            "PF": 0,
            "I_L1": 292,
            "I_L2": 292,
            "I_L3": 292,
            "V_L1": 0,
            "V_L2": 0,
            "V_L3": 0,
            "freq": 502.0,
            "P_total": 20000,
            "Q_total": 2100,
            "S_total": 20000,
            "dc_in_P1": 0,
            "dc_in_V1": 0,
            "total_yield": 52518000
        },
        "pv-inverter-3": {
            "PF": 0,
            "I_L1": 254,
            "I_L2": 254,
            "I_L3": 253,
            "V_L1": 0,
            "V_L2": 0,
            "V_L3": 0,
            "freq": 502.0,
            "P_total": 17300,
            "Q_total": 1700,
            "S_total": 17400,
            "dc_in_P1": 0,
            "dc_in_V1": 0,
            "total_yield": 50824000
        },
        "pv-inverter-4": {
            "PF": 0,
            "I_L1": 239,
            "I_L2": 239,
            "I_L3": 239,
            "V_L1": 0,
            "V_L2": 0,
            "V_L3": 0,
            "freq": 502.0,
            "P_total": 16300,
            "Q_total": 1600,
            "S_total": 16400,
            "dc_in_P1": 0,
            "dc_in_V1": 0,
            "total_yield": 54667000
        },
        "pv-inverter-5": {
            "PF": 0,
            "I_L1": 237,
            "I_L2": 237,
            "I_L3": 236,
            "V_L1": 0,
            "V_L2": 0,
            "V_L3": 0,
            "freq": 502.0,
            "P_total": 16100,
            "Q_total": 1500,
            "S_total": 16200,
            "dc_in_P1": 0,
            "dc_in_V1": 0,
            "total_yield": 52885000
        },
        "pv-inverter-6": {
            "PF": 0,
            "I_L1": 241,
            "I_L2": 241,
            "I_L3": 241,
            "V_L1": 0,
            "V_L2": 0,
            "V_L3": 0,
            "freq": 502.0,
            "P_total": 15900,
            "Q_total": 1500,
            "S_total": 16400,
            "dc_in_P1": 0,
            "dc_in_V1": 0,
            "total_yield": 51968000
        },
        "schneider-controller": {
            "pvinv_P_total": 101700.0,
            "pvinv_total_yield": 314021000.0
        }
    }
}
