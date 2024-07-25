from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

def test_sensor_color(sensor):
    while True:
        print("El color delbloque es: ", sensor.color())
        wait(1000)
