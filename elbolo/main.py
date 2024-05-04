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
ev3.screen.print("Hello World")


#Configura los motores
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
Motor3 = Motor(Port.D)
motor2 = Motor(Port.A)

    #mueve el motor3 media rotancion en sentido anti-horario
Motor3.run_angle(100, -180)
wait(1000)

#trabaja el motor a al 100% de su potencia es un elevador haz que suba y baje
motor2.run(-600)
wait(1000)
motor2.stop()
wait(1000)

#haz que retroceda el robot 5 cm 
robot = DriveBase(left_motor, right_motor, 100,100)
robot.drive(-1000, 0)
wait(1000)
robot.stop()

#haz que avance para adelante 15 cm
robot.drive(1000, 0)
wait(1000)
robot.stop()

#haz que se mueva hacia la izquierda 90 grados
robot.turn(200)
wait(1000)


#haz que baje la garra ahora de nuevo
motor2.run(350)
wait(1000)
motor2.stop()

#motor3 haz que abra la garra ahora de nuevo
Motor3.run_angle(100, 180)
wait(1000)

#avance en linea recta 
robot = DriveBase(left_motor, right_motor, 80, 80)


#Escribe lineas de codigo para que el robot avance y line recta 10 metros
#con una velocidad de 100 mm/s
# robot.drive(100, 0)
# wait(10000)
# robot.stop()

#cambia los sensonres para que detecte colores
sensor1 = ColorSensor(Port.S1)
sensor2 = ColorSensor(Port.S2)
sensor3 = ColorSensor(Port.S3)

#detener si el snesor 1 y 3 detectan color amarillo 
# #while True:
#     if sensor1.color() == Color.YELLOW and sensor3.color() == Color.YELLOW:
#         robot.stop()
#         break
#     robot.drive(100, 0)
#     wait(100)
#     robot.stop()
#     wait(100)
  
  #cambiar un sensor inflarojo a un sensor de color
sensor4 = ColorSensor(Port.S3)
  
   







