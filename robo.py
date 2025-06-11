from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction

LIMIAR_PRETO = 20
LIMIAR_BRANCO = 60
# Inicialização
class Robo:
    Kp = 2.5
    Ki = 0
    Kd = 0
    velocidade_base = 100
    integral = 0
    erro_anterior = 0
    hub = PrimeHub()
    sensor_esquerdo = ColorSensor(Port.A)
    sensor_direito = ColorSensor(Port.B)
    sensor_ultrassonico = UltrasonicSensor(Port.E)
    motor_esquerdo = Motor(Port.C, Direction.CLOCKWISE)
    motor_direito = Motor(Port.D, Direction.COUNTERCLOCKWISE)