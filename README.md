# TemperatureTrackerService
## Getting started
```
cp .env.example src/.env
# Edit .env appropriately
virualenv -p python3 env
start.sh
```
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
sudo pip3 install virtualenv
cd project/root
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
pip install RPI.GPIO
pip install adafruit-blinka
pip install adafruit-circuitpython-bme280
```

## SenseHat

```
sudo apt-get install python3-pip
sudo pip3 install virtualenv
sudo apt-get install sense-hat
cd project/root
virtualenv -p python3 --system-site-packages env
source env/bin/activate
pip install -r requirements.txt
```