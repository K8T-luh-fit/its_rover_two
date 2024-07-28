import motortest
import ultrasonic
import temp
import arm

forearmState = 350
wristState = 2380
clawState = 350

while True():
    listen for stuff i guess
    
    motortest.forward(speed)

    motortest.back(speed)

    motortest.right(speed)

    motortest.left(speed)

    arm.moveArm("up", forearmState, wristState)
    sleep(0.01)

    arm.moveArm("down", forearmState, wristState)
    sleep(0.01)

    arm.grab("release", clawState)
    sleep(0.01)

    arm.grab("grab", clawState)
    sleep(0.01)

    if ultrasonic.querydistance() < 5:
        motortest.forward(speed)
        sleep(0.5)
        motortest.stop() 

    temp.queryhumidity()

    temp.querytemp()

    