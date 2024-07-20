#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from aceleration import movimiento_recto, retrocede_recto, avanzar_hasta_color, retroceder_hasta_color
from girar import girar_90_grados

# Inicialización del brick EV3
ev3 = EV3Brick()
ev3.speaker.beep(1)
ev3.screen.print("Hello UAM, Welcome to Robotics Class")

# Configuración de los motores y sensores

left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
garra = Motor(Port.D)
grua = Motor(Port.A)
sensor_1 = ColorSensor(Port.S1)
sensor_2 = ColorSensor(Port.S2)
giroscopio = GyroSensor(Port.S3)

# Inicialización del robot
robot = DriveBase(left_motor, right_motor, 68.8, 124)
robot.settings(100, 100 ,100, 100)

################################################

def cerrar_garra():
    print("Cerrando garra")
    # garra.run_angle(150, -220)
    garra.run(-150)
    wait(1500)

################################################

def retroceder_robot(robot, tiempo = 1):
    tiempo *= 100
    velocidad = 0
    while velocidad > -100:
        robot.drive(velocidad,0)
        velocidad -= 1 
        wait(10)
    
    wait(tiempo)
    robot.stop()

# Función para bajar la garra
def bajar_garra():
    grua.run_target(100,0,Stop.HOLD, True)
    # print("finish bajar garra")
    # print(grua.angle())    

# Función para bajar la garra
def subir_garra():
    grua.run_target(100,-350,Stop.HOLD, True)
    # print("finish subir garra")
    # print(grua.angle())

#F Funcion para dejar un bloque sobre el otro
def reposar_bloque():
    grua.run_target(100,-180,Stop.HOLD, True)
    # print("finish reposar bloque")
    # print(grua.angle())

def mover_grua_angulo(angulo_buscado):
    grua.run_target(100,angulo_buscado,Stop.HOLD, True) 
    # print("finish subir garra")
    # print(grua.angle())

#Esta funcion lo que hace es posicionar la garra en un punto de referencia, para que no choque cuando vaya agarrar bloques
def posicionar_garra_desde_cero():
    garra.reset_angle(0) #Creo que esta linea de codigo no es necesaria

    garra.run_target(150, -130, Stop.HOLD, True)

def posicionar_garra_angulo(angle):
    garra.reset_angle(0)
    garra.run_target(150, angle, Stop.HOLD, True)

def abrir_garra():
    garra.stop()
    garra.run_target(150, 0, Stop.HOLD, True)

def girar_rad(cuarto_de_circunferencia, dir = 0):
    radio_robot = 12.29  # de de 12.15 a 
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

##################################################################

def primer_paso():
    #Posiciona la garra en un punto de referencia y retrocede hasta chocar con la pared, para despues avanzar 
    mover_grua_angulo(-27)
    
    posicionar_garra_desde_cero()

    retrocede_recto(right_motor, left_motor, 27)
    giroscopio.reset_angle(0)
    wait(100)
    movimiento_recto(right_motor, left_motor, 18.1) 

    # acelerar(robot, 1800)
    # girar(86)
    wait(100)
    robot.turn(90)

def recoger_escombro_1():
    #El robot retrocede hasta chocar con la pared para despues avanzar hacia el primer escombro
    retroceder_robot(robot, 0.8)
    # acelerar(robot,3000)
    wait(100)
    movimiento_recto(right_motor, left_motor, 31)
    ev3.speaker.beep(2)
    wait(100)
    mover_grua_angulo(-20)
    wait(100)
    cerrar_garra()
    mover_grua_angulo(-5)
    #///////////////

    #El robot retrocede hasta un punto de ref, gira y avanza hacia la primera pipa
    # avanzar(70,-40)
    retrocede_recto(right_motor, left_motor, 9.3)
    wait(500)
    robot.turn(-90)
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
    robot.turn(-90)
    movimiento_recto(right_motor, left_motor, 10)
    abrir_garra()
    retrocede_recto(right_motor, left_motor, 10)
    robot.turn(-90)
    #///////////////

    #El robot avanza hacia el punto de inicio y se endereza
    
    avanzar_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.RED)
    wait(100)
    movimiento_recto(right_motor, left_motor, 10)
    wait(500)
    robot.turn(-90)
    # bajar_garra()
    #///////////////
print
    
