import settings

# pylint: disable=unused-import
if settings.DEVICE == settings.BME280:
    from .bme280 import get_temperature
elif settings.DEVICE == settings.SENSE_HAT:
    from .sense_hat import get_temperature
elif settings.DEVICE == settings.DS18B20:
    from .ds18b20 import get_temperature
else:
    from .mock import get_temperature
# pylint: enable=unused-import
