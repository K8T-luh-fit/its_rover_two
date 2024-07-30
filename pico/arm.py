import servo
from time import sleep

forearm = servo.Servo(4)
wrist = servo.Servo(5)
claw = servo.Servo(6)

forearmState = 775
wristState = 775
clawState = 360
upperLimit = 2150
lowerLimit = 600
step = 200


def initialize():
    global forearmState
    global wristState
    global clawState
    forearm.write_us(forearmState)
    wrist.write_us(wristState)
    claw.write_us(clawState)
    sleep(1)


# Servo driving definitions
def grab(direction, state):
    """Set direction grab or release"""
    global clawState
    if direction == "grab" and clawState < upperLimit:
        claw.write_us(state + step)
        clawState += step
        print("grabbing")
    if direction == "release" and clawState > lowerLimit:
        claw.write_us(state - step)
        clawState -= step
        print("ungrabbingh")


def moveArm(direction, forearmRot, wristRot):
    """Set direction up or down"""
    global forearmState
    global wristState
    print(direction, wristState)
    if direction == "up" and forearmState < upperLimit:
        forearm.write_us(forearmRot + step)
        wrist.write_us(wristRot - step)
        forearmState += step
        wristState -= step
        print("upping")
    if direction == "down" and forearmState > lowerLimit:
        forearm.write_us(forearmRot - step)
        wrist.write_us(wristRot + step)
        forearmState -= step
        wristState += step