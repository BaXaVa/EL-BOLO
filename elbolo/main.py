#!/usr/bin/env pybricks-micropython
import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.tools import wait

ev3 = EV3Brick()

#Configura los motores

left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
elveador = Motor(Port.A)
#Configura el robot
# garra = Motor(Port.D)

sensor1 = ColorSensor(Port.S1)
sensor2 = ColorSensor(Port.S2)

sensor1.reflection()
sensor2.reflection()

def pid(left_motor, right_motor, sensor1, sensor2):
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
        left_motor.dc(motor_speed)
        right_motor.dc(motor_speed)

        print(sensor1.reflection())
        print(sensor2.reflection())
        wait(10)  # Wait for 10 milliseconds

# Initialize EV3 brick, motors, and sensors
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
sensor1 = ColorSensor(Port.S1)
sensor2 = ColorSensor(Port.S2)

def avanzar_robot(robot, tiempo = 1):
    tiempo *= 1000
    robot.drive(200, 0)
    wait(tiempo)
    robot.stop()

def retroceder_robot(robot, tiempo = 1):
    tiempo *= 1000
    robot.drive(-100, 0)
    wait(tiempo)
    robot.stop()
def girar_180_grados(robot):
    robot.drive(0, 90)
    wait(892)
    robot.stop()

def girar_derecha(robot):
    robot.drive(0, 85)
    wait(488)
    robot.stop()

def girar_izquierda(robot):
    robot.drive(0, -90)
    wait(495)
    robot.stop()

def primer_paso(robot):
    retroceder_robot(robot, 1) # El 1 representa 1 segundo
    wait(200)
    avanzar_robot(robot, 0.77)
    wait(200)
    girar_derecha(robot)
    wait(200)
    avanzar_robot(robot, 5.2)
    ev3.speaker.beep(2)
    girar_180_grados(robot) #Gira 180 grados

def main():
    # ev3.speaker.beep(1)
    # ev3.screen.print("Hello World")
    
    # robot = DriveBase(left_motor, right_motor, 68.8,250)
    
    # left_motor.reset_angle(0)
    # right_motor.reset_angle(0)

    # print("paso1")

    # primer_paso(robot)
    # pid(left_motor, right_motor, sensor1, sensor2)
    while True:
        print(sensor1.reflection())
        print(sensor2.reflection())
        
    
if __name__ == "__main__":  
    main()





