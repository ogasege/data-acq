import json
import logging
from datetime import datetime, timezone

def process_payload(payload):
    """Processes the raw payload and restructures it."""
    try:
        # Check if the payload is a string and convert it to a dictionary if necessary
        if isinstance(payload, str):
            raw_data = json.loads(payload)
        elif isinstance(payload, dict):
            raw_data = payload
        else:
            raise ValueError("Payload must be a string or a dictionary")

        # Ensure 't' (timestamp) is present
        if 't' not in raw_data:
            raise KeyError("'t' (timestamp) field is missing in the payload")

        timestamp = datetime.fromtimestamp(raw_data['t'], timezone.utc).isoformat()

        data = {}
        for reading in raw_data.get('r', []):
            vid = reading.get('_vid')
            if not vid:
                logging.warning("Missing _vid key in reading, skipping.")
                continue

            if vid not in data:
                data[vid] = {}

            for key, value in reading.items():
                if key.startswith('_') or value is None:
                    continue
                data[vid][key] = value

        structured_data = {
            'time': timestamp,
            'data': data
        }

        return structured_data
    except (json.JSONDecodeError, KeyError) as e:
        logging.error(f"Failed to process payload: {e}")
        return None
    except ValueError as ve:
        logging.error(f"Invalid payload type: {ve}")
        return None
    