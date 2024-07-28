import servo
from time import sleep

forearm = servo.Servo(4)
wrist = servo.Servo(5)
claw = servo.Servo(6)

forearmState = 360
wristState = 2380
clawState = 360


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
    if direction == "grab" and clawState < 2360:
        claw.write_us(state + 20)
        clawState += 20
        print("grabbing")
    if direction == "release" and clawState > 370:
        claw.write_us(state - 20)
        clawState -= 20
        print("ungrabbingh")


def moveArm(direction, forearmRot, wristRot):
    """Set direction up or down"""
    global forearmState
    global wristState
    print(direction, wristState)
    if direction == "up" and forearmState < 2360:
        forearm.write_us(forearmRot + 20)
        wrist.write_us(wristRot - 100)
        forearmState += 20
        wristState -= 20
        print("upping")
    if direction == "down" and forearmState > 370:
        forearm.write_us(forearmRot - 20)
        wrist.write_us(wristRot + 20)
        forearmState -= 20
        wristState += 20


# FOR TESTING
# def grab(degree, state):
#     """Set rotation between 350 and 2400 steps"""
#     for i in range(abs(degree - state) / 20):
#         if (degree - state) > 0:
#             claw.write_us(state + i * 20)
#             sleep(0.005)
#         elif (degree - state) < 0:
#             claw.write_us(state - i * 20)
#             sleep(0.005)
#     global clawState
#     clawState = degree


# def moveArm(degree, forearmRot, wristRot):
#     """Set rotation between 350 and 2400 steps"""
#     for i in range(abs(degree - forearmRot) / 20):
#         if (degree - forearmRot) > 0:
#             forearm.write_us(forearmRot + i * 20)
#             wrist.write_us(wristRot - i * 20)
#             sleep(0.005)
#         elif (degree - forearmRot) < 0:
#             forearm.write_us(forearmRot - i * 20)
#             wrist.write_us(wristRot + i * 20)
#             sleep(0.005)

#     global forearmState
#     global wristState
#     forearmState = degree
#     if (degree - forearmRot) > 0:
#         wristState = 2750 - degree
#     else:
#         wristState = 350 + 2400 - degree

initialize()

while True:
    for i in range(120):
        moveArm("up", forearmState, wristState)
        sleep(0.01)
    sleep(2)
    for i in range(120):
        moveArm("down", forearmState, wristState)
        sleep(0.01)
    sleep(2)
