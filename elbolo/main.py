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
<<<<<<< HEAD
    motor3.run_angle(200, -220)
    wait(1000)
    
def cerrar_garra_littler():
    motor3.run_angle(105, -130)
    wait(3000)
=======
    # motor3.run_angle(150, -220)
    motor3.run(-150)
    wait(1500)

>>>>>>> 412db48abc6c95645e44d59689908ee0097b7ca9
# Función para abrir la garra
def abrir_garra():
    motor3.run_angle(100, 220)
    wait(1000)

# Función para mover la garra hacia arriba o abajo
def subirElevador(velocidad, angulo):
    motor2.run(velocidad)
    wait(angulo)
<<<<<<< HEAD

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
=======
    

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

    print('2')
    print(giroscopio.angle())
    wait(100)
    robot.drive(0, 90)
    print('3')
    while True:
        print(giroscopio.angle())
        if abs(giroscopio.angle()) >= 87:
            break
    robot.stop()
    
def girar_180(robot):
    robot.drive(0, 90)
    while True:
        if abs(giroscopio.angle()) >= 177:
            break
        print(giroscopio.angle())
    robot.stop()
    print("done right")

def girar(angulo):
    left_motor.run(90)
    right_motor.run(-90)
    while True:
        if abs(giroscopio.angle()) >= angulo:
            left_motor.brake()
            right_motor.brake()
            break
        print(giroscopio.angle())
    


def girar_izquierda(robot):
    giroscopio.reset_angle(0)
    robot.drive(0, 90)
    while True:
        if abs(giroscopio.angle()) >= 90:
            break

    robot.stop()

def acelerar(robot, distancia, condicional = False, follow_distance = 0):
    initial_speed = 0
    final_speed = 140
    tiempo = (distancia*(18/7))/(68.8*pi)
    tiempo -= 5
    while initial_speed < final_speed:
        print(initial_speed)
        robot.drive(initial_speed, 0)
        initial_speed += final_speed /tiempo
        wait(100)
    if condicional:
        line_follower(follow_distance)
    robot.stop()
    

def primer_paso(robot):
    print("backing")
    retroceder_robot(robot, 1) # El 1 representa 1 segundo
    wait(500)
    print("foward")
    giroscopio.reset_angle(0)

    acelerar(robot, 1700)

    print("turn right")
    girar(87)
    wait(1000)
    print("acelerate and follow line")
    # robot.drive(200, 0)
    # wait(770)
    # robot.stop()
    acelerar(robot, 2200)
    ev3.speaker.beep(2)
    
    ev3.speaker.beep(3)
    wait(1000)
    girar(177)
    ev3.speaker.beep(4)
    avanzar(50,40)
    cerrar_garra()
    mover_garra(-800,1000)

    avanzar(50,-40)
    



    # avanzar_robot(robot, 0.5)
    
    


#######################################################

# Programa principal
try:

### Codigo Alenxader empieza
    primer_paso(robot)

 
### Codigo Alenxader termina


except:
    print()
#except KeyboardInterrupt:
#    robot.stop()
>>>>>>> 412db48abc6c95645e44d59689908ee0097b7ca9
