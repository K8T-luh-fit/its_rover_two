import servo
from time import sleep

forearm = servo.Servo(4)
wrist = servo.Servo(5)
claw = servo.Servo(6)

forearmState = 0
wristState = 2400
clawState = 0


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
    """Set rotation between 350 and 2400 steps"""
    if direction == "grab":
        claw.write_us(state + 20)
    global clawState
    clawState += 20
    if direction == "release":
        claw.write_us(state - 20)
    global clawState
    clawState -= 20


def moveArm(direction, forearmRot, wristRot):
    """Set rotation between 350 and 2400 steps"""
    if direction == "up":
        forearm.write_us(forearmRot + i * 20)
        wrist.write_us(wristRot - i * 20)
    if direction == "down":
        forearm.write_us(forearmRot - i * 20)
        wrist.write_us(wristRot + i * 20)
    global clawState
    clawState -= 20

    global forearmState
    global wristState
    if direction == "up":
        forearmState = forearmRot + 20
        wristState = wristRot - 20
    elif direction == "down":
        forearmState = forearmRot - 20
        wristState = wristRot + 20


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
