left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)


robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2


DRIVE_SPEED = 100


PROPORTIONAL_GAIN = 1.2


while True:
    # Calculate the deviation from the threshold.
    deviation = line_sensor.reflection() - threshold

    # Calculate the turn rate.
    turn_rate = PROPORTIONAL_GAIN * deviation

    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, turn_rate)

    # You can wait for a short time or do other things in this loop.
    wait(10)
  
   