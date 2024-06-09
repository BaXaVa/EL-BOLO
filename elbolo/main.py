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
    robot.drive(0, 90)
    while True:
        if giroscopio.angle() >= angulo:
            robot.stop()
            break
        print(giroscopio.angle())

def girar_izquierda(angulo):
    robot.drive(0, -90)
    
    while True:
        print(giroscopio.angle())

        if giroscopio.angle() <= angulo:
            print(giroscopio.angle())
            robot.stop()
            break

def enderezar_2(angulo, velocidad):
    robot.drive(0, velocidad)
    
    while True:
        print(giroscopio.angle())

        if giroscopio.angle() == angulo:
            print(giroscopio.angle())
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

# Función para subir la garra
def bajar_garra():
    motor2.run_target(100,0,Stop.HOLD, True)
    print("finish bajar garra")
    print(motor2.angle())    

# Función para bajar la garra
def subir_garra():
    motor2.run_target(100,-350,Stop.HOLD, True)
    print("finish subir garra")
    print(motor2.angle())

def reposar_bloque():
    
    motor2.run_target(100,-180,Stop.HOLD, True)
    print("finish reposar bloque")
    print(motor2.angle())


#Esta funcion lo que hace es posicionar la garra en un punto de referencia, para que no choque cuando vaya agarrar bloques
def posicionar_garra_desde_cero():
    motor3.reset_angle(0)

    motor3.run_target(150, -152, Stop.HOLD, True)

def abrir_garra():
    motor3.stop()
    motor3.run_target(150, 0, Stop.HOLD, True)
    print("finish abrir garra")

def enderezar(angulo):
    if giroscopio.angle() < angulo :
        print("turn right")
        robot.drive(0, 100)
        while True:
            if giroscopio.angle() > angulo:
                robot.stop()
                break
    else:
        robot.drive(0, -100)
        print("turn left")
        while True:
            if giroscopio.angle() < angulo:
                robot.stop()
                break



def primer_paso():
    posicionar_garra_desde_cero()
    print("backing")
    retroceder_robot(robot, 3) # El 1 representa 1 segundo
    wait(500)
    print("foward")
    giroscopio.reset_angle(0)

    acelerar(robot, 1800)

    print("turn right")
    girar(86)
    wait(1000)
    print("acelerate and follow line")
    
def agarrar_bloques():
    print("acelerar robot")
    acelerar(robot, 2430-300)
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
    girar_izquierda(90)
    avanzar(80,40)
    girar(180)
    avanzar(40,40)
    #///////////////

    #Deja reposar el bloque, baja la garra y se aleja
    print(motor2.angle())
    print("reposa bloque")
    reposar_bloque()
    wait(1000)
    print("abrir garra")
    abrir_garra() 
    posicionar_garra_desde_cero()
    print("bajar garra")
    bajar_garra() 
    print("retroceder")
    avanzar(10,20)
    cerrar_garra()
    avanzar(270,-40)
    girar(262)
    enderezar(270)
    avanzar(65,40)
    abrir_garra()
    avanzar(65,-40)

def recoger_escombro_1():
    retroceder_robot(robot, 1)
    acelerar(robot,3000)
    cerrar_garra()
    avanzar(78,-40)


    wait(500)
    girar_izquierda(-88)
    acelerar(robot, 4500)
    enderezar(-87)
    subir_garra()
    girar(-47)
    wait(500)
    girar_izquierda(-177)
    avanzar(50,20)


    abrir_garra()
    avanzar(50,-20)
    girar_izquierda(-267)

    #Cambie la aceleracion de 4500 a 4470
    acelerar(robot, 4350)
    wait(500)
    girar_izquierda(-357)
    enderezar(-360)
    bajar_garra()
    
    


#######################################################

# try:
#     primer_paso()
#     agarrar_bloques()
# except Exception as e:
#     print("Error: ", e)

recoger_escombro_1()
print("finish")
giroscopio.reset_angle(0)
primer_paso()
agarrar_bloques()

def probarGiro():
    robot.drive(0, 90)
    while True:
        print(giroscopio.angle())
        if giroscopio.angle() == 90:
            robot.stop()
            break
    wait(5000)

    robot.drive(0, -90)
    while True:
        print(giroscopio.angle())
        if giroscopio.angle() == 0:
            robot.stop()
            break
    wait(5000)
    robot.drive(0, 90)
    while True:
        print(giroscopio.angle())
        if giroscopio.angle() == 180:
            robot.stop()
            break

# girar(80)
# enderezar(90)

