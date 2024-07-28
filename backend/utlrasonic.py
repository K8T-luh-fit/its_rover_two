from machine import Pin
from hcsr04 import HCSR04

sensor = HCSR04(trigger_pin=28, echo_pin=22)


def querydistance():
    return sensor.distance_cm()


print(querydistance())
