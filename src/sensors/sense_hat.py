from sense_hat import SenseHat  # pylint: disable=import-error


def get_temperature():
    sense = SenseHat()
    sense.clear()
    return sense.get_temperature()
