#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


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
  Motor3 = Motor(Port.D)
  motor2 = Motor(Port.A)

  #cerrar garra de motor3 
motor3.run_angle(200 ,-180)
wait(1000)

#trabaja el motor a al 100% de su potencia es un elevador haz que suba 
motor2.run(-1000)
wait(1000)

#hace que el robot se haga para atras 

robot = DriveBase(left_motor, right_motor, 50,50)
robot.drive(-300, 0)
wait(1000)
robot.stop()

#haz que se mueva hacia la derecha 90 grados

robot.turn(-200)
wait(1000)

#haz que avance para adelante 5 cm
robot.drive(90, 0)
wait(1000)
robot.stop()

#haz que baje la garra ahora de nuevo
motor2.run(700)
wait(1000)
motor2.stop()

#motor3 haz que abra la garra ahora de nuevo
Motor3.run_angle(100, 180)
wait(1000)


#cambia los sensonres para que detecte colores
sensor1 = ColorSensor(Port.S1)
sensor2 = ColorSensor(Port.S2)
sensor3 = ColorSensor(Port.S3)



