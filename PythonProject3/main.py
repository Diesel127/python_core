import json
import datetime

def custom_decoder(dct):
    if "time" in dct:
        dct["time"] = datetime.datetime.fromisoformat(dct["time"])
    return dct
json_str = '{"name": "Alice", "age": 30, "time": "2025-11-27T09:48:09.999612"}'

data = json.loads(json_str, object_hook=custom_decoder)
print(data)