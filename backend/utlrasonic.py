from machine import Pin
from hcsr04 import HCSR04

sensorA = HCSR04(trigger_pin=28, echo_pin=22)
sensorB = HCSR04(trigger_pin=21, echo_pin=20)


def querydistance_A():
    return sensorA.distance_cm()


def querydistance_B():
    return sensorB.distance_cm()
