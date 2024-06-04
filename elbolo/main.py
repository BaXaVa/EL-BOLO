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
ev3.screen.print("####### WORKING ########")

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
motor2.reset_angle(0) #esto es para que la garra inicie en 0 grados

#--------------------------------------------------------------------------------------------------------------#
#FUNCIONES DE MOVIMIENTO 
#--------------------------------------------------------------------------------------------------------------#
def acelerar(distancia, condicional = False, follow_distance = 0):
    initial_speed = 0
    final_speed = 140
    tiempo = (distancia*(18/7))/(68.8*pi)
    tiempo -= 5
    while initial_speed < final_speed:
        print(initial_speed)
        left_motor.run(initial_speed) 
        right_motor.run(initial_speed)
        initial_speed += final_speed /tiempo
        wait(100)
    if condicional:
        line_follower(left_motor, right_motor, follow_distance)
    else:
        left_motor.brake()
        right_motor.brake()
#Funcion para acelerar el robot, recibe como parametro:
# La distancia, un condicional para saber si se debe seguir la linea y la distancia a seguir
    

def avanzar(distancia_cm, velocidad):
    tiempo_ms = (distancia_cm / velocidad) * 1000
    robot.drive(velocidad, 0)
    wait(tiempo_ms)
    robot.stop()

def retroceder_robot(robot, tiempo = 1):
    tiempo *= 1000
    robot.drive(-100, 0)
    wait(tiempo)
    robot.stop()
     
"""-> En este apartado tambien tenemos la funcion de seguir linea: line_follower()"""
#--------------------------------------------------------------------------------------------------------------#
# FUNCIONES DE GIRO
#--------------------------------------------------------------------------------------------------------------#

# funcion para que el robot gire de 0 a 90 grados
def girar_90_d(robot):
    robot.drive(0, 90)
    print('3')
    while True:
        print(giroscopio.angle())
        if abs(giroscopio.angle()) >= 90:
            break
    robot.stop()
def girar_90_i():
    robot.drive(0, -90)
    print('3')
    while True:
        print(giroscopio.angle())
        if abs(giroscopio.angle()) <= 90:
            break
    robot.stop()

def girar_180_D(robot):
    print('2')
    print(giroscopio.angle())
    
    robot.drive(0, 90)
    print('3')
    while True:
        print(giroscopio.angle())
        if abs(giroscopio.angle()) >= 180:
            break
    robot.stop()

def girar_270_D(robot):
    robot.drive(0, 90)
    while True:
        if abs(giroscopio.angle()) >= 270:
            break
        print(giroscopio.angle())
    robot.stop()
    print("done right")

#--------------------------------------------------------------------------------------------------------------#
#Funciones para operar la garra
#--------------------------------------------------------------------------------------------------------------#
# Función para cerrar la garra
def cerrar_garra():
    motor3.run_angle(150, -220)
    wait(1000)

# Función para abrir la garra
def abrir_garra():
    motor3.run_angle(150, 220)
    wait(1000)

# Función para mover la garra hacia arriba o abajo (Funcion necesaria mejorar)
def mover_garra(velocidad, angulo):
    motor2.run(velocidad)
    wait(angulo)
    motor2.stop()

# Función para subir la garra
def subir_garra():
    motor2.run_target(100,360,Stop.HOLD, True)

# Función para bajar la garra
def bajar_garra():
    motor2.run_target(100,0,Stop.HOLD, True)

#--------------------------------------------------------------------------------------------------------------#
# Reto
#--------------------------------------------------------------------------------------------------------------#

def primer_paso():
    #Retroceder el robot para alinearlo con el tope
    retroceder_robot(robot, 1) # El 1 representa 1 segundo
    wait(500)

    #ahora reseteamos la posicion en la que estamos como 0 grados
    giroscopio.reset_angle(0)

    #Aceleramos el robot hasta que quede alineado el vertice de las llantas con la linea negra
    acelerar(robot, 1700)
    wait(500)
    
    #Giramos el robot 90 grados exactos por la derecha
    girar_90_d(robot)
    wait(500)

def segundo_paso():
    print("acelerate and follow line")
    acelerar(1500, True, 200) # probar si la funcion puede pasar de acelerar a PID
    # line_follower(200)
    
    # VOY A PROBAR SI LA FUNCION DE ACELERAR PUEDE PASAR DE ACELERAR A PID
    # line_follower(left_motor, right_motor,200)
    ev3.speaker.beep(2)
    
    ev3.speaker.beep(3)
    wait(1000)
    girar_180_D(robot)

    ev3.speaker.beep(4)

    avanzar(54, 40)

    cerrar_garra()

    subir_garra()

    avanzar(54,-40)

    girar_90_i()

    avanzar(20, 40)

    girar_180_D(robot)

    ev3.speaker.beep(4)

    avanzar(54, 40)

    abrir_garra()

    bajar_garra()

    cerrar_garra()

    subir_garra()

def tercer_paso():
    avanzar(54, -40)
        
    


#######################################################

# Programa principal
try:

### Codigo Alenxader empieza
    primer_paso()
    segundo_paso()

    # robot.drive()
    

 
### Codigo Alenxader termina


except:
    print()
#except KeyboardInterrupt:
#    robot.stop()
