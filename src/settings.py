from dotenv import load_dotenv

load_dotenv()

import os

DEVICE = os.getenv("DEVICE", default="Mock")
WRITER = os.getenv("WRITER", default="CONSOLE")
API_URL = os.getenv("API_URL", default="")
NAME = os.getenv("NAME", default="")

BME280 = "BME280"
MOCK = "Mock"
SenseHat = "SenseHat"
DS18B20 = "DS18B20"

CONSOLE = "CONSOLE"
POST = "POST"
