def PID(robot, sensor1, sensor2):
    #Haz un PID que siga la linea con dos sensores
    #El PID debe ser capaz de seguir la linea negra
    ki=0.1
    kp=0.1
    kd=0.1
    integral=0
    last_error=0
    derivative=0
    error=0
    while wait(3000):
        error=sensor1.reflection()-sensor2.reflection()
        integral+=error
        derivative=error-last_error
        last_error=error
        robot.drive(250+kp*error+ki*integral+kd*derivative, 0)
        print(sensor1.reflection())
        print(sensor2.reflection())
       