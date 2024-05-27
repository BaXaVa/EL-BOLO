#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color
import time
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from PID import line_follower

# Inicialización del brick EV3
ev3 = EV3Brick()
ev3.speaker.beep(1)
ev3.screen.print("Hello UAM, Welcome to Robotics Class")

# Configuración de los motores y sensores
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
motor3 = Motor(Port.D)
motor2 = Motor(Port.A)
sensor_1 = ColorSensor(Port.S1)
sensor_2 = ColorSensor(Port.S2)
giroscopio = GyroSensor(Port.S3)

# Inicialización del robot
robot = DriveBase(left_motor, right_motor, 50, 50)

################################################
#Funciones Bayardo
# Función para avanzar el robot una distancia específica
def avanzar(distancia_cm, velocidad):
    tiempo_ms = (distancia_cm / velocidad) * 1000
    robot.drive(velocidad, 0)
    wait(tiempo_ms)
    robot.stop()

# Función para girar el robot un ángulo específico
def girar(angulo):
    robot.turn(angulo)
    wait(1000)
    robot.stop()

# Función para cerrar la garra
def cerrar_garra():
    motor3.run_angle(150, -220)
    wait(1000)

# Función para abrir la garra
def abrir_garra():
    motor3.run_angle(150, 220)
    wait(1000)

# Función para mover la garra hacia arriba o abajo
def mover_garra(velocidad, angulo):
    motor2.run(velocidad)
    wait(angulo)
    motor2.stop()

# Función para seguir la línea con condiciones específicas para los sensores
def seguir_linea():
    while True:
        color_1 = sensor_1.color
        color_2 = sensor_2.color
        
        if color_1 == Color.WHITE:
            robot.drive(20, 0)
        else:
            robot.stop()
            break
        
        if color_2 == Color.BLACK:
            robot.drive(20, 0)
        else:
            robot.stop()
            break

################################################
#Funciones Alexander

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

    giroscopio.reset_angle(0)
    print('2')
    print(giroscopio.angle())
    wait(4000)
    robot.drive(0, 90)
    print('3')
    while True:
        print(giroscopio.angle())
        if abs(giroscopio.angle()) >= 90:
            break
    robot.stop()
    
def girar_180(robot):
    robot.drive(0, 90)
    while True:
        if abs(giroscopio.angle()) >= 270:
            break
        print(giroscopio.angle())
    robot.stop()
    print("done right")

def girar_izquierda(robot):
    giroscopio.reset_angle(0)
    robot.drive(0, 90)
    while True:
        if abs(giroscopio.angle()) >= 90:
            break

    robot.stop()

def primer_paso(robot):
    print("backing")
    retroceder_robot(robot, 1) # El 1 representa 1 segundo
    wait(500)
    print("foward")
    avanzar_robot(robot, 0.55)
    wait(500)
    print("turn")
    girar_derecha(robot)
    wait(1000)
    print("foward")
    avanzar_robot(robot, 0.6)
    ev3.speaker.beep(2)
    line_follower()
    ev3.speaker.beep(3)
    wait(1000)
    girar_180(robot)
    ev3.speaker.beep(4)

    # avanzar_robot(robot, 0.5)
    
    


#######################################################

# Programa principal
try:

### Codigo Alenxader empieza
    primer_paso(robot)
    # line_follower(1000

 
### Codigo Alenxader termina


except:
    print()
#except KeyboardInterrupt:
#    robot.stop()
