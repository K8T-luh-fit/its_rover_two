from machine import Pin
from dht import DHT11
from time import sleep

try:
    sensor = DHT11(Pin(15, Pin.IN, Pin.PULL_UP))
    while True:
        sensor.measure()
        temp = sensor.temperature()
        humid = sensor.humidity()

        print("Temperature in C: ", temp)
        print("Humidity: ", humid)
        sleep(1)
finally:
    pass
