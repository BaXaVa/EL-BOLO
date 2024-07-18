from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from math import pi

# Define la velocidad constante
velocidad = 100  # Velocidad en grados por segundo
ev3 = EV3Brick()

giroscopio = GyroSensor(Port.S3)

def girar_90_grados(diametro_de_robot, diametro_de_rueda, right_motor, left_motor,division_del_circulo, velocidad = 100):
    right_motor.reset_angle(0)
    left_motor.reset_angle(0)

    # Calcula la distancia que cada rueda debe recorrer para girar 90 grados
    circunferencia_robot = pi * diametro_de_robot
    distancia_a_recorrer = circunferencia_robot / division_del_circulo  # 90 grados es un cuarto de la circunferencia
    
    # Calcula los grados que debe girar cada motor para recorrer la distancia_a_recorrer
    circunferencia_rueda =  pi * diametro_de_rueda

    threshold = 0.1
    grados_giro_motor = round((distancia_a_recorrer / circunferencia_rueda) * 360)  # Convertir a grados
    # grados_giro_motor = int(grados_giro_motor)  # Convertir a entero

    # Inicializa los motores para el giro
  
    right_motor.run_angle(velocidad, grados_giro_motor, wait=False)  # Gira en una dirección (derecha
    left_motor.run_angle(-velocidad, grados_giro_motor, wait=True)  # Gira en la dirección opuesta
    angulo_final_del_motor_d = right_motor.angle()
    angulo_final_del_motor_i = left_motor.angle()

    print("####################################### INICIACION GIRO #######################################")
    print("El motor debe de girar: ", grados_giro_motor, " El motor ha girado derecho: ", angulo_final_del_motor_d, " El motor ha girado izquierdo: ", angulo_final_del_motor_i)
    print("###########################################################################################")
    angd = right_motor.angle()
    angi = left_motor.angle()

    velocidad_correccion = 50
    i = 0
    # Esta es la nueva parte agregada, para corregir el giro de los motores al finalizar.
    while(abs(angulo_final_del_motor_d) != grados_giro_motor or abs(angulo_final_del_motor_i) != grados_giro_motor):
        i += 1
        if right_motor.angle() != grados_giro_motor or left_motor.angle() != -grados_giro_motor:
            #angulo_final_del_motor_d = angd
            #angulo_final_del_motor_i = angi

            correccion_derecha = (-grados_giro_motor) - angulo_final_del_motor_d
            correccion_izquierda = grados_giro_motor - abs(angulo_final_del_motor_i)

            print("------------------- Correccion #", i, " -------------------")
            print("- Correccion derecha: ", correccion_derecha, ", Correcion izquierda: ", correccion_izquierda)

            right_motor.reset_angle(0)
            left_motor.reset_angle(0)

            if(abs(correccion_derecha) >= threshold): right_motor.run_angle(velocidad_correccion, correccion_derecha, wait=False)
            else: print("!: La correccion derecha no se ha aplicado")

            if(abs(correccion_izquierda) >= threshold): left_motor.run_angle(velocidad_correccion, correccion_izquierda, wait=True)
            else: print("!: La correcion izquierda no se ha aplicado")
            
            # Actualiza los angulos finales de los motores  
            angulo_final_del_motor_d += right_motor.angle()
            angulo_final_del_motor_i += left_motor.angle()  

        print("####################################### Giro Corregido #######################################\n")
        print("El motor debio girar: ", grados_giro_motor, " El motor ha girado derecho: ", angulo_final_del_motor_d, " El motor ha girado izquierdo: ", angulo_final_del_motor_i)
        print("\n##############################################################################################")
    
    wait(200)
    ev3.speaker.beep(2)

    
