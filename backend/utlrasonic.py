from machine import Pin
from hcsr04 import HCSR04

sensor = HCSR04(trigger_pin=16, echo_pin=0)


def querydistance(self):
    return sensor.distance_cm()
