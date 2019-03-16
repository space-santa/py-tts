import json
from datetime import datetime, timezone

import requests
from requests.auth import HTTPBasicAuth

import settings


def _post_request(data, endpoint):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    reply = requests.post(
        f"{settings.API_URL}/{endpoint}/",
        data=json.dumps(data),
        headers=headers,
        auth=HTTPBasicAuth(settings.NAME, settings.PASSWORD),
    )
    print(reply.text)


def write(temperature):
    data = {
        "temperature": temperature,
        "device": settings.NAME,
        "timestamp": str(datetime.now(timezone.utc).astimezone()),
    }
    _post_request(data, "temperature")


def create_device():
    data = {"name": settings.NAME, "location": settings.LOCATION}
    _post_request(data, "device")
