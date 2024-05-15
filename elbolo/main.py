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


# Programa principal
try:
    # Seguir la línea
    seguir_linea()
    
    # Avanzar una distancia específica
    avanzar(388, 100)
    
    # Girar hacia la izquierda
    girar(-175)
    
    # Avanzar agarrar el bloque, se avanzara poco para que no lo empuje
    avanzar(40, 40)
    
    # Cierra la garra
    cerrar_garra()
    
    # sube la garra, elevador, dejar en negativo por que negativo sube, positivo baja
    mover_garra(-800, 1000)
    
    # Retroceder
    robot.drive(-62, 0)
    
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
