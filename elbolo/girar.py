from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from math import pi

# Define la velocidad constante
velocidad = 100  # Velocidad en grados por segundo

def girar_90_grados(radio_robot, radio_rueda, right_motor, left_motor,cuarto_de_circunferencia, velocidad = 100):
    right_motor.reset_angle(0)
    left_motor.reset_angle(0)

    # Calcula la distancia que cada rueda debe recorrer para girar 90 grados
    circunferencia_robot = 2 * pi * radio_robot
    distancia_giro_90 = circunferencia_robot / cuarto_de_circunferencia  # 90 grados es un cuarto de la circunferencia
    
    # Calcula los grados que debe girar cada motor para recorrer la distancia_giro_90
    circunferencia_rueda = 2 * 3.14159 * radio_rueda
    grados_giro_motor = (distancia_giro_90 / circunferencia_rueda) * 360  # Convertir a grados
    
    # Inicializa los motores para el giro
    right_motor.run_angle(velocidad, grados_giro_motor, wait=False)
    left_motor.run_angle(-velocidad, grados_giro_motor, wait=True)  # Gira en la dirección opuesta


