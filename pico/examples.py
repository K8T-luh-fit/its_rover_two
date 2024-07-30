from connections import connect_mqtt, connect_internet
from time import sleep
from constants import ssid, mqtt_server, mqtt_user, mqtt_pass
from machine import Pin, PWM
from dht import DHT11
import time
from hcsr04 import HCSR04
import servo
import arm

#motor pinout
out1F = PWM(0)
out1FP = 0
out2F = PWM(16)
out2FP = 16

out3F = PWM(1)
out3FP = 1
out4F = PWM(17)
out4FP = 17

out1B = PWM(2)
out1BP = 2
out2B = PWM(18)
out2BP = 18

out3B = PWM(3)
out3BP = 3
out4B = PWM(19)
out4BP = 19


# Driving motors
def setoff(pin, number):
    pin = Pin(number, Pin.OUT, Pin.PULL_DOWN)
    pin.off()


def seton(pin, number, duty):
    pin = PWM(number)
    pin.freq(5000)
    pin.duty_u16(duty)
    
seton(out1F, out1FP, 0)
seton(out2F, out2FP, 0)
seton(out3F, out3FP, 0)
seton(out4F, out4FP, 0)
seton(out1B, out1BP, 0)
seton(out2B, out2BP, 0)
seton(out3B, out3BP, 0)
seton(out4B, out4BP, 0)
    
# DRIVING DEFINITIONS
def forward(speed):
    """Speed as a decimal 0 to 1"""
    setoff(out2F, out2FP)
    setoff(out4F, out4FP)
    setoff(out2B, out2BP)
    setoff(out4B, out4BP)
    sleep(.01)
    duty = round(65000 * speed)
    seton(out1F, out1FP, duty)
    seton(out3F, out3FP, duty)
    seton(out1B, out1BP, duty)
    seton(out3B, out3BP, duty)
    
def back(speed):
    """Speed as a decimal 0 to 1"""
    setoff(out1F, out1FP)
    setoff(out3F, out3FP)
    setoff(out1B, out1BP)
    setoff(out3B, out3BP)
    sleep(0.5)
    duty = round(65000 * speed)
    seton(out2F, out2FP, duty)
    seton(out4F, out4FP, duty)
    seton(out2B, out2BP, duty)
    seton(out4B, out4BP, duty)
#     stop()

def left(speed):
    """Speed as a decimal 0 to 1"""
    setoff(out1F, out1FP)
    setoff(out4F, out4FP)
    setoff(out1B, out1BP)
    setoff(out4B, out4BP)
    sleep(0.5)
    duty = round(65000 * speed)
    seton(out2F, out2FP, duty)
    seton(out3F, out3FP, duty)
    seton(out2B, out2BP, duty)
    seton(out3B, out3BP, duty)
#     stop()

def right(speed):
    """Speed as a decimal 0 to 1"""
    setoff(out2F, out2FP)
    setoff(out3F, out3FP)
    setoff(out2B, out2BP)
    setoff(out3B, out3BP)
    sleep(0.5)
    duty = round(65000 * speed)
    seton(out1F, out1FP, duty)
    seton(out4F, out4FP, duty)
    seton(out1B, out1BP, duty)
    seton(out4B, out4BP, duty)
#     stop()

def stop():
    """Speed as a decimal 0 to 1"""
    sleep(0.01)
    setoff(out1F, out1FP)
    setoff(out3F, out3FP)
    setoff(out1B, out1BP)
    setoff(out3B, out3BP)
    setoff(out2F, out2FP)
    setoff(out4F, out4FP)
    setoff(out2B, out2BP)
    setoff(out4B, out4BP)


# Function to handle an incoming message

def cb(topic, msg):
    print(f"Topic: {topic}, Message: {msg}")
    msg = msg.decode("utf-8")
    print(msg)
    print(topic)
    if topic == b"direction":
        if msg == "w":
            forward(0.5)
        elif msg == "a":
            left(0.5)
        elif msg == "s":
            back(0.5)
        elif msg == "d":
            right(0.5)
        elif msg == "1":
            arm.moveArm("up", arm.forearmState, arm.wristState)
        elif msg == "2":
            arm.moveArm("down", arm.forearmState, arm.wristState)
        elif msg == "m":
             arm.grab("grab", arm.clawState)
        elif msg == "n":
             arm.grab("release", arm.clawState)
            
    if topic == b"stop":
        stop()
    

def main():
    arm.initialize()
    
    try:
        connect_internet('HAcK-Project-WiFi-2',password='UCLA.HAcK.2024.Summer')
        client = connect_mqtt("d36a339c75d44575b5341bede55cd6c6.s1.eu.hivemq.cloud", "nodeServer", "roverdaMOON123")

        sensor = DHT11(Pin(15, Pin.IN, Pin.PULL_UP))
#         change sensor2 pins
        sensor2 = HCSR04(trigger_pin=22, echo_pin=28, echo_timeout_us=10000)
        sleep(2)
        stop()
        client.set_callback(cb)
        client.subscribe("direction")
        client.subscribe("stop")
        
        interval = 2
        lastTime = time.time()
        
        cycles = 0
        while True:
            currentTime = time.time()
            
            if currentTime-lastTime>=interval:
                sensor.measure()
                temp = str(sensor.temperature())
                humid = str(sensor.humidity())
                distance = str(sensor2.distance_cm())
#             
                client.publish('temp', temp)
                client.publish('humidity', humid)
                client.publish('ultrasonic', distance)
                lastTime = currentTime
            client.check_msg()
            sleep(0.05)

    except KeyboardInterrupt:
        print('keyboard interrupt')
        

if __name__ == "__main__":
    main()

# def testpin():
#   pin = Pin(0)
#   pin.freq(5000)
#   pin.duty_u16(32000)
