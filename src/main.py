from output import writer
from sensors import temperature

writer.write(temperature.get_temperature())
