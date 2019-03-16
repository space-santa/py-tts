import glob
import os
import time

os.system("modprobe w1-gpio")
os.system("modprobe w1-therm")

BASE_DIR = "/sys/bus/w1/devices/"
DEVICE_FOLDER = glob.glob(BASE_DIR + "28*")[0]
DEVICE_FILE = DEVICE_FOLDER + "/w1_slave"


def read_temp_raw():
    with open(DEVICE_FILE, "r") as file:
        lines = file.readlines()
        return lines


def read_temp():
    lines = read_temp_raw()

    while lines[0].strip()[-3:] != "YES":
        time.sleep(0.2)
        lines = read_temp_raw()

    equals_pos = lines[1].find("t=")

    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2 :]
        temp_c = float(temp_string) / 1000.0
        return temp_c


def get_temperature():
    return read_temp()
