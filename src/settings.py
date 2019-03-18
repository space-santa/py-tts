import os

from dotenv import load_dotenv

load_dotenv()


DEVICE = os.getenv("DEVICE", default="Mock")
WRITER = os.getenv("WRITER", default="CONSOLE")
BASE_URL = os.getenv("BASE_URL", default="")
API_URL = BASE_URL + "api/"
NAME = os.getenv("NAME", default="")
LOCATION = os.getenv("LOCATION", default="")
PASSWORD = os.getenv("PASSWORD", default="")

BME280 = "BME280"
MOCK = "Mock"
SENSE_HAT = "SenseHat"
DS18B20 = "DS18B20"

CONSOLE = "CONSOLE"
POST = "POST"
