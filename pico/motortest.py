from machine import Pin, PWM
from time import sleep

# Initialize PWM on pins
out1FL = PWM(Pin(0))
out2FL = PWM(Pin(1))
out1FL.freq(5000)
out2FL.freq(5000)

# Set initial duty cycle to 0
out1FL.duty_u16(0)
out2FL.duty_u16(0)

try:
    while True:
        # Forward
        out1FL.duty_u16(64000)
        sleep(1)
        # Half speed
        out1FL.duty_u16(32000)
        sleep(1)
        out1FL.duty_u16(0)
        sleep(0.5)

        # Backward
        out2FL.duty_u16(64000)
        sleep(1)
        # Half speed
        out2FL.duty_u16(32000)
        sleep(1)
        out2FL.duty_u16(0)
        sleep(0.5)

finally:
    out1FL.duty_u16(0)
    out2FL.duty_u16(0)
