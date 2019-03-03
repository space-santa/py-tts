import requests
import settings
import json
from datetime import datetime, timezone


def write(temperature):
    data = {
        "temperature": temperature,
        "device": settings.NAME,
        "timestamp": str(datetime.now(timezone.utc).astimezone()),
    }
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    reply = requests.post(settings.API_URL, data=json.dumps(data), headers=headers)
    print(reply.text)
