from time import sleep
from machine import PWM, Pin
import board


# pin = PWM(0)
# pin.freq(5000)
# for i in range(650):
#     pin.duty_u16(i * 100)
#     print(i * 100)
#     sleep(0.01)

# for i in range(650):
#     pin.duty_u16(65000 - i * 100)
#     print(65000 - i * 100)
#     sleep(0.01)

out1F = PWM(0)
out3F = PWM(1)
out2F = PWM(16)
out4F = PWM(17)

out1F.freq(5000)
out3F.freq(5000)
out2F.freq(5000)
out4F.freq(5000)


def softstart(pin, speed):
    """Speed as a decimal 0 to 1"""
    duty = round(65000 * speed, 0)
    for i in range(duty / 1000):
        print(i * 1000)
        pin.duty_u16(i * 1000)
        sleep(0.01)


def forward(speed):
    """Speed as a decimal 0 to 1"""
    # stop()
    sleep(0.5)
    softstart(out1F, speed)
    softstart(out3F, speed)
    duty = round(65000 * speed)
    out1F.duty_u16(duty)
    out3F.duty_u16(duty)
    # out1B.duty_u16(duty)
    # out3B.duty_u16(duty)


def forward_nosoft(speed):
    """Speed as a decimal 0 to 1"""
    # stop()
    sleep(0.5)
    # softstart(out3F, 0.5)
    duty = round(65000 * speed)
    out1F.duty_u16(duty)
    out3F.duty_u16(duty)
    # out1B.duty_u16(duty)
    # out3B.duty_u16(duty)


def back(speed):
    """Speed as a decimal 0 to 1"""
    sleep(0.5)
    duty = round(65000 * speed)
    out2F.duty_u16(duty)
    out4F.duty_u16(duty)
    # out2B.duty_u16(duty)
    # out4B.duty_u16(duty)


out1F.duty_u16(0)
sleep(1)
print("soft")
forward(0.5)
sleep(1)
out1F.duty_u16(0)
out3F.duty_u16(0)

sleep(1)
print("nosoft")
forward_nosoft(0.5)
sleep(1)
out1F.duty_u16(0)
out3F.duty_u16(0)

out1F = Pin(0, Pin.OUT, Pin.PULL_DOWN)
sleep(1)
print("back")
back(0.5)
sleep(1)
out2F.duty_u16(0)
out4F.duty_u16(0)
