import settings

if settings.DEVICE == settings.BME280:
    from .bme280 import get_temperature
elif settings.DEVICE == settings.SenseHat:
    from .sense_hat import get_temperature
else:
    from .mock import get_temperature
