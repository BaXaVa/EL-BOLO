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
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
garra = Motor(Port.D)
grua = Motor(Port.A)
sensor_color_bloque = ColorSensor(Port.S2)
sensor_bloque_enfrente= ColorSensor(Port.S1)

giroscopio = GyroSensor(Port.S3)
    #sensor 2


    # # Inicialización del robot
robot = DriveBase(left_motor, right_motor, 68.8, 124)
robot.settings(100, 100, 69,276)
print(robot.settings())
usar_giro = True 

    # robot.heading_control()

set
    ################################################

def cerrar_garra():
        """Cierra la garra totalmente"""
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

def mover_grua_angulo(angulo_buscado):
        """Se le puede pasar un angulo a la grua para determinar la altura a la que queda"""
        grua.run_target(100,angulo_buscado,Stop.HOLD, True) 
        print("finish subir garra")
        print(grua.angle())

    # Función para bajar la garra
def bajar_garra():
        """Baja la grua hasta el tope inferior"""
        grua.run_target(100,0,Stop.HOLD, True)
        # print("finish bajar garra")
        # print(grua.angle())    

    # Función para bajar la garra
def subir_garra():
        """Sube la grua hasta el tope superior"""
        grua.run_target(100,-350,Stop.HOLD, True)
        # print("finish subir garra")
        # print(grua.angle())

    #F Funcion para dejar un bloque sobre el otro
def reposar_bloque():
        """
        Posiciona la grua para para que el bloque que sostiene quede sobre el otro"""
        grua.run_target(100,-190,Stop.HOLD, True)
        # print("finish reposar bloque")
        # print(grua.angle())

def mover_grua_angulo(angulo_buscado):
        """Se le puede pasar un angulo a la grua para determinar la altura a la que queda"""
        grua.run_target(100,angulo_buscado,Stop.HOLD, True) 
        # print("finish subir garra")
        # print(grua.angle())

    #Esta funcion lo que hace es posicionar la garra en un punto de referencia, para que no choque cuando vaya agarrar bloques
def posicionar_garra_desde_cero():
        """
        Esta funcion busca posicionar la garra en una forma medianamente cerrada
        

        """
        # garra.reset_angle(0) #Creo que esta linea de codigo no es necesariaE

        garra.run_target(150, -120, Stop.HOLD, True)

def posicionar_garra_angulo(angle, bool = True):
        """Parametros admitidos para el angulo: -350 a 0
        Se le puede pasar un angulo para determinar una agarre mejor
        """
        # garra.reset_angle(0)
        print("reseteado")
        garra.run_target(150, angle, Stop.HOLD, bool)
        print("posicionada")

def abrir_garra(esperar = True):
        """
        Abre la garra totalmente
        """
        garra.stop()
        print("hola ")
        garra.run_target(150, 0, Stop.HOLD, esperar)
        print("Como estas?")

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

def primer_paso():
        """
        El robot se ubica en el punto de inicio, osea el cuadro rojo. Y avanza hasta ubicarse en la linea horizontal
        paralela a los bloques
        """
        #Posiciona la garra en un punto de referencia y retrocede hasta chocar con la pared, para despues avanzar 
        mover_grua_angulo(-30)
        
        posicionar_garra_desde_cero()

        retrocede_recto(right_motor, left_motor, 10)
        giroscopio.reset_angle(0)
        wait(20300)
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
        retroceder_robot(robot, 10)
        # acelerar(robot,3000)
        wait(100)
        movimiento_recto(right_motor, left_motor, 31)
        ev3.speaker.beep(2)
        wait(100)
        
        cerrar_garra()

        #El robot retrocede hasta llegar al borde del punto de control y se direcciona hacia la pipa
        retroceder_hasta_color(right_motor, left_motor, sensor_color_bloque, Color.RED)
        retrocede_recto(right_motor, left_motor, 2) # de 1 a 1.3 a 1.5

        robot.turn(88)
        robot.stop()
        movimiento_recto(right_motor, left_motor, 45) # de 44 a 44.5 a 44.8
        subir_garra()
        robot.turn(-88)
        robot.stop()
        

        
        # DESDE AQUI COMENTE TODO

        # mover_grua_angulo(-100)
        # wait(500)
        # robot.turn(88)
        # robot.stop()
        # giroscopio.reset_angle(0)
        # print("Angulo 1: ",giroscopio.angle())   
        
        # movimiento_recto(right_motor, left_motor, 48)
        # #///////////////    

        # #El robot se endereza para que quede bien posicionado, sube el elevador y gira para activar la pipa
        # subir_garra()

        # #Se alinea contra la pared y se endereza
        # robot.turn(-88)
        # robot.stop()
        # giroscopio.reset_angle(0)
        # print("Angulo 1: ",giroscopio.angle())   
        retrocede_recto(right_motor, left_motor, 25)
        movimiento_recto(right_motor, left_motor, 2)
        wait(100)

        robot.turn(88)
        robot.stop()
        giroscopio.reset_angle(0)
        print("Angulo 1: ",giroscopio.angle())   
        retrocede_recto(right_motor, left_motor, 2)
        abrir_garra(False)
        wait(100)

        retroceder_hasta_color(right_motor, left_motor, sensor_color_bloque, Color.RED)
        retrocede_recto(right_motor, left_motor, 15)

        #///////////////

        #El robot avanza hacia el punto de inicio y se endereza
        robot.turn(-88)
        robot.stop()
        



        # # grua.reset_angle(0)
        

        # # bajar_garra()
        # #///////////////
        
