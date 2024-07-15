#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color, Stop
import time
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from math import pi
from aceleration import movimiento_recto, retrocede_recto, avanzar_hasta_color, retroceder_hasta_color
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
    tiempo *= 100
    velocidad = 0
    while velocidad > -100:
        robot.drive(velocidad,0)
        velocidad -= 1 
        wait(10)
    
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

def acelerar(robot, distancia):
    initial_speed = 0
    final_speed = 140
    tiempo = abs((distancia*(18/7))/(68.8*pi))
    tiempo -= 5
    while initial_speed < final_speed:
        
        robot.drive(initial_speed, 0)
        initial_speed += final_speed /tiempo
        wait(100)

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

def mover_garra_angulo(angulo_buscado):
    motor2.run_target(100,angulo_buscado,Stop.HOLD, True) 
    print("finish subir garra")
    print(motor2.angle())

#Esta funcion lo que hace es posicionar la garra en un punto de referencia, para que no choque cuando vaya agarrar bloques
def posicionar_garra_desde_cero():
    motor3.reset_angle(0) #Creo que esta linea de codigo no es necesaria

    motor3.run_target(150, -130, Stop.HOLD, True)

def posicionar_garra_angulo(angle):
    motor3.reset_angle(0)
    motor3.run_target(150, angle, Stop.HOLD, True)

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
    radio_robot = 12.864 # de 12.83 cm a 18 cm , de 18 a 14
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
    mover_garra_angulo(-27)
    
    posicionar_garra_desde_cero()

    retrocede_recto(right_motor, left_motor, 27)
    giroscopio.reset_angle(0)
    wait(100)
    movimiento_recto(right_motor, left_motor, 18.1) 

    # acelerar(robot, 1800)
    # girar(86)
    wait(100)
    girar_rad(4,1)

    
def agarrar_bloques():
    #El robot avanza y se alinea con el primer bloque
    print("acelerar robot")
    movimiento_recto(right_motor, left_motor, 25)
    # acelerar(robot, 2440-300)
    ev3.speaker.beep(2)

    #El robot gira y se acerca a los bloques
    print("girar hacia los bloques")
    # girar(177)
    wait(100)
    girar_rad(4,1)
    ev3.speaker.beep(4)
    wait(100)
    movimiento_recto(right_motor, left_motor, 6.5)
    #///////////////

    #El robot agarra el primer bloque rojo, lo sube y retrocede
    cerrar_garra()
    subir_garra()
    print("paso 3")
    ev3.speaker.beep(3)
    retrocede_recto(right_motor, left_motor, 6.5)

    #///////////////

    #El robot gira y se alinea con el siguiente bloque
    # girar_izquierda(90)
    wait(100)
    girar_rad(4)
    wait(100)
    movimiento_recto(right_motor, left_motor, 9.5)
    wait(100)
    # girar(180)
    girar_rad(4,1)
    wait(100)
    movimiento_recto(right_motor, left_motor, 6.5)
    #///////////////

    #Deja reposar el bloque, baja la garra, abre su garra y recoge ambos bloques
    reposar_bloque()
    abrir_garra() 
    
    posicionar_garra_desde_cero() #Esta funcion sirve para que la garra no choque con los bloques
    bajar_garra() 
    cerrar_garra()
    #///////////////

    #El robot retrocede hasta el area amarilla, gira deja los bloques y retrocede
    retrocede_recto(right_motor, left_motor, 35)

    girar_rad(4,1)
    movimiento_recto(right_motor, left_motor, 6.5)
    abrir_garra()
    retrocede_recto(right_motor, left_motor, 6.5)
    #///////////////

def recoger_escombro_1():
    #El robot retrocede hasta chocar con la pared para despues avanzar hacia el primer escombro
    retroceder_robot(robot, 0.8)
    # acelerar(robot,3000)
    wait(100)
    movimiento_recto(right_motor, left_motor, 31)
    ev3.speaker.beep(2)
    wait(100)
    mover_garra_angulo(-20)
    wait(100)
    cerrar_garra()
    mover_garra_angulo(-5)
    #///////////////

    #El robot retrocede hasta un punto de ref, gira y avanza hacia la primera pipa
    # avanzar(70,-40)
    retrocede_recto(right_motor, left_motor, 9.3)
    wait(500)
    girar_rad(4)
    movimiento_recto(right_motor, left_motor, 48)
    #///////////////

    #El robot se endereza para que quede bien posicionado, sube el elevador y gira para activar la pipa
    subir_garra()

    #Modificar nueva funcion para este paso
    girar_rad(8, 1)
    wait(500)
    #///////////////

    #Gira hacia la izquierda, deja caer el primer escombro y termina de girar para llegar al punto de inicio
    girar_rad(8)
    girar_rad(4)
    movimiento_recto(right_motor, left_motor, 10)
    abrir_garra()
    retrocede_recto(right_motor, left_motor, 10)
    girar_rad(4)
    #///////////////

    #El robot avanza hacia el punto de inicio y se endereza
    
    avanzar_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.RED)
    wait(100)
    movimiento_recto(right_motor, left_motor, 10)
    wait(500)
    girar_rad(4)
    # bajar_garra()
    #///////////////

    
