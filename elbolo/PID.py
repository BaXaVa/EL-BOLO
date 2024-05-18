from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,)
from pybricks.parameters import Port
from pybricks.tools import wait
# import pandas as pd
import time

def line_follower():
    #declarar motores
    left_motor = Motor(Port.C)
    right_motor = Motor (Port.B)
    
    left_sensor = ColorSensor(Port.S1)#iniciar los sensores
    right_sensor = ColorSensor(Port.S2)
    archivo = open("datos_Bolo.txt", "a")
    
    #iniciar el dataframe para guardar datos
    # df = pd.DataFrame(columns=['time', 'left_light', 'right_light', 'left_speed', 'right_speed', 'error', 'turn'])
    
    luz_negra = 15 #lo usaremos para hacer que el robot pare cuando ambos detecten menos de 15.
    speed = 200 #velocidad para los motores
    kp = 0.12 #preguntar a alexander. 
    
    #Usar un Error para saber hacia donde se esta desviando el robot y corregir.
    
    #Robot en la linea
    #Si left_light = right_light, error = 0, robot esta recto
    
    #Robot desviado a la derecha
    #left_light > rigth_light, error>0, robot debe girar a la izquierda
    
    #Robot desviado a la izquierda
    #left_light<right_light, error<0, robot debe girar a la derecha. 
    
    while True:
        #obtener valores de la luz
        timestamp = time.time()#obtener un timestamp
        left_light = left_sensor.reflection()
        right_light = right_sensor.reflection()
        
        #si ambos sensores estan en linea negra, entonces se acabo la linea y se detiene
        if left_light < 15 and right_light < 15:
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
        
        #meter los datos en el dataframe.  
        # df = df.append({
        #     'time': timestamp, 
        #     'left_light': left_light,
        #     'right_light': right_light,
        #     'left_speed': left_motor.speed(),
        #     'right_speed': right_motor.speed(),
        #     'error': error,
        #     'turn': turn,
        #     # podemos anadir mas datos si los necesitamos. Esto es una recopilacion de datos para analisis. 
        #     }, ignore_index= True) 
         #pausar el programa por 50ms
        archivo.write("\n")
        archivo.write(str(timestamp))
        archivo.write(",")
        archivo.write(str(left_light) )
        archivo.write(", ")
        archivo.write(str(right_light))
        archivo.write(", ")
        archivo.write(str(left_motor.speed()))
        archivo.write(", ")
        archivo.write(str(right_motor.speed()))
        archivo.write(", ")
        archivo.write(str(error))
        archivo.write(", ")
        archivo.write(str(turn))
        wait(25)
    archivo.close()
        
    # df.to_csv("datos_Bolo.csv", index=False)