def apilar_tres_bloques():#Esta funcion lo que hace es apilar los bloques desde el amarillo hasta el rojo
    #El robot avanza y se alinea con el primer bloque
    # print("acelerar robot")
    movimiento_recto(right_motor, left_motor, 45.5)
    ev3.speaker.beep(2)

    #El robot gira y se acerca a los bloques
    # print("girar hacia los bloques")
    
    wait(100)
    robot.turn(90)
    ev3.speaker.beep(4)
    wait(100)
    movimiento_recto(right_motor, left_motor, 6.23)
    #///////////////

    #El robot agarra el primer bloque rojo, lo sube y retrocede
    cerrar_garra()
    subir_garra()
    # print("paso 3")
    ev3.speaker.beep(3)
    retroceder_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.BLACK)
    #///////////////

    #El robot gira y se alinea con el siguiente bloque
    # girar_izquierda(90)
    wait(200)
    ev3.speaker.beep(4)
    robot.turn(90)
    wait(200)
    ev3.speaker.beep(4)
    movimiento_recto(right_motor, left_motor, 9.30)
    wait(200)

    robot.turn(-90)
    wait(200)
    movimiento_recto(right_motor, left_motor, 2.5)
    #///////////////

    #Deja reposar el bloque, baja la garra, abre su garra y recoge ambos bloques
    reposar_bloque()
    abrir_garra() 
    
    posicionar_garra_desde_cero() #Esta funcion sirve para que la garra no choque con los bloques
    mover_grua_angulo(-20)
    cerrar_garra()
    subir_garra()
    #///////////////

    #El robot retrocede hasta el area amarilla, gira deja los bloques y retrocede
    retroceder_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.BLACK)
    wait(100)
    robot.turn(90)
    movimiento_recto(right_motor, left_motor, 9.10)
    wait(100)
    robot.turn(-90)
    wait(100)
    movimiento_recto(right_motor, left_motor, 2.5)

    reposar_bloque()
    abrir_garra()
    posicionar_garra_desde_cero()

    mover_grua_angulo(-25)
    # movimiento_recto(right_motor, left_motor, 0.35)
    # retrocede_recto(right_motor, left_motor, 0.24)
    cerrar_garra()
    
    retrocede_recto(right_motor, left_motor, 35)
    wait(100)
    robot.turn(90)
    # retroceder_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.YELLOW)
    retrocede_recto(right_motor, left_motor, 2)
    abrir_garra()


    
    #///////////////


def segundo_escombro_por_linea_roja():
    robot.turn(90)
    robot.turn(90)
    avanzar_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.GREEN)
    movimiento_recto(right_motor, left_motor, 2)

    cerrar_garra()
    
    movimiento_recto(right_motor, left_motor, 3)

    robot.turn(90)
    retroceder_hasta_color(right_motor, left_motor, sensor_1, sensor_2, Color.RED)
    wait(200)
    #mods nuevas
    movimiento_recto(right_motor, left_motor, 3)
    wait(100)
    robot.turn(-90)

    movimiento_recto(right_motor, left_motor, 30) # ajustar distancia 45.5
    subir_garra()
    movimiento_recto(right_motor, left_motor, 7)
    
    reposar_bloque()
    abrir_garra()
    mover_grua_angulo(-25)
    cerrar_garra()

    robot.turn(90)

    movimiento_recto(right_motor, left_motor, 7)
    abrir_garra()

    subir_garra()
    robot.turn(-90)

    bajar_garra()
    
    posicionar_garra_angulo(-150) # Especificar angulo
    
    movimiento_recto(right_motor, left_motor, 16.5)
    subir_garra()
    girar_rad(8,1)
    wait(100)
    girar_rad(8)

    retrocede_recto(right_motor, left_motor, 16.5)
    robot.turn(90)











def encontrar_angulo():
    pass     


# //////////////////////////////////////////
# SECCION DE PRUEBA DE FUNCIONES:
def main(): 
    recoger_escombro_1()
    giroscopio.reset_angle(0)
    primer_paso()
    apilar_tres_bloques()
    segundo_escombro_por_linea_roja()
    giroscopio.reset_angle(0)
    



# right_motor.reset_angle(0)
# right_motor.run_angle(50, 157, wait=True)  # Gira en una dirección (derecha
# print(right_motor.angle())



main()
# //////////////////////////////////////////
# Llama a la función para girar 90 grados

#El robot con esta funcion puede girar 90 grados

# movimiento_recto(right_motor,left_motor)