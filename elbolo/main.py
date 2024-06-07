#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color
import time
from pybricks.tools import wait
from pybricks.robotics import DriveBase


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
#Estas son las funciones que se ocupan para el robot
#----------------------------------------------------------------#
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
    motor3.run_angle(200, -220)
    wait(1000)
    
def cerrar_garra_littler():
    motor3.run_angle(105, -130)
    wait(3000)
# Función para abrir la garra
def abrir_garra():
    motor3.run_angle(100, 220)
    wait(1000)

# Función para mover la garra hacia arriba o abajo
def subirElevador(velocidad, angulo):
    motor2.run(velocidad)
    wait(angulo)

# Programa principal
try:
    #cerrar poco la garra
    cerrar_garra_littler()
     
     # Avanzar una distancia específica
    avanzar(80, 100)
    
    # Girar hacia la derecha 
    girar(165)
    
    # Avanzar agarrar el bloque, se avanzara poco para que no lo empuje
    avanzar(165, 30)
    
    #girar al bloque, se avanzara poco para que no lo empuje
    girar(165)
    avanzar(49, 40)
    
    # Cierra la garra
    cerrar_garra()
    
    # sube la garra, elevador, dejar en negativo por que negativo sube, positivo baja
    subirElevador(-1000, 800)
    
    # Retroceder
    robot.drive(-62, 40)
    
    # Girar hacia la derecha 170 grados
    girar(170)
    
    # Avanzar nuevamente en linea recta
    avanzar(300, 100)
    
    # Abrir la garra
    abrir_garra()
    
    # Girar hacia la izquierda
    girar(-220)
except KeyboardInterrupt:
    robot.stop()
