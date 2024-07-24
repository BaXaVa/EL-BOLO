from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color, Stop
import time
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from math import pi

def avanzar_hasta_color(motor_b,motor_c,sensor_1,  target_color):
    desired = 0
    
    motor_b.reset_angle(0)
    motor_c.reset_angle(0)

    ki = 0.001
    kp = 0.3
    kd = 0.2

    
    integral = 0
    speed = 10
    while sensor_1.color() != target_color :

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

def retroceder_hasta_color(motor_b,motor_c,sensor_1,  target_color):
    desired = 0
    motor_b.reset_angle(0)
    motor_c.reset_angle(0)
    ki = 0.001
    kp = 0.3
    kd = 0.2

    
    integral = 0
    speed = -10
    while sensor_1.color() != target_color :
        # print(motor_b.angle(), motor_c.angle())
        # print(motor_b.angle(), motor_c.angle())
        # print("speed 1 =", speed)
        actual = abs(motor_b.angle()) - abs(motor_c.angle())

        error = desired - actual
        integral = integral + error
        derivative = error - actual
        correcion = (error*kp) + (integral*ki) + (derivative*kd)

        motor_b.run(speed - correcion)
        motor_c.run(speed + correcion)
        # print("Speed 2 = ", speed)
        if speed > -140: 
            speed -= 10
    motor_b.stop()
    motor_c.stop() 

def movimiento_recto(motor_b, motor_c, distancia):

    desired = 0
    motor_b.reset_angle(0)
    motor_c.reset_angle(0)
    ki = 0.012
    kp = 0.00182
    kd = 0.000190
    target_angle = ( distancia / (21.6) ) *360
    # print(target_angle)
    integral = 0
    speed = 1
    while motor_b.angle() < target_angle:
        # print(motor_b.angle(), motor_c.angle())
        # print(motor_b.angle(), motor_c.angle())
        actual = abs(motor_b.angle()) - abs(motor_c.angle())

        error = desired - actual
        integral = integral + error
        derivative = error - actual
        correcion = (error*kp) + (integral*ki) + (derivative*kd)

        motor_b.run(speed + correcion)
        motor_c.run(speed - correcion)

        if speed < 140: 
            speed += 1
    motor_b.stop()
    motor_c.stop()
        

        
def retrocede_recto(motor_b, motor_c, distancia):
            
        desired = 0
        motor_b.reset_angle(0)
        motor_c.reset_angle(0)
        ki = 0.001
        kp = 0.3
        kd = 0.2
        target_angle = ( distancia / (21.6) ) *360
        # print(target_angle)
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
                speed += 2

        motor_b.stop()
        motor_c.stop()