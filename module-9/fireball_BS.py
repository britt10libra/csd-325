import requests
import json
response = requests.get("https://ssd-api.jpl.nasa.gov/fireball.api?date-min=2026-09-01&date-max=2026-09-24&req-loc=true")
print(response.status_code)
print(response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())