def apilar_tres_bloques():#Esta funcion lo que hace es apilar los bloques desde el amarillo hasta el rojo
        #El robot avanza y se alinea con el primer bloque
        
        ######################### MEJORA PENDIENDTE: Ajustar la distancia para que se posicione con la linea roja #@@@@@@@@@@2
        movimiento_recto(right_motor, left_motor, 6)
        
        avanzar_hasta_color(right_motor, left_motor, sensor_color_bloque,  Color.RED)

        ev3.speaker.beep(4)
        
        movimiento_recto(right_motor, left_motor, 26)
        ev3.speaker.beep(2) 

        
        wait(100)
       
        robot.turn(-88)
        robot.stop()
        
        ev3.speaker.beep(4)
        wait(300)

        movimiento_recto(right_motor, left_motor, 7.5) # De 7 a 7.5 
        #///////////////
        wait(300)
        #El robot agarra el primer bloque rojo, lo sube y retrocede
        cerrar_garra()
        subir_garra()
        # print("paso 3")
        ev3.speaker.beep(3)
        retroceder_hasta_color(right_motor, left_motor, sensor_color_bloque,  Color.BLACK)
        #///////////////

        #El robot gira y se alinea con el siguiente bloque
        
        wait(200)
        ev3.speaker.beep(4)
        robot.turn(-88)
        robot.stop()
        
        wait(200)
        ev3.speaker.beep(4)
        movimiento_recto(right_motor, left_motor, 9.6)
        wait(200)

        robot.turn(88)
        robot.stop()
        wait(200)
        movimiento_recto(right_motor, left_motor, 1.3)
        #///////////////

        #Deja reposar el bloque, baja la garra, abre su garra y recoge ambos bloques
        reposar_bloque()

        #FALLA EN ESTA LINEA DE CODIGO
        abrir_garra() # se comento esta funcion por mejor funcionamiento
        
        posicionar_garra_desde_cero() #Esta funcion sirve para que la garra no choque con los bloques
        bajar_garra()
        cerrar_garra()
        subir_garra()
        #///////////////

        #El robot retrocede hasta el area amarilla, gira deja los bloques y retrocede
        retroceder_hasta_color(right_motor, left_motor, sensor_color_bloque,  Color.BLACK)
        wait(100)
        robot.turn(-88)
        robot.stop()
        wait(100)
        movimiento_recto(right_motor, left_motor, 9.10)
        wait(100)
        robot.turn(88)
        robot.stop()
        giroscopio.reset_angle(0)
        print("Angulo 1: ",giroscopio.angle())   
        wait(100)
        movimiento_recto(right_motor, left_motor, 0.5)

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
        retrocede_recto(right_motor, left_motor, 4.5) # 3 a 6
        abrir_garra()
        retrocede_recto(right_motor, left_motor, 6) #


        
        #///////////////
  

