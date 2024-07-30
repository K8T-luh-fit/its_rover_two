# import stepper
from machine import Pin, PWM
from time import sleep

# init

out1F = PWM(0)
out2F = PWM(16)
out1F.freq(5000)
out2F.freq(5000)

out3F = PWM(1)
out4F = PWM(17)
out3F.freq(5000)
out4F.freq(5000)

out1B = PWM(2)
out2B = PWM(18)
out1B.freq(5000)
out2B.freq(5000)

out3B = PWM(3)
out4B = PWM(19)
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
# stepperA = stepper.HalfStepMotor.frompins(8, 9, 10, 11)
# stepperA.reset()

# stepperB = stepper.HalfStepMotor.frompins(12, 13, 14, 15)
# stepperB.reset()


# init servo
servoA = PWM(4)
servoB = PWM(5)
servoA.freq(5000)
servoB.freq(5000)
servoA.duty_u16(0)
servoB.duty_u16(0)

servoAF = Pin(20, Pin.OUT, Pin.PULL_DOWN)
servoAB = Pin(21, Pin.OUT, Pin.PULL_DOWN)

servoBF = Pin(22, Pin.OUT, Pin.PULL_DOWN)
servoBB = Pin(23, Pin.OUT, Pin.PULL_DOWN)


def forward(speed):
    """Speed as a decimal 0 to 1"""
    stop()
    sleep(0.5)
    duty = round(65000 * speed, 0)
    out1F.duty_u16(duty)
    out3F.duty_u16(duty)
    out1B.duty_u16(duty)
    out3B.duty_u16(duty)


def back(self, speed):
    """Speed as a decimal 0 to 1"""
    stop()
    sleep(0.5)
    duty = round(65000 * speed, 0)
    out2F.duty_u16(duty)
    out4F.duty_u16(duty)
    out2B.duty_u16(duty)
    out4B.duty_u16(duty)


def left(self, speed):
    """Speed as a decimal 0 to 1"""
    stop()
    sleep(0.5)
    duty = round(65000 * speed, 0)
    out1F.duty_u16(duty)
    out3F.duty_u16(duty)
    out1B.duty_u16(0)
    out3B.duty_u16(duty)


def right(self, speed):
    """Speed as a decimal 0 to 1"""
    stop()
    sleep(0.5)
    duty = round(65000 * speed, 0)
    out2F.duty_u16(duty)
    out4F.duty_u16(duty)
    out2B.duty_u16(duty)
    out4B.duty_u16(0)


def stop():
    """Speed as a decimal 0 to 1"""
    sleep(0.5)
    out1F.duty_u16(0)
    out2F.duty_u16(0)
    out3F.duty_u16(0)
    out4F.duty_u16(0)
    out1B.duty_u16(0)
    out2B.duty_u16(0)
    out3B.duty_u16(0)
    out4B.duty_u16(0)


# front stepper
# def stepperAF(self, rot):
#     """Move stepper by amount of steps"""
#     stepperA.step(rot)
#     sleep(0.5)


# # back stepper
# def stepperBF(self, rot):
#     """Move stepper by amount of steps"""
#     stepperB.step(rot)
#     sleep(0.5)


# servo A


def rotateServoA(self, speed, time):
    """Speed as a decimal 0 to 1"""
    duty = round(65000 * speed, 0)
    if duty > 0:
        servoAB.off()
        sleep(0.1)
        servoAF.on()
    else:
        servoAF.off()
        sleep(0.1)
        servoAB.on()
    servoA.duty_u16(duty)
    sleep(time)
    servoA.duty_u16(0)


# servo B


def rotateServoB(self, speed, time):
    """Speed as a decimal 0 to 1"""
    duty = round(65000 * speed, 0)
    if duty > 0:
        servoBB.off()
        sleep(0.1)
        servoBF.on()
    else:
        servoBF.off()
        sleep(0.1)
        servoBB.on()
    servoB.duty_u16(duty)
    sleep(time)
    servoB.duty_u16(0)

forward(1)
stop()