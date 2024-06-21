from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Inicializa el EV3 Brick
ev3 = EV3Brick()

# Inicializa los motores en los puertos B y C
motorB = Motor(Port.B)
motorC = Motor(Port.C)

# Resetea los ángulos de los motores a 0
motorB.reset_angle(0)
motorC.reset_angle(0)

# Define la velocidad constante
velocidad = 100  # Velocidad en grados por segundo

def girar_90_grados(radio_robot, radio_rueda):
    # Calcula la distancia que cada rueda debe recorrer para girar 90 grados
    circunferencia_robot = 2 * 3.14159 * radio_robot
    distancia_giro_90 = circunferencia_robot / 4  # 90 grados es un cuarto de la circunferencia
    
    # Calcula los grados que debe girar cada motor para recorrer la distancia_giro_90
    circunferencia_rueda = 2 * 3.14159 * radio_rueda
    grados_giro_motor = (distancia_giro_90 / circunferencia_rueda) * 360  # Convertir a grados
    
    # Inicializa los motores para el giro
    motorB.run_angle(velocidad, grados_giro_motor, wait=False)
    motorC.run_angle(-velocidad, grados_giro_motor, wait=True)  # Gira en la dirección opuesta

# Llama a la función para girar 90 grados
radio_robot = 10  # Ajusta según el radio real de tu robot
radio_rueda = 2   # Ajusta según el radio real de las ruedas
girar_90_grados(radio_robot, radio_rueda)

# Detén los motores después del giro
motorB.stop()
motorC.stop()