def segundo_escombro_por_linea_roja():
        robot.turn(-90)
        robot.stop()
        wait(100) 

        robot.turn(-90)
        robot.stop()

        avanzar_hasta_color(right_motor, left_motor, sensor_color_bloque,  Color.GREEN)
        movimiento_recto(right_motor, left_motor, 2)

        cerrar_garra()
        
        movimiento_recto(right_motor, left_motor, 10)

        robot.turn(-88)
        robot.stop()
        giroscopio.reset_angle(0)
        print("Angulo 1: ",giroscopio.angle())   

        retrocede_recto(right_motor, left_motor, 50)

        avanzar_hasta_color(right_motor, left_motor, sensor_color_bloque,  Color.RED)
        wait(200)

        #mods nuevas
        # movimiento_recto(right_motor, left_motor, 3) Cambio por retrocede recto, al parecer la distancia no cuadra
        retrocede_recto(right_motor, left_motor, 2.5) # 2 a 2.5 
        wait(100)
        robot.turn(88)
        robot.stop()
  

        movimiento_recto(right_motor, left_motor, 17.5) # ajustar distancia 45.5
        reposar_bloque()
        movimiento_recto(right_motor, left_motor, 7)
        
        abrir_garra()
        mover_grua_angulo(-35)
        cerrar_garra()
        
        robot.turn(-90)
        robot.stop()
        
        movimiento_recto(right_motor, left_motor, 7)
        abrir_garra()

        subir_garra()
        robot.turn(88)
        robot.stop()

        bajar_garra()
        
        posicionar_garra_angulo(-150) # Especificar angulo
        
        movimiento_recto(right_motor, left_motor, 17)
        subir_garra()
        girar_rad(2)
 

        movimiento_recto(right_motor, left_motor, 17)
        robot.turn(88)
        robot.stop()
        
         

        #mods bobo 12 y 13 julio
        #funcion para llevar escombor amarillo y gris a la vez

def escombros_punto_de_control ():
        """
        Descripcion
        """
        #en la funcion anterior bajar toda la garra
        # garra.reset_angle(-200)#se establece el angulo interno de 0 a -350 EEs el garra
        # grua.reset_angle(-350) # Es el elevador

        """Comente lo anterior porque estamos en fase de pruebas final"""
        print("abriendo la garra")
        abrir_garra()#abrir hasta q llegue a 0
        wait(100)
        print("moviendo hacia los bloques")
        movimiento_recto(right_motor,left_motor,1.5) # 0.5 a 1.5 
        wait(100)
        bajar_garra()
        wait(100)
        cerrar_garra()
        #girar_rad(4,1)#4 es 1 es   2 mitad 4 es framento de 90 1 360 2 180 4 90 8 45
        robot.turn(-90)
        robot.stop()
        avanzar_hasta_color(right_motor, left_motor, sensor_color_bloque, Color.BLACK)
        robot.turn(90)
        robot.stop() #girar_rad(4) #4 izquierda y 4 1 derecha
        avanzar_hasta_color(right_motor, left_motor, sensor_color_bloque, Color.BLACK)
        robot.turn(-90)
        robot.stop()#girar_rad(4,1)#gira ala derecha
        avanzar_hasta_color(right_motor, left_motor, sensor_color_bloque, Color.RED)
        movimiento_recto(right_motor,left_motor,47)
        robot.turn(90)
        robot.stop()
        #girar_rad(4)
        movimiento_recto(right_motor,left_motor, 5)
        abrir_garra()
        subir_garra()

        print("volviendo al punto de control")
        retrocede_recto(right_motor,left_motor,7)
        robot.turn(90)
        robot.stop()
        #girar_rad(4)
        avanzar_hasta_color(right_motor, left_motor, sensor_color_bloque, Color.RED)
        movimiento_recto(right_motor,left_motor,10)
        robot.turn(90)
        robot.stop()
        #girar_rad(4)
        retrocede_recto(right_motor, left_motor, 9.3)
        wait(500)
        ev3.speaker.beep(4)
        print("bobo llego al punto de control")
        #fin mods hoy
        #:D

