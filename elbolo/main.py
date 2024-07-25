#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from aceleration import movimiento_recto, retrocede_recto, avanzar_hasta_color, retroceder_hasta_color
from girar import girar_90_grados
from testingBlockSensor import test_sensor_color

# Inicialización del brick EV3
ev3 = EV3Brick()
ev3.speaker.beep(1)
ev3.screen.print("Hello UAM, Welcome to Robotics Class")





left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
garra = Motor(Port.D)
grua = Motor(Port.A)
sensor_color_linea = ColorSensor(Port.S2)
sensor_bloque = ColorSensor(Port.S1)
giroscopio = GyroSensor(Port.S3)


# # Inicialización del robot
robot = DriveBase(left_motor, right_motor, 68.8, 124)
robot.settings(100, 100, 180,45)
print(robot.settings())
usar_giro = True 

# robot.heading_control()

set
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
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   

def mover_garra_angulo(angulo_buscado):
    grua.run_target(100,angulo_buscado,Stop.HOLD, True) 
    print("finish subir garra")
    print(grua.angle())

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
    grua.run_target(100,-190,Stop.HOLD, True)
    # print("finish reposar bloque")
    # print(grua.angle())

def mover_grua_angulo(angulo_buscado):
    grua.run_target(100,angulo_buscado,Stop.HOLD, True) 
    # print("finish subir garra")
    # print(grua.angle())

#Esta funcion lo que hace es posicionar la garra en un punto de referencia, para que no choque cuando vaya agarrar bloques
def posicionar_garra_desde_cero():
    garra.reset_angle(0) #Creo que esta linea de codigo no es necesaria

    garra.run_target(150, -140, Stop.HOLD, True)

def posicionar_garra_angulo(angle):
    garra.reset_angle(0)
    garra.run_target(150, angle, Stop.HOLD, True)

def abrir_garra(esperar = True):
    garra.stop()
    garra.run_target(150, 0, Stop.HOLD, esperar)

