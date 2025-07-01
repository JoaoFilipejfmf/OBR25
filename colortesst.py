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
    print(f'Esquerdo - H: {h1:3d}, S: {s1:3d}, V: {v1:3d}, Ref: {sensor_esquerdo.reflection():3d} || Direito - H: {h2:3d}, S: {s2:3d}, V: {v2:3d}, Ref: {sensor_direito.reflection():3d}')
    wait(10)