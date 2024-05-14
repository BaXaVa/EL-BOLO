#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from PID import pid 
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Write your program here.


def primer_paso(robot):
    print("paso3")
    
    print("paso4")
    robot.drive(-100, 0)
    wait(1000)
    robot.stop()
    wait(500)
    print("paso5")
    robot.drive(200, 0)
    wait(450)
    robot.stop()
    print("paso6")

def avanzar_robot(robot, sensor1, sensor2):
    robot.drive(200, 0)
    
    while wait(3000):
        print(sensor1.reflection())
        print(sensor2.reflection())
        # quiero que imprima los valores de los sensores mientras sigue avanzando, esto por 3 segundos

    robot.stop()
    

def main():
    ev3.speaker.beep(1)
    ev3.screen.print("Hello World")


    #Configura los motores
    print("paso2")
    left_motor = Motor(Port.C)
    right_motor = Motor(Port.B)
    elveador = Motor(Port.A)
    garra = Motor(Port.D)

    sensor1 = ColorSensor(Port.S1)
    sensor2 = ColorSensor(Port.S2)

    sensor1.reflection()
    sensor2.reflection()
    
    robot = DriveBase(left_motor, right_motor, 67,250)
    print("paso3")
    pid(robot, sensor1, sensor2)
    print("paso4")
    
    # primer_paso(robot)
    # #quiero que solo el motor izquierdo se mueva, para que el robot quede girado
    # #a la derecha
    # left_motor.run(100)
    # wait(3750)
    # left_motor.stop()
    # avanzar_robot(robot, sensor1, sensor2)
main()





