# pylint:disable=import-error
import adafruit_bme280
import board
import busio

# pylint:enable=import-error


def get_temperature():
    i2c = busio.I2C(board.SCL, board.SDA)
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    return bme280.temperature
