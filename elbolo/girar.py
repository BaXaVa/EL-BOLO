from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from math import pi

# Define la velocidad constante
velocidad = 100  # Velocidad en grados por segundo

def girar_90_grados(diametro_de_robot, diametro_de_rueda, right_motor, left_motor,division_del_circulo, velocidad = 100):
    right_motor.reset_angle(0)
    left_motor.reset_angle(0)

    # Calcula la distancia que cada rueda debe recorrer para girar 90 grados
    circunferencia_robot = pi * diametro_de_robot
    distancia_a_recorrer = circunferencia_robot / division_del_circulo  # 90 grados es un cuarto de la circunferencia
    
    # Calcula los grados que debe girar cada motor para recorrer la distancia_a_recorrer
    circunferencia_rueda =  pi * diametro_de_rueda

    grados_giro_motor = (distancia_a_recorrer / circunferencia_rueda) * 360  # Convertir a grados
    grados_giro_motor = int(grados_giro_motor)  # Convertir a entero

    # Inicializa los motores para el giro
 
    right_motor.run_angle(velocidad, grados_giro_motor, wait=False)  # Gira en una dirección (derecha
    left_motor.run_angle(-velocidad, grados_giro_motor, wait=True)  # Gira en la dirección opuesta
    
    if right_motor != grados_giro_motor or left_motor != grados_giro_motor:
        
        correccion_derecha = grados_giro_motor - right_motor.angle()
        correccion_izquierda = grados_giro_motor - left_motor.angle()

        right_motor.reset_angle(0)
        left_motor.reset_angle(0)

        right_motor.run_angle(50, correccion_derecha, wait=False)
        left_motor.run_angle(-50, correccion_izquierda, wait=True)    

    print("####################################### ############ #######################################")
    print("El motor debe de girar: ", grados_giro_motor, " El motor ha girado derecho: ", right_motor.angle(), " El motor ha girado izquierdo: ", left_motor.angle())
    print("####################################### girar 90 grados #######################################")
    

