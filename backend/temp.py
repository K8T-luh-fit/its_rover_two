from machine import Pin
from dht import DHT11
from time import sleep

try:
    sensor = DHT11(Pin(22, Pin.IN, Pin.PULL_UP))
finally:
    pass


def querytemp():
    sensor.measure()
    return sensor.temperature()


def queryhumidity():
    sensor.measure()
    return sensor.humidity()


# print(querytemp())
print(queryhumidity())
