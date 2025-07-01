
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

hub = PrimeHub(broadcast_channel=114, observe_channels=[2])

sensor_esquerdo = ColorSensor(Port.A)
sensor_direito = ColorSensor(Port.B)

def detectar_verde(h, s):
    return 100 <= h <= 140 and s > 30

def detectar_vermelho(h, s):
    return (0 <= h <= 20 or 340 <= h <= 360) and s > 30

while True:
    h1, s1, v1 = sensor_esquerdo.hsv()
    h2, s2, v2 = sensor_direito.hsv()
    # print(f'Esquerdo - H: {h1:3d}, S: {s1:3d}, V: {v1:3d}, Ref: {sensor_esquerdo.reflection():3d} || Direito - H: {h2:3d}, S: {s2:3d}, V: {v2:3d}, Ref: {sensor_direito.reflection():3d}')
    if s1 > 30 or s2 > 30:
        if detectar_verde(h1, s1) or detectar_verde(h2, s2):
            hub.ble.broadcast(1)
        elif detectar_vermelho(h1, s1) or detectar_vermelho(h2, s2):
            hub.ble.broadcast(2)
    else:
        hub.ble.broadcast(None)
    wait(10)