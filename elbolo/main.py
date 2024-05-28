#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.tools import wait
from pybricks.parameters import Port
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
    motor2.hold()
    
#funcion para retroceder al robot por una distancia especifica
def retroceder(distancia_cm, velocidad):
    tiempo_ms = (distancia_cm / velocidad) * 1000
    robot.drive(-velocidad, 0)
    wait(tiempo_ms)
    robot.stop()
    


# Programa principal
try:
    
    # Avanzar una distancia específica
    avanzar(570, 100)
    
    # Girar hacia la izquierda
    girar(-168)
    
    # Avanzar agarrar el bloque, se avanzara poco para que no lo empuje
    avanzar(42, 40)
    
    # Cierra la garra
    cerrar_garra()
    
    # sube la garra, elevador, dejar en negativo por que negativo sube, positivo baja
    mover_garra(-950, 1000)
    
    # Retroceder
    retroceder (54, 40)
    
    # Girar hacia la iq\zquierda 170 grados
    girar(-162)
    
    # Avanzar nuevamente en linea recta
    avanzar(157, 100)
    
    #girar de nuevo para pegar ambos bloques
    girar(160)
    
    #avanzar de nuevo para segundo bloque
    avanzar(34, 45)
    
    #bajar elevador para agarrar bloque 2
    mover_garra(250,1000)
    
    #abre garra para agar ambos bloques 
    abrir_garra()
    wait(3000)
    
    #bajar elevador completamente para agarrar ambos bloques
    mover_garra(800,1000)
    
    #cerrar garra para agarrar ambos bloques
    cerrar_garra()
    
    #subir elevador para no arrastrar bloques
    mover_garra(-800,1000)
    
    #hacerse hacia atras 

    retroceder(50,40)

    #retroceder(40,40)
    
    #girar hacia la derecha con el motor trabajando al 30% de su capacidad
    left_motor.run(30)
    right_motor.run(-30)
    girar(160)
    
    #avanzar 170 cm para llegar a la zona de deposito
    avanzar(225,60)
    
    #girar hacia la derecha
    girar(180)
    
    #avance 40 cm 
    avanzar(75,40)
    
    #bajar garra la derecha
    mover_garra(800,1000)
    wait(2000)
    
    #abrir garra para soltar bloques
    abrir_garra()
    
    

except KeyboardInterrupt:
    robot.stop()



#mueve la garra para no arrastrar bloques
while True:
    print(giroscopio.angle())
    wait(1000)
    
