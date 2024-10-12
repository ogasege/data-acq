## Part 1: Data acquisition from MQTT broker

### Context
At AMMP we acquire and process data from a range of different devices and vendors, in the context of (renewable) energy systems. While we do much of our data acquisition over REST APIs, we also have dataloggers deployed at several hundred sites. These read data directly from the energy equipment - such as PV inverters or batteries - and send it to us over MQTT.

#### Details on infra/architecture
With respect to MQTT, most dataloggers send directly to the main AMMP MQTT broker at mqtt.ammp.io. We also have a staging (testing) broker at mqtt.stage.ammp.io.

We use AWS for all hosting. Most of our code runs either directly on an EC2 instance, or in an ECS container, or as a Lambda (serverless) function. We generally use ECS for more resource-intensive or long-running acquisition functions, and we prefer to use Lambdas for more "bursty" loads.

The data pipeline consists of a number of AWS SQS queues, which represent different stages of the pipeline. For example there is a raw data queue, where newly acquired data is pushed by the acquisition functions - and from where it gets picked up by processing functions (and then sent to another queue).

### Task
This task involves both a conceptual part, as well as a coding part. The overall objective is to set up data acquisition from the AMMP MQTT broker.

For the coding part, you will have been provided with credentials for the MQTT broker separately. Using these, you should be able to subscribe to a data stream. 

#### 1(a) Conceptual part
- What pros and cons do you see with respect to obtaining readings from an MQTT broker, vs getting them via a REST API?
- How would you run an acquisition function that subscribes to an MQTT broker? For example would you trigger it periodically via a scheduler, or would you have it running as some sort of continuous "listener" function? 
- What underlying AWS service would you run it on? E.g. EC2 vs ECS vs Lambda, etc.

#### 1(b) Coding part

Write a script in Python 3, to carry out data acquisition from the AMMP MQTT broker, and output the acquired raw data to screen.

**Connection to broker**
To connect please use the following parameters:
- Host: mqtt.stage.ammp.io
- Port: 8883
- Encryption (TLS): Enabled
- CA certificate file: available at https://github.com/ammpio/ammp-edge/blob/main/resources/certs/ca-stage.crt
- Username: provided separately
- Password: provided separately
- Topic: payloads will be published on the topic `a/b827eb2bb2a9/u/data`

If you'd like to use the Mosquitto command-line tool to test the connection, you can do so with
```
mosquitto_sub -h mqtt.stage.ammp.io -p 8883 -t a/b827eb2bb2a9/u/data -u <username> -P <password> --cafile ca-stage.crt -v -d
```
(assuming you're running it from the same directory where you saved `ca-stage.crt`)

**Payload structure on broker:**

The payloads received on the MQTT broker are in JSON format and have the following structure:
```
{
  "t": 1625576100,
  "r": [
    {
      "_d": "logger",
      "_vid": "strato-1",
      "boot_time": 1625563315,
      "cpu_load": 0.06,
      "memory_usage": 17.2
    },
    {
      "_d": "logger_strato",
      "_vid": "strato-1",
      "cpu_temp": 60.148,
      "disk_usage": 45.8
    },
    {
      "_d": "diesel_sensor",
      "_vid": "gamicos-1",
      "analog": 5.814655303955078,
      "level": 0.5670797228813171,
      "genset_fuel_level_percent": 56.378482855283295,
      "genset_fuel_volume": 2477.2705366611485
    },
    {
      "_d": "dse855",
      "_vid": "dse-1",
      "E": 86744200,
      "P": 15983,
      "P_L1": 4823,
      "P_L2": 4720,
      "P_L3": 6440,
      "S": 17293,
      "S_L1": 5314,
      "S_L2": 5109,
      "S_L3": 6901,
      "V_L1": 229.5,
      "V_L2": 231,
      "V_L3": 229.70000000000002,
      "alarm_status": 0,
      "freq": 50,
      "fuel_used": null,
      "oil_pressure": 406,
      "power_factor": 0.92,
      "power_factor_L1": 0.9,
      "power_factor_L2": 0.92,
      "power_factor_L3": 0.93,
      "runtime": 14316904,
      "temp_coolant": 78,
      "temp_oil": null,
      "time_to_maintenance": null,
      "utilization_L1": null,
      "utilization_L2": null,
      "utilization_L3": null
    }
  ],
  "m": {
    "snap_rev": 670,
    "config_id": "c5b2543",
    "reading_duration": 0.9248790740966797,
    "reading_offset": 0
  }
}
```
At the top level, `t` is the timestamp in Unix epoch seconds, `r` is a list of readings from each device, and `m` is some metadata about the reading.

**Payload structure in data pipeline:**
The payload received over MQTT needs to be restructured into the form accepted by the data pipeline. This involves three things:
- Converting the timestamp (`t`) into an RFC3339-compatible timestamp stored as a string, under the `time` key
- Converting the list of readings from `r` into a nested dictionary under the `data` key (see below)
- Discarding the remaining metadata (under `m`)

The `data` dictionary has the following characteristics:
- Its top-level keys are the "vendor IDs" of each device. These are the `_vid` values in the original payload.
- Readings from multiple devices sharing the same vendor ID should therefore be combined in the dict structure
- Any fields with name starting in `_` should be discarded - this therefore includes the above-mentioned vendor IDs, as well as the `_d` (device name) fields
- Any readings that have `null` values should be discarded

The above are perhaps best-illustrated through an example. Given the input payload shown above, the output payload should look as follows:
```
{
  "time": "2021-07-06T12:55:00+00:00",
  "data": {
    "strato-1": {
      "boot_time": 1625563315,
      "cpu_load": 0.06,
      "memory_usage": 17.2,
      "cpu_temp": 60.148,
      "disk_usage": 45.8
    },
    "gamicos-1": {
      "analog": 5.814655303955078,
      "level": 0.5670797228813171,
      "genset_fuel_level_percent": 56.378482855283295,
      "genset_fuel_volume": 2477.2705366611485
    },
    "dse-1": {
      "E": 86744200,
      "P": 15983,
      "P_L1": 4823,
      "P_L2": 4720,
      "P_L3": 6440,
      "S": 17293,
      "S_L1": 5314,
      "S_L2": 5109,
      "S_L3": 6901,
      "V_L1": 229.5,
      "V_L2": 231,
      "V_L3": 229.70000000000002,
      "alarm_status": 0,
      "freq": 50,
      "oil_pressure": 406,
      "power_factor": 0.92,
      "power_factor_L1": 0.9,
      "power_factor_L2": 0.92,
      "power_factor_L3": 0.93,
      "runtime": 14316904,
      "temp_coolant": 78
    }
  }
}
```

Finally, be mindful of how you handle payloads that might deviate from the prescribed format. For instance, readings from some devices may be missing a vendor ID (`_vid`) key.

**Pushing the payload into the pipeline:**
Since you do not have access to the AMMP data pipeline, simply print the data payloads to screen.

**Assume the code will be running in production at some point**


You can either share your code via github, or zip and email your code as well as the conceptual answers to svet.bajlekov@ammp.io. 