# Hello Ms Terkper, this is my clawbot code.

def when_started1():
    global myVariable, TopBlockVariable, xnotdefinedyet
    JawsOfLife.set_velocity(50, PERCENT)
    while True:
        if controller.buttonUp.pressing():
            while not not controller.buttonUp.pressing():
                JawsOfLife.spin(FORWARD)
                wait(5, MSEC)
            JawsOfLife.stop()
        if controller.buttonDown.pressing():
            while not not controller.buttonDown.pressing():
                JawsOfLife.spin(REVERSE)
                wait(5, MSEC)
            JawsOfLife.stop()
        if controller.buttonR2.pressing():
            for repeat_count in range(4):
                JawsOfLife.spin_for(REVERSE, 90, DEGREES)
                JawsOfLife.spin_for(FORWARD, 90, DEGREES)
                drivetrain.drive_for(FORWARD, 23, INCHES)
                JawsOfLife.spin_for(REVERSE, 90, DEGREES)
                LiftUpMotor.spin_for(FORWARD, 120, DEGREES)
                drivetrain.turn_for(RIGHT, 180, DEGREES)
                drivetrain.drive_for(FORWARD, 46, INCHES)
                JawsOfLife.spin_for(FORWARD, 90, DEGREES)
                drivetrain.turn_for(RIGHT, 180, DEGREES)
                drivetrain.drive_for(FORWARD, 23, INCHES)
                wait(5, MSEC)
        wait(5, MSEC)

when_started1()
