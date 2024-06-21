from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color, Stop
import time
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from math import pi

"""The formula of an PID controller is the next one:
    Target(gyro target) = 0degrees
    Kp, ki, kd are constants
    
    value_motorA = Gyro Angles
    value_motorB = Gyro Angles
    error = target - value
    integral = integral + error 
    derivative = error - last_error
    
    correction = (error*Kp) + (integral*ki) + (derivative*kd)"""
def moviemiento_recto(motor_b, motor_c, distancia):

    desired = 0
    motor_b.reset_angle(0)
    motor_c.reset_angle(0)
    ki = 0.001
    kp = 0.3
    kd = 0.2
    target_angle = ( distancia / (21.6) ) *360
    print(target_angle)
    integral = 0
    speed = 10
    while motor_b.angle() < target_angle:
        # print(motor_b.angle(), motor_c.angle())
        actual = abs(motor_b.angle()) - abs(motor_c.angle())

        error = desired - actual
        integral = integral + error
        derivative = error - actual
        correcion = (error*kp) + (integral*ki) + (derivative*kd)

        motor_b.run(speed + correcion)
        motor_c.run(speed - correcion)

        if speed < 140: 
            speed += 10
    motor_b.stop()
    motor_c.stop()
        
# Funcion para comprobar cual de ambos movimientos es mas preciso
def avanzar3(motor_b, motor_c):

    motor_b.run(140)
    motor_c.run(140)
    while True:
        print(motor_b.angle(), motor_c.angle())
        
def retrocede_recto(motor_b, motor_c, distancia):
            
        desired = 0
        motor_b.reset_angle(0)
        motor_c.reset_angle(0)
        ki = 0.001
        kp = 0.3
        kd = 0.2
        target_angle = ( distancia / (21.6) ) *360
        print(target_angle)
        integral = 0
        speed = 10
        while motor_b.angle() > -target_angle:
            # print(motor_b.angle(), motor_c.angle())
            actual = abs(motor_b.angle()) - abs(motor_c.angle())
    
            error = desired - actual
            integral = integral + error
            derivative = error - actual
            correcion = (error*kp) + (integral*ki) + (derivative*kd)
    
            motor_b.run(-speed - correcion)
            motor_c.run(-speed + correcion)
    
            if speed < 140: 
                speed += 10
        motor_b.stop()
        motor_c.stop()