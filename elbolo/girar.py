from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from math import pi

# Define the constant speed
velocidad = 100  # Speed in degrees per second
ev3 = EV3Brick()

giroscopio = GyroSensor(Port.S3)

def girar_90_grados_trapezoidal(diametro_de_robot, diametro_de_rueda, right_motor, left_motor, division_del_circulo, tiempo, velocidad_maxima):
    right_motor.reset_angle(0)
    left_motor.reset_angle(0)
    giroscopio.reset_angle(0)
    # Calculate the distance each wheel needs to travel to turn 90 degrees
    circunferencia_robot = pi * diametro_de_robot
    distancia_a_recorrer = circunferencia_robot / division_del_circulo  # 90 degrees is a quarter of the circumference
    
    # Calculate the degrees each motor needs to turn to cover the distance_a_recorrer
    circunferencia_rueda =  pi * diametro_de_rueda

    threshold = 0.05  # Smaller threshold for finer correction
    grados_giro_motor = round((distancia_a_recorrer / circunferencia_rueda) * 360)  # Convert to degrees

    # Initialize motors for turning
    # Using trapezoidal velocity profile

    # Acceleration phase
    current_velocity = 0
    acceleration = velocidad_maxima / (tiempo / 3)

    while current_velocity < velocidad_maxima:
        wait(1)
        right_motor.run(current_velocity)
        left_motor.run(-current_velocity)
        current_velocity += acceleration

    # Constant velocity phase
    right_motor.run(velocidad_maxima)
    left_motor.run(-velocidad_maxima)
    wait(tiempo/3)

    # Deceleration phase
    while current_velocity > 0:
        wait(1)
        right_motor.run(current_velocity)
        left_motor.run(-current_velocity)
        current_velocity -= acceleration

    # right_motor.run_angle(velocidad, grados_giro_motor, wait=False)  # Turn in one direction (right)
    # left_motor.run_angle(-velocidad, grados_giro_motor, wait=True)  # Turn in the opposite direction 
    angulo_final_del_motor_d = right_motor.angle()
    angulo_final_del_motor_i = left_motor.angle()

    print("####################################### INITIATING TURN #######################################")
    print("Motor should turn: ", grados_giro_motor, " Right motor turned: ", angulo_final_del_motor_d, " Left motor turned: ", angulo_final_del_motor_i, " Giroscopio: ", giroscopio.angle())
    print("#############################################################################################")


    wait(200)
    ev3.speaker.beep(2)


def girar_90_grados(diametro_de_robot, diametro_de_rueda, right_motor, left_motor, division_del_circulo, velocidad = 100):
    right_motor.reset_angle(0)
    left_motor.reset_angle(0)
    giroscopio.reset_angle(0)
    # Calculate the distance each wheel needs to travel to turn 90 degrees
    circunferencia_robot = pi * diametro_de_robot
    distancia_a_recorrer = circunferencia_robot / division_del_circulo  # 90 degrees is a quarter of the circumference
    
    # Calculate the degrees each motor needs to turn to cover the distance_a_recorrer
    circunferencia_rueda =  pi * diametro_de_rueda

    threshold = 0.05  # Smaller threshold for finer correction
    grados_giro_motor = round((distancia_a_recorrer / circunferencia_rueda) * 360)  # Convert to degrees

    # Initialize motors for turning
    right_motor.run_angle(velocidad, grados_giro_motor, wait=False)  # Turn in one direction (right)
    left_motor.run_angle(-velocidad, grados_giro_motor, wait=True)  # Turn in the opposite direction
    angulo_final_del_motor_d = right_motor.angle()
    angulo_final_del_motor_i = left_motor.angle()

    print("####################################### INITIATING TURN #######################################")
    print("Motor should turn: ", grados_giro_motor, " Right motor turned: ", angulo_final_del_motor_d, " Left motor turned: ", angulo_final_del_motor_i, " Giroscopio: ", giroscopio.angle())
    print("#############################################################################################")


    wait(200)
    ev3.speaker.beep(2)