def apilar_tres_bloques():#Esta funcion lo que hace es apilar los bloques desde el amarillo hasta el rojo
    #El robot avanza y se alinea con el primer bloque
    print("acelerar robot")
    movimiento_recto(right_motor, left_motor, 45.5)
    ev3.speaker.beep(2)

    #El robot gira y se acerca a los bloques
    print("girar hacia los bloques")
    
    wait(100)
    girar_rad(4,1)
    ev3.speaker.beep(4)
    wait(100)
    movimiento_recto(right_motor, left_motor, 6.23)
    #///////////////

    #El robot agarra el primer bloque rojo, lo sube y retrocede
    cerrar_garra()
    subir_garra()
    print("paso 3")
    ev3.speaker.beep(3)
    retroceder_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.BLACK)
    #///////////////

    #El robot gira y se alinea con el siguiente bloque
    # girar_izquierda(90)
    wait(200)
    ev3.speaker.beep(4)
    girar_rad(4,1)
    wait(200)
    ev3.speaker.beep(4)
    movimiento_recto(right_motor, left_motor, 9.30)
    wait(200)

    girar_rad(4)
    wait(200)
    movimiento_recto(right_motor, left_motor, 2.5)
    #///////////////

    #Deja reposar el bloque, baja la garra, abre su garra y recoge ambos bloques
    reposar_bloque()
    abrir_garra() 
    
    posicionar_garra_desde_cero() #Esta funcion sirve para que la garra no choque con los bloques
    mover_garra_angulo(-20)
    cerrar_garra()
    subir_garra()
    #///////////////

    #El robot retrocede hasta el area amarilla, gira deja los bloques y retrocede
    retroceder_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.BLACK)
    wait(100)
    girar_rad(4,1)
    movimiento_recto(right_motor, left_motor, 9.10)
    wait(100)
    girar_rad(4)
    wait(100)
    movimiento_recto(right_motor, left_motor, 2.5)

    reposar_bloque()
    abrir_garra()
    posicionar_garra_desde_cero()

    mover_garra_angulo(-25)
    # movimiento_recto(right_motor, left_motor, 0.35)
    # retrocede_recto(right_motor, left_motor, 0.24)
    cerrar_garra()
    
    retrocede_recto(right_motor, left_motor, 35)
    wait(100)
    girar_rad(4,1)
    # retroceder_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.YELLOW)
    retrocede_recto(right_motor, left_motor, 2)
    abrir_garra()


    
    #///////////////


def segundo_escombro_por_linea_roja():
    girar_rad(4,1)
    girar_rad(4,1)
    avanzar_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.GREEN)
    movimiento_recto(right_motor, left_motor, 2)

    cerrar_garra()
    
    movimiento_recto(right_motor, left_motor, 3)

    girar_rad(4,1)
    retroceder_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.RED)
    wait(200)
    #mods nuevas
    movimiento_recto(right_motor, left_motor, 3)
    wait(100)
    girar_rad(4)

    movimiento_recto(right_motor, left_motor, 30) # ajustar distancia 45.5
    subir_garra()
    movimiento_recto(right_motor, left_motor, 7)
    
    reposar_bloque()
    abrir_garra()
    mover_garra_angulo(-25)
    cerrar_garra()

    girar_rad(4,1)

    movimiento_recto(right_motor, left_motor, 7)
    abrir_garra()

    subir_garra()
    girar_rad(4)

    bajar_garra()
    
    posicionar_garra_angulo(-150) # Especificar angulo
    
    movimiento_recto(right_motor, left_motor, 16.5)
    subir_garra()
    girar_rad(8,1)
    wait(100)
    girar_rad(8)

    retrocede_recto(right_motor, left_motor, 16.5)
    girar_rad(4,1)

    #mods bobo 12 y 13 julio
    #funcion para llevar escombor amarillo y gris a la vez