def segundo_apilar(): #casi listo
        movimiento_recto(right_motor,left_motor,13)#avanza un poco haia adelante
        robot.turn(-90)
        robot.stop()
        #girar_rad(4)
        movimiento_recto(right_motor,left_motor,31)
        robot.turn(88)
        robot.stop()
        #girar_rad(4,1)
        movimiento_recto(right_motor,left_motor,52)
        robot.turn(-88)
        robot.stop()
        #girar_rad(4)
        movimiento_recto(right_motor,left_motor,31)
        robot.turn(88)
        robot.stop()
        #girar_rad(4,1)
        posicionar_garra_desde_cero()
        avanzar_hasta_color(right_motor, left_motor, sensor_color_bloque, Color.BLACK)
        movimiento_recto(right_motor,left_motor,7)#esta de frente al bloque rojo 1 fila 2 
        wait(100)
         # garra.reset_angle(-200)#se establece el angulo interno de 0 a -350
         # grua.reset_angle(-350)
        bajar_garra()
        wait(100)
        cerrar_garra()
        subir_garra()
        print("en camino al block 1 rojo")
        retroceder_hasta_color(right_motor, left_motor, sensor_color_bloque, Color.BLACK)
        wait(100)
        robot.turn(88)
        robot.stop()
        #girar_rad(4,1)
        movimiento_recto(right_motor, left_motor,9.5)
        robot.turn(-88)
        robot.stop()
        #girar_rad(4)
        print("en frente rojo 2")
        movimiento_recto(right_motor, left_motor,0.5)
        #Deja reposar el bloque, baja la garra, abre su garra y recoge ambos bloques
        print("colocando rojo en rojo")
        reposar_bloque()#colocar block sobre otro #apilar_tres_bloques() 
        abrir_garra() 
        posicionar_garra_desde_cero
        print("abro")
        posicionar_garra_desde_cero() #Esta funcion sirve para que la garra no choque con los bloques
        print("cero")
        mover_grua_angulo(-20)
        cerrar_garra()
        subir_garra()#pendiente
        #apilar bloque 3 
        print("en camino al block amarillo")
        retroceder_hasta_color(right_motor, left_motor,  sensor_color_bloque, Color.BLACK)
        wait(100)
        robot.turn(90)
        robot.stop()
        #girar_rad(4,1)
        movimiento_recto(right_motor, left_motor,8.5)
        robot.turn(-90)
        robot.stop()
        #girar_rad(4)
        movimiento_recto(right_motor, left_motor,1)
        reposar_bloque()#apilar_tres_bloques()
        abrir_garra()
        posicionar_garra_desde_cero()
        mover_grua_angulo(-25)
        cerrar_garra()
        retrocede_recto(right_motor,left_motor,7)
        wait(100)
        robot.turn(92)
        robot.stop()
        #girar_rad(4,1)
        movimiento_recto(right_motor,left_motor,10)
        robot.turn(89)
        robot.stop()
        #girar_rad(4,1)
        movimiento_recto(right_motor,left_motor,7)
        bajar_garra()
        abrir_garra()

def escombro_final(): #condicional de control
        color_bloque_final_lineal = sensor_bloque_enfrente.color()
        if color_bloque_final_lineal == Color.BLUE:
                print("estamos frente la pila azul")
                print("posicion abajo de azul")
                retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.BLACK)
                robot.turn(-88)
                robot.stop()
                movimiento_recto(right_motor,left_motor,30)
                robot.turn(88)
                robot.stop()
                avanzar_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.RED)
                robot.turn(88)
                robot.stop()
                robot.turn(88)
                robot.stop()
                robot.turn(-90)
                robot.stop()
                movimiento_recto(right_motor,left_motor,63)
                posicionar_garra_desde_cero()
                cerrar_garra()
                retrocede_recto(right_motor,left_motor,10)
                robot.turn(88)
                robot.stop()
                avanzar_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.RED)
                robot.turn(-88)
                robot.stop()
                movimiento_recto(right_motor,left_motor,35)
                robot.turn(88)
                robot.stop()
                movimiento_recto(right_motor,left_motor,10)
                abrir_garra()
                retrocede_recto(right_motor,left_motor,10)
                robot.turn(88)
                robot.stop()
                avanzar_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.RED)
                robot.turn(88)
                robot.stop()
                retrocede_recto(right_motor,left_motor,20)
        else:
                print("estamos frente la pila verde")
                print("posicion arriba de verde")
                retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.BLACK)
                robot.turn(-88)
                robot.stop()
                movimiento_recto(right_motor,left_motor,53)
                robot.turn(-45)
                robot.stop()
                movimiento_recto(right_motor,left_motor,16.5)
                cerrar_garra()
                retrocede_recto(right_motor,left_motor,4)
                posicionar_garra_desde_cero()
                movimiento_recto(right_motor,left_motor,6)
                cerrar_garra()
                retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.BLACK)
                robot.turn(35)
                robot.stop()
                robot.turn(88)
                robot.stop()
                movimiento_recto(right_motor,left_motor,55)
                robot.turn(-88)
                robot.stop()
                movimiento_recto(right_motor,left_motor,30)
                robot.turn(88)
                robot.stop()
                movimiento_recto(right_motor,left_motor,10)
                abrir_garra()
                retrocede_recto(right_motor,left_motor,10)
                robot.turn(88)
                robot.stop()
                avanzar_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.RED)
                robot.turn(88)
                robot.stop()
                retrocede_recto(right_motor,left_motor,20)


