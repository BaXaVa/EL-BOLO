#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep
from time import sleep
import math
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
# Write your program here.
ev3.speaker.beep(1)
ev3.screen.print("Hello UAM, Welcome to Robotics Class")

#Configura los motores
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
motor3 = Motor(Port.D)
motor2 = Motor(Port.A)

#hacer que el robot avance 42 cm
robot = DriveBase(left_motor, right_motor, 50,50)
distancia_avance_cm = 60
robot.drive(1000, 0)
velocidad = 50
tiempo = (distancia_avance_cm / velocidad) * 1000

#hacer avanzar al robot 38 cm
wait(tiempo)
robot.stop()

#robot.drive(700, 0)
#wait(1000)
#robot.stop()

#hacer que haga un giro de 0 grados hacia la izquierda del robot
robot.turn(-175)
wait(1000)
robot.stop()

#hacer que avance 14 cm
robot.drive(49, 0)
wait(1000)
robot.stop()

#cerrar garra de motor3 
motor3.run_angle(150 ,-220)
wait(1000)

#haz que el motor trabaje el 100% de su potencia 
motor2.run(-700)
wait(1000)
motor2.stop()

#hace que el robot se haga para atras 
robot = DriveBase(left_motor, right_motor, 50,50)
robot.drive(-69, 0)
wait(1000)
robot.stop()

#haz que se mueva hacia la derecha 200 grados
robot.turn(180)
wait(1000)

#haz que avance para adelante 15 cm
robot.drive(600, 0)
wait(1000)
robot.stop()

#haz que baje la garra ahora de nuevo
motor2.run(700)
wait(1000)
motor2.stop()

#motor3 haz que abra la garra ahora de nuevo
motor3.run_angle(150, 220)
wait(1000)
motor3.stop()

