#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
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

# Función para retroceder al robot por una distancia específica
def retroceder(distancia_cm, velocidad):
    tiempo_ms = (distancia_cm / velocidad) * 1000
    robot.drive(-velocidad, 0)
    wait(tiempo_ms)
    robot.stop()

# Función para girar a la derecha utilizando el giroscopio
def girar_derecha():
    giroscopio.reset_angle(0)
    print('2')
    print(giroscopio.angle())
    wait(4000)
    robot.drive(0, 90)
    print('3')
    while True:
        print(giroscopio.angle())
        if abs(giroscopio.angle()) >= 90:
            break
    robot.stop()

# Función para girar 180 grados utilizando el giroscopio
def girar_180():
    giroscopio.reset_angle(0)
    robot.drive(0, 90)
    while True:
        if abs(giroscopio.angle()) >= 180:
            break
    robot.stop()

# Función para girar a la izquierda utilizando el giroscopio
def girar_izquierda():
    giroscopio.reset_angle(0)
    robot.drive(0, -90)
    while True:
        if abs(giroscopio.angle()) >= 90:
            break
    robot.stop()

# Función para retroceder el robot por un tiempo específico
def retroceder_robot(tiempo_segundos):
    robot.drive(-100, 0)
    wait(tiempo_segundos * 1000)
    robot.stop()

# Función para avanzar el robot por un tiempo específico
def avanzar_robot(tiempo_segundos):
    robot.drive(100, 0)
    wait(tiempo_segundos * 1000)
    robot.stop()

# Función de seguimiento de línea
def line_follower():
    while True:
        reflection = sensor_1.reflection() - sensor_2.reflection()
        threshold = 50
        error = reflection - threshold
        turn_rate = error * 1.2
        robot.drive(100, turn_rate)
        if ev3.buttons.pressed():
            break
        wait(10)

# Función principal del primer paso
def primer_paso():
    print("backing")
    retroceder_robot(1)
    wait(500)
    print("foward")
    avanzar_robot(1.15)
    wait(500)
    print("turn")
    girar_derecha()
    wait(1000)
    print("foward")
    avanzar_robot(0.6)
    ev3.speaker.beep(2)
    line_follower()
    ev3.speaker.beep(3)
    wait(1000)
    #girar_180()
    #ev3.speaker.beep(4)
    
    
    
    
    # Función para seguir la línea utilizando sensores de color
def line_follower():
    while True:
        reflection_1 = sensor_1.reflection()
        reflection_2 = sensor_2.reflection()
        
        # Ajustar el umbral y el factor de corrección según sea necesario
        threshold = 50
        error = reflection_1 - reflection_2
        turn_rate = error * 1.2
        
        robot.drive(100, turn_rate)
        
        if ev3.buttons.pressed():
            break
        wait(10)

# Función para avanzar el robot por un tiempo específico
def avanzar_robot(robot, tiempo_segundos):
    robot.drive(100, 0)
    wait(tiempo_segundos * 1000)
    robot.stop()

# Función para retroceder el robot por un tiempo específico
def retroceder_robot(robot, tiempo_segundos):
    robot.drive(-100, 0)
    wait(tiempo_segundos * 1000)
    robot.stop()

# Función para girar 180 grados utilizando el giroscopio
def girar_180(robot):
    giroscopio.reset_angle(0)
    robot.drive(0, 90)
    while abs(giroscopio.angle()) < 180:
        wait(10)
    robot.stop()

# Función para girar a la derecha utilizando el giroscopio
def girar_derecha(robot):
    giroscopio.reset_angle(0)
    robot.drive(0, 90)
    while abs(giroscopio.angle()) < 90:
        wait(10)
    robot.stop()

# Función para girar a la izquierda utilizando el giroscopio
def girar_izquierda(robot):
    giroscopio.reset_angle(0)
    robot.drive(0, -90)
    while abs(giroscopio.angle()) < 90:
        wait(10)
    robot.stop()

# Función principal de ejemplo
def ejemplo_seguidor_linea():
    avanzar_robot(robot, 2) # Avanzar por 2 segundos
    girar_derecha(robot)    # Girar a la derecha
    line_follower()         # Iniciar el seguidor de línea
    girar_izquierda(robot)  # Girar a la izquierda
    retroceder_robot(robot, 1) # Retroceder por 1 segundo
    girar_180(robot)        # Girar 180 grados

# Ejecutar el ejemplo
try:
    #ejemplo_seguidor_linea()

# Programa principal
try:
    
    ejemplo_seguidor_linea()
    
    # Avanzar una distancia específica
    avanzar(570, 100)
    
    # Girar hacia la izquierda
    girar(-168)
    
    # Avanzar y agarrar el bloque
    avanzar(42, 40)
    cerrar_garra()
    mover_garra(-950, 1000)
    
    # Retroceder
    retroceder(54, 40)
    
    # Girar hacia la izquierda
    girar(-162)
    
    # Avanzar nuevamente en línea recta
    avanzar(157, 100)
    
    # Girar y avanzar para el segundo bloque
    girar(160)
    avanzar(35, 45)
    mover_garra(300, 1000)
    abrir_garra()
    wait(3000)
    mover_garra(800, 1000)
    cerrar_garra()
    mover_garra(-800, 1000)
    
    # Retroceder
    retroceder(50, 40)
    
    # Girar y avanzar hacia la zona de depósito
    left_motor.run(30)
    right_motor.run(30)
    girar(160)
    avanzar(235, 60)
    girar(180)
    avanzar(85, 40)
    mover_garra(800, 1000)
    wait(2000)
    abrir_garra()
    retroceder(70, 40)
    
    # Girar y avanzar para agarrar otros bloques
    girar(170)
    avanzar(90, 50)
    girar(170)
    avanzar(42, 30)
    cerrar_garra()
    retroceder(50, 40)
    girar(-170)

except KeyboardInterrupt:
    robot.stop()