def girar_rad(cuarto_de_circunferencia, dir = 0):
    radio_robot = 12.5  # de de 12.15 a 
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
    mover_grua_angulo(-40)
    
    posicionar_garra_desde_cero()

    retrocede_recto(right_motor, left_motor, 27)
    giroscopio.reset_angle(0)
    wait(100)
    movimiento_recto(right_motor, left_motor, 18) # cambio de 18.1  a 18 para ajustar la distancia hacia el bloque amarilo 

    # acelerar(robot, 1800)
    # girar(86)
    wait(100)
    robot.turn(-88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   

def recoger_escombro_1():
    #El robot retrocede hasta chocar con la pared para despues avanzar hacia el primer escombro
    mover_grua_angulo(-30)
    retroceder_robot(robot, 0.8)
    # acelerar(robot,3000)
    wait(100)
    movimiento_recto(right_motor, left_motor, 31)
    ev3.speaker.beep(2)
    wait(100)
    
    cerrar_garra()

    #El robot retrocede hasta llegar al borde del punto de control y se direcciona hacia la pipa
    retroceder_hasta_color(right_motor, left_motor, sensor_color_linea, Color.RED)
    retrocede_recto(right_motor, left_motor, 2)
    wait(500)
    robot.turn(88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   
    
    movimiento_recto(right_motor, left_motor, 48)
    #///////////////    

    #El robot se endereza para que quede bien posicionado, sube el elevador y gira para activar la pipa
    subir_garra()

    #Se alinea contra la pared y se endereza
    robot.turn(-88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   
    retrocede_recto(right_motor, left_motor, 21)
    movimiento_recto(right_motor, left_motor, 2)
    wait(100)

    robot.turn(88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   
    retrocede_recto(right_motor, left_motor, 2)
    abrir_garra(False)
    wait(100)

    retroceder_hasta_color(right_motor, left_motor, sensor_color_linea, Color.RED)
    retrocede_recto(right_motor, left_motor, 15)

    #///////////////

    #El robot avanza hacia el punto de inicio y se endereza
    robot.turn(-88)
    robot.stop()
    
    print("Angulo 1: ",giroscopio.angle())   
    wait(100)


    # grua.reset_angle(0)
    

    # bajar_garra()
    #///////////////
    
def apilar_tres_bloques():#Esta funcion lo que hace es apilar los bloques desde el amarillo hasta el rojo
    #El robot avanza y se alinea con el primer bloque
    
    ######################### MEJORA PENDIENDTE: Ajustar la distancia para que se posicione con la linea roja #@@@@@@@@@@2
    movimiento_recto(right_motor, left_motor, 10)
    print("Paso para ver color: ", sensor_color_linea.color())  
    ev3.speaker.beep(4)
    avanzar_hasta_color(right_motor, left_motor, sensor_color_linea,  Color.BLACK)
    ev3.speaker.beep(4)
    movimiento_recto(right_motor, left_motor, 34)
    ev3.speaker.beep(2) 

    #El robot gira y se acerca a los bloques
    # print("girar hacia los bloques")
    
    wait(100)
    giroscopio.reset_angle(0)
    robot.turn(-88)
    robot.stop()
    
    print("Angulo 1: ",giroscopio.angle())   
    ev3.speaker.beep(4)
    wait(100)
    movimiento_recto(right_motor, left_motor, 6.1)
    #///////////////

    #El robot agarra el primer bloque rojo, lo sube y retrocede
    cerrar_garra()
    subir_garra()
    # print("paso 3")
    ev3.speaker.beep(3)
    retroceder_hasta_color(right_motor, left_motor, sensor_color_linea,  Color.BLACK)
    #///////////////

    #El robot gira y se alinea con el siguiente bloque
    
    wait(200)
    ev3.speaker.beep(4)
    robot.turn(-88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   
    
    wait(200)
    ev3.speaker.beep(4)
    movimiento_recto(right_motor, left_motor, 9.6)
    wait(200)

    robot.turn(88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   
    wait(200)
    movimiento_recto(right_motor, left_motor, 2.3)
    #///////////////

    #Deja reposar el bloque, baja la garra, abre su garra y recoge ambos bloques
    reposar_bloque()
    abrir_garra() # se comento esta funcion por mejor funcionamiento
    
    posicionar_garra_desde_cero() #Esta funcion sirve para que la garra no choque con los bloques
    bajar_garra()
    cerrar_garra()
    subir_garra()
    #///////////////

    #El robot retrocede hasta el area amarilla, gira deja los bloques y retrocede
    retroceder_hasta_color(right_motor, left_motor, sensor_color_linea,  Color.BLACK)
    wait(100)
    robot.turn(-88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   
    wait(100)
    movimiento_recto(right_motor, left_motor, 9.10)
    wait(100)
    robot.turn(88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   
    wait(100)
    movimiento_recto(right_motor, left_motor, 2.3)

    reposar_bloque()
    abrir_garra()
    posicionar_garra_desde_cero()

    mover_grua_angulo(-25)
    cerrar_garra()
    
    retrocede_recto(right_motor, left_motor, 35)
    wait(100)
    robot.turn(-88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   
    # retroceder_hasta_color(right_motor, left_motor, sensor_color_linea, sensor_2, Color.YELLOW)
    retrocede_recto(right_motor, left_motor, 2)
    abrir_garra()


    
    #///////////////


def segundo_escombro_por_linea_roja():
    robot.turn(-88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   
    robot.turn(-88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   
    avanzar_hasta_color(right_motor, left_motor, sensor_color_linea,  Color.GREEN)
    movimiento_recto(right_motor, left_motor, 2)

    cerrar_garra()
    
    movimiento_recto(right_motor, left_motor, 8)

    robot.turn(-88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   

    retrocede_recto(right_motor, left_motor, 50)
    # retroceder_hasta_color(right_motor, left_motor, sensor_color_linea, sensor_2, Color.RED)
    movimiento_recto(right_motor, left_motor, 10)

    avanzar_hasta_color(right_motor, left_motor, sensor_color_linea,  Color.RED)
    wait(200)
    #mods nuevas
    # movimiento_recto(right_motor, left_motor, 3) Cambio por retrocede recto, al parecer la distancia no cuadra
    retrocede_recto(right_motor, left_motor, 2)
    wait(100)
    robot.turn(88)
    robot.stop()

    print("Angulo 1: ",giroscopio.angle())   

    movimiento_recto(right_motor, left_motor, 15) # ajustar distancia 45.5
    mover_grua_angulo(-75)
    movimiento_recto(right_motor, left_motor, 7)
    
    reposar_bloque()
    abrir_garra()
    mover_grua_angulo(-35)
    cerrar_garra()
     
    giroscopio.reset_angle(0)
    robot.turn(-88)
    robot.stop()
    
    print("Angulo 1: ",giroscopio.angle())   

    movimiento_recto(right_motor, left_motor, 7)
    abrir_garra()

    subir_garra()
    robot.turn(-88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   

    bajar_garra()
    
    posicionar_garra_angulo(-150) # Especificar angulo
    
    movimiento_recto(right_motor, left_motor, 16.5)
    subir_garra()
    girar_rad(8,1)
    wait(100)
    girar_rad(8)

    retrocede_recto(right_motor, left_motor, 16.5)
    robot.turn(-88)
    robot.stop()
    giroscopio.reset_angle(0)
    print("Angulo 1: ",giroscopio.angle())   

    #mods bobo 12 y 13 julio
    #funcion para llevar escombor amarillo y gris a la vez
def escombros_punto_de_control ():
    #en la funcion anterior bajar toda la garra
    garra.reset_angle(-200)#se establece el angulo interno de 0 a -350 EEs el garra
    grua.reset_angle(-350) # Es el elevador
    abrir_garra()#abrir hasta q llegue a 0
    wait(100)
    movimiento_recto(right_motor,left_motor,0.5)
    wait(100)
    bajar_garra()
    wait(100)
    cerrar_garra()
    girar_rad(4,1)#4 es 1 es   2 mitad 4 es framento de 90 1 360 2 180 4 90 8 45
    avanzar_hasta_color(right_motor, left_motor,  sensor_color_linea, Color.BLACK)
    girar_rad(4) #4 izquierda y 4 1 derecha
    #detectar negro
    avanzar_hasta_color(right_motor, left_motor, sensor_color_linea, Color.BLACK)
    girar_rad(4,1)#gira ala derecha
    avanzar_hasta_color(right_motor, left_motor, sensor_color_linea, Color.RED)
    movimiento_recto(right_motor,left_motor,35)
    girar_rad(4)
    movimiento_recto(right_motor,left_motor,2)
    abrir_garra()
    print("volviendo al punto de control")
    retrocede_recto(right_motor,left_motor,7)
    girar_rad(4)
    avanzar_hasta_color(right_motor, left_motor, sensor_color_linea, Color.RED)
    movimiento_recto(right_motor,left_motor,10)
    girar_rad(4)
    retrocede_recto(right_motor, left_motor, 9.3)
    wait(500)
    ev3.speaker.beep(4)
    print("bobo llego al punto de control")
    #fin mods hoy
    #:D

def segundo_apilar():
    movimiento_recto(right_motor,left_motor,13)#avanza un poco haia adelante
    girar_rad(4)#derecha
    movimiento_recto(right_motor,left_motor,31)
    girar_rad(4,1)#izquierda
    movimiento_recto(right_motor,left_motor,52)
    girar_rad(4)#derecha
    movimiento_recto(right_motor,left_motor,29)
    girar_rad(4,1)#izquierda
    movimiento_recto(right_motor,left_motor,15)#esta de frente al bloque rojo 2
    movimiento_recto(right_motor,left_motor,0.5)#bobo se acerca un poco
    wait(100)
    garra.reset_angle(-200)#se establece el angulo interno de 0 a -350
    grua.reset_angle(-350)
    bajar_garra()
    wait(100)
    cerrar_garra()
    subir_garra()
    print("en camino al block 1 rojo")
    print("bloque verde o azul capturado")
    retroceder_hasta_color(right_motor, left_motor, sensor_color_linea, sensor_color_linea, Color.BLACK)
    wait(100)
    girar_rad(4,1)#izq
    movimiento_recto(right_motor, left_motor,8)
    girar_rad(4)#der en frente del sig bloque
    movimiento_recto(right_motor, left_motor,1)
    #Deja reposar el bloque, baja la garra, abre su garra y recoge ambos bloques
    reposar_bloque()#colocar block sobre otro #apilar_tres_bloques() 
    abrir_garra() 
    posicionar_garra_desde_cero() #Esta funcion sirve para que la garra no choque con los bloques
    mover_garra_angulo(-20)
    cerrar_garra()
    subir_garra()#pendiente
    #apilar bloque 3 
    print("en camino al block amarillo")
    retroceder_hasta_color(right_motor, left_motor, sensor_color_linea, sensor_color_linea, Color.BLACK)
    wait(100)
    girar_rad(4,1)#izq
    movimiento_recto(right_motor, left_motor,8)
    girar_rad(4)#der en frente del bloque amarillo
    movimiento_recto(right_motor, left_motor,0.5)
    reposar_bloque()#apilar_tres_bloques()
    abrir_garra()
    posicionar_garra_desde_cero()
    mover_garra_angulo(-25)
    cerrar_garra()
    retroceder_hasta_color(right_motor, left_motor, sensor_color_linea, sensor_color_linea, Color.BLACK)
    wait(100)
    girar_rad(4,1)#primer giro izq
    movimiento_recto(right_motor,left_motor,21)
    girar_rad(4,1)#segundo giro izq
    movimiento_recto(right_motor,left_motor,10)
    bajar_garra()
    abrir_garra()

def bucle_azul_verde():
    subir_garra()
    retrocede_recto(right_motor,left_motor,10)
    girar_rad(4)#primer giro der
    girar_rad(4)#segundo giro der 


#Ajustes
    #necesito ajustar al bajar la garra
    #motor3.run_target(150,-)x

#Sensor 4
 #////////////////////////////////////////////////////////////////////////////////////////
    #                                        SENSOR 4

    
#mods 15 julio
#modificar la 2do apilacion con el lado opuesto
# def blocks_amarillo_verdeoazul_azuloverde_lado_derecho():
#     print("subimos la garra")
#     subir_garra()
#     movimiento_recto(right_motor,left_motor,13)
#     print("giro a la derecha")
#     girar_rad(4,1)
#     movimiento_recto(right_motor,left_motor,74)
#     girar_rad(4,1)
#     ev3.speaker.beep(4)
#     wait(100)
#     # motor3.reset_angle(-200)#se establece el angulo interno de 0 a -350
#     # motor2.reset_angle(-350)
#     # abrir_garra()
#     bajar_garra()
#     wait(100)
#     movimiento_recto(right_motor,left_motor,0.5)
#     cerrar_garra()
#     subir_garra()
#     print("en camino al block 2")
#     print("bloque verde o azul capturado")
#     retroceder_hasta_color(right_motor, left_motor, sensor_color_linea, sensor_color_linea, Color.BLACK)
#     wait(100)
#     girar_rad(4,1)#der
#     movimiento_recto(right_motor, left_motor,8)
#     girar_rad(4)#izquierda en frente del sig bloque
#     movimiento_recto(right_motor, left_motor,2)
#     #Deja reposar el bloque, baja la garra, abre su garra y recoge ambos bloques
#     reposar_bloque()#colocar block sobre otro #apilar_tres_bloques() 
#     abrir_garra() 
#     posicionar_garra_desde_cero() #Esta funcion sirve para que la garra no choque con los bloques
#     mover_garra_angulo(-20)
#     cerrar_garra()
#     subir_garra()
#     #apilar bloque 3 
#     print("en camino al block amarillo")
#     retroceder_hasta_color(right_motor, left_motor, sensor_color_linea, sensor_color_linea, Color.BLACK)
#     wait(100)
#     girar_rad(4,1)#der
#     movimiento_recto(right_motor, left_motor,8)
#     girar_rad(4)#izquierda en frente del sig bloque
#     movimiento_recto(right_motor, left_motor,1.1)
#     reposar_bloque()#apilar_tres_bloques()
#     abrir_garra()
#     posicionar_garra_desde_cero()
#     mover_garra_angulo(-25)
#     cerrar_garra()
#     retroceder_hasta_color(right_motor, left_motor, sensor_color_linea, sensor_color_linea, Color.BLACK)
#     wait(100)
#     girar_rad(4,1)
#     movimiento_recto(right_motor,left_motor,21)
#     girar_rad(4,1)#derecha
#     movimiento_recto(right_motor,left_motor,16)
#     bajar_garra()
#     abrir_garra()

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
    #////////////////////////////////////////////////////////////////////////////////////////

    #def siguiente_paso : 17 JULY
    #fin mods hoy :D

                    #GIROS
    #girar_rad(8,1)#45 grados a la derecha
    #girar_rad(4,1)#90 grados derecha
    #girar_rad(4)#90 grados izquierda
    #girar_rad(2,1)#180 grados derecha
    #girar_rad(2)#180 grados izquierda
    #girar_rad(1)#360 grados izquierda
    #girar_rad(1,1)#360 grados derecha
    # Giro 360
    #    for i in range(16):
    #     girar_rad(4)
    #     wait(100)

# def encontrar_angulo():
#     pass    


#cubito largo 4.7 ancho 4.7 
# //////////////////////////////////////////
# SECCION DE PRUEBA DE FUNCIONES:
def main(): 
    # recoger_escombro_1()#paso 1 recoger escombro
    # giroscopio.reset_angle(0)
    # primer_paso()#paaso 1.1
    # apilar_tres_bloques()#paso 2 apilar bloques en cuadrito rojo
    # segundo_escombro_por_linea_roja()#paso 3 escombro 2 y 3 + palanca 1 y 2
    # giroscopio.reset_angle(0)
    # segundo_apilar() #paso 4 fila opuesta amarillo base, rojo , rojo
    # bucle_azul_verde()
    #blocks_amarillo_verdeoazul_azuloverde_lado_derecho() sera con el if //Paso 5 y 6
    test_sensor_color(sensor_bloque)
    

 
# right_motor.reset_angle(0)
# right_motor.run_angle(50, 157, wait=True)  # Gira en una dirección (derecha
# print(right_motor.angle())

main()
# //////////////////////////////////////////
# Llama a la función para girar 90 grados

#El robot con esta funcion puede girar 90 grados

# movimiento_recto(right_motor,left_motor)
