import json
import datetime


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super().default(obj)


data = {"name": "Alice", "age": 30, "now_time": datetime.datetime.now()}

json_str = json.dumps(data, cls=CustomEncoder, indent=4)

print(json_str)