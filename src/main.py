from sensors import temperature
from output import writer

writer.write(temperature.get_temperature())