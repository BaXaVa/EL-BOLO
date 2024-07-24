from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from math import pi

# Define the constant speed

ev3 = EV3Brick()

giroscopio_Derecho = GyroSensor(Port.S3)
girsocopio_izquierdo = GyroSensor(Port.S4)

def girar_90_grados2( right_motor, left_motor, velocidad = 30):
    right_motor.reset_angle(0)
    left_motor.reset_angle(0)
    giroscopio_Derecho.reset_angle(0)

    while girsocopio_izquierdo < 90:
        right_motor.run(velocidad)
        left_motor.run(-velocidad)
    right_motor.stop()
    left_motor.stop()
    

    print("\n####################################### INITIATING TURN #######################################")
    print(" Right motor turned: ", right_motor.angle(), " Left motor turned: ", left_motor.angle(), " Giroscopio: ", giroscopio_Derecho.angle(), " giscopioIz: ", girsocopio_izquierdo.angle())
    print("############################################################################################# \n")


    wait(200)
    ev3.speaker.beep(2)
