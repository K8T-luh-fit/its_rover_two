from machine import Pin, PWM
from time import sleep
import temp

# import Stepper

# init

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

# init stepper
# stepperA = Stepper.HalfStepMotor.frompins(8, 9, 10, 11)
# stepperA.reset()

# stepperB = Stepper.HalfStepMotor.frompins(12, 13, 14, 15)
# stepperB.reset()


# init servo
servoA = PWM(4)
servoB = PWM(5)
servoA.freq(5000)
servoB.freq(5000)
servoA.duty_u16(0)
servoB.duty_u16(0)


# Driving motors
def setoff(pin, number):
    pin = Pin(number, Pin.OUT, Pin.PULL_DOWN)
    pin.off()


def seton(pin, number, duty):
    pin = PWM(number)
    pin.freq(5000)
    pin.duty_u16(duty)


# init at 5khz
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
    sleep(0.5)
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
    stop()


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
    stop()


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
    stop()


def stop():
    """Speed as a decimal 0 to 1"""
    sleep(0.5)
    setoff(out1F, out1FP)
    setoff(out3F, out3FP)
    setoff(out1B, out1BP)
    setoff(out3B, out3BP)
    setoff(out2F, out2FP)
    setoff(out4F, out4FP)
    setoff(out2B, out2BP)
    setoff(out4B, out4BP)


# front stepper
def stepperAF(rot):
    """Move stepper by amount of steps"""
    stepperA.step(rot)
    sleep(0.5)


# back stepper
def stepperBF(rot):
    """Move stepper by amount of steps"""
    stepperB.step(rot)
    sleep(0.5)


# servo A


def rotateServoA(speed, time):
    """Speed as a decimal 0 to 1"""
    duty = round(65000 * speed, 0)
    servoA.duty_u16(duty)
    sleep(time)
    servoA.duty_u16(0)


# servo B


def rotateServoB(speed, time):
    """Speed as a decimal 0 to 1"""
    duty = round(65000 * speed, 0)
    servoB.duty_u16(duty)
    sleep(time)
    servoB.duty_u16(0)


# RUNNING SECTION
# print("forward")
# forward(1)
# sleep(1)
# print("back")
# back(1)
# sleep(1)
# print("stop")
# stop()

# print("left")
# left(1)
# sleep(1)
# print("right")
# right(1)
# sleep(1)
# print("stop")
# stop()


temp.querytemp()
