#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
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

# Inicialización del robot
robot = DriveBase(left_motor, right_motor, 50, 50)

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
    
   #hacer una funcion q retroceda 
def retroceda(velocidad, angulo):
    robot.drive(velocidad, 0)
    wait(angulo)
    robot.stop()

# Programa principal
try:
    
    
    # Avanzar una distancia específica
    avanzar(150, 100)
    
    # Girar hacia la izquierda
    girar(180)
    
    # Avanzar agarrar el bloque, se avanzara poco para que no lo empuje
    avanzar(60, 40)
    
    # Cierra la garra
    cerrar_garra()
    
    # sube la garra, elevador, dejar en negativo por que negativo sube, positivo baja
    mover_garra(-800, 1000)
    
    # Retroceder
    retroceder (-150,100)
    
    # Girar hacia la derecha 170 grados
    girar(-120)
    
    # Avanzar nuevamente en linea recta
    avanzar(200, 100)
    
    # Girar hacia la izquierda
    girar(-140)
    
    #avanzar para apilar el segundo bloque
    avanzar(56 ,40)
    
    #bajar elevador para
    mover_garra(300, 1000)
    wait(300)
    mover_garra(800, 1000)
    cerrar_garra()
    mover_garra(-800, 1000)
    

except KeyboardInterrupt:
    robot.stop()