#variable global
color_3_bloque = sensor_bloque_enfrente.color()

def condicional_definitivo(): #condicional para apilamiento de verde y azul
        print("estamos en frente de la 2da apilacion")
        retrocede_recto(right_motor,left_motor,17)
        robot.turn(88)
        robot.stop()
        avanzar_hasta_color(right_motor, left_motor,  sensor_color_bloque, Color.RED)
        robot.turn(-88)
        robot.stop()
        retrocede_recto(right_motor,left_motor,20)
        print("en el checkpoint")
        movimiento_recto(right_motor,left_motor,18)
        robot.turn(-88)
        robot.stop()
        movimiento_recto(right_motor,left_motor,45)
        print("Lllegando al bloque amarillo")
        robot.turn(-88)
        robot.stop()
        retrocede_recto(right_motor,left_motor,4)
        posicionar_garra_desde_cero()
        wait(100)
        movimiento_recto(right_motor,left_motor,8.8)
        bajar_garra()
        cerrar_garra()
        subir_garra()
        print("amarillo capturado")
        retroceder_hasta_color(right_motor, left_motor, sensor_color_bloque, Color.BLACK)
        wait(200)
        robot.turn(88)
        robot.stop()
        wait(100)
        movimiento_recto(right_motor,left_motor, 9.8)
        robot.turn(-88)
        robot.stop()
        wait(100)
        movimiento_recto(right_motor,left_motor, 1)
        reposar_bloque()
        print("apilacion doble completada")
        abrir_garra()
        retrocede_recto(right_motor,left_motor,4)
        bajar_garra()
        posicionar_garra_desde_cero()
        movimiento_recto(right_motor,left_motor,5)
        print("verificando color")
        color_bloque_final_lineal = sensor_bloque_enfrente.color()
        print(sensor_bloque_enfrente.color())
        print("guardamos el color del bloque 2")      
        retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque, Color.BLACK)
        robot.turn(88)
        robot.stop()
        wait(100)
        movimiento_recto(right_motor,left_motor,10)
        robot.turn(-88)
        robot.stop()
        movimiento_recto(right_motor,left_motor,1.5)
        print("en frente al segundo bloque")
        print("verificando color")
        color_bloque_tercero = sensor_bloque_enfrente.color()
        print(sensor_bloque_enfrente.color())
        print("guardamos el color del tercer bloque")
        if color_bloque_final_lineal == Color.GREEN and color_bloque_tercero == Color.BLUE:
                #esto es para bloque 2 es verde y bloque 3 es azul
                cerrar_garra()
                subir_garra()
                retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.BLACK)
                robot.turn(-88)
                robot.stop()
                movimiento_recto(right_motor,left_motor,9.8)
                robot.turn(88)
                robot.stop()
                reposar_bloque()
                print("apilacion triple completada")
                print("verde, amarillo, azul")
                retrocede_recto(right_motor,left_motor,4)
                bajar_garra()
                posicionar_garra_desde_cero()
                movimiento_recto(right_motor,left_motor,4)
                cerrar_garra()
                retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.BLACK)
                robot.turn(-88)
                robot.stop()
                movimiento_recto(right_motor,left_motor,60)
                robot.turn(-88)
                robot.stop()
                movimiento_recto(right_motor,left_motor,20)
                print("cuadrito verde")
                abrir_garra()




                robot.turn(90)
                robot.stop()
                abrir_garra()
                retrocede_recto(right_motor,left_motor,5)
                print("en camino al bloque azul") 
                robot.turn(-90)
                robot.stop()
                movimiento_recto(right_motor,left_motor,20)
                posicionar_garra_desde_cero()
                movimiento_recto(right_motor,left_motor,0.5)
                cerrar_garra()
                print("bloque amarillo capturado")
                retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.BLACK)
                robot.turn(90)
                robot.stop()
                movimiento_recto(right_motor,left_motor,6)
                robot.turn(-90)
                robot.stop()
                movimiento_recto(0.5)
                reposar_bloque()
                retrocede_recto(right_motor,left_motor,4)
                abrir_garra()
                posicionar_garra_desde_cero()
                mover_grua_angulo(-25)
                movimiento_recto(right_motor,left_motor,4)
                cerrar_garra()
                print("bloque 2 capturado")
                retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.BLACK)
                robot.turn(90)
                robot.stop()
                movimiento_recto(right_motor,left_motor,6)
                robot.turn(-90)
                robot.stop()
                movimiento_recto(0.5)
                reposar_bloque()
                retrocede_recto(right_motor,left_motor,4)
                abrir_garra()
                posicionar_garra_desde_cero()
                bajar_garra()
                movimiento_recto(right_motor,left_motor,4)
                print("verificando color")
                color_bloque_final_lineal = sensor_bloque_enfrente.color()
                print(sensor_bloque_enfrente.color())
                if color_bloque_final_lineal == Color.BLUE:
                        print("era azul")
                        cerrar_garra()
                        retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.BLACK)
                        robot.turn(-90)
                        robot.stop() 
                        movimiento_recto(right_motor,left_motor,20)
                        robot.turn(-90)
                        robot.stop()
                        movimiento_recto(right_motor,left_motor,15)
                        abrir_garra()
                        escombro_final()
        else :
                print("es diferente entonces vamos por el apliamiento doble azul")
                retrocede_recto(right_motor,left_motor,4)
                abrir_garra()
                posicionar_garra_desde_cero()
                movimiento_recto(right_motor,left_motor,4)
                cerrar_garra()
                retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.BLACK)
                robot.turn(-88)
                robot.stop()
                movimiento_recto(right_motor,left_motor,9.6)
                robot.turn(88)
                robot.stop()
                subir_garra()
                reposar_bloque()
                print("apilacion triple completada")
                print("azul, amarillo, verde")
                retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.BLACK)
                robot.turn(-90)
                robot.stop()
                movimiento_recto(right_motor,left_motor,38)
                robot.turn(-90)
                robot.stop()
                movimiento_recto()

                


