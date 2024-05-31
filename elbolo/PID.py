from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,)
from pybricks.parameters import Port
from pybricks.tools import wait
from math import pi
import time

left_motor = Motor(Port.C)
right_motor = Motor (Port.B)

left_sensor = ColorSensor(Port.S1)#iniciar los sensores
right_sensor = ColorSensor(Port.S2)

def line_follower(distancia=None):

    luz_negra = 15 #lo usaremos para hacer que el robot pare cuando ambos detecten menos de 15.
    speed = 140 #velocidad para los motores, 100mm/s
    kp = 0.09 #preguntar a alexander. 

    starTime = time.time()
    
    if distancia == None:
        condicional = False
    else:
        print("iniciando")
        condicional = True
    
    tiempo = (distancia*(18/7))/(68.8*pi)
    
    timeW = time.time()
    while True:
        #obtener valores de la luz
        timestamp = time.time()#obtener un timestamp
        left_light = left_sensor.reflection()
        right_light = right_sensor.reflection()
        
        #si ambos sensores estan en linea negra, entonces se acabo la linea y se detiene
        if time.time() - starTime  > 3 and left_light < 15 and right_light < 15:
            left_motor.brake()
            right_motor.brake()
            break
        
        if condicional and time.time() - starTime > tiempo:
            left_motor.brake()
            right_motor.brake()
            break
        #para calcular el error
        error = left_light - right_light
    
        #calcular ajuste proporcional. Control proporcional.
        turn = kp * error #propagacion del error. 
    
        #ajustar motores
        left_motor.run(speed + turn) #speed en grados/s. 200 grados por segundo
        right_motor.run(speed - turn)
        timeWFinal= time.time()
        print(timeWFinal-timeW)
        
    
        
    # df.to_csv("datos_Bolo.csv", index=False)