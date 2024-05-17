# from pybricks.tools import wait
# import time

# def pid(robot, sensor1, sensor2):
#     #Haz un PID que siga la linea con dos sensores
#     #El PID debe ser capaz de seguir la linea negra
#     ki=1
#     kp=0.1
#     kd=0.1
#     integral=0
#     last_error=0
#     derivative=0
#     error=0
#     star_time = time.time()

#     while time.time() - star_time < 4:
#         error=sensor1.reflection()-sensor2.reflection()
#         integral+=error
#         derivative=error-last_error
#         last_error=error
#         robot.drive(250+kp*error+ki*integral+kd*derivative, 0)
#         print(sensor1.reflection())
#         print(sensor2.reflection())

import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait

def pid(robot, sensor1, sensor2):
    ki = 1
    kp = 0.1
    kd = 0.1
    integral = 0
    last_error = 0
    derivative = 0
    error = 0
    start_time = time.time()

    while time.time() - start_time < 4:  # Run for 4 seconds (adjust as needed)
        error = sensor1.reflection() - sensor2.reflection()
        integral += error
        derivative = error - last_error
        last_error = error

        # Calculate motor speed using PID formula
        motor_speed = 250 + kp * error + ki * integral + kd * derivative

        # Apply motor speed to control robot movement
        robot.left_motor.dc(motor_speed)
        robot.right_motor.dc(motor_speed)

        print(sensor1.reflection())
        print(sensor2.reflection())
        wait(10)  # Wait for 10 milliseconds

# Initialize EV3 brick, motors, and sensors
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
sensor1 = ColorSensor(Port.S1)
sensor2 = ColorSensor(Port.S2)

# Call the PID function
pid(robot=ev3, sensor1=sensor1, sensor2=sensor2)