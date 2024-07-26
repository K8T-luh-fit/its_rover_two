from machine import Pin
from dht import DHT11
from time import sleep

try:
    sensor = DHT11(Pin(15, Pin.IN, Pin.PULL_UP))
finally:
    pass


def querytemp(self):
    sensor.measure()
    return sensor.temperature()


def queryhumidity(self):
    sensor.measure()
    return sensor.humidity()
