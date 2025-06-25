from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

hub = PrimeHub()

sensor_esquerdo = ColorSensor(Port.A)
sensor_direito = ColorSensor(Port.B)

while True:
    h1, s1, v1 = sensor_esquerdo.hsv()
    h2, s2, v2 = sensor_direito.hsv()
    print(f'E: {h1:3d}, {s1:3d}, {v1:3d}, {sensor_esquerdo.reflection():3d} || D: {h2:3d}, {s2:3d}, {v2:3d}, {sensor_direito.reflection():3d}')
    wait(10)