#         else:
#                 robot.turn(90)
#                 robot.stop() 
#                 movimiento_recto(right_motor,left_motor,20)
#                 robot.turn(-90)
#                 robot.stop() 
#                 movimiento_recto(right_motor,left_motor,15)
#                 robot.turn(90)
#                 robot.stop() 
#                 posicionar_garra_desde_cero()
#                 movimiento_recto(right_motor,left_motor,0.5)
#                 cerrar_garra()
#                 print("bloque amarillo capturado")
#                 retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.BLACK)
#                 robot.turn(90)
#                 robot.stop()
#                 movimiento_recto(right_motor,left_motor,6)
#                 robot.turn(-90)
#                 robot.stop()
#                 movimiento_recto(0.5)
#                 reposar_bloque()
#                 retrocede_recto(right_motor,left_motor,4)
#                 abrir_garra()
#                 posicionar_garra_desde_cero()
#                 mover_grua_angulo(-25)
#                 movimiento_recto(right_motor,left_motor,4)
#                 cerrar_garra()
#                 print("bloque 2 capturado")
#                 retroceder_hasta_color(right_motor,left_motor,sensor_color_bloque,Color.BLACK)
#                 robot.turn(90)
#                 robot.stop()
#                 movimiento_recto(right_motor,left_motor,6)
#                 robot.turn(-90)
#                 robot.stop()
#                 movimiento_recto(0.5)
#                 reposar_bloque()
#                 retrocede_recto(right_motor,left_motor,4)
#                 abrir_garra()
#                 posicionar_garra_desde_cero()
#                 bajar_garra()
#                 movimiento_recto(right_motor,left_motor,4)
#                 print("verificando color")
#                 color_bloque_final_lineal = sensor_bloque_enfrente.color()
#                 print("era verde")
#                 retrocede_recto(right_motor,left_motor,40)
#                 abrir_garra()


def main(): 
        
        # recoger_escombro_1()  
        # primer_paso()
        # apilar_tres_bloques()                #paso 2 apilar bloques en cuadrito 
        # segundo_escombro_por_linea_roja()    #paso 3 escombro 2 y 3 + palanca 1 y 2
        # escombros_punto_de_control()         #paso 4 llevar escombro amarillo y gris a la vez
        # segundo_apilar()                     #paso 4 fila opuesta amarillo base, rojo , rojo
        #condicional_definitivo()             #paso 5 y 6 condicional con todas las probabilidades + escombro final
        escombro_final()

        #funciones al 100%
        
        #segundo_apilar()

main()
