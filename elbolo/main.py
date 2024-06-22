#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color, Stop
import time
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from math import pi
from aceleration import moviemiento_recto, retrocede_recto
from girar import girar_90_grados

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
    ev3.speaker.beep(2)
    left_motor.reset_angle(0)
    angulo_initial_motor = abs(left_motor.angle())
    robot.drive(0, 90)
    
    while True:
        if giroscopio.angle() >= angulo:
            robot.stop()
            break
        print(giroscopio.angle())
    ev3.speaker.beep(2)
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
        
        robot.drive(initial_speed, 0)
        initial_speed += final_speed /tiempo
        wait(100)
    if condicional:
        line_follower(follow_distance)
    robot.stop()

# Función para bajar la garra
def bajar_garra():
    motor2.run_target(100,0,Stop.HOLD, True)
    print("finish bajar garra")
    print(motor2.angle())    

# Función para bajar la garra
def subir_garra():
    motor2.run_target(100,-350,Stop.HOLD, True)
    print("finish subir garra")
    print(motor2.angle())
#F Funcion para dejar un bloque sobre el otro
def reposar_bloque():
    motor2.run_target(100,-180,Stop.HOLD, True)
    print("finish reposar bloque")
    print(motor2.angle())


#Esta funcion lo que hace es posicionar la garra en un punto de referencia, para que no choque cuando vaya agarrar bloques
def posicionar_garra_desde_cero():
    motor3.reset_angle(0) #Creo que esta linea de codigo no es necesaria

    motor3.run_target(150, -152, Stop.HOLD, True)

def abrir_garra():
    motor3.stop()
    motor3.run_target(150, 0, Stop.HOLD, True)
    

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
def girar_rad(cuarto_de_circunferencia, dir = 0):
    radio_robot = 12.93  # Ajusta según el radio real de tu robot
    radio_rueda = 6.88   # Ajusta según el radio real de las ruedas
    if dir == 0:
        girar_90_grados(radio_robot, radio_rueda,right_motor, left_motor,cuarto_de_circunferencia)
    else:
        girar_90_grados(radio_robot, radio_rueda,right_motor, left_motor,cuarto_de_circunferencia, velocidad=-100)
    # Detén los motores después del giro
    left_motor.stop()
    right_motor.stop()
    wait(100)
    ev3.speaker.beep(2)


def primer_paso():
    #Posiciona la garra en un punto de referencia y retrocede hasta chocar con la pared, para despues avanzar 
    posicionar_garra_desde_cero()
    # retroceder_robot(robot, 3) # El 1 representa 1 segundo

    retrocede_recto(right_motor, left_motor, 32)
    giroscopio.reset_angle(0)
    moviemiento_recto(right_motor, left_motor, 18)

    # acelerar(robot, 1800)
    # girar(86)
    wait(100)
    girar_rad(4,1)

    
def agarrar_bloques():
    #El robot avanza y se alinea con el primer bloque
    print("acelerar robot")
    moviemiento_recto(right_motor, left_motor, 25)
    # acelerar(robot, 2440-300)
    ev3.speaker.beep(2)

    #El robot gira y se acerca a los bloques
    print("girar hacia los bloques")
    # girar(177)
    wait(100)
    girar_rad(4,1)
    ev3.speaker.beep(4)
    wait(100)
    avanzar(50,40)
    #///////////////

    #El robot agarra el primer bloque rojo, lo sube y retrocede
    cerrar_garra()
    subir_garra()
    print("paso 3")
    ev3.speaker.beep(3)
    avanzar(50,-40)
    #///////////////

    #El robot gira y se alinea con el siguiente bloque
    # girar_izquierda(90)
    wait(100)
    girar_rad(4)
    wait(100)
    avanzar(65,40)
    wait(100)
    # girar(180)
    girar_rad(4,1)
    wait(100)
    avanzar(45,40)
    #///////////////

    #Deja reposar el bloque, baja la garra, abre su garra y recoge ambos bloques
    reposar_bloque()
    abrir_garra() 
    
    posicionar_garra_desde_cero() #Esta funcion sirve para que la garra no choque con los bloques
    bajar_garra() 
    avanzar(10,20)
    cerrar_garra()
    #///////////////

    #El robot retrocede hasta el area amarilla, gira deja los bloques y retrocede
    avanzar(270,-40)
    # girar(262)
    girar_rad(4,1)
    avanzar(65,40)
    abrir_garra()
    avanzar(65,-40)
    #///////////////

def recoger_escombro_1():
    #El robot retrocede hasta chocar con la pared para despues avanzar hacia el primer escombro
    retroceder_robot(robot, 1)
    # acelerar(robot,3000)
    moviemiento_recto(right_motor, left_motor, 31)
    ev3.speaker.beep(2)
    wait(100)
    cerrar_garra()
    #///////////////

    #El robot retrocede hasta un punto de ref, gira y avanza hacia la primera pipa
    # avanzar(70,-40)
    retrocede_recto(right_motor, left_motor, 9)
    wait(500)
    girar_rad(4)
    moviemiento_recto(right_motor, left_motor, 48)
    wait(10000)
    #///////////////

    #El robot se endereza para que quede bien posicionado, sube el elevador y gira para activar la pipa
    subir_garra()
    girar_rad(8, 1)
    wait(500)
    #///////////////

    #Gira hacia la izquierda, deja caer el primer escombro y termina de girar para llegar al punto de inicio
    girar_rad(8)
    girar_rad(4)
    avanzar(50,20)
    abrir_garra()
    avanzar(50,-20)
    girar_rad(4)
    #///////////////

    #El robot avanza hacia el punto de inicio y se endereza
    
    moviemiento_recto(right_motor, left_motor, 47)
    wait(500)
    girar_rad(4)
    bajar_garra()
    #///////////////

recoger_escombro_1()
giroscopio.reset_angle(0)
primer_paso()
agarrar_bloques()


# //////////////////////////////////////////
# SECCION DE PRUEBA DE FUNCIONES:
# //////////////////////////////////////////
# Llama a la función para girar 90 grados

#El robot con esta funcion puede girar 90 grados

# moviemiento_recto(right_motor,left_motor)