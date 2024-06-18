from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color, Stop
import time
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from PID import line_follower
from math import pi

def aceleracion_recta(motor_b, motor_c, left_sensor, right_sensor):
    motor_b.reset_angle(0)
    motor_c.reset_angle(0)
    ki = 0.12
    speed = 140
    while True:
        print(motor_b.angle(), motor_c.angle())
        diferencia = abs(motor_b.angle()) - abs(motor_c.angle())

        correcion = diferencia * ki

        motor_b.run(speed - correcion)
        motor_c.run(speed + correcion)
        

        if left_sensor.reflection() < 15 and right_sensor.reflection()  < 15:
            motor_b.brake()
            motor_c.brake()
            break
        
            
