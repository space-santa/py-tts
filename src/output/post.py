import json
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

import settings


class PostRequestHandlerException(Exception):
    pass


class PostRequestHandler:
    LOGIN_URL = f"{settings.BASE_URL}Identity/Account/Login"

    def __init__(self):
        self.session = requests.Session()
        self._login()

    def _login(self):
        page = self.session.get(self.LOGIN_URL)
        soup = BeautifulSoup(page.content, "html.parser")

        for tag in soup.find_all("input"):
            if tag["name"] == "__RequestVerificationToken":
                token = tag["value"]
        payload = {
            "Input.Email": settings.NAME,
            "Input.Password": settings.PASSWORD,
            "__RequestVerificationToken": token,
        }
        reply = self.session.post(self.LOGIN_URL, data=payload)
        if reply.status_code != 200:
            raise PostRequestHandlerException(f"Couldn't log in: {reply.text}")

    def post_request(self, data, endpoint):
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        reply = self.session.post(
            f"{settings.API_URL}{endpoint}/", data=json.dumps(data), headers=headers
        )
        if reply.status_code != 201:
            raise PostRequestHandlerException(f"Couldn't post request: {reply.text}")
        return reply


def write(temperature):
    data = {
        "temperature": temperature,
        "deviceid": _get_or_create_device_id(),
        "timestamp": str(datetime.now(timezone.utc).astimezone()),
    }
    handler = PostRequestHandler()
    handler.post_request(data, "temperature")


def _get_device_id():
    response = requests.get(f"{settings.API_URL}device/")
    for device in response.json():
        if device["name"] == settings.NAME:
            return device["id"]
    raise PostRequestHandlerException("Device doesn't exist.")


def _get_or_create_device_id():
    try:
        return _get_device_id()
    except PostRequestHandlerException:
        data = {"name": settings.NAME, "location": settings.LOCATION}
        handler = PostRequestHandler()
        response = handler.post_request(data, "device")
        return response.json()["id"]
