try:
    from .bme280 import get_temperature
except ModuleNotFoundError as e:
    from .mock import get_temperature