def escombros_punto_de_control ():
    #en la funcion anterior bajar toda la garra
    motor3.reset_angle(-200)#se establece el angulo interno de 0 a -350
    motor2.reset_angle(-350)
    abrir_garra()#abrir hasta q llegue a 0
    wait(100)
    movimiento_recto(right_motor,left_motor,0.5)
    wait(100)
    bajar_garra()
    wait(100)
    cerrar_garra()
    girar_rad(4,1)#4 es 1 es   2 mitad 4 es framento de 90 1 360 2 180 4 90 8 45
    avanzar_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.BLACK)
    girar_rad(4) #4 izquierda y 4 1 derecha
    #detectar negro
    avanzar_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.BLACK)
    girar_rad(4,1)#gira ala derecha
    avanzar_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.RED)
    movimiento_recto(right_motor,left_motor,35)
    girar_rad(4)
    movimiento_recto(right_motor,left_motor,2)
    abrir_garra()
    print("volviendo al punto de control")
    retrocede_recto(right_motor,left_motor,7)
    girar_rad(4)
    avanzar_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.RED)
    movimiento_recto(right_motor,left_motor,10)
    girar_rad(4)
    retrocede_recto(right_motor, left_motor, 9.3)
    wait(500)
    ev3.speaker.beep(4)
    print("bobo llego al punto de control")
    #fin mods hoy
    #:D

    #mods 15 julio
def blocks_amarillo_verdeoazul_azuloverde_lado_derecho():
    movimiento_recto(right_motor,left_motor,10)
    girar_rad(4,1)
    movimiento_recto(right_motor,left_motor,50)
    girar_rad(4,1)
    ev3.speaker.beep(4)
    wait(100)
    motor3.reset_angle(-200)#se establece el angulo interno de 0 a -350
    motor2.reset_angle(-350)
    bajar_garra()
    movimiento_recto(right_motor,left_motor,3)
    cerrar_garra()
    subir_garra()
    print("en camino al block 2")
    print("bloque verde o azul capturado")
    retroceder_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.BLACK)
    wait(100)
    girar_rad(4,1)#der
    movimiento_recto(right_motor, left_motor,3)
    girar_rad(4)#izquierda en frente del sig bloque
    movimiento_recto(right_motor, left_motor,3)
    #Deja reposar el bloque, baja la garra, abre su garra y recoge ambos bloques
    reposar_bloque()
    abrir_garra() 
    posicionar_garra_desde_cero() #Esta funcion sirve para que la garra no choque con los bloques
    mover_garra_angulo(-20)
    cerrar_garra()
    subir_garra()
    #apilar bloque 3 
    print("en camino al block amarillo")
    retroceder_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.BLACK)
    wait(100)
    girar_rad(4,1)#der
    movimiento_recto(right_motor, left_motor,3)
    girar_rad(4)#izquierda en frente del sig bloque
    movimiento_recto(right_motor, left_motor,3)#aqui
    reposar_bloque()
    abrir_garra()
    posicionar_garra_desde_cero()
    mover_garra_angulo(-25)
    cerrar_garra()
    retroceder_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.BLACK)
    wait(100)
    girar_rad(8,1)#giro completo? #verificar con alexander
    movimiento_recto(right_motor,left_motor,21)
    girar_rad(4,1)#derecha
    movimiento_recto(right_motor,left_motor,18)
    bajar_garra()
    abrir_garra()
    #sensor 4 para detectar color de bloque depnedecia de azul o verde
    #falta colocar sensor 4 al bobo
    #por si acaso
    #bucle para ver si el primer block es azul o verde
    # if :
    #     print("El bloque es verde")
    #     #apilar block 2 y 3
    #     movimiento_recto(right_motor, left_motor,17)
    #     wait(100)
    #     reposar_bloque()
    #     abrir_garra()
    #     #fin
    # else:
    #     print("El bloque es azul")
    #     #apilar block 2 y 3
    #     girar_rad(4)#izq
    #     movimiento_recto(right_motor, left_motor,3)
    #     girar_rad(4,1)#der
    #     movimiento_recto(right_motor, left_motor,17)
    #     wait(100)
    #     reposar_bloque()
    #     abrir_garra()
    #     #fin

    #def siguiente_paso :
    #fin mods hoy :D
    
    # recoger_escombro_1()
    # giroscopio.reset_angle(0)
    # primer_paso()
    # apilar_tres_bloques()
    # segundo_escombro()

    # retroceder_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.BLACK) 

    # for i in range(16):
    #     girar_rad(4)
    #     wait(100)

    # for i in range(4):
    #     girar_rad(4)
    #     wait(100)

        #    for i in range(16):
        #     girar_rad(4)
        #     wait(100)
    #    for i in range(16):
    #     girar_rad(4)
    #     wait(100)

    # //////////////////////////////////////////
    # SECCION DE PRUEBA DE FUNCIONES:
def main():
    blocks_amarillo_verdeoazul_azuloverde_lado_derecho()#probar
main()
# //////////////////////////////////////////
# Llama a la función para girar 90 grados
#El robot con esta funcion puede girar 90 grados
# movimiento_recto(right_motor,left_motor)
