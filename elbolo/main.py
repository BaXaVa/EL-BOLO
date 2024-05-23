#!/usr/bin/env pybricks-micropython
import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.tools import wait
from PID import line_follower

ev3 = EV3Brick()

#Configura los motores

# left_motor = Motor(Port.C)
# right_motor = Motor(Port.B)
# elveador = Motor(Port.A)
# #Configura el robot
# # garra = Motor(Port.D)

# ev3 = EV3Brick()
# left_motor = Motor(Port.B)
# right_motor = Motor(Port.C)
# izquierdo = ColorSensor(Port.S1)
# derecho = ColorSensor(Port.S2)
# robot = DriveBase(left_motor, right_motor, 68.8, 250)

line_follower(1000)