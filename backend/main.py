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


def forward(speed):
    """Speed as a decimal 0 to 1"""
    # stop()
    sleep(0.5)
    # duty = round(65000 * speed, 0)
    duty = 64000
    out1F.duty_u16(duty)
    out3F.duty_u16(duty)
    out1B.duty_u16(duty)
    out3B.duty_u16(duty)


while True:
    forward(1)
    sleep(10)
