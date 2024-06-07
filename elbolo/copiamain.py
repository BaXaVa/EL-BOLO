#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
<<<<<<< HEAD:elbolo/copiamain.py
=======
from pybricks.tools import wait
>>>>>>> a8c546967952b4b478d72e602d9de2bd0ce2c72d:elbolo/main.py
from pybricks.parameters import Port, Color
import time
from pybricks.tools import wait
from pybricks.robotics import DriveBase
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
    motor3.run_angle(150, -220)
    wait(1000)

# Función para abrir la garra
def abrir_garra():
    motor3.run_angle(150, 220)
    wait(1000)

# Función para mover la garra hacia arriba o abajo
def subirElevador(velocidad, angulo):
    motor2.run(velocidad)
    wait(angulo)
    motor2.hold()
    
#funcion para retroceder al robot por una distancia especifica
def retroceder(distancia_cm, velocidad):
    tiempo_ms = (distancia_cm / velocidad) * 1000
    robot.drive(-velocidad, 0)
    wait(tiempo_ms)
    robot.stop()




<<<<<<< HEAD:elbolo/copiamain.py
=======


>>>>>>> a8c546967952b4b478d72e602d9de2bd0ce2c72d:elbolo/main.py
# Programa principal
try:
    
    # Avanzar una distancia específica
<<<<<<< HEAD:elbolo/copiamain.py
    avanzar(58, 100)
=======
    avanzar(582, 100)
>>>>>>> a8c546967952b4b478d72e602d9de2bd0ce2c72d:elbolo/main.py
    
    # Girar hacia la izquierda
    girar(-168)
    
    # Avanzar agarrar el bloque, se avanzara poco para que no lo empuje
<<<<<<< HEAD:elbolo/copiamain.py
    avanzar(80, 40)
    
    #girar al bloque, se avanzara poco para que no lo empuje
    girar(-175)
    avanzar(40, 40)
=======
    avanzar(54, 40)
>>>>>>> a8c546967952b4b478d72e602d9de2bd0ce2c72d:elbolo/main.py
    
    # Cierra la garra
    cerrar_garra()
    
    # sube la garra, elevador, dejar en negativo por que negativo sube, positivo baja
    subirElevador(-800, 1000)
    
    # Retroceder
<<<<<<< HEAD:elbolo/copiamain.py
    robot.drive(-62, 40)
=======
    retroceder (52, 40)
>>>>>>> a8c546967952b4b478d72e602d9de2bd0ce2c72d:elbolo/main.py
    
    # Girar hacia la iq\zquierda 170 grados
    girar(-160)
    
    # Avanzar nuevamente en linea recta
    avanzar(162, 100)
    
    #girar de nuevo para pegar ambos bloques
    girar(168)
    
    #avanzar de nuevo para segundo bloque
    avanzar(54, 40)
    
    #bajar elevador para agarrar bloque 2
    mover_garra(270,1000)
    
    #abre garra para agar ambos bloques 
    abrir_garra()
    wait(3000)
    
    #bajar elevador completamente para agarrar ambos bloques
    mover_garra(800,1000)
    
    #cerrar garra para agar ambos bloques
    cerrar_garra()
    
    #subir elevador para no arrastrar bloques
    mover_garra(-800,1000)
    
    

except KeyboardInterrupt:
    robot.stop()



#mueve la garra para no arrastrar bloques
while True:
    print(giroscopio.angle())
    wait(1000)
    