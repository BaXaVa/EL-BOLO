from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color, Stop
import time
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from math import pi

import threading

def motor_c_running(motor_b, motor_c, distancia, target_angle, desired, ki, kp, kd, integral, speed, correcion):
    print("comoe stas")
    while motor_c.angle() < target_angle:

        actual = abs(motor_b.angle()) - abs(motor_c.angle())

        error = desired - actual
        integral = integral + error
        derivative = error - actual
        correcion = (error*kp) + (integral*ki) + (derivative*kd)

        motor_c.run(speed - correcion)

        if speed < 140: 
            speed += 1
            
    motor_b.stop()
    motor_c.stop()

def motor_b_running(motor_b, motor_c, distancia, target_angle, desired, ki, kp, kd, integral, speed, correcion):  
    print("hola")
    while motor_b.angle() < target_angle:

        actual = abs(motor_b.angle()) - abs(motor_c.angle())

        error = desired - actual
        integral = integral + error
        derivative = error - actual
        correcion = (error*kp) + (integral*ki) + (derivative*kd)

        motor_b.run(speed + correcion)

        if speed < 140: 
            speed += 1
    motor_b.stop()
    motor_c.stop()



def movimiento_recto2(motor_b, motor_c, distancia):

    desired = 0
    motor_b.reset_angle(0)
    motor_c.reset_angle(0)
    ki = 0.012
    kp = 0.00182
    kd = 0.000190

    target_angle = ( distancia / (21.6) ) *360
   
    integral = 0
    speed = 1
    correcion = 0
   
    print("no es ta entranfdo")
    t1 = threading.Thread(target=motor_b_running)
    t2 = threading.Thread(target=motor_c_running)
    print("hajda")
    t1.start() 
    print("hola")
    t2.start()
    # print(target_angle)

    
        
