from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

sensor_esquerdo = ColorSensor(Port.A)
sensor_direito = ColorSensor(Port.B)
motor_esquerdo = Motor(Port.C, Direction.COUNTERCLOCKWISE)
motor_direito = Motor(Port.D, Direction.CLOCKWISE)
motor = DriveBase(motor_esquerdo, motor_direito, 40, 211)
ultrassonico = UltrasonicSensor(Port.E)

def testar_sensores_de_luz():
    print(sensor_esquerdo.hsv())
    print(sensor_direito.hsv())

def testar_ultrassonico():
    print(ultrassonico.distance())

def obter_dist_entre_ultrassonico_eixo_rotacao(compr: int):
    d1 = 0
    for i in range(200):
        d1 += ultrassonico.distance()
        wait(10)
    d1 /= 200
    print()
    motor.turn(180)
    d2 = 0
    for i in range(200):
        d2 += ultrassonico.distance()
        wait(10)
    d2 /= 200
    print((compr - d1 - d2) / 2)

obter_dist_entre_ultrassonico_eixo_rotacao(580)