from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from math import pi

# Define the constant speed
velocidad = 100  # Speed in degrees per second
ev3 = EV3Brick()

giroscopio = GyroSensor(Port.S3)

def girar_90_grados(diametro_de_robot, diametro_de_rueda, right_motor, left_motor, division_del_circulo, velocidad = 100):
    right_motor.reset_angle(0)
    left_motor.reset_angle(0)

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
    print("Motor should turn: ", grados_giro_motor, " Right motor turned: ", angulo_final_del_motor_d, " Left motor turned: ", angulo_final_del_motor_i)
    print("#############################################################################################")
    angd = right_motor.angle()
    angi = left_motor.angle()

    velocidad_correccion = 30  # Slower correction speed
    i = 0
    # New part added for correcting motor turn at the end.
    while(abs(angulo_final_del_motor_d) != grados_giro_motor or abs(angulo_final_del_motor_i) != grados_giro_motor):
        i += 1
        if right_motor.angle() != grados_giro_motor or left_motor.angle() != -grados_giro_motor:
            correccion_derecha = (-grados_giro_motor) - angulo_final_del_motor_d
            correccion_izquierda = grados_giro_motor - abs(angulo_final_del_motor_i)

            print("------------------- Correction #", i, " -------------------")
            print("- Right correction: ", correccion_derecha, ", Left correction: ", correccion_izquierda)

            right_motor.reset_angle(0)
            left_motor.reset_angle(0)

            if(abs(correccion_derecha) >= threshold): 
                right_motor.run_angle(velocidad_correccion, correccion_derecha, wait=False)
            else: 
                print("!: Right correction not applied")

            if(abs(correccion_izquierda) >= threshold): 
                left_motor.run_angle(velocidad_correccion, correccion_izquierda, wait=True)
            else: 
                print("!: Left correction not applied")
            
            # Update final angles of motors  
            angulo_final_del_motor_d += right_motor.angle()
            angulo_final_del_motor_i += left_motor.angle()  

        print("####################################### Corrected Turn #######################################\n")
        print("Motor should turn: ", grados_giro_motor, " Right motor turned: ", angulo_final_del_motor_d, " Left motor turned: ", angulo_final_del_motor_i)
        print("\n#############################################################################################")
    
    wait(200)
    ev3.speaker.beep(2)
