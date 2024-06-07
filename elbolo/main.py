#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color, Stop
import time
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from PID import line_follower
from math import pi
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

    tiempo_ms = abs((distancia_cm / velocidad) * 1000)
    robot.drive(velocidad, 0)
    wait(tiempo_ms)
    robot.stop()

# Función para girar el robot un ángulo específico
# def girar(angulo):
#     robot.turn(angulo)
#     wait(1000)
#     robot.stop()

# Función para cerrar la garra
def cerrar_garra():
    print("Cerrando garra")
    # motor3.run_angle(150, -220)
    motor3.run(-150)
    wait(1500)

# Función para abrir la garra

# Función para mover la garra hacia arriba o abajo
def mover_garra(velocidad, angulo):
    motor2.run(velocidad)
    wait(angulo)
    

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

def girar(angulo):
    left_motor.run(90)
    right_motor.run(-90)
    while True:
        if abs(giroscopio.angle()) >= angulo:
            left_motor.brake()
            right_motor.brake()
            break
        print(giroscopio.angle())
def girar_izquierda(angulo):

    robot.drive(0, -90)
    while True:
        if abs(giroscopio.angle()) <= angulo:
            robot.stop()
            break
def acelerar(robot, distancia, condicional = False, follow_distance = 0):
    initial_speed = 0
    final_speed = 140
    tiempo = abs((distancia*(18/7))/(68.8*pi))
    tiempo -= 5
    while initial_speed < final_speed:
        print(initial_speed)
        robot.drive(initial_speed, 0)
        initial_speed += final_speed /tiempo
        wait(100)
    if condicional:
        line_follower(follow_distance)
    robot.stop()

# def bajar_garra():
#     motor2.stop()
#     motor2.run_angle(150, 800)
#     wait(1000)
    
# def estado_de_garra_semicerrada():
# Función para subir la garra
def bajar_garra():
    motor2.run_target(100,350,Stop.HOLD, True)
    print("finish subir garra")

# Función para bajar la garra
def subir_garra():
    motor2.run_target(100,-350,Stop.HOLD, True)
    print("finish bajar garra")

def reposar_bloque():
    motor2.reset_angle(0)
    motor2.run_target(100,180,Stop.HOLD, True)
    print("finish reposar bloque")


#Esta funcion lo que hace es posicionar la garra en un punto de referencia, para que no choque cuando vaya agarrar bloques
def posicionar_garra_desde_cero():
    motor3.reset_angle(0)

    motor3.run_target(150, -152, Stop.HOLD, True)

def abrir_garra():
    motor3.run_target(150, 0, Stop.HOLD, True)
    print("finish abrir garra")

def primer_paso():
    posicionar_garra_desde_cero()
    print("backing")
    retroceder_robot(robot, 1) # El 1 representa 1 segundo
    wait(500)
    print("foward")
    giroscopio.reset_angle(0)

    acelerar(robot, 1800)

    print("turn right")
    girar(86)
    wait(1000)
    print("acelerate and follow line")
    # robot.drive(200, 0)
    # wait(770)
    # robot.stop()
    
def segundo_paso():
    print("acelerar robot")
    acelerar(robot, 2440)
    ev3.speaker.beep(2)
    
    wait(500)
    #El robot gira y se acerca a los bloques
    print("girar hacia los bloques")
    girar(177)
    ev3.speaker.beep(4)
    avanzar(45,40)
    #///////////////

    #El robot agarra el bloque, lo sube y se aleja
    cerrar_garra()
    subir_garra()
    print("paso 3")
    ev3.speaker.beep(3)
    avanzar(45,-40)
    #///////////////

    #El robot gira y se acerca al siguiente bloque
    girar_izquierda(87)
    avanzar(80,40)
    girar(176)
    avanzar(40,40)
    #///////////////

    #Deja reposar el bloque, baja la garra y se aleja
    print(motor2.angle())
    print("reposa bloque")
    reposar_bloque()
    wait(5000)
    print("abrir garra")
    abrir_garra()
    posicionar_garra_desde_cero()
    print("bajar garra")
    bajar_garra() 
    print("retroceder")

    cerrar_garra()
    avanzar(300,-40)
    girar(270)
    avanzar(80,40)
    
    



    # avanzar_robot(robot, 0.5)
    
    


#######################################################

try:
    primer_paso()
    segundo_paso()
except Exception as e:
    print("Error: ", e)
