from sense_hat import SenseHat


def get_temperature():
    sense = SenseHat()
    sense.clear()
    return sense.get_temperature()