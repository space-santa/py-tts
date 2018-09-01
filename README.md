# TemperatureTrackerService
## BME280
Install the [requirements](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
and the [driver](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/python-circuitpython-test).

On a clean raspbian lite, it looks like so:

```
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools
# enable interfaces > i2c and spi
sudo raspi-config
# check that they are enabled
ls /dev/i2c* /dev/spi*
# returns /dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1
pip3 install RPI.GPIO
pip3 install adafruit-blinka
pip3 install adafruit-circuitpython-bme280

```