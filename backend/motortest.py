from machine import Pin, PWM
from time import sleep
import Stepper

# init

out1F = PWM(0)
out2F = PWM(1)
out1F.freq(5000)
out2F.freq(5000)

out3F = PWM(2)
out4F = PWM(3)
out3F.freq(5000)
out4F.freq(5000)

out1B = PWM(4)
out2B = PWM(5)
out1B.freq(5000)
out2B.freq(5000)

out3B = PWM(6)
out4B = PWM(7)
out3B.freq(5000)
out4B.freq(5000)

# init
out1F.duty_u16(0)
out2F.duty_u16(0)
out3F.duty_u16(0)
out4F.duty_u16(0)
out1B.duty_u16(0)
out2B.duty_u16(0)
out3B.duty_u16(0)
out4B.duty_u16(0)


# init stepper
stepperA = Stepper(2038, 8, 10, 9, 11)
stepperA.setSpeed(0)

stepperB = Stepper(2038, 12, 14, 13, 15)
stepperB.setSpeed(0)


def forward(self, speed):
    """Speed as a decimal 0 to 1"""
    stop()
    sleep(0.5)
    duty = round(65000 * speed, 0)
    out1F.duty_u16(speed)
    out3F.duty_u16(speed)
    out1B.duty_u16(speed)
    out3B.duty_u16(speed)


def back(self, speed):
    """Speed as a decimal 0 to 1"""
    stop()
    sleep(0.5)
    duty = round(65000 * speed, 0)
    out2F.duty_u16(speed)
    out4F.duty_u16(speed)
    out2B.duty_u16(speed)
    out4B.duty_u16(speed)


def left(self, speed):
    """Speed as a decimal 0 to 1"""
    stop()
    sleep(0.5)
    duty = round(65000 * speed, 0)
    out1F.duty_u16(speed)
    out3F.duty_u16(speed)
    out1B.duty_u16(0)
    out3B.duty_u16(speed)


def right(self, speed):
    """Speed as a decimal 0 to 1"""
    stop()
    sleep(0.5)
    duty = round(65000 * speed, 0)
    out2F.duty_u16(speed)
    out4F.duty_u16(speed)
    out2B.duty_u16(speed)
    out4B.duty_u16(speed)


def stop(self):
    """Speed as a decimal 0 to 1"""
    stop()
    sleep(0.5)
    out1F.duty_u16(0)
    out2F.duty_u16(0)
    out3F.duty_u16(0)
    out4F.duty_u16(0)
    out1B.duty_u16(0)
    out2B.duty_u16(0)
    out3B.duty_u16(0)
    out4B.duty_u16(0)
